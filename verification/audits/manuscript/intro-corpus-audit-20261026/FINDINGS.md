# Findings for the Introduction (audit synthesis)

*Recorded by the coordinator from the audit-synthesis agent's report, because the agent's tool refused report files, and revised by the coordinator to apply the independent review's required changes RC-1 to RC-12 (`review/INDEPENDENT-REVIEW.md`): R-01, R-02 and R-07 carry the reviewer's texts, R-06, R-10 and R-19 are amended, R-33 and R-34 are added, and OD-3 and the counts are updated.*

**Objects.** `papers/Introduction.md` at `4a260ca9` (sha256 `beb0a520…b936feb8`); line numbers (`Lnn`) refer to that blob. The corpus is `main` at `eae01647`, as read by the mappers; the Introduction cites `b64919cd`, and the `OIBridge` sources are byte-identical at `17b830bc`, `b64919cd` and `eae01647`.

**Inputs.** `matrix.json` (409 rows; human-readable form `MATRIX.md`), `completeness.json` (`CMP-01`–`CMP-26`), `consistency.json` (`CON-01`–`CON-48`), the mapper notes `matrix/part-B1.md`…`part-B5.md`, and the inventories under `inventory/`. Each proposed text below was re-checked against its source before it was written (the checks are recorded under *Pressure test*), and each *Current* span was checked mechanically to be a verbatim substring of its line.

**Summary.**

- 358 of 409 rows are FAITHFUL after the synthesis and the independent review re-rated some rows (`matrix/resolutions.json`). The 51 others, the seven completeness rows recommended *add* or *strengthen*, and the two rows whose mapper disagreement resolved against the Introduction (I-013, I-008) reduce to **34 required changes** (part a; R-33 and R-34 were added by the independent review), deduplicated across the abstract, the body, §6.2 and §6.3.
- **24 optional changes** (part b; O-7 and O-12 of the 26 listed there have moved into R-01 and R-07) and **15 owner decisions** (part c).
- The **corpus corrections** outside the Introduction fall into eight proposed pull requests (part d).
- **Length.** The main text runs through p. 12 at 4,966 words, about 414 words a page. After the independent review the required changes add about 610 words in full form (R-01, R-02 and R-07 lengthened; R-33 and R-34 added; the short forms withdrawn); cuts C-1 to C-8 bring the net to about +400 words, roughly one page (part c, OD-13). Page count is measured by building (`sh ./build.sh`), not estimated.

| Tier | Findings | Count |
|---|---|--:|
| 1. Overclaims and unsupported claims | R-01–R-05 | 5 |
| 2. Underclaims and omissions (high or medium priority) | R-06–R-10, R-34 | 6 |
| 3. Miscitations and attributions | R-11–R-19 | 9 |
| 4. Imprecisions | R-20–R-33 | 14 |

Severity inside a tier runs from first to last. Where a matrix verdict is IMPRECISE but its direction is an overclaim (R-01, R-03, R-05), the finding is ranked in tier 1 and the reason is given.

***

## (a) Required changes

### Tier 1: overclaims and unsupported claims

#### R-01 — Page value "for all but an exponentially negligible fraction of initial conditions" (high)

- **Covers:** I-225 (OVERCLAIM: a vacuous conditional, re-rated by the independent review); I-223 and I-286 (IMPRECISE, re-rated by the independent review); CON-01 (high); CMP-25 (BHb C2, required); context I-226–I-228, I-244.
- **Lines:** L162, L183.
- **Why tier 1.** Theorem A.8 of [GR] consists of an unconditional cycle-counting lemma and a step that is H-scramble (GR.md:817–841@eae01647). It counts initial *configurations* on Σ_E, with the B|R bipartition aligned to the configuration coordinates (GR.md:827, :837–:841). Every orbit of a configuration consists of basis states, which are product states across the aligned cut. So the radiation entropy is zero at every step, H-scramble fails for every bijection (GR.md:833; BHb C1), and A.8's conclusion is false for every counted initial condition. A.8 is true only vacuously and has no instance in the setting it counts; A.9 inherits this. The Introduction reports A.8's quantified conclusion as a result.
- **Evidence.**
  - GR.md:817@eae01647 (statement of A.8), :827 and :837–:841 (the counting runs over configurations of Σ_E);
  - GR.md:833 (every orbit of a definite configuration is product across the aligned cut);
  - GR.md:835 attributes the failure to "the setting of Theorem A.7's proof" only; the anchor is A.8's own counting (CON-01);
  - BHb C1 (one-line proof: a permutation maps basis vectors to basis vectors), C2 (entanglement at an aligned bipartition under any permutation is at most the entropy of the initial configuration distribution), C6(a)–(c) (`bh02_scramble_v1/REPORT.md`), and its review (`review/REVIEW.md`:69–76).
- **Proposed text** (independent review, RC-1).

  > **Current (L162).** For all but an exponentially negligible fraction of initial conditions, the full-cycle time average of the radiation's entanglement entropy, at the bipartition of each stage held fixed, equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$, up to the correction term of Theorem A.8 [Pag93; GR, Thms A.8–A.9]. This holds under the scrambling hypothesis H-scramble, that the orbit ensemble equidistributes over quantum pure states on the shell; H-scramble fails for every bijection acting on a definite initial configuration with the bipartition aligned to the configuration coordinates and is not established [GR App. A.7; BHb, C1, C6(a)–(b)].
  >
  > **Proposed.** Theorem A.8 of [GR] derives the Page value $S_{\rm Page}(d_B,d_R)$ for the full-cycle time average of the radiation's entanglement entropy, at the bipartition of each stage held fixed and up to its correction term, from the scrambling hypothesis H-scramble, that the orbit ensemble equidistributes over quantum pure states on the shell; the Page value enters only through that hypothesis [Pag93; GR, Thms A.8–A.9; BHb, C6(b)]. The theorem counts initial configurations, with the bipartition aligned to the configuration coordinates; every state on such an orbit is a product state, so the radiation entropy is zero at every step, H-scramble fails for every bijection, and the theorem has no instance in that setting [GR App. A.7; BHb, C1, C6(a)]. Under a bijection, the entanglement at an aligned bipartition never exceeds the entropy of the initial configuration distribution [BHb, C2], so a Page value requires an initial superposition over at least $e^{S_{\rm Page}}$ configurations or a bipartition not aligned with them; neither is specified, and H-scramble is not established.

  Consequential edits:
  - I-223, L162: "…addresses recovery under its own conditions, which are not established".
  - I-286, L183: "whether the substratum supplies an initial superposition or a non-aligned bipartition on which H-scramble holds, and whether H-decouple holds".
  - The abstract's "the framework's Page curve is not established" stays accurate.
- **Length:** about +45 words.
- **Pressure test.** The text no longer leads with the quantified conclusion as a conditional result (§A.30: remove the assertion, keep the derivation). It states what A.8 derives, why it has no instance in its counted setting, and the unconditional bound BHb C2 that survives. It does not claim the Page value fails for superposed initial states or non-aligned cuts; that is open. R-01 does not wait on GR's restatement of A.8 (OD-9). [Pag93]'s citation is decided under OD-8.

#### R-02 — "no unconditional implication holds among" the three notions (moderate)

