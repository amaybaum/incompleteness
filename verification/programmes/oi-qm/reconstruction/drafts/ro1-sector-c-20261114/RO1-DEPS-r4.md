# RO-1 step 2: premise dependency assessment for sector C, r4

**UNREVIEWED.** This is the fourth draft of the RO-1 step 2 assessment. It is a dependency assessment
and not a proof. It establishes no result, adopts no premise, extension E or sector condition C, and
changes no Issue's scope, tier, readiness, authorization or writer.

**Revision r4.** r4 applies the focused review of r3 (`REVIEW-DEPS-r3.md`, ACCEPT WITH CHANGES at
`4fc3f4aa`):
- C1: the interface ceilings and D-A8 exclude quantum operations only, not PR (§§4, 5, 5.1, 6, 7.7);
- C2: track (c) now reports what holds under global P-vii (§§7.4, 7.6);
- X5, the Bell analogue of X4, is flagged (§7.7);
- the minor findings m1–m4.

Dispositions are in `RESPONSE-DEPS-r3.md`. r3 (`RO1-DEPS-r3.md`, SHA-256
`aee284f2d9f51df8a698aff0f08c64f5db922f9495f39fdb31c4bcc76d65451d`) is left unchanged. The verdict
stays UNDETERMINED (§7.4 explains why C2 does not change it).

**Revision r3.** r3 applied the independent review of r2 (`REVIEW-DEPS-r2.md`, REVISE at `3b7d5aac`):
- F1: on each track the step named first is now the earliest open step (§7);
- F2: four cross-track conflicts are flagged (§7.7);
- the central question gains reuse with retention as the one partial discriminator (§5.1);
- the residues R1–R7.

Dispositions are in `RESPONSE-DEPS-r2.md`. r2 (`RO1-DEPS-r2.md`, SHA-256
`01809afbba839b3fcc6aada8d54ddf17f6c2d463a16568659346d871f1d6545e`) is left unchanged. The verdict
stays UNDETERMINED.

**Revision r2.** r2 applied the independent review of r1 (`REVIEW-DEPS-r1.md`, REVISE at `9504385a`):
- the blocking findings B1–B4;
- the medium findings M1–M5;
- the minor findings N1–N5;
- the reviewer's additions relayed by the coordinator: four tracks reported separately; incompatible
  combinations kept apart from executable countermodels; no claim of minimality; imported structure
  not counted as a derivation; no finite-to-infinite transfer without an argument.

Each finding was checked at source; the dispositions are in `RESPONSE-DEPS-r1.md`. r1
(`RO1-DEPS-r1.md`, SHA-256
`2d3ce3676d50c829d4684e6d0218d8ad6d307f07aa4b3b99d624bb45de593390`) is left unchanged. The verdict is
re-derived in §7 and stated per track.

**Authority.** #914 c.6883931412 (`amaybaum`, 2026-11-14T20:43:54Z), item 1, quoted verbatim in part:
"I authorize RO-1 Step 2 as a bounded, paper-only dependency assessment, with Claude as writer and
ChatGPT as independent exact-head reviewer. First investigate whether the existing OI axioms, posits
and conditions, considered together, already impose the physical restrictions needed to select
quantum operational behaviour." "Stop wherever progress requires adopting a new premise, choosing
Q7, resolving an open model-identity question or changing the scientific target." "Preserve RO-1 r3
and its reviews. No new physical premises, scientific computation, Lean work, manuscript changes or
merges are authorized." "Physical source remains NOT PASSED."

