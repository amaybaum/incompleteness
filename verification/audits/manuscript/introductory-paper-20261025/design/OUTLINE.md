# Introductory paper: outline (design stage, for owner review)

Stage: paper design only, as approved by the owner on 2026-10-26. This outline drafts no paper
text and changes no repository file. Claim IDs (`§3-a`, …) are defined in `SOURCES.md`. That file
gives each claim's exact file:line, its kernel declaration, its verification layer, its correctness
status, its originality class and its evidence basis.

- **Main commit.** `687e885b1cfd24d6f17eee439101afc8acf07015` (Merge #933).
  - #932 changed Main:522 and Main:610 one line for one, so Main's line numbering is the same as
    at `52e2db40`, the novelty audit's base.
  - The only other changes since `52e2db40` are GR:20, glossary:39 and FULL (F29), and ch18 (PE-01).
    This was checked by `git diff 52e2db40 687e885b`.
- **Novelty classes.** From `novelty-v5/AUDIT.md` r4, as re-checked (Rc4, ACCEPT WITH NITS), at the
  audit branch head `1e9c05c7`. That branch is not on `main` (see `SOURCES.md`, "Provenance").
- **Black-hole findings.** Only results whose package has a separate-agent internal review that
  closes with ACCEPT count as established here: BH-01 at `df2ea6f5` and BH-02/BH-04 at `ce7937d2`.
  Everything else in the black-hole programme is cited as open. Since review, the packages have
  had wording-only changes (`606c98d8`, `84aca6b0`; diff checked). Their own status line says the
  review is "not external validation or owner adoption" (`bh01_access_v1/review/README.md:3`).

## Positioning

The paper is a **technical perspective with original mathematical components**. It is not a new
derivation of quantum mechanics. It is written for physicists and mathematicians and runs 12–15
pages. It is built on the finite observable-law correspondence of Main, with a bounded black-hole
information illustration.

- Correctness and originality are kept in separate columns throughout. A kernel proof is not
  evidence of originality, and a KNOWN class is not evidence against correctness (AUDIT:37–42,
  :308–311).
- The paper follows the technical register of §A.32/§A.33: no self-assessment, no reader
  instructions, no revision-history voice, and no capitals for emphasis.

**Working title** (PLAN.md:3–4): *Observational Incompleteness: From Deterministic Dynamics to
Quantum Observations*. Its "from … to" form can be read as announcing a derivation. That is the
same exposure as Main's title (F4, open), so the title is risk R1 and an item for the owner.
Neutral alternatives:
- *Observational Incompleteness: Finite Observable Laws of Embedded Observers and Their Quantum
  Representation*;
- *Embedded Observation and the Finite Stochastic–Reversible–Unitary Correspondence*.

## Displayed equivalences and their directional witnesses (§A.34)

Every displayed equivalence must name a kernel witness for each direction, beside the display.

| Display | → witness | ← witness | Where |
|---|---|---|---|
| **E1** $S \iff D \iff Q_{\mathrm{fb}}$ (finite horizon $K$, finite alphabet) | S→D `S_imp_D` (Equivalence:422); D→Q `D_imp_Qfb` (:294); Q→S `Qfb_imp_S` (:245) | D→S `Qfb_imp_S ∘ D_imp_Qfb`; Q→D `S_imp_D ∘ Qfb_imp_S`; S→Q `D_imp_Qfb ∘ S_imp_D` — the compositions at Equivalence:466–468, assembled in `finite_horizon_equivalence` (:462) | §3 |
| **E2** (operational-completion characterization) on a nonempty finite carrier, the available families at every ancilla level are exactly the normalized finite Kraus instruments ⟺ conditions (i)–(v) | `physical_of_exactAll` (PhysicalCharacterization:301) | `exactAll_of_physical_general` (GeneralCarrier:93), via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness` (AncillaClosure:373), `exactAll_of_levelOne` (LevelOneSeam:196); assembled in `exactAll_iff_physical_general` (GeneralCarrier:100) | §6 |
| *Alt only:* **E3** rooted family realizable by one finite permutation with a shared prior ⟺ `PPer` | `pper_of_finiteRootedRealizable` (RootedClassification:339) | `pper_has_responseRealization` (RootedClassificationAllTime:162); assembled in `finiteRootedRealizable_iff_pper` (:192) | §5, Alt-X |
| *Alt only:* **E4** OI⁺ ⟺ exact finite endomorphic operational QM | `qm_of_oiPlus` (CarrierGeneralOIPlus:191) | `oiPlus_of_qm` (:198); assembled in `carrier_general_oiPlus` (:213) | §6, Alt-X |

The displayed non-implication "bare finite OI ⇏ QM" (GR:222) is witnessed by `oi_alone_not_qm`
(GeneralCarrier:160). It is a countermodel, not an equivalence.

**Not to be displayed as equivalences.** These statements lack a kernel witness for at least one
direction. Each is stated in prose with its directions named and its unformalized links listed.
- **The universal memory biconditional (§4-b).** Each direction applies `pushforward_identity`.
  The converse also uses `S_imp_D`. Two links are not formalized: the time-$t$ joint-law reading
  and the CMI vanishing criterion (Main:99, :580(2)).
- **The characterization (ii) ⟺ (iii) (§4-e).** Both directions are prose (Main:608).
- **The rooted recurrence dichotomy (C8-D).** It rests on prose steps B3, B4 and A1, and it is not
  a statement on `main` (`SOURCES.md` UNTRACED-3).
- **The per-witness form (Main:610).** It is prose.

## Section-by-section outline: the recommended scope (body 13.25 pp, references 1.0 pp, total 14.25 pp)

Each table gives the claim, its exact source at `687e885b`, its verification layer and its novelty
class. "Not classified" means AUDIT r4 assigns no class: either no literature was examined, or the
item is a definition or an interpretation. The tables do not restate SOURCES.md's correctness
column.

### Abstract (0.25 pp)

The abstract carries four things:
- the hypothesis (§1-a);
- E1 at its proved scope (§3-a), with Markov laws included;
- where the discriminating content lies: hidden memory (§4-a) and recurrence indivisibility
  (§5-c, §5-e);
- the three statuses of §6-c, the bounded black-hole application (§7) and the open problems (§8).

It does not mention a derivation of quantum mechanics, a resolution of the information paradox, or
novelty.

### 1. Introduction: embedded observation and the OI hypothesis (1.25 pp)

Purpose: state the physical hypothesis, the mathematical question it poses, and what the paper does
and does not establish.

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §1-a | OI hypothesis: what an embedded observer records are the visible marginals of a finite reversible deterministic system of which the observer is a proper part; the physical identification of nature with such a system is a representation choice, motivated empirically, and the paper's theorems are mathematical | Main:28, :62, :702, :704 | prose (statement of hypothesis) | not classified ((e), interpretation; AUDIT:1409–1460) |
| §1-b | The question: what this reduction imposes on the form of the observer's laws | Main:28 | prose | n/a |
| §1-c | What is shown: the finite observable-law correspondence, where non-Markovian content sits, and how far the correspondence is from operational QM | Main:22, :534, :622, :758 | prose (roadmap) | n/a |
| §1-d | Incompleteness here is inaccessibility of the hidden sector, not the uncertainty relations | Main:28, :572 | prose | not classified |

### 2. Setting and definitions (1.0 pp)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §2-a | Observation $(S,\varphi,V)$, $V \subsetneq S$, finitely many visible states | Main:44, :48 | definition | n/a |
| §2-b | The bijective finite substratum is the reversible representative, a reconstruction choice; total finiteness is a posit | Main:56, :62, :708 (ii) | prose | n/a |
| §2-c | The hidden prior is part of the realization datum, so the visible law depends on $(\varphi,\mathcal P,\mu_H)$; invariance alone does not select the measure | Main:60, :86; kernel `invariance_does_not_select` (CanonicalMeasure:242) | kernel (measure clause); definition | not classified ((e), AUDIT:1416–1423) |
| §2-d | The classes $S$, $D$ (initial law on $V\times H$ that may correlate the coordinates) and $Q_{\mathrm{fb}}$ (projective readout in one fixed basis at every step, from a diagonal initial state) | Main:98–99, :526–530; `Stochastic`, `RevRealizable`, `QfbRealizable` (Equivalence:147, :182, :216) | kernel definitions | n/a |
| §2-e | (C1)–(C4) as diagnostics of a realization, not hypotheses of the correspondence | Main:72, :74–80, :596 | definition / prose | n/a |

### 3. The finite observable-law correspondence (1.75 pp)

**Display E1** (witnesses in the table above).

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §3-a | E1: for each finite alphabet and horizon $K$ the three classes coincide, each being all laws on $V^{K+1}$ | Main:16–18, :526–532, :580(1); `finite_horizon_equivalence` | kernel (six directions) | PARTLY KNOWN; packaging part PROVISIONAL (C4; AUDIT:631–709) |
| §3-b | S⇒D by a clock plus trajectory record: one iterated bijection, initial law possibly correlated | Main:532, :500 (kernel scope); `S_imp_D` | kernel | PARTLY KNOWN (C1; EG Prop. 13; "not located" part PROVISIONAL) |
| §3-c | Remark: a realization with hidden prior independent of $x_0$ (uniform tape; response tables for real kernels) | Main:496–500, :498 | prose proof + exact probes (`process_dilation_probes.py`, `review4_probes.py` P-G); independence not formalized (Main:500) | PARTLY KNOWN (C1′; EG Prop. 16, LPW Prop. 1.5; packaging PROVISIONAL) |
| §3-d | D⇒$Q_{\mathrm{fb}}$ by the permutation unitary; collapse in the configuration basis does not disturb diagonal states | Main:262–266, :532; `D_imp_Qfb`, `permMatrix_mem_unitaryGroup` (EquivalenceChain:179), `isDiag_Phi` (:253) | kernel | KNOWN (C2; B25 v3 p.12, B23 §4.3, B26 §4) |
| §3-e | $Q_{\mathrm{fb}}$⇒S: the every-step fixed-basis record is a probability law | Main:532; `Qfb_imp_S` | kernel | REFRAMING (C3; Strasberg–García Díaz Eq. (3), FT-r4) |
| §3-f | The representation is universal: Markov laws are included, so existence of a realization or a representation does not discriminate; the bare form "non-Markovian ⟺ a realization exists" is false | Main:98–99, :534, :592, :596–598 | prose (follows from E1) | C4-old WITHDRAWN (AUDIT:697–702); the remark is not classified |
| §3-g | The Born dictionary $p=\lvert U\rvert^2$ belongs to the definition of $Q_{\mathrm{fb}}$; the construction does not select the exponent (permutation entries 0/1 give the same table for every $p>0$) | Main:20, :534; check 6 of `equivalence_recovery_probes.py` | prose + probe | KNOWN and non-discriminating (C2 sub-item; B26 Thm 3.1; AUDIT:588–592) |
| §3-h | No exact all-time realization of a nonperiodic law by one fixed finite substratum (finite order) | Main:618 | prose proof | not classified (elementary) |

### 4. Where non-Markovian content lives (1.25 pp)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §4-a | In every faithful deterministic realization: (a) next-step law $= (f_x)_\#\mu_p$; (b) next-step TV gap ≤ posterior TV gap; (c) $M_t \le I(X_{<t};H_t\mid X_t) \le \log_2\lvert\mathcal C_H\rvert$ — kernel for a joint law of history, present and hidden state; reading a realization's time-$t$ law as that joint law not formalized | Main:582–590; `unavoidable_hidden_predictive_memory` (HiddenMemory:185), `pushforward_identity` (:83), `distinguishability_floor` (:114), `capacity_floor` (:170) | kernel (with stated gap) + exhaustive probe (`memory_probes.py`, 1,464 cases) | REFRAMING (DPI); attribution PROVISIONAL (C10) |
| §4-b | Prose biconditional, directions named: $M_t>0$ exactly when every faithful realization carries readout-relevant hidden memory at $t$ (forward: the pushforward identity in each realization; converse: the same identity in one realization, which exists by `S_imp_D`), with both unformalized links stated | Main:99, :580(2), :592 | kernel components + prose | REFRAMING (C10-B) |
| §4-c | Capacity: $\log_2 m \ge I^*$, the per-process bound | Main:484–494; `c3_necessity` (C3Necessity:80), `card_hidden_ge_two_pow_Istar` (:117), `c3_necessity_and_capacity` (:130) | kernel | REFRAMING; attribution PROVISIONAL (C11) |
| §4-d | Readback lemma: a TV gap δ between two histories of probability ≥ $p_0$ gives $I \ge p_0\delta^2/\ln 2$ | Main:167–170; `c4_backflow_probes.py` | prose proof (Pinsker) + exact probe | REFRAMING; PROVISIONAL (C9) |
| §4-e | Characterization (ii) ⟺ (iii), corrected for F29, stated in prose only, with its reduction: (C4) coincides with (ii) in every faithful realization, so (ii)⇒(iii) adds only existence of a realization | Main:516–522, :596, :608, :610; F29 record `verification/audits/manuscript/f29-witness-quantifier/result.md:6–30` | prose (both directions; not formalized); finite acceptance test | REFRAMING, near-definitional (C12). **Recommended: one sentence, no display** |
| §4-f | (C1)–(C3) without (C4) admit zero-backflow realizations (the tape-and-ledger coin) | Main:172; `review3_probes.py` | exact probe | not classified |

### 5. Quantum-like behaviour from observational restriction (1.75 pp)

Purpose: show, on exact finite examples, how marginalizing a reversible dynamics produces
stochasticity, memory, revival and non-stochastic intermediate maps. State the exact scope of each
phenomenon.

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §5-a | Stochasticity from marginalization: the observer knows $x$ but not $h$ | Main:90, :105 | definition | n/a |
| §5-b | Minimal model: 2 visible × 6 hidden states, $\sigma^2=\mathrm{id}$; $T(1,0)$ has entries 2/3, 1/3; $T(2,0)=I$; $\Lambda(2,1)$ has negative entries; memory witness $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ against $P(x_2{=}0\mid x_1{=}1)=1/3$ | Main:178–196 | exact computation (in text; re-checked for this design by an exact scratch script, not a repository artifact) | not classified (illustration) |
| §5-c | A non-permutation one-step matrix plus finite recurrence ($\varphi^N=\mathrm{id}$) gives P-indivisibility, by TV contraction under a stochastic divisor | Main:115–129; kernel counterpart `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148) — census `manuscript: []` | kernel (rooted form) + prose | KNOWN (C8; RHP 2014 Thm 2.4 "only if", BD Prop. 1; DO3 v3 Prop. 1 concurrent) |
| §5-d | TV monotonicity is necessary, not sufficient, for P-divisibility | Main:121; `translation_probes.py` | exact probe | not classified |
| §5-e | A stochastic matrix with a stochastic one-sided inverse is a permutation; hence (C4) readback on a fixed finite reversible representative forces indivisibility somewhere in the recurrence cycle. The step from history-level (C4) to a non-permutation rooted map is prose; the kernel has it from a routed-readback witness | Main:133–141; `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110), `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) | kernel (lemma; routed level) + prose (history-level step, F11) | KNOWN (C7; C8 mechanism) |
| §5-f | Scope: memory does not force short-window P-indivisibility. The XOR family ($X_2=X_0\oplus X_1$) has one bit of conditional memory and a matrix family that factors through $\Lambda=I$ | Main:141, :606; `review4_probes.py` | exact probe | KNOWN (RHP 2014 Eq. (15), FT-r4; DO3 v3 App. A concurrent; no first-statement claim) |
| §5-g | Stochastic P-indivisibility of populations is not quantum non-Markovianity outside the diagonal-preserving class (Hadamard family); the framework's permutation-dilation channels are diagonal-preserving, where P-indivisibility implies CP-indivisibility | Main:322–330, :334; `c1_cp_scope_probes.py` (exact over $\mathbb Q(\sqrt2)$) | prose proof + exact probe | not classified |