- **Covers:** I-127 (OVERCLAIM, the matrix's only one); CON-42 (medium).
- **Lines:** L106.
- **Evidence.**
  - Main.md:334@eae01647 says only that no implication "is asserted here";
  - Main.md:606, Remark (two notions of memory): "Markov implies P-divisible (chain factorization), so P-indivisibility is the strictly stronger property";
  - RHP14 Cor. 2.1 (read first-hand by mapper B2).

  So P-indivisibility of the population law forces $M_t>0$ at some $t$: one unconditional implication holds, and the Introduction's sentence is false as written.
- **Proposed text.**

  > **Current (L106).** Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion.
  >
  > **Proposed** (independent review, RC-2). Three notions are distinct [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. For the rooted family of a visible law in which every initial value has positive probability, a law with $M_t=0$ for every $0<t<n$ is P-divisible on $\{0,\dots,n\}$, so P-indivisibility there implies $M_t>0$ for some $0<t<n$ [Main §3.4, Remark (two notions of memory)]; the converse fails (Appendix B.2).

- **Length:** about +40 words.
- **Assumptions** (independent review, §3; owner, 2026-10-26: "Markovianity ⇒ P-divisibility, and therefore … P-indivisibility ⇒ non-Markovianity … under the specific definitions, time domain, and assumptions establishing the first implication"):
  - *Positive-probability roots.* The kernel's rooted map defines a row for every root whatever the law of $x_0$. With a zero-mass root the implication fails: the two-card game with $x_0$ fixed has a P-indivisible rooted family while the process from its one root is Markov.
  - *A multi-time visible law.* Notion (2) also covers population families of quantum channels (the Hadamard family at L106), for which $M_t$ is undefined.
  - *Time range.* The memory lies somewhere in $(0,n)$; for Theorem 3, $n$ is the return time, so it need not lie in Main's accessible window.
  - *Definitions.* Under L72's $M_t$ and Main's Characterization theorem, "non-Markovian at some order" is $M_t>0$ for some $t$ (via the vanishing criterion [CT06], not machine-checked), so either wording is licensed.
- **Pressure test.** The text states exactly the direction that holds, with its assumptions, and nothing about (3). The converse failure is Appendix B.2 (and L104).

#### R-03 — "exact probes" for floating-point computations (medium)

- **Covers:** I-054 (IMPRECISE), I-103 (IMPRECISE); CON-25 (medium); bears on I-071's tag (R-08).
- **Lines:** L30, L84; L56 is consistent once L30 is fixed.
- **Why tier 1.** Under the Code Review Rules, floating-point evidence does not certify an exact quantity, and the Introduction's own definition (L30) promises "an exhaustive computation in exact rational arithmetic".
- **Evidence.**
  - L84's probe `papers/oi_lattice_code/foundations/c4_backflow_probes.py@eae01647` builds exact `Fraction` laws but accumulates the conditional mutual information as `float(p)*log2(float(…))` (line 23) and asserts with tolerance `abs(I-1.0)<1e-12` (line 52), on hand-picked families.
  - Main.md:170 says "Certified exactly" for the same probe (CON-25).
  - L56's probes (`process_dilation_probes.py`; `review4_probes.py` P-G, lines 170–222) are exact `Fraction` computations, but on named instances, not every law of a class, so they fail "exhaustive" while meeting "exact".
- **Proposed text.**

  > **Current (L30).** an "exact probe" is an exhaustive computation in exact rational arithmetic at small size
  >
  > **Proposed.** an "exact probe" is a computation in exact rational arithmetic on stated small instances

  > **Current (L84).** (proved on paper, with exact probes) [Main §2.3; CT06]
  >
  > **Proposed.** (proved on paper) [Main §2.3; CT06]

- **Length:** −3 words.
- **Pressure test.** With the narrowed definition every remaining "exact probe" claim (L56) is true. The alternative (keep "exhaustive" and relabel L56) is OD-7. The Pinsker bound itself is correct (B2 re-derived it), so only the tag goes. CMP-01's proposed ε-realization text also said "with exact probes"; `opglue_probes.py` compares total variations in floating point with tolerances (lines 161, 176, 181, 193), so R-07 drops that tag too.

#### R-04 — "a minimal model … with six hidden states" and "the smallest realization" (low)

- **Covers:** I-123, I-124 (the mappers disagree; resolved below); CON-24 (low).
- **Lines:** L98, L219 (the B.1 heading).
- **Disagreement.** B2 rated I-123 IMPRECISE ("minimal" is Main §2.4's title, meaning simple) and I-124 UNSUPPORTED (no proof anywhere). B5 rated I-123 UNSUPPORTED (no measure makes it true) and I-124 IMPRECISE (true, but "the" is not unique). The merged matrix kept B2's rows.
- **Re-check.** An exact recomputation (`Fraction`, scratch, not committed) gives:
  - a three-hidden-state model (h = 1 flips x; h = 2, 3 swap) reproduces every B.1 number: $\Gamma_1$, $\Gamma_2=I$, the conditionals 1 and 1/3, and $a/(2-a)$;
  - with one hidden value no bijection is a Theorem 3 witness;
  - at (2, 2), 16 of the 24 bijections are witnesses.

  So B5's reading holds for I-123: as a size claim, "minimal" is false. For I-124 both readings hold: "smallest" is true in alphabet sizes, by a two-line argument that no corpus document writes, and "the" is not unique (Main:421's φ(v,h) = (v⊕h, h) is another 2×2 realization). The fix removes both size claims.
- **Proposed text.**

  > **Current (L98).** Appendix B works examples: a minimal model of Theorem 3 with six hidden states, memory without short-window indivisibility, and a two-card game, the smallest realization of Theorem 3.
  >
  > **Proposed.** Appendix B works examples: a six-hidden-state model of Theorem 3 [Main §2.4], memory without short-window indivisibility, and a two-card game, which realizes Theorem 3 with two visible and two hidden values.

  > **Current (L219).** ### B.1 A minimal model
  >
  > **Proposed.** ### B.1 A six-hidden-state model

- **Length:** +3 words in the main text.
- **Pressure test.** Retaining "the fewest possible" with its one-line reason would put a result in the Introduction that no corpus document states, against its no-new-result contribution statement (L28), so it is OD-10, not the default.

#### R-05 — scope qualifiers dropped in §6.1 and §6.4 (low)

- **Covers:** I-246 (IMPRECISE), I-300 (IMPRECISE). Both are overclaims of scope.
- **Lines:** L168, L189.
- **Evidence.**
  - L168: Theorem 1 holds per horizon. L68 and Main.md:618@eae01647 state that a nonperiodic law has no exact all-time realization by one fixed finite substratum.
  - L189: Theorem 4 is proved for nonempty finite carriers (GeneralCarrier:100); H-∞ is open (ROADMAP.md:71@eae01647); the abstract (L12) already says "Exact finite operational quantum mechanics".
- **Proposed text.**

  > **Current (L168).** the fixed-basis statistics of quantum theory are the visible laws of an embedded observer
  >
  > **Proposed.** the fixed-basis statistics of quantum theory are, at every finite horizon, visible laws of an embedded observer

  > **Current (L189).** Exact operational quantum mechanics is reached only under
  >
  > **Proposed.** Exact finite operational quantum mechanics is reached only under

- **Length:** +4 words.
- **Pressure test.** B4 also cited the kernel's `qStar_not_subset_finiteRootedRealizable`. Its census family is kernel-only, so the fix rests on L68 and Main:618, not on that declaration.

### Tier 2: underclaims and omissions

#### R-06 — the substratum-sourcing results and Theorem 4's reach (high)

- **Covers:**
  - matrix: I-146, I-258, I-281 (UNDERCLAIM) and I-013 (abstract; FAITHFUL in B1, resolved below);
  - I-015 (IMPRECISE; same sentence of the abstract);
  - completeness: CMP-02 (high, strengthen) and CMP-03 (medium, add);
  - consistency: the corpus side of CON-14.
- **Lines:** L12, L120, L173, L183, and Appendix A (L215).
- **Disagreement.** B1 rated the abstract's "Open are which of conditions (iii)–(v) a physical substratum supplies" FAITHFUL. B2 and B4 rated the same claim at L120, L173 and L183 UNDERCLAIM. Re-reading GR.md:228 and :260–:266, ROADMAP.md:69 and :1521–:1538, and the kernel statements below shows that B2/B4's reading holds: the abstract carries the same understatement and takes the same fix.
- **Evidence** (kernel at `eae01647`, identical at `17b830bc`):
  - **Conversely, full control realizes the OI core.** `realizesSealedOICore_of_control` (OIRealization:252): every qubit theory with composite unitary control, which is condition (iv) (`HasCompositeUnitaryControl`, OperationalAssembly:665; the bundle at PhysicalCharacterization:295), realizes the sealed C1–C4 core. GR.md:228: "the theorem is a classification of the completions compatible with embedded observation, not a derivation of quantum mechanics from it".
  - **No phases from the stated access.** `permClass_onesFixing` (PhaseSource:79), `onesFixing_not_phasesAvailable` (:52) and `substratumClass_not_onesFixing` (:196): the stated dynamics and access supply no quarter phase (GR.md:260).
  - **No state mixing in the substratum class.** `substratum_residual` (StructuralClosure:383) and `substratumClass_not_drivesElementary` (:370): the monomial substratum class is structurally closed but drives no elementary transition, and its generated qubit theory is not quantum. `monomialSource_not_control` (SubstratumInterface:186) and `readWriteSourced_not_control` (ReadWriteControl:169): on the qubit (iv) fails.
  - **Adding control suffices.** `substratum_plus_control_qm` (StructuralClosure:414): a structurally closed extension that drives the elementary transitions generates exact finite endomorphic operational QM on every nonempty finite carrier (GR.md:262, boxed).
  - **What stays open.** ROADMAP.md:69, F2 OPEN ("the present architecture is settled negatively"); ROADMAP.md:1521–1538 lists phases and dense control as INDEPENDENT.
  - **Census.** The families "substratum source", "phase source" and "completion classification" are `current`, carried by GR and Main.
- **Proposed text** (full form; the short form is in OD-2):

  > **Current (L12).** Open are which of conditions (iii)–(v) a physical substratum supplies, the selection of the evolution relating two times, and any test of the hypothesis.
  >
  > **Proposed.** The finite bijective substratum, with the observer's stated access, supplies neither the phases nor continuously tunable state mixing, and adding both yields exact finite operational quantum mechanics (machine-checked). Open are whether a physical substratum supplies them, the selection of the evolution relating two times, and any experiment that distinguishes OI from standard quantum theory.

  > **Current (L120).** Which of (iii)–(v) a physical substratum supplies is open [GR §3.3].
  >
  > **Proposed.** Conversely, every qubit theory satisfying (iv) realizes that process, so Theorem 4 classifies the completions compatible with embedded observation and does not derive quantum mechanics from it. Because a bijective intervention acts on configurations as a permutation operator, the substratum as stated, finite bijective dynamics with the observer's read and write access, supplies no quarter phase; with a phase intervention assumed, its operations are monomial, with no continuously tunable state mixing, and on the qubit a theory of such operations fails (iv) and is not quantum; adding continuous control of the elementary transitions, with the closure properties kept, yields exact finite operational quantum mechanics on every nonempty finite carrier (machine-checked for the substratum class as formalized in [GR §3.3]). Whether a physical substratum supplies the phases and that control is open.

  > **Current (L173).** which of (iii)–(v) a physical substratum supplies is open
  >
  > **Proposed.** whether a physical substratum supplies the phases and the continuous state-mixing control that the stated substratum lacks is open

  > **Current (L183).** whether a physical substratum supplies completion conditions (iii)–(v)
  >
  > **Proposed.** whether a physical substratum supplies the phases and the continuous state-mixing control with which the stated substratum yields exact finite operational quantum mechanics

  Appendix A, L215: add `realizesSealedOICore_of_control` (OIRealization:252); `permClass_onesFixing`, `onesFixing_not_phasesAvailable` (PhaseSource:79, :52); `monomialSource_not_control` (SubstratumInterface:186); `substratum_residual`, `substratum_plus_control_qm` (StructuralClosure:383, :414).
- **Length:** +158 words in full form (L12 +30, L120 +103, L173 +10, L183 +15); +118 with the short L120 of OD-2. Appendix A is outside the main-text budget.
- **Modelling premise** (independent review, RC-4). The negative results follow from modelling reversible interventions as bijections of configurations, which act as permutation operators (monomial ones once the phase is stipulated); a continuously tunable mixing operator is not monomial (`offDiagonal_interp_not_monomial`). This is an exact account of what the stated architecture lacks, not a physical no-go for richer substrata. The identification of the Lean substratum class with the manuscripts' stated substratum is a paper-level modelling step, hence "as formalized".
- **Pressure test.**
  - **Not used.** B4's `frozen_sourcing_verdict` and `readWriteSourced_not_qm` framing. FrozenSourcing's census family is kernel-only (no manuscript carries it, §A.35), so the text cites only current-family declarations.
  - **Not claimed.** That the substratum *supplies* (iii) and (v). GR states structural closure (spectator stability, adjoint, relabelling), not conditions (iii) and (v) of Theorem 4, so the text names only (iv).
  - **Scope.** The negative half is stated on the qubit, where the kernel proves it. The positive half is stated on every nonempty finite carrier.
  - **Closure hypothesis.** `substratum_plus_control_qm` needs the extension to stay structurally closed, hence "with the closure properties kept".
  - **Phases.** "Phases" means the relative-phase intervention that GR states as an assumption. The kernel shows the stated access does not source the quarter phase, so "supplies no quarter phase" is the exact form.
  - **Abstract.** "Any experiment that distinguishes OI from standard quantum theory" is the sourced form of I-015 (L183; Main:704).

#### R-07 — the ε-realization half of §3.4 (high)

- **Covers:** CMP-01 (high, strengthen), CMP-08 (medium, add), I-159 (IMPRECISE: the heading is broader than the body and reuses "carrier"); O-12 (now required).
- **Lines:** L12 (abstract), L128, L130.
- **Evidence.**
  - Main.md:544@eae01647, Theorem (finite operational realization and gluing — ε-form);
  - Main.md:560, Corollary (single controlled dynamics): one autonomous dynamics serving every adaptive protocol needs a program register exponential in $K$;
  - Main.md:562 (an operational realization theorem, not a uniqueness theorem; non-quantum families are realized too);
  - Main.md:576, Theorem (uniform continuum realization — mutual ε-density);
  - Main.md:578 (density, not identity, at fixed (d, m));
  - Main.md:580 (Summary, item 4);
  - Main.md:460, Theorem (intervention dilation: the finite classical action-labelled comb).

  All are proved on paper, with no kernel statement. `opglue_probes.py` computes laws exactly on named qubit instances but compares total-variation distances in floating point (tolerances 1e-15 and 1e-12): numerical evidence on instances, not certification.
- **Proposed text** (independent review, RC-3; owner, 2026-10-26: "a positive realization theorem should not be treated as secondary merely because the Introduction currently emphasizes an obstruction").

  > **Current (L128).** ### 3.4 No fixed finite carrier reproduces a qubit
  >
  > **Proposed.** ### 3.4 Finite realizations of quantum experiments

  > **Current (L130).** The obstruction does not touch Theorem 1, whose realization is chosen per law.
  >
  > **Proposed.** The obstruction does not touch Theorem 1, whose realization is chosen per law. At finite accuracy the realization direction holds. Fix a $d$-dimensional system with an initial state, a finite family of instruments with finitely many Kraus operators (preparations entering as channels), a horizon $K$ and an accuracy $\varepsilon$: one finite reversible realization, which applies one fixed bijection per instrument to a digitized copy of the unnormalized quantum state held in its hidden sector, reproduces the outcome law of every adaptive protocol over the family within $\varepsilon$ in total variation, and for instruments with at most $m$ outcomes the realized and quantum operational theories are mutually $\varepsilon$-dense at horizon $K$ (proved on paper) [Main §3.4, Theorems (finite operational realization and gluing — ε-form) and (uniform continuum realization — mutual ε-density)]. A single autonomous dynamics serving every adaptive protocol needs a program register that grows exponentially with $K$ [Main §3.4, Corollary (single controlled dynamics)]. This is density, not identity: the construction also realizes non-quantum instrument families, and no fixed finite realization reproduces the exact theory. Classical action-labelled interventions are realized exactly by one fixed realization [Main §3.4, Theorem (intervention dilation: the finite classical action-labelled comb)].

  > **Abstract (L12), added clause.** Finite reversible realizations reproduce every finite quantum experiment to any stated accuracy (proved on paper); exact finite operational quantum mechanics is characterized by five completion conditions, none implied by OI alone.
- **Length:** about +170 words in the main text, including the abstract clause. The short form is withdrawn (OD-3).
- **Pressure test.** "Approximately, the converse holds" is withdrawn: the result is a finite-accuracy realization at a fixed instrument family, not the converse of the obstruction. The text states the fixed initial state, what the realization is (one fixed bijection per instrument acting on a digitized state), the program-register cost of a single autonomous dynamics, and that it is density and not identity. The "exact probes" tag is not used. The heading change also resolves I-159.

#### R-08 — the independent-prior realization holds for every law (medium)

- **Covers:** I-071 (UNDERCLAIM); CMP-22 (medium, strengthen); CON-20.
- **Lines:** L56.
- **Evidence.**
  - Main.md:496@eae01647: the theorem's statement is restricted to rational laws, which is why L56 reads as it does.
  - Main.md:498, Extension (arbitrary priors — the response-table form): "The rationality restriction is a property of the uniform-tape presentation, not of realizability … reproduced for arbitrary real kernels".
  - Main.md:715 (status ledger).
  - `review4_probes.py` P-G: an exact `Fraction` check on one non-Markov instance.
  - Main:500: the independence is not formalized.
- **Proposed text.**

  > **Current (L56).** For a law with rational probabilities, a realization whose hidden prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation)]
  >
  > **Proposed.** For every law, a realization whose hidden prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation) and its Extension (arbitrary priors — the response-table form)]