**Verdict standards** (the reviewer's, relayed by the coordinator):
- **SUFFICIENT**: one model and interface excludes non-quantum behaviour and keeps the required
  quantum preparations, coherent operations, incompatible measurements, Bell correlations and
  compositions;
- **INSUFFICIENT**: a proof that one model satisfies every premise at once, and a demonstration that
  the non-quantum experiment is physically available;
- **UNDETERMINED**: the first missing implication is named, with the evidence that would settle it.

**Writer:** Claude Code. **Reviewer:** ChatGPT, after an independent review.

**Base.** `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`. Lean modules under
`verification/lean-mathlib/OIBridge/` are cited by their statements as read, not rebuilt.

**Off-`main` sources**, at exact commits. Each reference is traced under §A.42 item 8 in §9.
- SEL-ACCESS-1 (#1224) at `1b966a03`, SEL-EXCL-1 (#1228) at `0ecfddeb` and SEL-DISC-1 (#1281) at
  `445b17f7`: each reviewed, not merged.
- `RO1-SPEC-r3.md` on PR #1294: ChatGPT ACCEPT WITH NITS, review 5906972784.
- RO-3 on PR #1303 at `78089e5e`. The README reads "UNREVIEWED — NOT AUTHORITATIVE", and
  `RO3-INVENTORY-r4.md` is headed "UNREVIEWED". Owner item 2 (#914 c.6883931412) accepts only the
  direct proofs of the OBL-RO3-2 unit and closes that unit at its stated scope: "The result is mixing
  under Haar measure, within its hypotheses".
- LEDGER, `LEDGER-r8.md` on the ledger branch at `9ff3b8d9`: an off-main record.

**Method:** reading only. No computation on OI rules, no Lean, no edit, no post.

**Labels.**
- **[R]** existing result, with its evidence state:
  - *main*: a manuscript statement;
  - *kernel*: a Lean statement on `main`, with its carrier;
  - *record on main*: a verification record on `main` whose own status is paper-level and not
    adopted, not an established premise (§A.46 items 1 and 7);
  - *reviewed, not merged*;
  - *off-main record*.
- **[P]** proposed obligation or definition.
- **[A]** unproved assumption. **[A-inf]** marks an inference drawn here: unreviewed, and treated as
  unproved.
- **[STOP Sn]** a stop, listed in §8.

**Domains.** No result is carried across domains. The words "finite carrier" have two senses, and
they are kept apart:
- **F**: one fixed finite *ontic* carrier, RO-3's class. **F₂**: the two-state ontic carrier,
  `Fin 2`.
- **G**: a family of finite models of growing size. **I**: an infinite completion.
- **Op**: the finite index set of the complex matrices in an operational theory under imported
  complex kinematics (P-CK). It is not an ontic carrier.

[R, off-main record] RO-3 keeps three properties apart: exact recurrence, exact common visible return
and recurrence-based P-indivisibility. They hold on F at recurrence-cycle scope and need new proofs
on I (`RO3-INVENTORY-r4.md` §§1.1–1.3, 2.4–2.6).

**Scope.** §1 covers the premises that bear on sector C. Following the review, three downstream
items that can affect the verdict are now included:
- GR's Theorem A.8 scope;
- the superposed-initial-state premise;
- SM's uses of A5.

§10 lists what remains.

**Verdict, in one line.** **UNDETERMINED**, reported on four tracks, each with its earliest open
step (§7):
- **(a) Quantum operations and coverage.** The target's carrier, then the interface typing. Given
  both, the physical sourcing of completion condition (iv).
- **(b) Bell coverage.** An independently defined reference class, then the resolution of C-1. Global
  linearity blocks the quantum Bell target; that is a coverage problem, not INSUFFICIENT.
- **(c) Quantum-set soundness.** After C-1, the two-wing interface and setting availability (S3,
  S6–S8). Only then a bound on remote-setting response. Under global P-vii the separated-wing Bell
  experiments on F are sound, at the cost of Bell coverage.
- **(d) PR countermodels.** A definition of "executable". Only then a construction checked against
  every premise. None is on record.

Five cross-track conflicts constrain the routes (§7.7). In particular, an operation that supplies
coverage enlarges what soundness must control, so the tracks must be answered on one interface.

***

## 1. Premise dependency matrix

The columns are:
- **Kind**: foundational assumption (FA), derived result (DR), conditional (CO), imported structure
  (IS), empirically selected (ES), stated intervention principle (SI), or proposed extension (PX);
- **Domain and dependencies**: where the item is proved or stated, and what it rests on;
- **Adopted**: whether the manuscript adopts it;
- **Joint satisfiability**: whether one fixed substratum and interface can satisfy it together with
  the others. The conflicts are named in §3.

### 1.1 Foundations, posits and stated inputs

| ID | Statement (source) | Kind | Domain and dependencies | Adopted | Joint satisfiability |
|---|---|---|---|---|---|
| P-Ax1 | "**Axiom 1** … tokened differentiation occurs … equivalently, *embedded representation occurs*" (`papers/Main.md`:36) | FA | All; `V ⊊ S` is part of the primitive on the perspectival reading (:38) | Yes | No conflict found |
| P-Def | "An *observation* is a triple `(S, φ, V)` … an observer `V ⊊ S` — a proper subsystem with finitely many distinguishable internal states, coupled to the complement" (:42) | FA, carrying the finite-capacity stipulation | All | Yes | No conflict found |
| P-L1 | Lemma 1: "The observer has finitely many distinguishable internal states, so the visible configuration space is finite" (:46). "Lemma 1 delivers finiteness of the observer's distinguishable states from the finite-capacity clause of the Definition" (:724) | DR from P-Def | Observer only. "The recurrence proof … requires S finite, which Lemma 1 does not supply" (`papers/GR.md`:138, as quoted in RO-3 §1.1) | Yes | Compatible with F, G and I |
| P-L2 | Lemma 2: "The observer is a proper subsystem … The complement `H = S \ V` is the hidden sector" (:48) | FA, from P-Def | All | Yes | No conflict found |
| P-L3 | Lemma 3: `φ` is deterministic and, "as the reversible representative of §1.2, a bijection" (:54) | DR (determinism, :44) / ES (bijectivity, posit (iii), "part-empirical rather than a pure lemma", :724) | All | Yes | No conflict found |
| P-i | Axiom 2, recurrence: "owned as a posit with a non-derivability countermodel" (:724, item (i)) | FA (posit) | Finite representative. [R, off-main record] Open on I (RO-3 §1.1). [R, off-main record] On the infinite-lattice linear update, mixing under Haar measure holds within OBL-RO3-2's hypotheses (owner item 2) | Yes | **Conflicts with the target** if read as exact recurrence of the whole model (C-2) |
| P-ii | Total finiteness of the bijective representative, A1 (:724, item (ii)) | FA (posit) | F | Yes | **Conflicts with the target** (C-2) |
| P-iv | "the maximal-entropy invariant measure compatible with the observer's records" (:724, item (iv)); Lemma 3's counting measure (:54) | FA (posit) | F. On I a replacement is needed; `referenceState` invariance is open (owner item 2) | Yes | Open on I |
| P-v | The hidden-sector mixing hypothesis (:724, item (v)) | CO | The C2-slow necessity direction; "remains open" | Conditionally | No direct bearing on C |
| P-vi | Spatial isotropy, "entering as empirical input E4 of the reconstruction" (:724, item (vi)) | ES | The spatial reconstruction | Yes | No direct bearing on C |
| P-vii | Linearity of the update, A5 (:724, item (vii); `papers/Substratum.md`:100: "the further restriction to linear is imposed") | FA (posit) | Spatial results. SM uses it in the form lemma (`papers/SM.md`:224) and in the wave equation and Stage 2(b) (LEDGER §9, Bell–SM row) | Yes, globally | **Conflicts with the preparation-indexed implementation of the adopted Bell branch** (C-1). No stated status for the "equivalent nonlocal response map" (:412) |
| P-viii–xiii | Site factorization; bounded degree; nearest-neighbour range "on the reference vacuum/uniform state class"; center independence; background independence; the second-order form, "a posit of the selected lattice model, not derived and not an axiom of OI" (:724) | FA (posits) | Spatial results | Yes | (x) is scoped to the reference class (:724), and so is Stage 2 (`papers/Substratum.md`:171, per LEDGER §9). P-vii is not scoped |
| P-xiv | Measurement independence, `p(Ω | a,b) = p(Ω)`, "a posit about the initial condition, not derived" (:724, item (xiv)) | FA (posit) | Bell only | Yes: "the Bell-violating branch adopted in §3.3 retains measurement independence" (:80). Its admissibility is ledger Q8 (LEDGER:938) | **[STOP S5]** |
| P-C1–C4 | (C1)–(C4) (:72–78). "our universe lies in the observer-admitting subset of substrata … This is the C1–C4 selection condition" (:34; `papers/Structure.md`:120) | FA (selection commitment) and DR (diagnostics) | F at recurrence scale for the derived parts (:80). (C4) is met by "a pre-sampled hidden variable revealed by the history … (the response-table construction, §3.4)" (:78) | Yes | No conflict found. Independent of (i)–(v) (D-oi-alone) |
| P-EM | (EM) and `τ_mix ≪ τ_S`, with "bounded coupling, finiteness of `S`, the canonical-typicality result [31]" (:742, :758) | CO | F | Conditionally | [A-inf] Needs a transfer to the target's carrier |
| P-E1E2 | "**Inputs:** E1 (unitary QM), E2 (Bell violations), E3 (finite boundary entropy), A1 (finiteness), A2 (determinism), and M1" (`papers/Substratum.md`:123). LEDGER §9 QM–SM: "SM uses QM as input" | ES (observed data used as inputs to the reverse reconstruction, Theorem 23, `papers/Substratum.md`:193) | The reconstruction | As inputs to that theorem | [P] Not admissible as premises of C or of SUFFICIENT: that would give coverage by import, which non-circularity bars (RO1-SPEC-r3 §6.1) |
| P-M1B | M1-B: "Bell-violating composites take [Main §3.3]'s measurement-independent, ontically parameter-dependent branch with operational no-signaling" (`papers/Substratum.md`:123) | ES / modelling premise | Bell composites | Adopted as the branch (:80) | **Its preparation-indexed implementation conflicts with global P-vii** (C-1) |
| P-HBell | H-Bell (i) ontic parameter dependence, (ii) operational no-signalling, (iii) a metric/Ollivier–Ricci stability condition (`papers/Substratum.md`:133) | CO (open hypothesis) | The Bell branch | No: open | PR meets (i) and (ii). (iii) is not applied to PR (RO1-SPEC-r3 §7.4) |
| P-MD | The measurement-dependent alternative, `CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}` (:416–423) | PX | Bell | "recorded, not adopted" | Allows 4 |
| P-phase | The phase intervention: one of the substratum's "stated interventions (its finite bijective read-write dynamics and the phase intervention)" (:80); the phases, "as a stated intervention principle rather than a consequence of its finite states and bijective dynamics" (:588) | SI (an assumption on the substratum class; outside the posit ledger, :724) | [R, kernel] In `substratumClass` (`phaseOperator_supplied`, `StructuralClosure.lean`:331). Outside the configuration-level sourced interface (`phaseOperator_outside_ceiling`, `FrozenSourcing.lean`:285) | Stated as an intervention of the class. Not sourced at the configuration interface | Not sourced: "Physical source remains NOT PASSED" |
| P-mix | "the continuously tunable state-mixing operation … added as an empirical controllability resource" (:588) | PX | Op | No | Not sourced |
| P-CK | Complex matrix kinematics, "a kinematics whose derivation from operational premises is open" (:562). Decision 4: "Allowed as a conditional mathematical input, not a physical explanation" (#914 c.6875046763) | IS | Op | As a conditional input | **[STOP S9]** for use in C |
| P-Born | "The Born dictionary `p = |U|²` is part of the definition of `Q_fb` … does not select the quadratic exponent" (:18) | IS (definitional) | Finite horizons | As definition | **Conflicts with Structure's wording** (C-3) |
| P-OI⁺ | OI⁺, "well-formedness together with observational independence, reversible richness, and observer recursion" (:584), with primitive-source and substratum-source forms (:588; `papers/GR.md`:256) | PX (characterization) | Op, "every nonempty finite carrier", "within the same complex matrix kinematics" (:584) | No: "not a claim that bare OI entails the added principles" (:588) | **[STOP S9]** |
| P-super | A superposed initial state of the black-hole/radiation system: "A preparation (initial superposition) or a non-aligned bipartition" is LEDGER §8.4's first missing step. GR: "A Page value at a bipartition aligned with the configuration coordinates needs entropy in the initial state" (`papers/GR.md`:823) | PX (open; not sourced) | The black-hole branch | No | [R, record on main] BH-02's superposition is analyst-supplied: "SUPPLIED marks a quantum ensemble, circuit or superposition chosen by the analyst" (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:8, 16). It bears on coherent preparation (§5) and conflicts with P-iv and P-xiv (§7.7, X1) |

### 1.2 Derived results that bear on C

| ID | Result (source) | Kind and support | Domain | What it does not give |
|---|---|---|---|---|
| D-SDQ | `S ⟺ D ⟺ Q_fb` on every finite horizon (:14–16, :80) | DR; [R, kernel] `finite_horizon_equivalence` (per LEDGER §2.1) | Finite horizons, fixed basis | It is "universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process" (:18) |
| D-real | Every finite law "has a finite reversible OI realization; bounded quantum instrument families are uniformly realizable to arbitrary finite accuracy" (:80); fixed finite adaptive families (:556) | DR (paper; kernel in parts) | F per law; G across accuracies | Mathematical availability, not sourcing (§2.5) |
| D-glue | The gluing theorem covers "incompatible measurements, adaptive interventions, preparation and instrument statistics"; it is "an **operational realization theorem**, not a uniqueness theorem: the same reversible machinery can realize non-quantum finite instrument families" (:582). Spatially separated instruments compose "as `𝓘_a ⊗ 𝓘_b` on the joint branch register" (:572) | DR (paper) | F at finite resolution | It realizes quantum and non-quantum families alike. It sources neither |
| D-PR | "the same reversible response-table construction … also realizes PR-box behavior" with "globally coupled setting-dependent hidden dynamics" (:360) | DR (paper) | F | Not shown to meet P-vii, P-x or P-M1B. Not shown executable |
| D-cone | Influence moves at most one graph edge per update. "Finiteness of `V` is used in the first step" (:362) | DR (paper); the algebraic causal cone is in the kernel (`QuasilocalAlgebra.lean`:1323–1328) | F only: `S = ∏ S_i` with `V` and each `S_i` finite. On I a transfer is needed (§3, C-2). [P] A route: posit (xiii)'s finite-range clause, "each `F_i` reading the current values at finitely many sites and each site read by finitely many `F_i`" (:724). Not given here | — |
| D-ceil | Bell ceiling for a screened local completion, under (i)–(iv), gives `|S_CHSH| ≤ 2` (:364–389) | DR (paper; the pointwise bound over 16 response tables is exhaustive in a script on `main`, per LEDGER §3.1) | F, through D-cone | It excludes PR and the quantum value alike |
| D-lin | Under linearity the dependence graph is the same at every state, so the preparation-indexed edges lie "outside ledger item (vii)" (:362, :414; `papers/SM.md`:104) | DR (exact algebra, per LEDGER §3.1) | Spatial | It says nothing about the "equivalent nonlocal response map" (:412) |
| D-comp | With complex kinematics given, the available families "are exactly the normalized finite Kraus instruments" iff (i)–(v) (:562) | DR; [R, kernel] `exactAll_iff_physical_general` (:562) | Op (endomorphic theory on one carrier with ancilla levels, rules (a)–(f), :562) | The two-wing Bell composite is not a stated instance (§4, R5) |
| D-oi-alone | (i)–(v) are "each independent of the others and of the C1–C4 process, witnessed on the qubit by theories realizing one fixed finite C1–C4 process" (:562) | DR; [R, kernel] `five_way_minimality`, `oi_alone_not_qm` | Op, qubit witness | — |
| D-iv | "Under the substratum's stated interventions … (iv), full reversible control, is not supplied" (:80; `papers/GR.md`:224) | DR; [R, kernel] `substratumGen_not_control`, stated for `genTheory substratumClass … (Fin 2)`: "every monomial conjugation preserves the diagonal and the rotation `rot` does not" (`StructuralClosure.lean`:344–348). `substratumClass` includes the phase operators (:331) | F₂, with the phases | Other carriers and extended mechanisms: "whether an extended OI mechanism supplies (iv) … [is] open" (`papers/GR.md`:224) |
| D-nonneg | `frozen_sourcing_verdict`: `¬ PhasesAvailable (permTheory (Fin 2)) ∧ ¬ DenseUnitaryControl (permTheory (Fin 2)) ∧ ¬ DerivedOI (permTheory (Fin 2))` (`FrozenSourcing.lean`:318–321); `nonnegBounded_verdict` for `FiniteOperationalTheory (Fin 2)` (:327). The carrier-general observer theory is `permTheory` on the configuration space "under the finiteness A1 supplies" (`SubstratumInterfaceAudit.lean`:766–770). Programme summary: `verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84 | DR; [R, kernel] | F₂ for the verdicts; F under A1 for the carrier-general parts | The configuration-level interface *without* the phases. `sourcing_rule_independent` holds by definition: the observer theory "is the sourced theory on the configuration space: the rule does not occur in it" (`SubstratumInterfaceAudit.lean`:773–775) |
| D-phaseQ | On the quasilocal completion, "a phase automorphism at one site preserves locality without arising from any reversible finite-range bijection" (:588; [R, kernel] `phaseQ_ne_heisQ`) | DR | I (the quasilocal completion) | A partial transfer of "phases are not generated by bijective dynamics" to I. Nothing on (iv) there |
| D-dim | No fixed finite carrier reproduces "the entire exact continuum operational theory of even a qubit at all preparations/effects and all precisions" (:558, :562) | DR (paper; factorization half proved, unboundedness imported from [55], per LEDGER §2.1) | F | Not about G or I |
| D-approx | Approximate inclusion to accuracy ε (:596–598); "`D_finite` is strictly larger … its closure contains non-quantum operational theories too" (:598) | DR (paper) | G | — |
| D-OIplus | "OI⁺ ⟺ exact finite endomorphic operational QM" (:586), each principle independent (:588) | DR; [R, kernel] `carrier_general_oiPlus`, `oiPlus_independence` | Op | Not entailed by bare OI. No two-wing statement |
| D-sub | Substratum plus "one continuously tunable state-mixing operation" gives operational QM; finite reversible read-write dynamics "does not itself generate quantum state mixing" (:588) | DR; [R, kernel] `substratum_plus_control_qm`, `qm_generated_by_substratum_extension`, `readWriteControl_independent` | Op | The added operation is P-mix |
| D-memory | (C4) forces conditional memory; (C3) holds in every faithful realization; C2-structural holds by reversibility; indivisibility at recurrence-cycle scope "follows from any non-deterministic visible step … and does not require C4" (:80) | DR | F at recurrence scale. [R, off-main record] On I, it needs exact common visible return or a replacement (RO-3 §1.3) | No coherent operation (D-oi-alone) |
| D-A8 | At bipartitions aligned with the configuration coordinates, "The orbit of a configuration consists of configurations, each a product state across that bipartition … H-scramble fails for every bijection" (`papers/GR.md`:823; :805). Entropy at an aligned cut is bounded by the initial distribution's entropy, `S(ρ_R(t)) ≤ H(p₀)`, for every bijection (:823–827, per LEDGER §8.1) | DR (paper; exhaustive at small sizes per LEDGER §8.1) | F, aligned bipartitions | [A-inf] Bijective dynamics started from definite configurations prepares no entanglement across aligned cuts. Coherent preparation needs a superposed initial state (P-super) or a non-aligned cut |

### 1.3 Verification records on `main` (paper-level, not established)

| ID | Statement (source) | Domain | Bearing on C |
|---|---|---|---|
| V-OA1 | Under one affine `φ`, "a stored setting acts on a carrier only by translation … Fredkin bijections supply control"; "The configuration-level interface is capped for every rule [K]" (`verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`:48–59) | Affine class | Classical-control limits come from the rule class |
| V-OA2 | Theorem C, finite groups of reversible operations at a fixed finite carrier. Designed control N2.3: "A reversible classical computer `𝔊_K` shows an exact, preparation-contextual gbit at each bounded horizon, under C-PM′ and C-PM, with its uniform bath under μ-G". Theorem E(b), simplex-embeddable under (H1), H-AR, (H3), (H4), (SP), (xiv) (`…/oa-2-20261112/STATUS.md`:56–69) | F; affine class; bounded horizons | N2.3 is a designed non-quantum prepare–measure behaviour (§7) |
| V-OA3 | Lemma OBS: three consecutive held sites determine "the entire configuration of a finite ring of `L` sites within `2(L−3)` ticks"; Theorem S: under its conditions `G_SM`'s fragment "is a simplex"; "not an impossibility result for `G_SM`" (`…/oa-3-20261112/STATUS.md`:48–67) | F; `G_SM` | §2.1 |
| V-EAR | One added-access extension's "first state/readout bridge fails … not a no-go for bare OI" (`…/oi-qm-ext-1/whole-model-bridge.md`:9–19) | F | — |
| V-CA | A conditional composition theorem with "the stated physical/access closure" as hypothesis; "it does not claim that the native lattice meets its hypotheses" (`…/composition-access-20261024/REPORT.md`:1–8, 34–39) | A fixed menu | Access closure is a hypothesis, not a result |
| V-B4 | Record-law equality and the two-sided gauge relation differ (`…/bsel-2-b4prime-20261105/B4PRIME.md`:19, 367; Q2A and M-1 RESULT.md) | `PPer` and the all-unitary class, small dimensions | O11 |

### 1.4 Reviewed results off `main` (reviewed, not merged)

| ID | Statement (source, exact commit) | Scope |
|---|---|---|
| X-MENU | A passive-law selector "is **not sufficient** to guarantee target completeness" in a class containing a full/restricted-menu pair (SEL-ACCESS-1 §2, ll. 41–51, at `1b966a03`) | Conditional on the class hypotheses |
| X-PR | `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-EXCL-1 l. 33, at `0ecfddeb`), CHSH 4, under an interface "**specified, not derived from the native OI/SM dynamics**" (l. 46). Fresh-cell no-signalling in the declared grammar (§3); same-seed signalling in the enlarged grammar (§7) | Designed countermodel |
| X-IC2 | PR gives `J = 2`; classical-local and quantum-local references give `J ≤ 1`; the native principle is "Not supplied" (SEL-DISC-1 D5–D8, at `445b17f7`) | Conditional discriminator |

## 2. Joint implications

### 2.1 Incomplete information versus limits on executable interventions

[R, main] P-L2 gives incomplete momentary access (:48). No axiom, lemma or posit of Main specifies an
intervention repertoire. The comb theorem "realizes any FIXED finite adaptive family" (:556), and the
gluing theorem realizes quantum and non-quantum instrument families alike (D-glue).

Two kinds of limit appear in the records, and neither comes from incompleteness:
- [R, record on main] Limits on *classical control* come from the rule class: affine `φ` gives
  translation-only control, while Fredkin bijections do not limit it (V-OA1).
- [R, kernel] The *quantum-resource* ceiling of D-nonneg comes from how the configuration-level
  interface is defined. The rule does not occur in it (`SubstratumInterfaceAudit.lean`:773–775).

[R, record on main] Incomplete momentary access does not bound reconstruction over time (V-OA3,
Lemma OBS).

[R, reviewed, not merged] A passive-law selector cannot force an operation repertoire (X-MENU).

[A-inf] **Incomplete information does not by itself limit executable interventions, or select a
quantum repertoire.**

### 2.2 Observer capacity versus total finiteness

[R, main] P-L1 makes the observer finite per moment, derived from P-Def. Total finiteness (P-ii) is a
separate posit (:724). Lemma 1 does not make `S` finite (`papers/GR.md`:138).

[R, main] Exact coverage of a qubit's operational theory is impossible on one fixed finite carrier
(D-dim). Record: the target excludes "one fixed finite total carrier" (#914 c.6875046763).

[A-inf] **Observer capacity is compatible with an infinite `S`. P-ii is incompatible with the target's
exact coverage (C-2).** Dropping P-ii removes the domain of several results used below, as C-2 lists.

### 2.3 Determinism versus locality versus measurement independence

[R, main] On F, D-ceil holds: determinism, local setting operations, readouts outside the remote cone,
and P-xiv give CHSH ≤ 2. That excludes PR and the quantum value alike.

[R, main] The three can be weakened as follows:
- **Give up parameter independence, keep P-xiv.** This is the adopted branch (:80; P-M1B). Its
  preparation-indexed implementation lies outside P-vii (D-lin), so under global P-vii it is
  unavailable (C-1). The response-map alternative (:412) has no stated status relative to P-vii.
- **Give up P-xiv.** P-MD allows CHSH up to 4. Main also gives "reaching the quantum value requires
  `I_ont ≥ 0.0309…` bits", a necessary bound "not claimed tight" (:416–423).
- **Determinism** is not given up (P-L3).

[A-inf] **No combination of these premises in the corpus excludes PR while keeping the quantum Bell
value.** Under global P-vii both are excluded for separated wings on F. Under the adopted branch
with H-Bell, or under P-MD, neither is excluded.

### 2.4 Memory versus P-indivisibility versus coherent operations

[R, main] (C4) forces conditional memory. P-indivisibility at recurrence-cycle scope follows from any
non-deterministic visible step without (C4) (D-memory, on F).

[R, kernel] (i)–(v) are independent of the C1–C4 process (D-oi-alone).

[A-inf] **Memory and P-indivisibility do not imply coherent operations.**

[R, off-main record] On I, recurrence-based P-indivisibility needs exact common visible return or a
replacement (RO-3 §1.3).

### 2.5 Mathematical availability versus physically sourced operations

[R, main] D-real, D-glue, D-approx and D-PR are realization theorems. Some finite reversible system
realizes a given law or bounded family, quantum or not (:582).

There are two interfaces, and r1 merged them.
- **Interface A: `substratumClass`.** [R, kernel] Its operators are the bijective, phase and
  read-write operators, all monomial (`StructuralClosure.lean`:327–335). It is Main's "stated
  interventions", phases included (:80). On F₂ it does not supply (iv), because monomial
  conjugations preserve the diagonal (D-iv). It *does* contain the phases, by a stated intervention
  principle (P-phase).
- **Interface B: the configuration-level observer theory, `permTheory`.** [R, kernel] It has no
  phases, no dense unitary control and no `DerivedOI`, on F₂ (`frozen_sourcing_verdict`). It is
  defined on the configuration space under A1 (D-nonneg).

[A-inf] **What can be realized is not what is sourced.**
- On Interface B, the phases fail on F₂ (kernel). (iv) fails there by one unstated step from ¬`DenseUnitaryControl`, since exact control gives dense control (`DiscreteCompletion.lean`:45–48).
- On Interface A, the phases are present by assumption and (iv) still fails on F₂.
- Neither verdict is stated for G or I. The one partial transfer found is D-phaseQ: on the quasilocal
  completion a one-site phase automorphism does not arise "from any reversible finite-range bijection"
  (:588).

## 3. Compatible and incompatible combinations

**Contradictions, named.**

| ID | Combination | Why it fails | Source | Status |
|---|---|---|---|---|
| **C-1** | Global P-vii with the *preparation-indexed* implementation of P-M1B | Under linearity the dependence graph is the same at every state, so preparation-indexed edges lie "outside ledger item (vii)" | [R, main] :362, :414; `papers/SM.md`:104, 224. LEDGER §9, Bell–SM: "known not to, for global A5 with the preparation-indexed adjacency route; undetermined for the 'equivalent response map' alternative and with A5 restricted to the reference class" | Owner direction: "Test A5 scoped to an independently defined reference class", keeping the wave equation, Stage 2(b), harmonic modes and the H-D uses as controls (#914 c.6880010243 item 4). Not done (#1234) |
| **C-2** | Total finiteness (P-ii) with exact coverage on one fixed model | D-dim; the target excludes a fixed finite total carrier | [R, main] :558, :562; #914 c.6875046763 | Dropping P-ii removes the stated domain of: P-i (recurrence); D-memory at recurrence scale; P-EM; P-iv's counting measure; **D-nonneg's carrier-general parts (under A1) and both verdicts (F₂)**; **D-iv (F₂)**; **D-cone and D-ceil (finite `V`, :362)**. Each needs a transfer or a replacement on I (OB-T) |
| **C-3** | Structure: "Born rule, unitarity, non-Markovian marginal are features of any embedded-observer system" (:872), "forced by the structure of observation" (:886); against Main | Main: the Born form is "part of the definition of `Q_fb`" (:18); "representability alone is not the framework's discriminating content" (:554); `oi_alone_not_qm` (:562) | [R, main] | A manuscript correction candidate under §A.25, outside this unit (S12) |

**Differences recorded but not shown to be contradictions.**
- **C-4.** Main:588 says the substratum "supplies the structural architecture — closure under
  composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance,
  reversibility". Main:80 and GR:224 say "whether the substratum supplies (iii) and (v) [is] open".
  [A] The first is stated at the level of an implementation architecture, and the second at the
  level of the operational theory's conditions (iii), inert spectators, and (v), iterated
  composition. Whether architecture-level stability implies (iii) and (v) for the substratum's
  generated theory is not reconciled here. If it is not reconciled at source, it is a §A.25 candidate
  beside C-3 (S12).
- **P-xiv.** It is adopted (:80), and its admissibility is ledger Q8 (S5).

**Compatible combinations, at their domains.**
- [R, main] Bare OI with C1–C4 on F: realized by finite reversible systems with memory-bearing laws
  (D-real, D-memory). Compatible, but it does not select QM (D-oi-alone).
- [R, kernel] P-CK with (i)–(v), or with OI⁺, on Op: exactly Kraus instruments, or exactly finite
  endomorphic operational QM (D-comp, D-OIplus). These are compatible as operational theories with
  imported kinematics. They are not shown to be the theory of one ontic model.
- [A-inf] Bare OI without P-ii, on I: no contradiction found in what was read. The finite results do
  not transfer automatically.
- [A] Whether the posit list with P-vii scoped to a reference class has any model meeting P-M1B and
  H-Bell together is not established. No such model is constructed in the corpus.

## 4. Candidate restrictions: premise removal, necessity and sufficiency

"Excludes PR, given availability" asks whether a protocol realizing PR is excluded when its operations
are physically available. In every row availability is unsourced (S3).

| # | Restriction | What follows | Removing one premise | Countermodels and controls | Excludes PR, given availability? | Sufficiency / necessity |
|---|---|---|---|---|---|---|
| R1 | Bare OI: P-Ax1, P-Def, P-L1–L3, P-i, P-ii, P-iv | D-SDQ, D-real, D-glue, D-PR on F | Without P-ii: the F results need transfer (C-2) | D-PR; D-glue's non-quantum families; classical control realizable | **No** (D-PR) | Not sufficient for soundness or coverage |
| R2 | R1 + C1–C4 | D-memory | Without (C4): the tape-and-ledger fair coin meets (C1)–(C3) with zero conditional memory (:78) | `oi_alone_not_qm`; (C4) met by response-table realizations (:78) | **Not shown** | Not sufficient for coverage (kernel, Op). Soundness untested |
| R3 | R2 + global P-vii + P-viii–xiii + P-xiv, wings outside each other's cone | D-cone, D-ceil, on F | Without P-xiv: up to 4 (P-MD). Without global P-vii: preparation-indexed edges become available, and nothing stated bounds the correlations | The 16 response tables (per LEDGER §3.1). The quantum Bell reference is excluded by the same theorem | **Yes, on F**, for separated wings. On I a transfer of D-cone is needed (finite `V` used, :362) | Fails Bell coverage. Not a selector |
| R4 | R2 + P-M1B + P-HBell, with P-vii scoped to a reference class (the Q2 direction, not done) | Ontic parameter dependence with operational no-signalling | Without H-Bell (iii): the GR continuum step is lost, with no Bell consequence stated | PR meets H-Bell (i)–(ii). No model meeting all of R4 is constructed | **Not shown** | Undetermined (#1060) |
| R5 | P-CK + (i)–(v) | D-comp | Without (iv): the substratum's stated interventions do not supply it on F₂ (D-iv). Without any one: not QM (`five_way_minimality`) | `oi_alone_not_qm` | **Not shown.** The two-wing composite's relation to the ancilla levels is not stated. RO1-SPEC-r3 §7.4: "On one carrier without `Θ`, a PR table is an ordinary classical channel and is not excluded" | **Sufficient for exact endomorphic coverage within P-CK, on Op** (kernel; necessary as well, by the characterization). **Soundness against PR: conditional on a stated two-wing typing under `Θ` (S8) and on access closure; not proved.** Not sourced; S9 |
| R6 | OI⁺ or its source forms, with P-mix | D-OIplus, D-sub | Without P-mix: read-write dynamics "does not itself generate quantum state mixing" (:588) | `oiPlus_independence` | **Not shown**, as R5 | As R5: coverage within P-CK on Op; soundness conditional and not proved; S9 |
| R7 | Interface B (D-nonneg); the affine class (V-OA1, V-OA2); `G_SM` with its observers (V-OA3) | No phases or dense control on F₂; simplex-embeddable fragments under stated hypotheses | Without the affine restriction: Fredkin control (V-OA1). Adding the phase intervention gives Interface A, which still lacks (iv) on F₂ | The classical simplex | [A-inf] **Interface B: no.** The PR gate `T` is a bijection of configurations, so its conjugation is a permutation, which is monomial and preserves nonnegative entries. **Affine class:** the stated gate is not affine (`x ∧ y`), so it lies outside the class. Whether another affine realization gives a supraquantum two-wing table is not shown. The simplex results concern prepare–measure fragments, not two-wing correlations | Fails coverage (kernel on F₂; record on main for the affine class). Does not exclude PR at Interface B |
| R8 | IC₂ (off main) | X-IC2 | Without the one-bit protocol in `Γ`: no exclusion | Classical-local and quantum-local references satisfy it | **Yes**, for fresh one-use PR, if the protocol is executable | Conditional discriminator. Barred from C until the four conditions of #914 c.6883249235 item 4 are met |
| R9 | The RO-1 frame (RO1-SPEC-r3) | — | — | An enlargement of the PR model, if one exists (RO1-SPEC-r3 §7.2) | **Not shown**; needs K-X | Not sufficient |

[A-inf] **Sufficiency and necessity, kept apart.**
- R5 and R6 are proved sufficient and necessary for exact endomorphic *coverage* on Op within imported
  kinematics. They are not proved sufficient for *soundness* against a two-wing supraquantum
  behaviour.
- R3 is sufficient to exclude PR on F and fails Bell coverage.
- No row is shown sufficient for both, and none is physically sourced.

## 5. Embedded observation: what the premises give

| Aspect | What the premises give | What they do not give | Sources |
|---|---|---|---|
| Preparation | A common source law (P-iv); exact point preparations on F | Coherent preparation. [R, main] From definite configurations, bijective dynamics gives no entanglement at aligned cuts: `S(ρ_R(t)) ≤ H(p₀)` (D-A8). A superposed initial state is an open, unsourced premise (P-super). [R, record on main] Holding a selected hidden carrier with its choice record fails under μ-G for every bijection; a ready-cell supply or history-record convention resolves it classically (V-OA1, Gap 1) | `papers/GR.md`:805–827; OA-1 STATUS |
| Intervention | Interface A: bijective, read-write and phase operators, monomial. Interface B: configuration-level permutations | (iv) on F₂ (both). Phases on Interface B (F₂). Nothing stated for G or I beyond D-phaseQ | §2.5 |
| Access | `V ⊊ S`, finite per moment | A limit on reconstruction over time (V-OA3); a limit on interventions (§2.1) | :46, :48 |
| Retention | C2-structural by reversibility in every bijective realization (:80) | Retention of coherence, open at #1032 (#1143 c.6692765618) | :74, :80 |
| Resources | [R, reviewed, not merged] A closed finite world bounds output entropy (SEL-DISC-1 l. 79) | A separator: "Scarcity alone is not a separator" (P5, l. 53) | SEL-DISC-1 §4 |
| Repeated use | Retention with reuse is the one partial discriminator on record (§5.1). Fresh-cell use keeps PR no-signalling; same-seed reuse signals (X-PR) | Whether either is executable (#913, #866). A rule on renewal and resources | SEL-EXCL-1 §§3, 7; :80 |
| Composition | Spatially separated instruments compose as `𝓘_a ⊗ 𝓘_b` in the realization construction (:572). (iii) and (v) as conditions of D-comp | Whether the substratum supplies (iii) and (v): open (:80; `papers/GR.md`:224; C-4). The two-wing composite with local instruments under `Θ` | :562, :572, :588 |

[A-inf] Embedded observation, as the premises state it, constrains momentary access and observer size.
It does not constrain the correlation strength between wings. Its constraints on reuse are partial
(§5.1). Its constraints on operations and preparation (D-iv, D-nonneg, D-A8) exclude quantum
operations and coherent preparation, but not PR: the PR gate is a permutation of configurations, and
its correlations are classical correlations of configurations (§5.1).

### 5.1 The central question

*Can the same embedded-observer limitations both support quantum operations and exclude non-quantum
correlations?*

[A-inf] On the record, the limitations fall into four classes. None excludes non-quantum correlations
while keeping quantum operations.
- **Excludes both.** Only the Bell ceiling: D-ceil, under global P-vii and P-xiv, for separated wings
  on F.
- **Excludes quantum only.** The interface ceilings (D-iv, D-nonneg, on F₂) and the preparation limit
  (D-A8, on F). They exclude operations that do not preserve the diagonal or nonnegative entries, and
  entanglement from definite configurations. The PR implementation of record is a bijection of
  configurations, `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-EXCL-1 l. 33). Its conjugation is a
  permutation, monomial and nonnegative, so it passes both ceilings. D-A8 bounds entanglement and
  says nothing about classical correlations, PR included. On one carrier a PR table is "an ordinary
  classical channel" (RO1-SPEC-r3 §7.4).
- **Excludes neither.** Access, capacity and retention as stated (§§2.1, 2.2, 2.4).
- **Partial discriminator.** Retention with reuse, at the scope below.

[A-inf] The "quantum only" class is the worst case for the central question. Those limitations remove
quantum operations and leave the PR machinery inside permutation-level operations. The restriction
that soundness needs therefore falls on the executability of settings and renewal (S3, #913), not
only on any added coverage operation (§7.7, X4).

**The one partial discriminator: retention with reuse.**
- [R, main] C2-structural holds by reversibility in every bijective realization: a written hidden
  record persists (:74, :80).
- [R, reviewed, not merged] If the same hidden source cell can be used again, with the first output
  retained, the PR implementation signals in complete local histories. In the same-register variant,
  `b₂ = x₂`; with a fresh output register, `b₁ ⊕ b₂′ = x₂` (SEL-EXCL-1 §7, at `0ecfddeb`; SEL-DISC-1
  D3). Under `Θ`, if adopted (S8), local instruments with no message give complete local-history no-signalling
  (SEL-DISC-1 §6.3), so this is a soundness failure for the same-seed implementation.
- *Exact scope.* It rejects the **same-seed** PR implementation, and only when the same-seed
  continuation is executable (S3). A stipulated supply of fresh independent cells defeats it: the
  fresh-cell lemma gives complete local-history no-signalling (SEL-EXCL-1 §3). And "Scarcity alone is
  not a separator" (SEL-DISC-1 P5, l. 53). It is not shown against any other non-quantum model, and
  it says nothing about coverage.
- [A-inf] So the discriminating question moves to **renewal and resources**: whether one fixed model
  can execute fresh independent source cells without limit, and at what cost. Renewal is #913's
  (O-REUSE), and preparation is #866's. No premise on record settles it.

**The question must be answered on one interface** (§7.7, X4). An operation that supplies coverage
enlarges the executable set, and under access closure soundness must then hold for that enlarged
set.

## 6. Soundness and coverage together

[P] The comparison uses RO1-SPEC-r3's structure-preserving correspondence `Θ` (§6.3 there). Its
adoption is S8.

[A-inf] The candidates of §4 fall into four groups:
- **Sound against PR for separated wings, not covering:** R3, under global P-vii, on F.
- **Not covering, and not excluding PR at Interface B:** R7. The interface ceilings exclude quantum
  operations only (§5.1).
- **Covering within imported kinematics, with soundness not proved:** R5 and R6, on Op.
- **Neither shown:** R1, R2, R4 and R9.
- **A test, not a restriction:** R8.

[A-inf] No combination of *established* premises keeps the required quantum preparations, coherent
operations, incompatible measurements, Bell correlations and compositions in one model.
- On F₂ under both interfaces, (iv) fails. Coherent preparation from definite configurations fails at
  aligned cuts (D-A8).
- Under global P-vii, the Bell value fails for separated wings (R3).
- Incompatible-measurement statistics are realizable (D-glue). They are not sourced.

## 7. Verdict, by track

**UNDETERMINED.** The verdict is reported on four tracks. Bell is a separate constraint: "Bell is a
separate constraint rather than one of those conditions" (:80); "Bell is not an extra rung of that
lift" (:582). Owner decision 3 makes Bell a "Separate research track, mandatory for full equivalence"
(#914 c.6875046763).

Four rules govern this section:
- **An incompatible combination is not a countermodel.** An incompatible combination of premises is a
  coverage or consistency finding. It is not INSUFFICIENT unless one compatible model with an
  executable non-quantum experiment is also shown.
- **Imported structure is not a derivation.** E1 and E2 (P-E1E2), the phase intervention (P-phase),
  the initial superposition (P-super), complex kinematics (P-CK) and the mixing resource (P-mix) are
  inventoried in §1. None counts as an OI derivation.
- **No transfer without an argument.** No finite-carrier theorem is carried to the target's carrier
  without an explicit transfer argument. This includes the Lean operation ceilings (D-iv, D-nonneg)
  and the Bell cone and ceiling (D-cone, D-ceil). None is given here, so each such result stays at its
  stated carrier.
- **The first open step is the earliest step that is open.** Each track's chain is listed in order,
  and an open step is named first only if every step it presupposes is settled. The ultimate goal of a
  track is stated separately and is not counted as a step.

### 7.1 Why not SUFFICIENT, overall

- [P] E1 and E2 are not admissible as premises (P-E1E2).
- [R, kernel] On F₂, (iv) is not supplied by Interface A (D-iv). [A-inf] Interface B supplies neither
  the phases nor (iv) on F₂. The kernel states ¬`DenseUnitaryControl (permTheory (Fin 2))`
  (`FrozenSourcing.lean`:318–321). Exact control gives dense control with `V = U` and `c = 1`
  (`DiscreteCompletion.lean`:45–48), so the absence of (iv) follows in one step that is not a stated
  theorem.
- [A-inf] R5 and R6 are sufficient for exact endomorphic coverage on Op, within P-CK. They rest on
  P-CK and P-mix, which are imported or posited. Their two-wing soundness is not proved (track (c)).

### 7.2 Track (a): quantum operations and coverage

**Ultimate goal.** The actual substratum and interface physically provide the coherent operations the
reconstruction needs.

| Item | Content |
|---|---|
| Carrier | Results exist on F₂ (D-iv; D-nonneg's verdicts) and on F under A1 (the carrier-general observer theory). On I there is only D-phaseQ (:588). The target's carrier is not F (C-2) and is not chosen (OB-T; #1055) |
| Dynamics | Finite bijective read-write dynamics (P-L3, :588). On I, the evidence uses the globally linear second-order rule (OBL-RO3-2, off-main record; D-phaseQ). See §7.7, X2 |
| Interface | A: `substratumClass`, monomial operators with the phases. B: `permTheory` on configurations, without the phases (§2.5). Where an added operation is typed is S7 |
| Assumptions | P-CK (imported) for the target theory. The phase intervention is a stated principle on A (P-phase) |
| Evidence status | [R, kernel] (iv) is not supplied on F₂ under A. [A-inf] On F₂ under B, as §7.1 states. [R, kernel] Phases are absent under B on F₂. [R, main] Read-write dynamics "does not itself generate quantum state mixing" (:588). [R, main] No coherent preparation from definite configurations at aligned cuts (D-A8, F) |

**Chain, in order.**
1. **The target's carrier is fixed.** Open: OB-T, #1055, #1169 EXACT. This is the earliest open step.
   The carrier comes first here and last on track (b), for this reason [A-inf]: on F₂ the
   track-(a) question is already refuted, so what is open lies on another carrier, whereas track (b)'s
   C-1 is a consistency question that can be settled on F and then transferred.
2. **The interface typing is fixed: where an added operation lives (S7).** Open. It is constrained by
   P-L3 (§7.7, X3).
3. **Given 1 and 2: the premises imply a physically sourced operation supplying completion condition
   (iv) in one fixed model.** It is refuted on F₂ under A (kernel) and under B (A-inf), and has no
   statement on G or I.
4. **The co-requisites, each with its own status.**
   - The phases: present on A by stated principle; absent on B on F₂; D-phaseQ a partial negative on
     I.
   - Coherent preparation: D-A8, with P-super unsourced. P-super conflicts with P-iv and P-xiv, and
     its non-aligned-cut alternative depends on step 3 (§7.7, X1).

**First open step: step 1, then step 2.** Given a carrier and a typing, step 3 is first. [R, main]
"First" at step 3 means first refuted on the record. It does not mean first in an order among (i)–(v),
which are mutually independent (D-oi-alone, :562). Whether the substratum supplies (iii) and (v) is
open (:80).

**Evidence that would settle step 3**, once steps 1 and 2 are fixed:
- *Positive:* a sourced operation, typed per S7, that does not preserve the diagonal. It comes with
  its preparation, record and resources (#866; #1169).
- *Negative:* a proof, on the chosen carrier and typing, that every interface meeting the existing
  premises consists of monomial operators. That would extend `substratumGen_not_control`, which uses
  that "every monomial conjugation preserves the diagonal" (`StructuralClosure.lean`:344–345).
- *For the phases, separately:* a sourced mechanism, or an extension of
  `phaseOperator_outside_ceiling` and D-phaseQ. "`PhasesAvailable` is never identified with
  `DenseUnitaryControl`" (`FrozenSourcing.lean`:12).

### 7.3 Track (b): Bell coverage

**Ultimate goal.** The quantum Bell correlations are realized by the premises' model.

| Item | Content |
|---|---|
| Carrier | D-cone and D-ceil are proved on F, using finiteness of `V` (:362). [P] A route to I: posit (xiii) says "each `F_i` reading the current values at finitely many sites and each site read by finitely many `F_i`" (:724). Finite range of this kind would let the cone hold without finiteness of `V`. The transfer is not given here (OB-T) |
| Dynamics | The posited linear second-order rule, with site factorization and nearest-neighbour range on the reference class (P-vii, P-viii–xiii) |
| Interface | Setting operations local to disjoint regions; readouts outside the remote cone (D-ceil (ii)–(iii)) |
| Assumptions | P-xiv, adopted (:80), with its admissibility at S5. P-M1B, adopted. H-Bell, open |
| Evidence status | [R, main] Under global P-vii, preparation-indexed edges are excluded (D-lin). For separated wings on F, CHSH ≤ 2 whatever the intervention repertoire (D-ceil). This is a **coverage problem**, not INSUFFICIENT. The response-map alternative (:412) has no stated status |

**Chain, in order.**
1. **Precondition: an independently defined reference class**, as the owner's direction requires: "Test
   A5 scoped to an independently defined reference class" (#914 c.6880010243 item 4). Open.
2. **C-1 is resolved.** The premises are consistent with a Bell-violating branch. This needs the A5
   scoping test, with the wave equation, Stage 2(b), harmonic boundary modes and the eight H-D uses as
   controls (#1234; S11), or a stated status for the response-map alternative relative to P-vii.
3. **A specified response rule.** [R, off-main record] LEDGER §3.4: "a specified preparation-indexed
   edge rule (or response map) for which the CHSH value is the quantum one and the remote marginal is
   setting-independent" (#1060).
4. **Transfer of D-cone to the target's carrier**, for instance through (xiii) (OB-T).

**First open step: step 1, with step 2 at once after it.** C-1 is a consistency question among
premises and does not need the interface.

### 7.4 Track (c): quantum-set soundness

**Ultimate goal.** Every physically performable two-wing experiment of one model is in the quantum
correlation set, under a two-wing correspondence with complete access closure. A single-carrier OI⁺
characterization is not enough.

| Item | Content |
|---|---|
| Carrier | Not fixed. D-comp and D-OIplus are on Op, not on an ontic carrier |
| Dynamics | Not fixed beyond P-L3 |
| Interface | A two-wing interface with local settings, records and messages, mapped to quantum subsystems by `Θ` (RO1-SPEC-r3 §6.3). It is not specified |
| Assumptions | `Θ` (proposed, S8); access closure (required, #1169 c.6876591512, answer 4); the reading (S6) |
| Evidence status | Indexed by the reading of P-vii. **Under global P-vii:** [R, main] for separated wings on F, D-ceil gives a local hidden-variable model, so `|S_CHSH| ≤ 2` (:20, :364–389). Its hypotheses are: (i) deterministic dynamics; (ii) setting operations on disjoint regions at one step, each reading and writing only its own region; (iii) readouts outside the remote cone; (iv) `p(Ω | a,b) = p(Ω)`; and a ±1 outcome recorded in every run. [A-inf] Local correlations lie in the quantum set, so the two-wing Bell experiments within that scope are sound. That is at the cost of Bell coverage (track (b)). It says nothing about wings inside each other's cone (:414), experiments with messages, other two-wing experiments, or I (no transfer given). **Under the scoped reading:** not shown. [R, kernel] D-comp and D-OIplus have no two-wing statement. [R, reviewed, not merged] "On one carrier without `Θ`, a PR table is an ordinary classical channel and is not excluded" (RO1-SPEC-r3 §7.4). [R, main] Separated instruments compose as `𝓘_a ⊗ 𝓘_b` (:572); "the same reversible machinery can realize non-quantum finite instrument families" (:582) |

**Chain, in order.**
1. **C-1 is resolved** (track (b), step 2). Under global P-vii no model of the premises reaches the
   quantum value for separated wings on F. So no bound below 4 that keeps 2√2 can be tested until C-1
   is resolved.
2. **The two-wing interface is specified:**
   - `Θ` (S8);
   - where the operations live (S7);
   - the reading (S6);
   - the setting operations and their availability (S3);
   - the criterion for "executes through `Obs`" (RO1-SPEC-r3 S3).

   All are open.
3. **The premises imply a bound on remote-setting response dependence**: CHSH strictly below 4, with
   2√2 kept, under `Θ` and access closure. This is K-X / `R*` of RO1-SPEC-r3 §7.3, with its route at
   Q7 (S2).
4. **The bound holds for the enlarged executable set** if track (a)'s operation is added (§7.7, X4).

**First open step: step 2**, given step 1. The bound is step 3, not the first open step.

**Why the global-reading result does not change the first step or the verdict.** [A-inf] Under global
P-vii, soundness holds for separated wings on F only because the quantum value is excluded with PR
(D-ceil). The target needs soundness *with* Bell coverage (#914 c.6875046763, decision 3;
c.6875548603). So step 1, C-1, is still needed before a K-X that keeps 2√2 can be tested (RO1-SPEC-r3
§7.3, test (b)). The global-reading result is partial in scope, and it coexists with a coverage
failure. So it does not give SUFFICIENT. It shows no executable supraquantum experiment, so it does
not give INSUFFICIENT. The label stays UNDETERMINED.

### 7.5 Track (d): PR countermodels

**Ultimate goal.** INSUFFICIENT's condition: one model that satisfies every relevant premise at once,
with an executable supraquantum two-wing experiment.

| Item | Content |
|---|---|
| Carrier | D-PR, X-PR and V-OA2 N2.3 are all on F |
| Dynamics | D-PR: "globally coupled setting-dependent hidden dynamics" (:360). X-PR: `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-EXCL-1 l. 33). N2.3: a reversible classical computer |
| Interface | X-PR: "specified, not derived from the native OI/SM dynamics" (l. 46). `T` writes no setting (RO1-SPEC-r3 §7.2) |
| Assumptions | The settings, controllers and access grammar are stipulated |
| Evidence status | **No compatible model is on record.** [A-inf] Under global P-vii the PR gate fails P-vii, being nonlinear over `F₂`, but the quantum branch fails it too (track (b)). Under P-vii scoped to a reference class, no model is shown to meet P-L1–L3, C1–C4, P-viii–xiii, P-xiv, P-M1B and H-Bell together with an executable PR experiment. N2.3 is designed under C-PM′, C-PM and μ-G and not checked against the spatial posits. Separately built countermodels are not combined |

**Chain, in order.**
1. **"Executable" is defined.** This needs an availability criterion for setting writes, setting
   sources, clocks, records and reuse: S3, and RO1-SPEC-r3 S3's "executes through `Obs`". Open. Until
   it is defined, no construction can be checked.
2. **The reading of "one model" (S6) and the reading of P-vii are fixed.** The premise list that step 3 checks against depends on whether P-vii is global or scoped (OB-b0, OB-b1).
3. **One construction is checked against the premise list of §1 clause by clause**, with its
   preparation, setting, record and reuse operations shown executable by its own dynamics. This is
   #1143's work, with availability at #866 and #913.

**First open step: step 1.**

### 7.6 Summary

| Track | Finding | First open step | Next |
|---|---|---|---|
| (a) Operations and coverage | Coverage fails on F₂ under both interfaces; no statement on the target's carrier | The target's carrier (OB-T), then the typing (S7) | Sourcing of (iv), given both |
| (b) Bell coverage | Coverage problem under global P-vii (C-1) | An independently defined reference class | C-1 resolved by the A5 scoping test |
| (c) Quantum-set soundness | Under global P-vii: sound for separated wings on F (D-ceil), with Bell coverage lost; nothing inside the cone, with messages, or on I. Under the scoped reading: not shown | The two-wing interface and setting availability (S3, S6–S8), after C-1 | The bound `R*` |
| (d) PR countermodels | None compatible on record | A definition of "executable" (S3) | A construction checked against every premise |

No track reaches SUFFICIENT or INSUFFICIENT. The overall verdict is **UNDETERMINED**.

### 7.7 Cross-track compatibility

Five conflicts between one track's route and another track or an adopted premise. None changes the
verdict. Each constrains a route or its settling evidence.

| # | Conflict | Source | Effect |
|---|---|---|---|
| **X1** | **Superposed initial state against P-iv and P-xiv.** Track (a)'s co-requisite route to coherent preparation is P-super. P-iv selects a probability measure on configurations as the source law (:54; :724 (iv)), and P-xiv is stated on a distribution of `Ω` (:724 (xiv)). A superposed initial state is neither. The alternative, a non-aligned cut, is a change of bipartition, not a preparation. Making it physically available presupposes observables outside the configuration basis | [R, main] :54, :724; `papers/GR.md`:823 | [A-inf] Adopting P-super would need P-iv replaced, and P-xiv restated for track (b). The non-aligned-cut alternative is not independent of track (a), step 3. OB-a3 is therefore not an independent route |
| **X2** | **Track (a)'s evidence on I against track (b)'s scoped P-vii.** Track (a)'s only evidence on I uses the globally linear second-order rule (OBL-RO3-2) and the reversible finite-range update (D-phaseQ). Track (b)'s route scopes P-vii to a reference class and admits preparation-indexed dependence elsewhere | [R, off-main record] OBL-RO3-2-r2 §0; [R, main] :588 | [A-inf] Under the scoped reading, track (a)'s evidence on I covers the reference class only. It says nothing about the states where the Bell branch lives |
| **X3** | **Placement of the added operation against P-L3.** Track (a)'s positive route asks for an operation that does not preserve the diagonal. Placed in `φ`, it makes `φ` no longer a bijection of configurations, against P-L3 (:54). Main places the mixing operation as "an empirical controllability resource" (:588). The same holds for the phases: a complex diagonal is not a bijection of configurations | [R, main] :54, :588 | [A-inf] The route is compatible with P-L3 only if the operation, P-mix or P-phase, is typed into `Γ` or `Obs`. This constrains S7. The negative evidence for step 3 must be stated relative to that typing |
| **X4** | **The coverage operation enlarges the executable set under access closure.** Track (c) requires complete access closure (#1169 c.6876591512, answer 4). Track (a)'s operation enlarges `Γ`. The enlarged `Γ` then contains every composite of the new operation with the existing reversible machinery, which realizes "non-quantum finite instrument families" (:582) and PR "with globally coupled setting-dependent hidden dynamics" (:360). See also X-MENU | [R, main] :360, :582; [R, reviewed, not merged] SEL-ACCESS-1 §2 | [A-inf] An operation that supplies coverage can make a track-(d) countermodel executable unless the same interface restricts it. Tracks (a), (c) and (d) must therefore be answered on **one** interface. A coverage route that is not checked for soundness on the same enlarged `Γ` does not advance SUFFICIENT. Sharpened by §5.1: the PR machinery already lies within permutation-level operations, so the restriction soundness needs falls on the executability of settings and renewal (S3, #913) as well as on the added operation |
| **X5** | **Track (b)'s route enlarges what track (c) must bound.** Track (b) reaches the quantum value through ontic remote-setting dependence: H-Bell (i) and the adopted branch (:80). Left unrestricted, that dependence is the mechanism of D-PR, "globally coupled setting-dependent hidden dynamics" (:360). PR meets H-Bell (i)–(ii) (P-HBell row; R4) | [R, main] :80, :360; `papers/Substratum.md`:133 | [A-inf] Completing track (b) by its stated route admits the dependence that track (c) must then limit. Tracks (b) and (c) must be settled on **one** interface. Track (c)'s step 3 carries this in substance: K-X "must then limit the form or extent of that dependence" (RO1-SPEC-r3 §7.3). The verdict does not change: X5 constrains the route, and it is why track (b)'s completion cannot count toward SUFFICIENT without track (c) on the same interface |

## 8. Earliest unresolved obligations and stops

### 8.1 Earliest unresolved obligations

Named only, after §§2–7. **No minimality is claimed.** The authorization asks for "the smallest
missing independently justified physical principle, if one is needed". Minimality is not proved for
any item, so this section reports each track's obligations in the order of §7. Adopting any item as a
premise is a new premise (S10).

| # | Obligation | Track and position | What it must deliver | Home |
|---|---|---|---|---|
| OB-T | The target's carrier, with transfer arguments for the results C-2 lists. For D-cone, through (xiii) | (a) first; (b) step 4 | The carrier on which the other obligations are stated | #1055; #1169 EXACT |
| OB-S7 | The interface typing: where an added operation lives | (a) second; (c) step 2 | Constrained by P-L3 (X3) | Owner (S7) |
| OB-a1 | A sourced operation, typed per OB-S7, that does not preserve the diagonal | (a) third | Completion condition (iv), with preparation, record and resources | #866; #1169 |
| OB-a2 | A sourced phase mechanism, or confirmation that the phase intervention stays an assumption | (a) co-requisite | The phases, separately from (iv) | #866 |
| OB-a3 | A sourced coherent preparation | (a) co-requisite | Coherent preparation (D-A8). Not independent of OB-a1, P-iv and P-xiv (X1) | #866; G11 |
| OB-b0 | An independently defined reference class | (b) first | The precondition of the A5 scoping test | #1234 |
| OB-b1 | Resolution of C-1 | (b) second; (c) first | A5 scoped to the reference class with its controls, or a stated status of the response-map alternative | #1234 |
| OB-b2 | A specified response rule (LEDGER §3.4) | (b) third | The quantum value with setting-independent remote marginals | #1060 |
| OB-c0 | The two-wing interface: `Θ`, typing, reading, setting availability, and the "executes through `Obs`" criterion | (c) second; (d) first, as its availability part | The interface on which soundness is posed | S3, S6–S8; #866 |
| OB-c1 | A bound on remote-setting response dependence, under `Θ` and access closure, on the enlarged `Γ` (X4) | (c) third and fourth | CHSH strictly below 4, with 2√2 and classical contexts kept | #1060 (Q7, H-Bell); #1143 (an information principle) |
| OB-d1 | One compatible model with an executable PR experiment, or a proof that none exists under the premises | (d) third | INSUFFICIENT's condition, or its refutation | #1143; #866; #913 |

[A-inf] Whether one principle could discharge several tracks is open. By X4, any candidate must be
assessed for coverage and soundness on one interface.

### 8.2 Stops

| Stop | Where | Owner decision or open question |
|---|---|---|
| S1 / O11 | §§1.3, 7 | Model identity. [A-inf] The *label* UNDETERMINED holds under each candidate relation. A coarser `≈` only merges models: it creates no sourced experiment and no sufficiency proof. The settling evidence in §§7.2–7.5 speaks of "one fixed model", and the proposed menu constraint is S1's own question (RO1-SPEC-r3 §2.3). So S1 bears on what would settle the verdict, and stays open |
| S2 / Q7 | §§7.3–7.4, OB-c1 | H-Bell route, or exclusion stated on C directly. Not chosen |
| S3 | §§4, 5.1, 7.4, 7.5 | Availability of setting, reuse, message and coherent operations, and the criterion for "executable" (#866, #913). It is the first open step of track (d) and part of track (c)'s |
| S5 | P-xiv | Ledger Q8 |
| S6 | §§7.4–7.5 | Class or sector reading of "one model" (RO1-SPEC-r3 §2.2). INSUFFICIENT's single-model requirement depends on it |
| S7 | §§7.2, 8.1 | Typing: where an added operation lives (`φ`, `Γ` or `Obs`). P-mix is "an empirical controllability resource" (:588). OB-a1's "in one fixed model" and the negative evidence depend on it (RO1-SPEC-r3 §2.1). Placing it in `φ` conflicts with P-L3 (§7.7, X3) |
| S8 | §§4, 6 | Adoption of `Θ` |
| S9 | P-CK, P-OI⁺ | May C use complex kinematics or the OI⁺ principles as a conditional input? |
| S10 | §8.1 | Adopting any missing principle is a new premise |
| S11 | C-1; track (b)'s first link | The A5 scoping test (#1234), not authorized here |
| S12 | C-3, C-4 | Manuscript correction candidates, outside this unit |

No stop requires changing the scientific target.

## 9. Off-`main` references traced (§A.42 item 8)

Each reference is classified by the claim it is attached to:
- **provenance**: the claim does not use the content;
- **support on main**: the content the claim uses is on `main`;
- **support off main**: a gap.

| Reference | Claim it is attached to | Classification |
|---|---|---|
| RO-3, `RO3-INVENTORY-r4.md` at `78089e5e` | The three properties are distinct, and the F results need new proofs on I (header; P-i; D-memory; C-2; OB-T) | **Support off main** (gap). The underlying statements it cites, Main:113–127, :135–139, :141, :143, :155 and :157, GR:138 and the kernel modules, are on `main`. The classification across F, G and I is RO-3's, and RO-3 is unreviewed at its head |
| OBL-RO3-2-r2 at `78089e5e` | Mixing under Haar measure on the infinite-lattice linear update (P-i) | **Support off main** (gap). Accepted at its scope by owner item 2, not merged |
| LEDGER at `9ff3b8d9` §2.4, §3.4 | The QM and Bell first missing steps (§7) | **Provenance**, for the comparison "LEDGER names". The tracks' first links rest on Main:80, :582, D-iv and D-ceil, which are on `main` |
| LEDGER §3.1 | 16 response tables exhaustive; D-cone's kernel cone | **Support on main**, via the script named there, `papers/oi_lattice_code/foundations/equivalence_recovery_probes.py`, check 11, and the kernel module `OIBridge/QuasilocalAlgebra.lean` (the algebraic causal cone, l. 1328). Not re-run here |
| LEDGER §9, Bell–SM and QM–SM; §8.1, §8.4 | C-1's scoping sentence; P-E1E2; P-super; D-A8's exhaustive check | **Provenance** for C-1 (support on main: Main:362, 414; SM:104, 224). **Support on main** for D-A8 (GR:805–827). **Support on main** for P-super's BH-02 statement (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:8, 16) |
| LEDGER Q8 (l. 938) | S5 | **Provenance**: it names the question only |
| `RO1-SPEC-r3.md` on PR #1294 | `Θ`, K-X / `R*`, S1, S6, S7 | **Support off main** (gap) |
| SEL-ACCESS-1, SEL-EXCL-1, SEL-DISC-1 at their reviewed commits | X-MENU, X-PR, X-IC2; §5 Resources and Repeated use | **Support off main** (gap). Owner item 3 (#914 c.6883249235) allows the citation |
| #1143 c.6692765618 | Retention of coherence is open at #1032 | **Provenance**: a planning record |

[P] Every claim classed *support off main* is not established (§A.46 item 1), and neither is any
[A-inf] built on one.

## 10. What remains of the inventory

**Not inventoried, and not found to bear on the verdict.**
- **SM:** gauge and flavour content; H-link, H-cust, H-χ′, H-spin′.
- **GR:** the Einstein-equation route (`papers/GR.md`:162); H-count, H-slope, H-frame, H-Hawking; G3.
- **Cosmology.**
- **Structure:** its hierarchy placements, except C-3.

**Listed but not traced to every dependency.**
- The full hypothesis list of D-real's uniform-continuum theorem (:596–598).
- D-comp's rules (a)–(f) against the two-wing interface (R5).
- C-4: architecture-level supply against conditions (iii) and (v).
- The transfer of D-cone and D-ceil to I. A route through posit (xiii)'s finite-range clause is named in D-cone, not given.
- The scope of `phaseOperator_outside_ceiling` beyond the configuration interface.

[P] **Next step, proposed.** Review r3.