### 6. Reproduced behaviour versus a derivation of quantum mechanics (1.75 pp)

Purpose: the central boundary of the paper. **Display E2.**

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §6-a | Representation, not explanation: the correspondence says which laws admit realizations and representations, not why nature exhibits a given law | Main:616 | prose | not classified ((e)) |
| §6-b | Representability does not select the relating evolution: one visible family admits coherent unitary lifts whose relating evolutions differ; the fixed-basis correspondence acts on the quotient by visible equality. Only the kernel-backed clauses are carried; the fibre-Gram classification and the ancilla-separation remark are not carried, because Main names no artifact for them (UNTRACED-1) | Main:624; `bridge_traj` (TrackBQfbBridge:276), `rooted_eq_iff_slice_eq` (:180), `realData_traj_stochastic` (:286), `padData_rooted` (OperationalSourcing:476) | kernel (carried clauses) | not classified |
| §6-c | Three statuses kept apart: finite observable-law representability is established; exact finite operational QM is characterized conditionally; selection of a unique relating evolution is open | Main:624 (closing sentences) | prose | n/a |
| §6-d | E2 plus independence: each of (i)–(v) is independent of the others and of the C1–C4 process; a theory that never creates coherence realizes the OI core and is not quantum; so bare finite OI does not select QM | GR:216–226; Main:352, :542; `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160), `realizesSealedOICore_of_control` (OIRealization:252) | kernel | not classified (AUDIT r4 does not examine it) |
| §6-e | Classical-dimension obstruction: no fixed finite ontic carrier reproduces the full prepare-and-measure behaviour of a qubit exactly (elementary factorization proved; unbounded nonnegative rank imported) | Main:538, :540, :580(3); `nogo_probes.py` | prose + imported result | REFRAMING of the Hardy-type no-go; PROVISIONAL (C14; Hardy 2004 and [55] unread) |
| §6-f | Cited, not used: Main states finite-accuracy ε-realization and gluing theorems for bounded quantum instrument families. These are realization theorems, not uniqueness theorems, since the same machinery realizes non-quantum families | Main:544–562 (:562 for "not a uniqueness theorem"), :578, :580(4) | prose proof + exact probes (`opglue_probes.py`); no kernel anchor (F7 open) | not classified (C15; no literature examined). **Paper relies on no conclusion from it** |

### 7. Bounded application: black-hole information as an access problem (1.75 pp)

Purpose: illustrate the distinction between conservation in the global reversible dynamics and
recoverability from an observer's records. Also show which steps of the framework's Page-curve
argument are hypotheses. Every computational item is a finite toy model. None is a statement about
physical black holes (BH01 REPORT:285–302; BH02 REPORT:203).

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §7-a | Setting: nested partition $S=\mathcal C_V\times\mathcal C_B\times\mathcal C_D$; radiation registers emitted from $B$ into $V$ | ch07:120–122; GR:719 | definition | n/a |
| §7-b | Bijectivity conserves global information; this is the part of ch07's resolution sentence the computations support | ch07:118 (first sentence); BH01 MANUSCRIPT-AUDIT:91 | definition-level | n/a |
| §7-c | Bijectivity of the global map neither implies nor is necessary for recovery from the accessible records; zero accessible advantage requires $\lvert K\rvert \ge \lvert M\rvert$ | BH01 REPORT:17–18, :35–47 | exhaustive exact enumeration + written proof; reviewed ACCEPT (`df2ea6f5`) | not classified (no literature map; C16-S unclassified) |
| §7-d | Sufficient conditions: bijective dynamics with complete endpoint access give exact recovery; an inaccessible endpoint set $K$ gives $P_{\mathrm{succ}} \ge 1/\lvert K\rvert$, the only necessary-side fact proved; the conditions are sufficient, not necessary | BH01 REPORT:20–21, :49–58, :66–86, :98–112 | written proof + exhaustive check; reviewed | known in kind (the report calls C2 "the remnant-capacity form of a known fact", :110–112); not literature-mapped |
| §7-e | The direct and sequential nested trace-outs agree for every map (Fubini), so nested-trace consistency carries no recovery content | BH01 REPORT:29, :139–142; GR:731; ch07:124 | written proof + exhaustive check; reviewed | not classified |
| §7-f | Decoupling of $D$ over the evaporation: GR A.7's stated support ($\tau_{\mathrm{evap}}\ll\tau_B^D$) is reversed at 30 $M_\odot$ by at least $10^{57}$; $t_P/\tau_B^D \ge 1.153\times10^{57}$; what this does and does not show | BH01 REPORT:30, :211–245; review REVIEW.md:3; GR:811, :813 | exact interval arithmetic; reviewed independently | audit observation (BH01 REPORT:257, "NEW" assumption-watch) |
| §7-g | A permutation acting on a configuration state generates no entanglement across configuration-aligned cuts; from any state, $S(R)\le H(p_0)$, and the overlap with $\lvert+^n\rangle$ is conserved | BH02 REPORT:14–15, :26–42 | one-line proofs + exhaustive exact sweeps; reviewed ACCEPT (`ce7937d2`) | known in kind (elementary); not literature-mapped |
| §7-h | In the setting GR Appendix A uses, H-scramble fails for every bijection; the Page value enters only through the Haar ensemble H-scramble posits, not through bijectivity or the cycle decomposition | BH02 REPORT:18–19, :77–102; GR:817, :833 | proof (from §7-g); reviewed | not classified |
| §7-i | Page-time fraction $t_P/t_{\mathrm{evap}} = 1-(\beta/(1+\beta))^{3/2}$: 0.646 at β = 1; ≈ 0.538 at Page's β ≈ 1.485; a constant greybody or species factor cancels; β > 1 in the quasi-stationary semiclassical regime | ch07:137–143; GR:859–865; BH02 REPORT:22, :118–134 | exact algebra + literature | KNOWN (C16a, Page 2013 Eq. (8); C16b, Page 2005 Eqs. (5)–(10)) |
| §7-j | Open: H-scramble (ch07:126; GR:833); the step from the A.8 time average to A.9 pointwise in $t$ (BH02 REPORT:21, :112–114); the generalized second law (ch07:155–157; GR:805); QES agreement on the Page time (ch07:147); the island correspondence, conjectured (ch07:147–151); BH-03 and BH-05 to BH-07 not run (PROGRAMME.md:3) | as listed | — | C16d WITHDRAWN items stay out (AUDIT:1362–1371) |

The paper must not carry the following. Each would contradict a reviewed finding or the AUDIT:
- ch07:110's "resolves the paradox … because $\varphi$ is bijective" (BH01 MANUSCRIPT-AUDIT:56–60:
  "contradicts" claim A);
- ch07:159–161's falsification framing (BH01 MANUSCRIPT-AUDIT:143–160, the L155 entries at `809fac52`, now ch07:161);
- any "derivation of the Page curve" without H-scramble.
See risk R11 for the corpus-propagation consequence.

### 8. Open problems and limitations (1.0 pp)

| ID | Item | Source | Status |
|---|---|---|---|
| §8-a | The coherent-instrument and composite (operational-lifting) layer; which of (iii)–(v) the substratum supplies | Main:22, :542, :758; GR:226 | open |
| §8-b | Selection of the relating evolution | Main:624 | open |
| §8-c | Origin of the quadratic Born exponent | Main:20, :534 | open (frontier item) |
| §8-d | Formalization gaps: history-level (C4) ⇒ non-permutation rooted map (F11); time-$t$ joint-law reading; CMI vanishing criterion; prior independence in C1′; the (ii) ⟺ (iii) proof | Main:99, :139, :500, :580(2), :608 | stated as not formalized |
| §8-e | The variational identity $\inf_{\mathcal R} I = M_t$, false in its naive fixed-dimension form | Main:594 | open |
| §8-f | Recurrent-family gluing; approximation on windows $t\ll t_R$ | Main:618 | open |
| §8-g | C2 necessity conditional on the hidden-sector mixing hypothesis; ETH as motivation | Main:433–451, :480, :720 | conditional |
| §8-h | Bell: a deterministic completion with pointwise cones and a setting-independent ensemble is Bell-local (Bell's theorem applied); the framework's adopted branch needs H-Bell | Main:360–377 (check 11, `equivalence_recovery_probes.py`), :392–394 | proved (ceiling); H-Bell open |
| §8-i | No ontology-level falsifier is established; the posit ledger (twelve items) | Main:702–704, :708 | stated |
| §8-j | Black-hole items of §7-j | §7-j | open |

### 9. Related work (0.75 pp)

Built only from AUDIT §7's related-work list (AUDIT:2047–2076), with the descriptions it requires:
- Barandes B23, B25 and B26, with [11] and [12] correctly assigned (F17);
- Egri et al. (EG) for the trajectory-labelling realization;
- RHP 2014 Thm 2.4 and BD Prop. 1 for the divisibility form;
- DO3 v3 Prop. 1 and App. A as concurrent work;
- Milz et al. 2020 and Strasberg–García Díaz 2019, described as studying Kolmogorov consistency of
  projective records;
- BLP 2009 as a one-way witness, and BJA for the bijective distinguishability characterization;
- GO, SCH, JDM, LPW, SC (the ε-machine contrast), GH and MO;
- Page 1993, 2005 and 2013, and Penington 2019.

Pending reading before positioning sentences may be written: 't Hooft 2016, Spekkens 2007,
Hardy 2004, HKLP [55], Rutten, the comb-realization theorem, Popescu–Short–Winter and
Hayden–Preskill (AUDIT §5).

Not to be imported:
- the ≤ n³ bound, the Main:210 contrast and the Main:504 definition (F13; AUDIT:1917–1918);
- Main's descriptions of Calvo, Pimenta and Doukas (F14–F16);
- Main:220's Born-equilibrium sentence (F18).

### 10. Conclusion (0.25 pp)

The conclusion restates E1 at its scope, then where the discriminating content lies (§4-a, §5-e),
the three statuses (§6-c), and the bounded black-hole reading (§7-c, §7-h). It adds no new claim.

### Appendix A. Claim and kernel map (0.5 pp)

A table, one row per claim: kernel declaration (module:line at the drafting commit) or "prose" or
"probe", with the unformalized links listed. "Machine-checked" covers only the listed declarations
(AUDIT:2040–2045). This appendix replaces any need for the Explainer's summary tables.

### References (1.0 pp)

## Alternative scopes (for owner decision 1)

| Scope | Changes from the recommended scope | Pages |
|---|---|---|
| **Alt-L (lean)** | §7 cut to 1.0 pp, carrying only §7-b, §7-c, §7-d, §7-h and §7-i (drops §7-e, §7-f and §7-g); §6-f and §8-h dropped; Appendix A folded into §3 | ≈ 12.25 |
| **Recommended** | as above | ≈ 14.25 |
| **Alt-X (expanded)** | adds C8-R as new manuscript content with display E3 and no priority sentence (+0.5); OI⁺ with display E4 and `readWriteSourced_not_qm` (+0.25); the Leggett–Garg value $K=3/2$ reproduced by an invasive classical comb (Main:460–464, `lg_comb_probes.py`; not classified) (+0.25); §8 trimmed to 0.75 | ≈ 15.0 |

Kept out of every scope:
- C5, C6 and C13 (not needed for the argument);
- C8-D as a display (prose steps; not on `main`);
- C12 as a display (§A.34);
- the posit-level cosmology;
- PE-01. PE-01 concerns a book sentence on unpredictability. It does not bear on the finite-law
  correspondence, and it is covered in kind by prior work. If the owner wants it, one sentence in
  §8 would suffice, citing ch18:114.