- **Length:** +6 words.
- **Pressure test.**
  - The rest of L56 ("it is proved on paper, with exact probes") stays true only under R-03's narrowed definition: P-G is one exact instance, not an exhaustive one.
  - The Extension is argued in a paragraph, not a displayed theorem, so the citation names it as an Extension.
  - The kernel's `responseRealization` covers rooted families only, so the text adds no "machine-checked".

#### R-09 — open problem (3), exact gluing (medium-low)

- **Covers:** I-292 (UNDERCLAIM); CMP-23 (medium, cite); CON-28.
- **Lines:** L185.
- **Evidence.**
  - `finiteRootedRealizable_iff_pper` (RootedClassificationAllTime:192): a rooted family is realizable at every time by one finite reversible system exactly when it is row-stochastic, the identity at the root, and periodic.
  - Its census family is **kernel-only**; no manuscript states it. Main.md:618 and ROADMAP.md:1569 list "exact gluing for recurrent target families" as open.
- **Proposed text** (interim; the full form waits on OD-4):

  > **Current (L185).** (3) exact gluing for recurrent target families
  >
  > **Proposed.** (3) exact gluing for recurrent families of multi-time laws

- **Length:** +2 words.
- **Pressure test.**
  - The multi-time-law version is open (Main.md:618).
  - Naming it avoids listing the rooted case as open without citing a kernel-only result.
  - Once Main states the rooted classification with its census anchor, append "(for rooted families, periodicity is necessary and sufficient [Main §3.4])", +12 words, as O-6.

#### R-10 — open obligations missing from §6.3 (medium)

- **Covers:** CMP-17 (medium, add); CON-15 (low; touches Theorem 4's stated setting, L114).
- **Lines:** L185, extending the list.
- **Evidence.**
  - Pre-quantum kinematics: ROADMAP.md:68@eae01647, P1 "K — … to the complex matrix kinematics the finite characterization assumes", OPEN.
  - Finite scope: ROADMAP.md:71, H-∞ OPEN; GR.md:262 ("The scope is finite and endomorphic"); GR.md:288 (the region completion is not a characterization of all infinite-dimensional instruments).
  - CON-15: no manuscript states the kinematics assumption. A grep of `papers/` and `book/` for "matrix kinematics" and "pre-quantum" finds none.
- **Proposed text.**

  > **Current (L185).** motivated by eigenstate thermalization [Main §3.4].
  >
  > **Proposed.** motivated by eigenstate thermalization [Main §3.4]; (5) a derivation of the complex matrix kinematics that Theorem 4 takes as given, and the extension of Theorem 4 to infinite-dimensional systems [GR §3.3].

  (If R-26 lands, apply this to R-26's replacement for item (4).)
- **Two stages** (independent review, RC-7). Stage 1, now: append only "and the extension of Theorem 4 to infinite-dimensional systems [GR §3.3]". Stage 2, after the corpus correction PR-B states the kinematics assumption in GR §3.3 (CON-15): add "a derivation of the complex matrix kinematics that Theorem 4 takes as given". Until then [GR §3.3] does not carry the kinematics item, and the Introduction does not cite it for that.
- **Length:** +25 words.
- **Pressure test.**
  - "[GR §3.3]" carries the finite scope now, but carries the kinematics item only after CON-15's correction adds it. Until then the citation for (5) is ROADMAP P1, which the Introduction does not yet cite (OD-14).
  - The (Obs, μ) interface and the lattice cut of (C4) are also ROADMAP-only. They are optional (O-11), because the Introduction does not use the lattice construction.

#### R-34 — the central narrative: "stop short of operational quantum mechanics" (high)

- **Covers:** I-040 (UNDERCLAIM, independent review RC-8); the abstract and §6.4's second sentence; owner, 2026-10-26: "assess whether the Introduction's central scientific narrative needs adjustment".
- **Lines:** L26, L12, L189.
- **Evidence.** Once R-06 and R-07 land, the framework's quantum-reconstruction results read: exact at the fixed-basis level (Theorem 1, kernel); ε-exact for every finite operational experiment (Main §3.4, paper); exact operational quantum mechanics exactly when one control resource is added, which OI does not supply (GR §3.3, kernel, for the substratum class as formalized). "Stop short of operational quantum mechanics" omits the second and third.
- **Proposed text.**

  > **Current (L26).** its foundation and quantum-emergence results, which stop short of operational quantum mechanics (§§2–3)
  >
  > **Proposed.** its foundation and quantum-emergence results, which reach the fixed-basis statistics exactly and every finite quantum experiment to any stated accuracy, while exact operational quantum mechanics needs completion conditions OI does not imply (§§2–3)

  Align the abstract (with R-07's clause) and §6.4's second sentence with that wording.
- **Length:** about +20 words.
- **Not changed.** The memory-centred thesis, the representation-not-derivation stance and the cosmological-constant conditionality are faithful (independent review §12).

### Tier 3: miscitations and attributions

#### R-11 — where the proofs are (moderate)

- **Covers:** I-052 (MISCITED), I-042 (IMPRECISE).
- **Lines:** L26, L28.
- **Evidence.**
  - Theorem 4 and §3.2–§3.3 are stated in GR §3.3 (GR.md:218) and Main.md:624. Neither writes a proof; the proofs are the `OIBridge` declarations of Appendix A. The inventory lists GR:218 as kernel-only.
  - §5 rests on BHa/BHb and GR App. A, not on Main.
- **Proposed text.**

  > **Current (L26).** Proofs, the status ledger and the probe code are in [Main], which this paper introduces;
  >
  > **Proposed.** The status ledger and the probe code are in [Main], which this paper introduces, the written proofs in [Main], [GR] and [BHa; BHb], and the machine-checked declarations in Appendix A;

  > **Current (L28).** The results of §3.2–§3.3 are proved in [GR] and [Main].
  >
  > **Proposed.** The results of §3.2–§3.3 are stated in [GR §3.3] and [Main §3.4] and proved in the Lean declarations of Appendix A.

- **Length:** +26 words.

#### R-12 — Theorem 3's source

- **Covers:** I-114 (IMPRECISE, citation scope); CON-41; and a census finding added here.
- **Lines:** L92; Appendix A L211.
- **Evidence.**
  - The Introduction's statement matches `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148) exactly.
  - [Main §2.3] (Main.md:115) proves only the case s = 1 under the uniform prior.
  - "Fixed hidden prior" is `RootedRealization.prior`, "shared by every root" (CausalReadback:181).
  - The census family "recurrence horizon" is **kernel-only**, with no manuscript anchor, and `verification/lean-manuscript-census.json` does not list `papers/Introduction.md` among its manuscripts.
- **Proposed text.**

  > **Current (L92).** **Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with a fixed hidden prior.
  >
  > **Proposed.** **Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with a hidden prior independent of $x_0$.

  This keeps "[Main §2.3]" on the condition that Main §2.3 states the general rooted form with its census anchor first (OD-4, PR-G). If that does not happen before landing, use the interim citation "(recurrence and overlap; [Main §2.3] for a non-permutation one-step matrix under the uniform prior)".
- **Length:** +2 words; +11 with the interim citation.

#### R-13 — the routed-readback declaration

- **Covers:** I-121 (MISCITED); CON-43; B5's note on I-329.
- **Lines:** Appendix A L212. L96 is unchanged: its gloss matches the storage-time reading.
- **Evidence.**
  - `PhysicalC4Discharge.lean`:27–29@eae01647 records that its `RoutedReadback` store clause is the frozen "seed-posterior" spelling, which is not the discovery round's storage-time clause.
  - `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256) transcribes the storage-time reading, which is the Introduction's gloss: "a visible-history record written into the hidden state is read back later".
  - Both proofs use only the overlap, so the conclusion ∃n, PIndivisibleWithin n is the same.
  - Both modules' census families are **kernel-only**.
- **Proposed text.**

  > **Current (L212).** - **Readback forces indivisibility** (§2.5): `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for routed readback; on paper for (C4).
  >
  > **Proposed.** - **Readback forces indivisibility** (§2.5): `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256) for routed readback with the record read from the hidden state at the storage time, and `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for the reading conditioned on the initial hidden state; on paper for (C4).

- **Length:** 0 in the main text (+24 in Appendix A).
- **Pressure test.** Adding a declaration needs its axiom report in the retained result `papers/introduction_repro/` (§A.42; OD-15). The choice of declaration is OD-5.

#### R-14 — [Pag93] for the statement of the information problem

- **Covers:** I-206 (MISCITED).
- **Lines:** L156; reference L323.
- **Evidence.** [Pag93] is "Average entropy of a subsystem" (random pure states); it is the right source for $S_{\rm Page}$ at L162. Page's black-hole paper of the same year is "Information in black hole radiation", PRL 71, 3743, hep-th/9306083. Both were checked at abstract level only (B3).
- **Proposed text.**

  > **Current (L156).** [Haw76; Pag93; Pag13]
  >
  > **Proposed.** [Haw76; Pag13]

  Alternatively, add the 1993 PRL as a new entry after a first-hand read (OD-8).
- **Length:** −1 word.

#### R-15 — the Doukas attribution

- **Covers:** I-116 (IMPRECISE); I-051 (FAITHFUL in B1; same attribution, resolved below).
- **Lines:** L28, L94.
- **Evidence.** Dou26 v3, §4.2.1, read first-hand for this synthesis: Prop. 1 (no distinguishability revival) states that Markov compatibility, a column-stochastic family with the Chapman–Kolmogorov property, implies that the total variation of two preparations cannot increase. Its proof is the ℓ1 contraction. The paper has no overlap, no return and no finite recurrence. Its example is Rabi oscillation.
- **Disagreement.** B1 rated L28's "stated concurrently by Doukas" FAITHFUL; B2 rated L94's "the same overlap-and-return argument" IMPRECISE. L28 is ambiguous: "stated" can attach to the recurrence argument, which overstates, or to the contraction criterion, which is true. B2's reading of the source holds, and both sites take the same fix.
- **Proposed text.**

  > **Current (L28).** stated concurrently by Doukas [Dou26]
  >
  > **Proposed.** which Doukas states concurrently as a no-revival obstruction [Dou26, Prop. 1]

  > **Current (L94).** Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]
  >
  > **Proposed.** Doukas states the contraction argument concurrently, as a no-revival obstruction to Markovian realizers [Dou26, Prop. 1]

- **Length:** +12 words.
- **Pressure test.** B2's proposed wording, "the obstruction that this argument instantiates", overstates slightly. Prop. 1's hypothesis (Chapman–Kolmogorov composition) is stronger than the P-divisibility of L90, so its stated conclusion is weaker than Theorem 3's, even though its proof uses only the one-step factorization. The proposed text attributes the argument, not the theorem.

#### R-16 — RHP14 and BD16

- **Covers:** I-113 (IMPRECISE).
- **Lines:** L90.
- **Evidence.**
  - RHP14 Thm 2.4 is an iff, of which L90 uses only the "only if" half. The "if" half needs contraction of every vector and invertible rooted maps.
  - BD16 v3, read first-hand: Prop. 1 is the semiclassical case and Cor. 1 the classical one.
- **Proposed text.**

  > **Current (L90).** This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].
  >
  > **Proposed.** This is the 'only if' half of the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1 and Cor. 1].

- **Length:** +8 words.

#### R-17 — explicit tasks for qubit simulation

- **Covers:** I-162 (IMPRECISE).
- **Lines:** L130.
- **Evidence.** Mon08 proves a lower bound on the ontological dimension and gives no task. The explicit finite prepare-and-measure tasks are HKLP24 Thm 4, which Main:538 cites as [55] and L130 already cites at the sentence's end.
- **Proposed text.**

  > **Current (L130).** explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and
  >
  > **Proposed.** explicit tasks are given by Galvão and Hardy [GH03] and Heinosaari et al. [HKLP24, Thm 4], and

- **Length:** +4 words.

#### R-18 — the Barandes and Schmidt dilations

- **Covers:** I-078 (IMPRECISE).
- **Lines:** L60.
- **Evidence.** Main's W equals Bar26's Thm 3.3 construction with Θ = √Γ entrywise. Bar26 fn. 1 reports an apparent error in Schmidt's partial-isometry construction, so "coincides with … Schmidt" claims more than was checked. Main makes no coincidence claim, and n is undefined at L60.
- **Proposed text.**

  > **Current (L60).** and the one-step $n^2$-dimensional ancilla dilation of [Main §3.1] coincides with the constructions of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]
  >
  > **Proposed.** and the one-step $n^2$-dimensional ancilla dilation of [Main §3.1], for a stochastic matrix on $n$ states, has the form of the dilations of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]

- **Length:** +9 words.

#### R-19 — [Sha79] unread

- **Covers:** I-222 (IMPRECISE, conditional on a first-hand check).
- **Lines:** L160; reference L335, which carries the VERIFY comment "content … cited from memory and not read".
- **Evidence.** BHa C4 proves the rank law (`bh01_access_v1/REPORT.md`:125–132). Its proof names the linear secret-sharing threshold ("This is the linear secret-sharing threshold") without a source (independent review, RC-6), and [Sha79], the Introduction's source for it, is unread.
- **Proposed text** (unless Sha79 is read first-hand before landing; OD-8):

  > **Current (L160).** and its linear case is the secret-sharing threshold [BHa; Sha79]
  >
  > **Proposed.** and its linear case is a rank law [BHa]

- **Length:** −1 word. The [Sha79] entry is removed if unused.

### Tier 4: imprecisions

#### R-20 — the BHa endpoint sentence: prior, population, and "sufficient for what"

- **Covers:** I-217, I-218, I-219, I-220 (IMPRECISE).
- **Lines:** L160.
- **Evidence** (all at `bh01_access_v1/REPORT.md@eae01647`):
  - :104–112 and :297: the bound holds under a uniform message prior with uniform unread data;
  - :155: the population is the 256 self-maps of {0,1}², with a two-bit message and one register unread, so |U| = 2 and the bound is 1/2. The 32 maps are those whose read register is constant;
  - :66–86: 14,496 and 36,416 bijections recover exactly with registers unread.
- **Proposed text.**

  > **Current (L160).** For bijective dynamics, complete endpoint access gives exact recovery, and with $\mathcal U$ inaccessible $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage in a bijective instance requires $|\mathcal U|\ge|\mathcal M|$; 32 non-injective maps of $\{0,1\}^2$ violate the bound on $P_{\mathrm{succ}}$ [BHa]. These endpoint guarantees are sufficient, not necessary.
  >
  > **Proposed.** For bijective dynamics, complete endpoint access gives exact recovery; with a uniformly distributed message, uniform unread initial data and $\mathcal U$ inaccessible, $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage in a bijective instance requires $|\mathcal U|\ge|\mathcal M|$; with a two-bit message and one register unread, 32 non-injective maps of $\{0,1\}^2$ fall below $1/2$ [BHa]. These endpoint conditions are sufficient for recovery, not necessary: bijections with registers unread can also recover exactly [BHa].

- **Length:** +25 words.
- **Pressure test.** B3's remark that the bound holds for any prior is an auditor's argument, not a corpus result, so the text keeps BHa's prior.

#### R-21 — what the §5 results are

- **Covers:** I-208, I-209, I-265 (IMPRECISE).
- **Lines:** L156, L175.
- **Evidence.**
  - BHa C1/C2 and BHb C1 are universal written proofs, checked exhaustively at small size (BHa REPORT:302).
  - BHa item F and BHb C6(b)–(d) are analyses of GR's formulas and theorems.
  - The toy models use the construction's layout with arbitrary bijections in place of the substratum dynamics (BHa REPORT:288–292). This is the surrogate check of the Code Review Rules.
- **Proposed text.**

  > **Current (L156).** The results below are finite computations in toy models of configurations, permutations and configuration reads. They concern the framework's nested-partition construction [GR App. A; Book §7.6], not a particular black hole.
  >
  > **Proposed.** The results below from [BHa; BHb] are written proofs and exhaustive finite computations in toy models of configurations, permutations and configuration reads; they use the layout of the framework's nested-partition construction [GR App. A; Book §7.6] with arbitrary bijections in place of its dynamics, and concern no particular black hole.

  > **Current (L175).** concern finite toy models, each proved on paper or checked exhaustively at small size or by exact arithmetic.
  >
  > **Proposed.** are finite toy-model results, each proved on paper or checked exhaustively at small size or by exact arithmetic, and analyses of the hypotheses of [GR App. A].

- **Length:** +28 words.

#### R-22 — the capacity bound: I* undefined, no locator

- **Covers:** I-102 (IMPRECISE).
- **Lines:** L84.
- **Evidence.** Main.md:492, Corollary (per-process capacity bound), defines $I^*=\sup_t I(X_{<t};X_{>t}\mid X_t)$. The kernel has `card_hidden_ge_two_pow_Istar` (C3Necessity:117) for the joint-law object of Theorem 2.
- **Proposed text.**

  > **Current (L84).** A realization of a law whose conditional past–future information reaches $I^*$ needs $|\mathcal C_H|\ge2^{I^*}$ (machine-checked in the same form as Theorem 2).
  >
  > **Proposed.** A realization of a law needs $|\mathcal C_H|\ge2^{I^*}$, with $I^*=\sup_t I(X_{<t};X_{>t}\mid X_t)$ its conditional past–future information (machine-checked in the same form as Theorem 2) [Main §3.4, Corollary (per-process capacity bound)].

- **Length:** +8 words.

#### R-23 — (C4): time index and positive probability

- **Covers:** I-105, I-105.a (IMPRECISE).
- **Lines:** L86.
- **Evidence.** (C4) ⇒ $M_t>0$ needs both histories to have positive probability, or their next-step laws are undefined, and the coincidence holds at the matching t (Main.md:97, :596).
- **Proposed text.**

  > **Current (L86).** in which two histories with the same present induce different next-step laws. In a faithful realization (C4) coincides with $M_t>0$
  >
  > **Proposed.** in which two positive-probability histories with the same present induce different next-step laws. In a faithful realization (C4) at $t$ coincides with $M_t>0$

- **Length:** +3 words.

#### R-24 — "deterministic completion" (undefined, and used in a second sense at L136)

- **Covers:** I-299 (IMPRECISE); I-008 (FAITHFUL in B1; resolved below).
- **Lines:** L12, L189.
- **Disagreement.** B1 rated the abstract's "every deterministic completion carries the visible memory" FAITHFUL, reading it as "faithful realization". B4 rated the same wording at L189 IMPRECISE. The content is correct at both sites; it is Theorem 2(c), and B1 is right on content. But the term is undefined in the Introduction, and L136 uses "deterministic completion" in the Bell sense of any deterministic hidden-variable completion. So B4's reading holds for both sites.
- **Proposed text.**

  > **Current (L12).** every deterministic completion carries the visible memory in its hidden state
  >
  > **Proposed.** every reversible realization of a law carries its visible memory in its hidden state

  > **Current (L189).** which every deterministic completion carries in its hidden state
  >
  > **Proposed.** which every faithful realization carries in its hidden state

- **Length:** +3 words.

#### R-25 — "(each with one step not machine-checked)"

- **Covers:** I-010 (IMPRECISE).
- **Lines:** L12.
- **Evidence.**
  - The count is right for Theorem 2(c) (the time-t identification, L80) and for readback (the history-level step, L96).
  - It is wrong if the memory clause is read as the Corollary, which has two unchecked ingredients (L82).
  - Main.md:580 states the split.
- **Proposed text.**

  > **Current (L12).** (each with one step not machine-checked)
  >
  > **Proposed.** (each machine-checked except for steps proved on paper)

- **Length:** +2 words.

#### R-26 — open problem (4): (C2) necessity is proved under a hypothesis

- **Covers:** I-294 (IMPRECISE); CMP-24 (low, strengthen); I-109's note.
- **Lines:** L185.
- **Evidence.**
  - Main.md:433 and :447@eae01647 prove (C2) necessity on paper under the mixing hypothesis;
  - the ledger (Main.md:720) and GR.md:565 say "conditional";
  - ROADMAP.md:1591 lists the hypothesis as a declared input.

  The open item is the hypothesis, not the necessity.
- **Proposed text.**

  > **Current (L185).** (4) (C2) necessity, which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §3.4]
  >
  > **Proposed.** (4) whether the hidden-sector mixing hypothesis, motivated by eigenstate thermalization, under which the necessity of (C2) is proved on paper, holds for a physical hidden sector [Main §3.4]

- **Length:** +11 words.

#### R-27 — open problem (1): which steps lack a machine check

- **Covers:** I-289 (IMPRECISE).
- **Lines:** L185.
- **Evidence.** The listed steps are unformalized (B4 grepped OIBridge), but the list omits §3.1's Hadamard example and §3.4's factorization half. R-07 adds further paper-only results to §3.4.
- **Proposed text.**

  > **Current (L185).** (1) machine checks of the steps of §2.2, §2.4 and §2.5 that lack one
  >
  > **Proposed.** (1) machine checks of the steps of §2 and §3 proved only on paper

- **Length:** 0.

#### R-28 — the §3.3 heading

- **Covers:** I-147 (IMPRECISE).
- **Lines:** L122.
- **Evidence.** Main.md:624: representability, with ordinary coherence, does not select the relating evolution, and the selection question is open. The bare heading reads as "nothing selects it".
- **Proposed text.**

  > **Current (L122).** ### 3.3 The evolution relating two times is not selected
  >
  > **Proposed.** ### 3.3 Representability does not select the evolution relating two times

- **Length:** +1 word.

#### R-29 — the §4 labels

- **Covers:** I-182, I-277 (IMPRECISE).
- **Lines:** L144, L178.
- **Evidence.**
  - GR uses "Level G1–G4" both for its dependency ladder (GR.md:12) and for Structure's gauge axis (GR.md:30, :597, :681), signal S12; ch19 says "rung".
  - GR.md:356: the descriptive distinction is established, and only the proposal is conditional.
- **Proposed text.**

  > **Current (L144).** (Level G3 of [GR])
  >
  > **Proposed.** (rung G3 of the dependency ladder of [GR])

  > **Current (L178).** §4 is conditional on the covariant field equations
  >
  > **Proposed.** §4's proposal is conditional on the covariant field equations

- **Length:** +5 words.

#### R-30 — "send it to different futures" read universally

- **Covers:** I-025 (IMPRECISE).
- **Lines:** L20.
- **Evidence.** A realization with $f_x$ constant on the posterior's support is visibly deterministic (`process_dilation_probes.py`, P4). Main.md:105 has the same wording, which is a corpus item for PR-H.
- **Proposed text.**

  > **Current (L20).** Hidden states compatible with the same $x$ send it to different futures, so the visible sector evolves stochastically
  >
  > **Proposed.** Hidden states compatible with the same $x$ can send it to different futures, so the visible sector can evolve stochastically

- **Length:** +2 words.

#### R-31 — "What the paper states are the cited theorems and their scopes."

- **Covers:** I-280 (IMPRECISE, unsupported).
- **Lines:** L179.
- **Evidence.**
  - The sentence is narrower than the paper, which also states a hypothesis, a proposal, computations, open problems and uncited examples.
  - It is self-description of the kind §A.32 removes.
  - Deleting it loses nothing: item 8's first sentence stands alone.
- **Proposed text.** Delete " What the paper states are the cited theorems and their scopes." (L179).
- **Length:** −11 words.

#### R-32 — "A card arrangement violates no Bell inequality"

- **Covers:** I-383 (IMPRECISE).
- **Lines:** L255.
- **Evidence.**
  - True for local card moves with settings independent of the deal: Main.md:360, Theorem (Bell ceiling for a screened local completion), and the book's "local classical toy".
  - False without that restriction by Main.md:356 (unrestricted finite reversible dynamics realizes PR-box behaviour), in the very section cited.
  - §6.2 item 6's "it violates no Bell inequality" (I-274, FAITHFUL) refers to the specific game of B.3, so B4 and B5 do not conflict.
- **Proposed text.**

  > **Current (L255).** A card arrangement violates no Bell inequality [Book §1.11; Main §3.3].
  >
  > **Proposed.** A card arrangement whose moves act only on each player's own cards, with settings chosen independently of the deal, violates no Bell inequality [Book §1.11; Main §3.3, Theorem (Bell ceiling for a screened local completion)].

- **Length:** 0 in the main text (+24 in Appendix B).

#### R-33 — "the fixed-dimension form is false" stated without its evidence (low)

- **Covers:** I-291 (IMPRECISE, independent review RC-5); CON-26.
- **Lines:** L185.
- **Evidence.** Main.md:594@eae01647 supports the falsity with `memory_probes.py`, which searches the uniform prior only and computes entropies in floating point. The audit's countercheck over arbitrary priors (`matrix/scripts/b4probe/fixeddim.py`) is a Nelder–Mead optimisation. The claim ranges over all realizations of fixed hidden dimension; neither probe covers that scope exactly, and the counts disagree (Main's "1 of 15" against the audit's "2 of 16", unresolved).
- **Proposed text.**

  > **Current (L185).** (the fixed-dimension form is false)
  >
  > **Proposed.** (the fixed-dimension form fails in numerical probes [Main §3.4])

  Alternatively, keep the flat statement once Main carries an exact certificate.
- **Length:** +3 words.

### Coverage check

Every non-FAITHFUL matrix row maps to a finding:

| Row | Finding | Row | Finding | Row | Finding | Row | Finding |
|---|---|---|---|---|---|---|---|
| I-010 | R-25 | I-105 | R-23 | I-146 | R-06 | I-219 | R-20 |
| I-015 | R-06 | I-105.a | R-23 | I-147 | R-28 | I-220 | R-20 |
| I-025 | R-30 | I-113 | R-16 | I-159 | R-07 | I-222 | R-19 |
| I-042 | R-11 | I-114 | R-12 | I-162 | R-17 | I-225 | R-01 |
| I-052 | R-11 | I-116 | R-15 | I-182 | R-29 | I-246 | R-05 |
| I-054 | R-03 | I-121 | R-13 | I-206 | R-14 | I-258 | R-06 |
| I-071 | R-08 | I-123 | R-04 | I-208 | R-21 | I-265 | R-21 |
| I-078 | R-18 | I-124 | R-04 | I-209 | R-21 | I-277 | R-29 |
| I-102 | R-22 | I-127 | R-02 | I-217 | R-20 | I-280 | R-31 |
| I-103 | R-03 | | | I-218 | R-20 | I-281 | R-06 |
| I-289 | R-27 | I-292 | R-09 | I-294 | R-26 | I-299 | R-24 |
| I-300 | R-05 | I-383 | R-32 | I-223 | R-01 | I-286 | R-01 |
| I-291 | R-33 | I-040 | R-34 | | | | |

The completeness rows recommended *add* or *strengthen* map as follows: CMP-01 to R-07, CMP-02 to R-06, CMP-03 to R-06, CMP-08 to R-07, CMP-17 to R-10, CMP-22 to R-08 and CMP-24 to R-26.

***

## (b) Optional changes

The *cite* recommendations of COMPLETENESS.md and the low-priority items. None is needed for faithfulness; each adds words against the budget.

| ID | Source | Change | Lines | Words | Note |
|---|---|---|---|--:|---|
| O-1 | CMP-05 | §3.3: where coherent completions exist (on some finite carriers none does), two with the same complete operational data are related by a unitary or one global antiunitary, and no selector reading only those data fixes which (machine-checked) [GR §3.3] | L124–L126 | ~45 | State the existence caveat with the classification, so it is not read as "OI determines QM up to orientation". |
| O-2 | CMP-07 | §3.3: the one-time freedom is classified exactly (the off-diagonal part of the fibre-Gram data modulo phases) [Main §3.4, Remark (scope …)] | L124 | ~30 | Not to be called machine-checked until Main cites `TwoSidedGauge` (§A.35). |
| O-3 | CMP-09 | §3.5: measurement dependence costs at least 0.031 bits for the quantum CHSH value (a necessary bound); without spatial structure, Theorem 1's realizations produce PR-box correlations [Main §3.3] | L136 | ~45 | |
| O-4 | CMP-12 | Open problem (2): "over realizations reduced to the canonical predictive quotient [Main §3.4]" | L185 | ~10 | |
| O-5 | CMP-14 | L38: "(machine-checked)" after "maximal-entropy default"; add `determinism_reversibility_selected_measure` (CanonicalMeasure:276) to Appendix A | L38 | 1 | Needs a new axiom report (OD-15). |
| O-6 | CMP-23 | Open problem (3): "(for rooted families, periodicity is necessary and sufficient [Main §3.4])" | L185 | ~12 | Only after Main states it with a census anchor (OD-4). |
| O-7 (now required, in R-01) | CMP-25 | §5, after the H-scramble failure: "under a permutation, entanglement at an aligned bipartition never exceeds the basis entropy of the initial state [BHb, C2]" | L162 | ~25 | Sharpens R-01. |
| O-8 | CMP-10 | §2.4: one sentence naming Main's Characterization theorem, labelled "proved on paper; not machine-checked", time-homogeneous | L86 | ~45 | OD-6. |
| O-9 | CMP-04 | §3.2: (iii)–(v) restated as observational independence, reversible richness and observer recursion, each independent of the OI core [GR §3.3] | L120 | ~25 | Risks reading as a derivation; not recommended. |
| O-10 | CMP-18 | One pointer sentence to [SM], "conditional on the carrier hypothesis H-link" | L26 | ~20 | Outside the deliberate scope. |
| O-11 | CMP-17 (c)(d) | §6.3: the (Obs, μ) observer interface, and (C4) at the lattice cut beside the cosmological one | L183, L185 | ~25 | ROADMAP-only (OD-14). |
| O-12 (now required, in R-07) | CMP-01 | Abstract: one clause on the ε-realization | L12 | ~20 | OD-3. |
| O-13 | CMP-26 | §5: "accessible advantage cannot decrease as records accumulate, though advantage from the current records alone can [BHa, D1–D2]" | L160 | ~20 | |
| O-14 | CMP-11 | §3.3: the kernel non-uniqueness of the continuous interpolation (`continuous_extension_not_unique`) | L124 | ~20 | A second non-selection result. |
| O-15 | CMP-06 | Bohr-frequency completeness, kernel half only; the two-branch form rests on the open H-BG | — | — | Leave out. |
| O-16 | CMP-13, CMP-15, CMP-16, CMP-19, CMP-20, CMP-21 | — | — | — | Leave out. Each is outside the Introduction's scope or would lend a conditional result more weight. |
| O-17 | B5 | References [BHa], [BHb]: add "not adopted", mirroring the records' own README wording | L267, L269 | 4 | |
| O-18 | B1 | §2.1's \|C_V\| ≥ 2 is narrower than the kernel needs (`Fintype V`); harmless as written | L36 | 0 | No change recommended. |
| O-19 | CON-45 | H-Bell's third clause (Substratum:132) is the adopted branch itself; the Introduction's two-clause reading matches Main | L136 | 0 | No change. |
| O-20 | CON-47 | L126 states the two directions separately, which is the faithful form; the corpus side (Main:624) is PR-B | L126 | 0 | No change. |
| O-21 | CON-37 | "Level G3" → "rung G3" (R-29) suffices; Main's (G1)–(G3) genericity labels are a corpus item | — | 0 | |
| O-22 | B4 | `levelOne_eq` reports propext only; Appendix A does not cite it, so "exactly these three" (L195) holds | L195 | 0 | No change. |
| O-23 | B4 | The reproduction recipe reads `papers/introduction_repro/` by relative path, so it needs a clone that contains #918 or its landing; state this if the recipe is kept | L195 | ~10 | |
| O-24 | B1 | Define n where the n²-dimensional dilation first appears (R-18 does this) | L60 | — | Folded into R-18. |
| O-25 | Offsets | The cuts C-1–C-8 of OD-13 | various | −212 | Each is optional; together they absorb most of the required additions. |
| O-26 | E3-16 | L198: cite the version DOI of release 3.1.4, 10.5281/zenodo.23608753, beside the concept DOI, which resolves to the latest version; the 3.1.4 archive carries the probes byte-identical to the corpus commit | L198 | ~8 | |

***

## (c) Owner decisions

Each decision gives the options, a recommendation and the reason.

**OD-1. Main's title.**
- **The issue.** [Main] is cited at L261 as "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation".
- **The evidence.** Main's own scope statements (Main.md:20 and :758: "exact bidirectional equivalence of finite observable stochastic laws and their quantum representations") and GR §3.3's kernel result that bare finite OI does not imply QM are narrower than the title. The Introduction denies a derivation (I-145, I-252) and must cite the title as it is (CON-16).
- **Recommendation.** Retitle Main in a corpus PR, for example "… The Finite-Law Equivalence of Embedded Observation and Quantum Representations", and update Methodology.md:585, Structure.md:1416 and the Introduction's reference.
- **Reason.** The title is the one place where the corpus claims more than Main's own theorem, and the Introduction cannot correct it from outside.

**OD-2. Whether and how to report the substratum-sourcing results (R-06).**
- **Recommendation.** Report them: the full L120 text, the abstract sentence, the narrowed §6.2/§6.3 items, and the Appendix A declarations.
- **Reason.** The owner's goal names "what remains open". The corpus has narrowed this open question with kernel results, and L120, L173, L183 and the abstract state it as if nothing were known (CMP-02, high). The converse clause (CMP-03) also guards against an overclaim: it says that Theorem 4 classifies and does not derive.
- **Short form withdrawn.** After the independent review, required content is not shortened for budget (OD-13), and the earlier short L120 form lacked the permutation-operator premise and the "as formalized" label (RC-4).
- **Do not cite** `frozen_sourcing_verdict`: its census family is kernel-only.

**OD-3. The ε-realization addition (R-07).**
- **Recommendation** (independent review, RC-3). Add the full R-07 text to §3.4 as proved on paper, without "exact probes", together with the abstract clause (O-12). The short form is withdrawn.
- **Reason.** Without it §3.4 reads the obstruction as the whole story; both results must appear with their domains, assumptions and proof strengths (owner, 2026-10-26). Required content is not traded for page budget (OD-13).

**OD-4. Kernel-only results that no manuscript states.**
- **Affected results.** Three results the Introduction states or would state rest on census families marked `kernel-only`:
  - the general Theorem 3 (RecurrenceHorizon; R-12);
  - the routed-readback conclusion (PhysicalC4Discharge and PhysicalC4StorageReadback; R-13);
  - the all-time rooted classification (RootedClassification*; R-09, O-6).

  FrozenSourcing and QuantumRepresentationT2 are kernel-only as well.
- **A second gap.** `verification/lean-manuscript-census.json` does not list `papers/Introduction.md` among its manuscripts, so the census checks none of the Introduction's identifiers.
- **Recommendation.** Make a corpus PR (PR-G) before the Introduction lands:
  - Main §2.3 states the general rooted overlap form and the routed-readback conclusion with their kernel anchors.
  - Main §3.4's consolidation remark (Main.md:618) states the rooted classification and narrows open item (a) to multi-time laws.
  - Each family moves from `kernel-only` to `current` with an anchor (§A.35).
  - `papers/Introduction.md` is added to the census manuscripts on landing.
- **Reason.** The Introduction would otherwise be the only publication-facing site for three kernel results, outside the census contract.
- **Not recommended.** Leaving them uncited would understate Theorem 3, which the Introduction already states in general form and which is fully proved in the kernel.

**OD-5. Which routed-readback declaration to cite (R-13).**
- **Recommendation.** Cite `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256) as primary and keep `routed_forces_indivisible_somewhere` as the seed-conditioned reading.
- **Reason.** The storage-time predicate transcribes the Introduction's gloss (L96). The cited module itself records that its frozen spelling differs from that clause (PhysicalC4Discharge:27–29), and both proofs reach the same conclusion.
- **Cost.** One new axiom report (OD-15).

**OD-6. Naming the Characterization theorem.**
- **Recommendation.** Do not name it.
- **Reason.** The Introduction carries its proved content at equal or higher rigor: Theorem 1 (kernel) for existence, the Corollary, the Pinsker bound, and L86. The theorem itself is proved on paper only, has no ledger or census row (CON-17), and its clause (i) is imported under (T).
- **If named.** Use O-8's sentence, with its status and the time-homogeneity hypothesis. Main's §3.4 heading ("The Characterization Theorem: Necessity of the Conditions") is the section the Introduction already cites for Theorem 1.

**OD-7. The "exact probe" convention (R-03).**
- **Recommendation.** Narrow the definition to "a computation in exact rational arithmetic on stated small instances", and drop the tag at L84. In the corpus, Main.md:170's "Certified exactly" becomes a numerical statement (CON-25, PR-F).
- **Alternative.** Keep "exhaustive" and relabel L56 as well.
- **Reason.** No probe the Introduction cites is exhaustive over a class.

**OD-8. [Pag93], [Sha79] and the VERIFY comments.**
- **[Pag93] (R-14).** Add Page, "Information in black hole radiation", PRL 71, 3743 (1993), as a separate entry after a first-hand read, and cite it at L156. Otherwise drop Pag93 from L156; it stays at L162 for $S_{\rm Page}$.
- **[Sha79] (R-19).** Read it first-hand before landing, or drop it and cite [BHa] alone.
- **[CT06] and [Har04].** These also carry VERIFY comments. CT06 is cited for two textbook facts (the vanishing criterion and Pinsker's inequality); a first-hand check of the edition's locators is recommended. Har04 is cited only "as reported in [Mon08]", which the wording at L130 already says.

**OD-9. Restating GR Theorem A.8 (CON-01).**
- **Recommendation.** In a corpus PR (PR-E):
  - GR restates A.8 over an ensemble of initial pure states, or with a non-aligned bipartition, and recounts the excluded fraction over that ensemble;
  - the "fails" sentence moves into A.8 itself;
  - appendix A row G11 and ch19:72 mirror the caveat.

  The Introduction's §5 then follows the restated theorem, replacing R-01's text.
- **Reason.** As stated, A.8's hypothesis fails in the setting where its conclusion is counted.

**OD-10. A minimality claim for the card game (R-04).**
- **Recommendation.** No minimality claim.
- **If kept.** "the fewest possible, since with one hidden value every $\Gamma_s$ is a permutation matrix" (+14 words), after Main or the book states it with that measure (CON-24).

**OD-11. The empirical record.**
- **The issue.** Book appendix A reports empirical comparisons for S-class rows. Those test OI together with a specific substratum and named hypotheses, not OI as stated in §1.1.
- **Recommendation.** Keep §6.2 item 5 ("No claim that the physical hypothesis is established or tested") and adopt R-06's abstract wording ("any experiment that distinguishes OI from standard quantum theory").
- **Reason.** Both are faithful for OI as stated. Mentioning the applications' comparisons would need their hypotheses and would leave the paper's scope.

**OD-12. OI⁺ and the coherent-completion classification (CMP-04, CMP-05).**
- **Recommendation.** Leave out OI⁺ (O-9), which restates Theorem 4. Add the coherent-completion classification (O-1) only if the budget allows, with its existence caveat.

**OD-13. The length budget.**
- **The numbers.** The main text has 4,966 words in 12 pages.
- **Candidate cuts**, each checked to remove no claim the audit needs:

| Cut | Line | Words | What goes |
|---|---|--:|---|
| C-1 | L28 | −26 | "It presents the established mathematical results of OI together, …" (self-description, §A.32) |
| C-2 | L26 | −15 | "Neither application is a demonstrated resolution of its problem; §6 states what would decide each." (restated in the abstract, §6.2 and §6.4) |
| C-3 | L162 | −28 | Shorten the single-shell gloss to "That requires the energy to be constant there." |
| C-4 | L150 | −28 | Condense the related-work sentence to "The trace-free Einstein equations [EvEMU11] and vacuum-energy sequestering [KP14] also remove the vacuum energy of matter as a source of curvature, and Volovik argues that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]." |
| C-5 | L60 | −26 | The [SGD19]/[Milz20] omitted-measurement clause and the [Milz20] reference |
| C-6 | L142 | −15 | "The invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum energy;" |
| C-7 | L108 | −43 | The [Cal26] contrast and its reference |
| C-8 | L177 | −31 | §6.2 item 6 reduced to "No claim that the card game produces quantum rather than classical statistics (Appendix B.3)." |

- **After the independent review.** The required additions are about +610 words in full form; the short forms of OD-2 and OD-3 are withdrawn for required content. With C-1–C-8 the net is about +400 words, roughly one page.
- **Recommendation** (independent review). Required content (R-01, R-06 and R-07 in full) is not traded for budget. Take C-1–C-8 first, build and measure. If the main text then exceeds 12 pages, the owner decides between relaxing the 12-page constraint and further editorial cuts that remove no claim the audit needs; R-10 is deferred only for its citation (RC-7), not for length.
- **AGENTS.md check.** After building, check the page count and the median characters per page.

**OD-14. Citing ROADMAP-only open items.**
- **The issue.** The open status of the complex matrix kinematics (R-10), the (Obs, μ) interface and the lattice cut of (C4) is stated only in ROADMAP.
- **Recommendation.** Land CON-15's one clause in GR §3.3 and Main §3.4 (PR-B), so that R-10 can cite [GR §3.3]. Do not add ROADMAP to the reference list.

**OD-15. Extending Appendix A and the retained Lean result.**
- **The issue.** R-06 and R-13, and O-5 if adopted, add declarations to Appendix A. Each needs its `#print axioms` report in the retained expected result `papers/introduction_repro/`, regenerated by its recipe at `17b830bc`, whose sources are identical at the corpus commit. The L195 sentence then covers them.
- **Recommendation.** Regenerate the result in the same revision (§A.42).
- **Line numbers.** All proposed module:line references were read at `eae01647`, where the OIBridge sources are byte-identical to `17b830bc`.

***

## (d) Corpus corrections outside the Introduction

These are proposals for separate PRs; this audit edits no corpus file. Rows marked † also touch the Introduction: their corpus side is listed here, and their Introduction side is in part (a). Severity is CONSISTENCY.md's.

| PR | Scope | Rows not touching the Introduction | Rows also touching it (corpus side) | Highest severity |
|---|---|---|---|---|
| PR-E | Black-hole status | — | CON-01† (GR A.8 restatement, appendix A G11, ch19:72; OD-9), CON-02† (book "resolved" at ch07:110, ch19:20/:72, ch09:125, ch19:334 and FULL), CON-03† (BHa REPORT header against its review) | high |
| PR-A | Cosmological constant and GR status | CON-05 (GR:573 unconditional), CON-07 (appendix C:317 "proofs are complete"), CON-08 (GR:352/ch07:185 "determined", optional), CON-31 (dark-sector budget "Derived"), CON-36 (GR universality theorem without a written proof) | CON-04† ("Dissolution" headings at GR §6, ch07 §7.7, ch18:142 and ch19 §19.2; ch00:97, SM:1576), CON-06† (GR:344, ch07:177 assert Einstein's equations while G3 is open) | medium |
| PR-B | Quantum-emergence reach and status | CON-09 (GR:330 "delivers QM"), CON-11 (measurement problem "Dissolved"; Main:666–672), CON-13 (Main:220 Schrödinger), CON-14 (Main:99, :210, :348, :758 framing), CON-29 (H-BG status at first use), CON-46 (ch00:39 scope), CON-48 (GR:216 setting omits fields) | CON-10† ("derivation of QM" at Substratum:420, Structure:1294, ch01:261, ch02:120), CON-12† and CON-44† (Born-exponent framing: Main:220, :345, ch18:34, ch19:126), CON-15† (kinematics clause; OD-14), CON-16† (Main's title; OD-1), CON-45† (H-Bell clauses), CON-47† (Main:624 directional witnesses) | medium |
| PR-C | Main §3 remarks, the Characterization theorem and appendix B | CON-17 (no census or ledger row), CON-18 (Main:72 reference), CON-19 (appendix B.7.6's proof structure), CON-23 (Main:131, :717 hypothesis), CON-27 (Main:706 against :704), CON-30 (appendix B.2.5 scope), CON-38 (ch18:64), CON-39 (appendix B:280 drafting residue) | CON-42† (Main:334 "is asserted" and :606) | medium |
| PR-D | SM numerics and #939 residue | CON-32 (SM:14 and Juno:140 "0.23σ" against 0.8σ), CON-33 (chain-table labels), CON-34 (appendix A cells, Juno:346), CON-35 (counts at ch06:12, ch07:321); CON-40 is a verification summary needing no action | — | medium |
| PR-F | Probe and evidence statements | — | CON-25† (Main:170 "Certified exactly"), CON-26† (Main:594 states the prior class; its count differs from B4's recheck and is unresolved), CON-24† (Main:178 heading, ch01:273 "minimal") | medium |
| PR-G | Kernel-only results into the manuscripts, with census anchors | — | CON-41† (general Theorem 3 in Main §2.3), CON-28† (rooted classification in Main:618), CON-43† (routed readback); and the Introduction added to the census manuscripts (OD-4) | low, but a precondition for R-09, R-12 and R-13 |
| PR-H | Foundations wording | — | CON-21† (Methodology:235/:253 "bijectivity … lemma"), CON-22† (Main:46 finiteness from Lemma 1), CON-37† (label collisions); and Main:105's universal wording (R-30) | medium |

- **Count.** All 25 rows that do not touch the Introduction are in PR-A to PR-D: CON-05, -07, -08, -09, -11, -13, -14, -17, -18, -19, -23, -27, -29, -30, -31, -32, -33, -34, -35, -36, -38, -39, -40, -46 and -48.
- **Mapper notes.** These corpus findings in the mapper notes are covered by these rows: B1's Main:46 (CON-22), GR:326 (CON-04), ch01:261 (CON-10), Main:706 (CON-27); B2's ch00:39 (CON-46), Main:624 (CON-47); B4's appendix C:317 (CON-07), Main:758 (CON-14); B5's ch01:273 (CON-24) and appendix B:92 (CON-30).

***

## (e) What the Introduction gets right

The record shows a careful paper whose defects are local.

- **Overall.** 358 of 409 rows are FAITHFUL. There are two OVERCLAIM verdicts (R-01 and R-02), and no central claim is too weak to stand (COMPLETENESS.md: the deliberate limits are all borne out). Those limits are: no derivation of QM, the Born exponent not selected, Λ a proposal, and the Page curve not established.
- **Theorem 1.** Exactly as stated: each inclusion is kernel-proved by its own declaration (`S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`), and the Lean classes match §2.1's definitions, including the correlated initial law of D_K and the every-step fixed-basis readout of Q_K (B1, B5).
- **Theorem 4.** Kernel-proved in both directions, with separate witnesses for each (§A.34; `exactAll_iff_physical_general` is literally the pair), for every nonempty finite carrier. Its standing structure matches the kernel's fields more completely than GR's own prose (CON-48).
- **Status splits.** The Introduction states the kernel/paper division precisely where it matters: Theorem 2 for a joint law, with the time-t identification on paper; the Corollary's two unchecked ingredients; and readback in routed form.
- **Appendix A.** All 28 declarations sit at the stated module:line. Each retained `#print axioms` report reads exactly `[propext, Classical.choice, Quot.sound]`, and the build and gate passed in the retained record (B5).
- **Appendix B.** Every number was re-derived in exact rational arithmetic (B5).
- **§4.** Faithful throughout: the conditional status, the open G3 rung, Λ as an input, the dimensional identity, and the Weinberg citations placed as the reference audit applied them.
- **§5.** The status statements are faithful (H-decouple, the proper shell, the single trajectory, the GSL, islands).
- **More careful than parts of the corpus.** On several points the corpus overstates and the Introduction follows the authoritative anchor: the book's "resolved" information paradox (CON-02), the "Dissolution" headings (CON-04), Einstein's equations asserted while G3 is open (CON-06), "derivation of QM" (CON-10), the Born-exponent framing (CON-12, CON-44), bijectivity as a lemma (CON-21), and finiteness from Lemma 1 (CON-22).
- **Literature.** The attributions checked first-hand hold, apart from the five in R-14–R-18: EGGH26, Bar23, Bar25, Bar26, SGD19, RHP14, BD16, BJA17, BLP09, HKLP24, LP17, Dou26, and the earlier audit's Wei89, EvEMU11, KP14, Vol06, tH14, Cal26 and BBS24.

***

## (f) Method and limits

**What was checked, and how.**
- **Claims.** 385 claims and 24 directional sub-claims (`inventory/claims.json`), each a verbatim span of the Introduction at `4a260ca9`, checked mechanically. Equivalences were traced one direction at a time (§A.34).
- **Mapping.** Every row traced to its strongest source across the core corpus (Main, GR, SM, Substratum, Structure, Methodology, Juno, the book's appendices and physics chapters, OIBridge, the census registry, the coverage ledger, ROADMAP and the black-hole programme records), at `eae01647`. Each link records a layer and a status, and each row takes its weakest link (PLAN.md, step 3; `MATRIX.md`).
- **Kernel declarations.**
  - Every Appendix A identifier was grepped at its module:line and its statement read (B5).
  - For this synthesis, every declaration the proposed texts cite was grepped at `eae01647`, and its census family and status read from `verification/lean-manuscript-census.json`. This check removed `frozen_sourcing_verdict` and exposed the kernel-only families of OD-4.
- **Exact arithmetic.**
  - Appendix B was re-computed with `Fraction` and sympy (B5).
  - The I-123/I-124 disagreement was re-computed exactly for this synthesis (R-04).
  - B4's fixed-dimension countercheck (`matrix/scripts/b4probe/fixeddim.py`) is a Nelder–Mead optimisation, so it is numerical evidence, not certification.
- **Literature read first-hand.** By the mappers: EGGH26, Bar23, Bar25, Bar26, Sch21, LP17, BD16, Dou26, SGD19, RHP14, BJA17, BLP09 and HKLP24. For this synthesis, Dou26 v3 §4.2.1 and BD16 v3 Prop. 1/Cor. 1 were re-read.
- **Proposed texts.** Each *Current* span was checked to be a verbatim substring of its line, and each proposed text was word-counted (scratch scripts, not committed).

**What was not checked.**
- **No Lean rebuild.** The axiom reports come from the retained record `papers/introduction_repro/results-121598983127.json` at `4a260ca9` (run 40330683786, job 121598983127), which exists only on #918's branch. The proposed new Appendix A declarations have no retained report yet (OD-15).
- **Unread sources.**
  - [CT06] and [Har04] are unread, and [Sha79] too; the mappers relied on standard content and on reports.
  - [Pag93] and Page's 1993 PRL were checked at abstract level only.
  - [Mon08] was read in its retained text by B2, not re-read here.
  - [Milz20] was read in the earlier audit and not re-read.
- **Classifications by hand.** Some proof-location classifications in the inventory are hand overrides (`inventory/scripts/proofs/proof_overrides.py`).
- **Unresolved count.** CON-26's count (Main's "1 of 15" against B4's "2 of 16 over arbitrary priors") was not reproduced by mapper C or here.
- **The corpus commit.** The corpus was read at `eae01647`, not re-checked against any later `main`. PLAN.md requires a re-check if `main` has moved before the Introduction is revised.
- **No build.** Page counts in part (c) are word-based estimates, not builds.
- **Audit-internal defects found during synthesis** are corrected: `matrix/resolutions.json` applies the resolved verdicts, statuses and fixes (I-008, I-013, I-123, I-124, and the independent review's I-223, I-225, I-286, I-291, I-040 and RC-12 status changes), and CMP-10 cites CON-17 to CON-19 in its generator and its outputs.
- **Status labels.** `exhaustive-exact` marks exhaustive enumeration in exact arithmetic over a stated finite domain; `numerical` marks floating-point or otherwise inexact evidence (independent review, RC-12).
- **Independent review.** `review/INDEPENDENT-REVIEW.md`: ACCEPT WITH CHANGES; its required changes RC-1 to RC-12 are applied in this file and the matrix. The evidence verification of PLAN.md step 7 and its independent review are separate.

