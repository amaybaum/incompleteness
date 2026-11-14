# RO-1 step 2: premise dependency assessment for sector C, r1

**UNREVIEWED.** This is the first draft of the RO-1 step 2 assessment. It is a dependency assessment
and not a proof. It establishes no result, adopts no premise, extension E or sector condition C, and
changes no Issue's scope, tier, readiness, authorization or writer.

**Authority.** #914 c.6883931412 (`amaybaum`, 2026-11-14T20:43:54Z), item 1, quoted verbatim in part:
"I authorize RO-1 Step 2 as a bounded, paper-only dependency assessment, with Claude as writer and
ChatGPT as independent exact-head reviewer. First investigate whether the existing OI axioms, posits
and conditions, considered together, already impose the physical restrictions needed to select
quantum operational behaviour." It continues: "Stop wherever progress requires adopting a new premise,
choosing Q7, resolving an open model-identity question or changing the scientific target." And:
"Preserve RO-1 r3 and its reviews. No new physical premises, scientific computation, Lean work,
manuscript changes or merges are authorized." "Physical source remains NOT PASSED."

**Reviewer's standards, relayed by the coordinator.** The assessment ends with one of three verdicts:
- **SUFFICIENT.** One model and interface excludes non-quantum behaviour and keeps the required
  quantum preparations, coherent operations, incompatible measurements, Bell correlations and
  compositions.
- **INSUFFICIENT.** There is a proof that one model satisfies every premise at the same time, and the
  non-quantum experiment is shown to be physically available.
- **UNDETERMINED.** The first missing implication is named, with the evidence that would settle it.

**Writer:** Claude Code. **Reviewer:** ChatGPT, after an independent review.

**Base.** `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`. Off-`main` sources are cited at
exact commits:
- SEL-ACCESS-1 #1224 at `1b966a03`, SEL-EXCL-1 #1228 at `0ecfddeb` and SEL-DISC-1 #1281 at
  `445b17f7`: each reviewed, not merged;
- RO-1 `RO1-SPEC-r3.md` on PR #1294, ChatGPT ACCEPT WITH NITS (review 5906972784);
- RO-3 on PR #1303 at `78089e5e`, accepted at its stated scope by #914 c.6883931412 item 2;
- LEDGER, `LEDGER-r8.md` on the ledger branch at `9ff3b8d9`: an off-main record.

**Method:** reading only. No computation on OI rules, no Lean, no edit, no post.

**Labels.**
- **[R]** existing result, with its evidence state:
  - *main*: a manuscript statement on `main`;
  - *kernel*: a Lean theorem on `main`, cited from the manuscript or a programme file; not rebuilt
    here;
  - *record on main*: a verification record on `main` whose own status is paper-level and not
    adopted. Under §A.46 items 1 and 7 it is not an established premise, and it is used here only at
    its stated scope;
  - *reviewed, not merged*;
  - *off-main record*.
- **[P]** proposed obligation or definition.
- **[A]** unproved assumption. **[A-inf]** marks an inference drawn here: unreviewed, and treated as
  unproved.
- **[STOP Sn]** a point where progress needs an owner decision, a new premise, Q7, the O11 choice or
  a change of target. These are listed in §9.

**Domains.** Each result is stated only for the carriers it is proved on. RO-3's classes are used:
- **F**: one fixed finite carrier;
- **G**: a family of finite models of growing size;
- **I**: an infinite completion.

[R, off-main record] RO-3 finds that exact recurrence, exact common visible return and
recurrence-based P-indivisibility are three different properties. They hold on F at recurrence-cycle
scope and do not transfer to I without new proofs (`RO3-INVENTORY-r4.md` §§1.1–1.3, 2.4–2.6, at
`78089e5e`; the confirmation addendum keeps them distinct).

**Scope of r1.** The matrix in §1 covers the premises that bear on sector C: membership, confinement,
closure, soundness and coverage. Premises that bear only on downstream branches are not inventoried
here. §10 lists them: the SM gauge and flavour content, the GR field equation and its coupling,
cosmology, and black-hole information.

**Verdict, in one line.** **UNDETERMINED.** [A-inf] The existing premises are not sufficient for
coverage under the interface they presently source. Soundness against supraquantum behaviour is
undetermined. The first missing implication is named in §7.

***

## 1. Premise dependency matrix

The columns are:
- **Kind**: foundational assumption (FA), derived result (DR), conditional (CO), imported structure
  (IS), empirically selected (ES), or proposed extension (PX);
- **Domain and dependencies**: where the item is proved or stated, and what it rests on;
- **Adopted**: whether the manuscript adopts it;
- **Joint satisfiability**: whether one fixed substratum and interface can satisfy it together with
  the others. Conflicts are named in §3.

### 1.1 Foundations and posits (`papers/Main.md`)

| ID | Statement (source) | Kind | Domain and dependencies | Adopted | Joint satisfiability |
|---|---|---|---|---|---|
| P-Ax1 | "**Axiom 1** … tokened differentiation occurs … equivalently, *embedded representation occurs*" (:36) | FA | All; the perspectival reading makes `V ⊊ S` part of the primitive (:38) | Yes | No conflict found |
| P-Def | "An *observation* is a triple `(S, φ, V)` … an observer `V ⊊ S` — a proper subsystem with finitely many distinguishable internal states, coupled to the complement" (:42) | FA | All | Yes | No conflict found |
| P-L1 | Lemma 1: "The observer has finitely many distinguishable internal states, so the visible configuration space is finite" (:46). Finiteness "is stipulated per moment rather than derived" (:724) | FA (stipulated) | Observer only. It does not make `S` finite: "The recurrence proof … requires S finite, which Lemma 1 does not supply" (`papers/GR.md`:138, quoted in RO-3 §1.1) | Yes | Compatible with F, G and I |
| P-L2 | Lemma 2: "The observer is a proper subsystem … The complement `H = S \ V` is the hidden sector" (:48) | FA | All | Yes | No conflict found |
| P-L3 | Lemma 3: `φ` is deterministic and, "as the reversible representative of §1.2, a bijection" (:54) | DR / ES | Determinism follows from the composition law (:44). Bijectivity is posit (iii), "part-empirical rather than a pure lemma" (:724) | Yes | No conflict found |
| P-i | Axiom 2, recurrence: "owned as a posit with a non-derivability countermodel" (:724, item (i)) | FA (posit) | Finite representative. [R, off-main record] On I, recurrence is open, and for the posited linear rule at prime `q` "no nonzero finitely supported configuration is periodic" (RO-3 §1.1). [R, off-main record] On the infinite-lattice linear update, mixing under Haar measure holds within the hypotheses of OBL-RO3-2-r2 (#914 c.6883931412 item 2) | Yes | **Conflicts with the target if read as exact recurrence of the whole model** (C-2, §3) |
| P-ii | Total finiteness of the bijective representative, A1 (:724, item (ii)) | FA (posit) | F | Yes, in the manuscript | **Conflicts with the target** (C-2) |
| P-iv | "the maximal-entropy invariant measure compatible with the observer's records" (:724, item (iv)); Lemma 3's counting measure (:54) | FA (posit) | F, where the counting measure exists. On I a replacement is needed. [R, off-main record] Haar measure in OBL-RO3-2; `referenceState` invariance is open (#914 c.6883931412 item 2) | Yes | Open on I |
| P-v | The hidden-sector mixing hypothesis (:724, item (v)) | CO | C2-slow necessity direction; "remains open" | Conditionally | Not bearing on C directly |
| P-vii | Linearity of the update, A5 (:724, item (vii); `papers/Substratum.md`:100: "the further restriction to linear is imposed") | FA (posit) | Spatial results | Yes, globally | **Conflicts with the adopted Bell branch** (C-1) |
| P-viii–xiii | Site factorization; bounded degree; nearest-neighbour range on the reference class; center independence; background independence; the second-order form (:724, items (viii)–(xiii)) | FA (posits) | Spatial results, causal cone and Bell ceiling (§3.3), observer selection (§4.6). (xiii) is "a posit of the selected lattice model, not derived and not an axiom of OI" | Yes | (x) holds "on the reference vacuum/uniform state class" only; see C-1 |
| P-xiv | Measurement independence, `p(Ω | a,b) = p(Ω)`, "a posit about the initial condition, not derived" (:724, item (xiv)) | FA (posit) | Bell analysis only | Yes: "the Bell-violating branch adopted in §3.3 retains measurement independence" (:80). Ledger Q8 asks whether it is admissible as a posit (LEDGER:938) | **[STOP S5]** (RO1-SPEC-r3 S5) |
| P-C1–C4 | (C1) non-zero coupling (:72), (C2) memory persistence (:74), (C3) capacity (:76), (C4) history readback (:78). "our universe lies in the observer-admitting subset of substrata … This is the C1–C4 selection condition" (:34); "observer-admitting" (`papers/Structure.md`:120) | FA (selection commitment) and DR (diagnostics) | F at recurrence scale for the derived parts (:80). (C4) is met by "a pre-sampled hidden variable revealed by the history … (the response-table construction, §3.4)" (:78) | Yes | No conflict found. Independent of the completion conditions (D-oi-alone) |
| P-EM | The effective-mixing hypothesis (EM), with `τ_mix ≪ τ_S` (:742, :758) | CO | Observer selection (§4.6). It uses "bounded coupling, finiteness of `S`, the canonical-typicality result [31], and … (EM)" (:758) | Conditionally | Finite `S` conflicts with the target's carrier, so a transfer is needed (A-inf) |
| P-M1B | M1-B: "Bell-violating composites take [Main §3.3]'s measurement-independent, ontically parameter-dependent branch with operational no-signaling" (`papers/Substratum.md`:123) | ES / modelling premise | Bell composites | Adopted as the branch (:80) | **Conflicts with global P-vii** (C-1) |
| P-HBell | H-Bell: preparation-indexed graphs must "(i) supply the required ontic parameter dependence, (ii) preserve operational no-signaling, and (iii) satisfy a metric/Ollivier–Ricci stability condition" (`papers/Substratum.md`:133) | CO (open hypothesis) | The Bell branch | No: open | Compatible with PR on (i) and (ii); (iii) is not applied to PR (RO1-SPEC-r3 §7.4) |
| P-MD | The measurement-dependent alternative: `CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}` (:416–423) | PX | Bell | "recorded, not adopted" | Does not exclude PR (bound allows 4) |
| P-CK | Complex matrix kinematics, "a kinematics whose derivation from operational premises is open" (:562). Decision 4 (#914 c.6875046763): "Allowed as a conditional mathematical input, not a physical explanation" | IS | F (finite carrier) | As a conditional input only | **[STOP S9]** for use in C (RO1-SPEC-r3) |
| P-Born | "The Born dictionary `p = |U|²` is part of the definition of `Q_fb`: the equivalence exhibits the Born form and does not select the quadratic exponent" (:18) | IS (definitional) | Finite horizons | As definition | No conflict with Main. **Conflicts with Structure's wording** (C-3) |
| P-mix | "the continuously tunable state-mixing operation … added as an empirical controllability resource" (:588); the phases "as a stated intervention principle rather than a consequence of its finite states and bijective dynamics" (:588) | PX | F, every nonempty finite carrier | No | Not sourced: "Physical source remains NOT PASSED" |
| P-OI⁺ | OI⁺: "well-formedness together with observational independence, reversible richness, and observer recursion", with "OI⁺ ⟺ exact finite endomorphic operational QM" (:584–586); its primitive-source and substratum-source forms (:588; `papers/GR.md`:256) | PX (characterization) | F, "every nonempty finite carrier" | No: "not a claim that bare OI entails the added principles" (:588) | Within complex matrix kinematics (:584). **[STOP S9]** |

### 1.2 Derived results that bear on C

| ID | Result (source) | Kind and support | Domain | What it does not give |
|---|---|---|---|---|
| D-SDQ | `S ⟺ D ⟺ Q_fb` on every finite horizon (:14–16, :80) | DR; [R, kernel] `finite_horizon_equivalence` (LEDGER §2.1) | Finite horizons, fixed basis | It is "universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process" (:18). It does not give "all coherent preparations, noncommuting interventions, and composites" (:554) |
| D-real | "every finite stochastic law, including every finite quantum record, has a finite reversible OI realization; bounded quantum instrument families are uniformly realizable to arbitrary finite accuracy" (:80); fixed finite adaptive families via the comb theorem (:556) | DR (paper; kernel in parts) | F per law or family; G across accuracies | It is mathematical availability, not physical sourcing (§2.5). "the all-horizons fixed-representation question remains open" (:556) |
| D-PR | "if the two wings are allowed to share globally coupled setting-dependent hidden dynamics, the same reversible response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box behavior" (:360) | DR (paper) | F | It does not show the construction is physically executable, or that it meets the spatial posits (P-vii, P-x) |
| D-cone | The coupling-graph causal cone: influence moves at most one graph edge per update (:362) | DR (paper; algebraic cone in kernel per LEDGER §3.1) | `S = ∏ S_i` with `V` and each `S_i` finite (:362) | Relative to the identification (viii) |
| D-ceil | Bell ceiling for a screened local completion: under (i) determinism, (ii) product setting operations on disjoint regions, (iii) readouts outside the remote cone and (iv) `p(Ω | a,b) = p(Ω)`, `|S_CHSH| ≤ 2` (:364–389) | DR (paper; 16 response tables exhaustive per LEDGER §3.1) | As stated | Excludes PR *and* the quantum value under the same hypotheses |
| D-lin | Under linearity, the dependence graph is the same at every state, so preparation-indexed edges lie "outside ledger item (vii)" (:362, :414; `papers/SM.md`:104) | DR (exact algebra, per LEDGER §3.1) | Spatial | — |
| D-comp | The operational-completion characterization: with complex matrix kinematics given, the available families "are exactly the normalized finite Kraus instruments" iff (i) valid probabilities, (ii) trivial-ancilla consistency, (iii) inert spectators, (iv) full reversible control, (v) iterated composition (:562) | DR; [R, kernel] `exactAll_iff_physical_general` (:562) | F, every nonempty finite carrier | The kinematics is imported (P-CK) |
| D-oi-alone | (i)–(v) are "each independent of the others and of the C1–C4 process, witnessed on the qubit by theories realizing one fixed finite C1–C4 process" (:562) | DR; [R, kernel] `five_way_minimality`, `oi_alone_not_qm` (:562) | F (qubit witness) | — |
| D-iv | "Under the substratum's stated interventions … (iv), full reversible control, is not supplied" (:80) | DR; [R, kernel] `substratumGen_not_control`, "on the two-state carrier" (:80) | F, two-state carrier | Other carriers and extended mechanisms are open (:80) |
| D-nonneg | "every operation the present observer interface sources preserves nonnegative entries (`NonnegBounded`), a property that the quantum phases and dense unitary control each violate" | DR; [R, kernel, record on main] `frozen_sourcing_verdict`, `nonnegBounded_verdict`, `sourcing_rule_independent` (`verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84). "this is a sourcing no-go for the presently stated architecture … it does not show that an extended architecture cannot source the resource" | The present interface | Extended architectures |
| D-dim | No fixed finite carrier reproduces "the entire exact continuum operational theory of even a qubit at all preparations/effects and all precisions" (:558, :562) | DR (paper; factorization half proved, unboundedness of nonnegative rank imported from [55], per LEDGER §2.1) | F | It does not cover I or G |
| D-approx | One finite reversible realization reproduces a bounded quantum envelope to accuracy ε (:596–598). "`D_finite` is strictly larger … its closure contains non-quantum operational theories too" (:598) | DR (paper) | G | Approximate, not exact (#914 c.6875046763, decision 2) |
| D-OIplus | "OI⁺ ⟺ exact finite endomorphic operational QM", each principle independent (:586–588) | DR; [R, kernel] `carrier_general_oiPlus`, `oiPlus_independence` | F, every nonempty finite carrier | Not entailed by bare OI (:588) |
| D-sub | Substratum plus "one continuously tunable state-mixing operation" is equivalent to operational QM, while "finite reversible read-write dynamics … does not itself generate quantum state mixing" (:588) | DR; [R, kernel] `substratum_plus_control_qm`, `qm_generated_by_substratum_extension`, `readWriteControl_independent` | F | The added operation is posited (P-mix) |
| D-memory | C4 forces conditional memory; C3 holds in every faithful realization; C2-structural holds by reversibility; indivisibility at recurrence-cycle scope "follows from any non-deterministic visible step … and does not require C4" (:80) | DR (kernel and paper, per :80) | F at recurrence scale. [R, off-main record] On I it needs exact common visible return or a replacement (RO-3 §§1.2–1.3) | It gives no coherent operation (D-oi-alone) |

### 1.3 Verification records on `main` (paper-level, not established)

| ID | Statement (source) | Domain | Bearing on C |
|---|---|---|---|
| V-OA1 | "Under one affine `φ` acting on every cell, a stored setting acts on a carrier only by translation … Fredkin bijections supply control, so the restriction is specific to the gauge-derived affine class"; "The configuration-level interface is capped for every rule [K]" (`verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`:48–59) | Affine class | Intervention limits come from the rule class, not from incompleteness |
| V-OA2 | Theorem C: "At a fixed finite carrier, reversible trace-preserving emergent operations form a finite group, for every rule"; Theorem E(b): under (H1), H-AR, (H3), (H4), (SP) and (xiv), "the prepare–measure fragment is simplex-embeddable" (`…/oa-2-20261112/STATUS.md`:56–69) | F; affine class | Under its hypotheses the fragment is classical: a coverage failure, not a soundness failure |
| V-OA3 | Lemma OBS: an additive observer holding three consecutive sites "determines the entire configuration of a finite ring of `L` sites within `2(L−3)` ticks"; Theorem S: under its conditions `G_SM`'s prepare–measure fragment "is a simplex"; "not an impossibility result for `G_SM`" (`…/oa-3-20261112/STATUS.md`:48–67) | F; `G_SM` | Incomplete momentary access need not limit reconstruction over time (§2.1) |
| V-EAR | One candidate extension's "first state/readout bridge fails … not a no-go for bare OI, other preparation/access principles, or finite-menu representations with growing dimension" (`…/oi-qm-ext-1/whole-model-bridge.md`:9–19) | F | A failed added-access extension |
| V-CA | "If (1), initialization …, and the stated physical/access closure hold, then every finite adaptive protocol over this menu has the same full record law as its reference instrument protocol"; "it does not claim that the native lattice meets its hypotheses" (`…/composition-access-20261024/REPORT.md`:1–8, 34–39) | A fixed menu | Access closure appears as a hypothesis, not a result |
| V-B4 | Record-law equality and the two-sided gauge relation differ (`…/bsel-2-b4prime-20261105/B4PRIME.md`:19, 367; Q2A and M-1 RESULT.md) | `PPer` and all-unitary class, small dimensions | O11 (RO1-SPEC-r3 §2.3) |

### 1.4 Reviewed results off `main` (reviewed, not merged)

The §A.42 gap applies to each (#914 c.6883249235 item 3).

| ID | Statement (source, exact commit) | Scope |
|---|---|---|
| X-MENU | SEL-MENU: a selector depending only on passive-law data "is **not sufficient** to guarantee target completeness" in a class containing a full/restricted-menu pair (SEL-ACCESS-1 §2, ll. 41–51, at `1b966a03`) | Conditional on its class hypotheses |
| X-PR | The reversible PR model, CHSH 4, under an interface "**specified, not derived from the native OI/SM dynamics**" (SEL-EXCL-1 l. 46, at `0ecfddeb`); fresh-cell no-signalling within the declared grammar (§3); same-seed reuse signalling in the enlarged grammar (§7) | Designed countermodel; menu assumed |
| X-IC2 | PR gives `J = 2`; classical-local and quantum-local references give `J ≤ 1`; native principle "Not supplied" (SEL-DISC-1 D5–D8, at `445b17f7`) | Conditional discriminator |

## 2. Joint implications

### 2.1 Incomplete information versus limits on executable interventions

[R, main] P-L2 gives incomplete momentary access: "an observer that could access all of `S` would have
nothing external to observe" (:48).

[R, main] No axiom, lemma or posit of Main specifies an intervention repertoire. The interventions
that §3.4 uses are supplied with the experiment family. The comb theorem "realizes any FIXED finite
adaptive family" (:556), and (iv) is not supplied by the substratum's stated interventions (:80).

[R, record on main] Limits on executable interventions found so far come from the rule class (V-OA1:
affine `φ` gives translation-only control; Fredkin bijections do not). They do not come from
incompleteness.

[R, record on main] Incomplete momentary access does not bound what is learned over time: an
observer holding three consecutive sites of the `G_SM` ring determines the whole configuration
within `2(L−3)` ticks (V-OA3, Lemma OBS).

[R, reviewed, not merged] SEL-MENU: a selection that reads only passive data cannot force an
operation repertoire (X-MENU).

[A-inf] **Incomplete information does not, by itself, limit executable interventions, and does not,
by itself, select a quantum repertoire.** Any limit on interventions must come from a premise about
the rule, the access interface or resources.

### 2.2 Observer capacity versus total finiteness

[R, main] P-L1 makes the observer finite "per moment". P-ii (A1) makes the whole representative
finite, and it is a separate posit (:724).

[R, main] GR:138: Lemma 1 does not supply finiteness of `S`.

[R, main] Exact coverage of a qubit's whole operational theory is impossible on one fixed finite
carrier (D-dim). Record: "the target cannot assume one fixed finite total carrier" (#914
c.6875046763).

[A-inf] **Observer capacity is compatible with an infinite `S`. Total finiteness (P-ii) is
incompatible with the exact coverage the target requires.** This is contradiction C-2 (§3).

[R, off-main record] With P-ii dropped, recurrence (P-i), exact common visible return and
recurrence-based P-indivisibility do not transfer to I without new proofs (RO-3).

### 2.3 Determinism versus locality versus measurement independence

[R, main] D-ceil: determinism, setting operations local to disjoint regions with readouts outside the
remote cone, and P-xiv together give CHSH ≤ 2. That excludes PR and the quantum value alike.

[R, main] Each of the three can be weakened, with these consequences:
- **Keep P-xiv and determinism, give up parameter independence.** This is the adopted branch (:80;
  P-M1B). Its implementation by preparation-indexed edges "lies outside ledger item (vii)" (D-lin).
  Under P-vii applied globally, it is unavailable: contradiction C-1.
- **Give up P-xiv.** `CHSH ≤ min{4, …}` allows 4, so PR is not excluded (P-MD). Main also gives
  "reaching the quantum value requires `I_ont ≥ 0.0309…` bits", a necessary bound "not claimed
  tight" (:416–423).
- **Determinism is not given up.** It follows from P-L3.

[A-inf] **No combination of these three premises in the corpus excludes PR while keeping the quantum
Bell value.** Every combination either excludes both (D-ceil) or excludes neither (the adopted
branch with H-Bell, or P-MD). The adopted branch states no bound between 2√2 and 4.

### 2.4 Memory versus P-indivisibility versus coherent operations

[R, main] (C4) forces conditional memory. P-indivisibility at recurrence-cycle scope follows from any
non-deterministic visible step, without (C4) (D-memory). Both hold at their stated domains.

[R, kernel] The completion conditions (i)–(v) are independent of the C1–C4 process: a fixed finite
C1–C4 process is realized by theories that are not QM (D-oi-alone, `oi_alone_not_qm`).

[A-inf] **Memory and P-indivisibility do not imply coherent operations.** The observer conditions
constrain the process, not the operation repertoire.

[R, off-main record] On I, recurrence-based P-indivisibility needs exact common visible return or a
replacement proof (RO-3 §1.3).

### 2.5 Mathematical availability versus physically sourced operations

[R, main] D-real, D-approx and D-PR are realization theorems: for a given law or bounded family, some
finite reversible system realizes it.

[R, kernel, record on main] The operations that the present interface actually sources preserve
nonnegative entries, which "the quantum phases and dense unitary control each violate" (D-nonneg).

[R, main] (iv) is not supplied on the two-state carrier (D-iv).

[A-inf] **What can be realized is not what is sourced.** D-real shows that quantum laws and PR laws
are both realizable. It shows neither is executable. Under the presently sourced interface, coherent
operations are absent.

## 3. Compatible and incompatible combinations

**Contradictions, named.**

| ID | Combination | Why it fails | Source | Status |
|---|---|---|---|---|
| **C-1** | Global linearity (P-vii) with the adopted Bell branch (P-M1B) implemented by preparation-indexed adjacency | Under linearity the dependence graph is the same at every state, so preparation-indexed edges "lie outside ledger item (vii)" | [R, main] :362, :414; `papers/SM.md`:104. Recorded as J-1/J-2 (LEDGER; #1234) | Owner direction for Q2: "Test A5 scoped to an independently defined reference class" (#914 c.6880010243 item 4). Not done. The "equivalent nonlocal response map" (:412) has no stated status relative to (vii) |
| **C-2** | Total finiteness (P-ii) with exact coverage of QM_fin on one fixed model | No fixed finite carrier reproduces the exact operational qubit theory (D-dim). The target excludes a fixed finite total carrier | [R, main] :558, :562; #914 c.6875046763 | The target already drops P-ii. Its uses (P-i, D-memory at recurrence scale, P-EM's finite `S`) need replacement on I (RO-3) |
| **C-3** | Structure's "Born rule, unitarity, non-Markovian marginal are features of any embedded-observer system" and "forced by the structure of observation" with Main's statements | Main: the Born form is "part of the definition of `Q_fb`" and is not selected (:18); "representability alone is not the framework's discriminating content" (:554); C1–C4 do not select QM (`oi_alone_not_qm`, :562) | [R, main] `papers/Structure.md`:872, :886; `papers/Main.md`:18, 554, 562. Recorded as D12 (LEDGER) | A manuscript inconsistency. It is a correction candidate under §A.25, outside RO-1's authorization |

**Tensions that are not contradictions.**
- P-xiv is adopted in the manuscript (:80), and its admissibility as a posit is ledger Q8. This is
  S5.
- P-EM and P-iv are stated with a finite `S` or counting measure. On I they need replacement, and
  `referenceState` invariance is open (#914 c.6883931412 item 2).

**Compatible combinations, at their domains.**
- [R, main] Bare OI (P-Ax1, P-Def, P-L1–L3, P-i, P-ii, P-iv) with C1–C4, on F: realized by finite
  reversible systems carrying memory-bearing laws (D-real, D-memory). This is compatible, but it does
  not select QM (D-oi-alone).
- [R, kernel] P-CK with (i)–(v) on F gives exactly Kraus instruments (D-comp). P-CK with OI⁺ gives
  exactly finite endomorphic operational QM (D-OIplus). Both are compatible on F, with imported
  kinematics.
- [A-inf] Bare OI without P-ii, on I: no contradiction is found in what was read. The finite-carrier
  results do not transfer (RO-3).
- [A] Whether the full posit list (i)–(xiv), with P-vii scoped to a reference class, has any model
  that also meets P-M1B and H-Bell is not established. No such model is constructed in the corpus.

## 4. Candidate restrictions: premise removal, necessity and sufficiency

"Excludes PR under executable protocols" asks whether a protocol that realizes PR is excluded when the
protocol's operations are physically available. In every row, availability is unsourced (S3), so the
answer is about the premises, given availability.

| # | Restriction (premises) | What follows | Effect of removing one premise | Countermodels and controls | Excludes PR, given availability? | Sufficiency / necessity |
|---|---|---|---|---|---|---|
| R1 | Bare OI: P-Ax1, P-Def, P-L1–L3, P-i, P-ii, P-iv | D-SDQ, D-real, D-PR on F | Without P-ii: the F results do not transfer (RO-3) | D-PR realizes PR. Classical control: realizable (D-real) | **No** (D-PR) | Not sufficient for soundness. Not sufficient for coverage (D-iv, D-nonneg) |
| R2 | R1 + C1–C4 | D-memory | Without (C4): the tape-and-ledger fair coin meets (C1)–(C3) with zero conditional memory (:78) | `oi_alone_not_qm` on the qubit (D-oi-alone). (C4) is met by response-table realizations (:78) | **Not shown.** [A-inf] Nothing in C1–C4 bounds correlations between wings | Not sufficient for coverage (kernel). Soundness against PR untested |
| R3 | R2 + P-vii global + P-viii–xiii + P-xiv, with wings outside each other's cone | D-cone, D-ceil | Without P-xiv: P-MD, up to 4. Without P-vii: preparation-indexed edges allowed (D-lin); then nothing stated bounds the correlations (P-HBell (i)–(ii) are met by PR) | The 16 response tables (exhaustive, per LEDGER §3.1). Quantum Bell reference: excluded by the same theorem | **Yes**, for wings outside the cone | Fails coverage: the quantum value is excluded too. Not a selector |
| R4 | R2 + P-M1B + P-HBell, with P-vii scoped to a reference class (Q2 direction) | Ontic parameter dependence with operational no-signalling | Without (iii) of H-Bell: the GR continuum step is lost, with no Bell consequence stated | PR satisfies (i)–(ii) (RO1-SPEC-r3 §7.4). No model meeting all of R4 is constructed | **Not shown.** [A-inf] Nothing stated bounds CHSH below 4 | Undetermined. H-Bell is open (#1060) |
| R5 | P-CK + completion conditions (i)–(v) on a finite carrier | D-comp: exactly Kraus instruments, with composites through ancilla levels | Without (iv): the substratum's interventions do not supply it (D-iv). Without any one: not QM (`five_way_minimality`) | `oi_alone_not_qm` | [A-inf] Yes for the available families: Kraus instruments on composites obey quantum bounds. This holds only if every executable operation of the model is an available family (access closure) | Sufficient and necessary *relative to P-CK, on F*. Not physically sourced. Its use in C is S9 |
| R6 | OI⁺, its primitive-source form, or its substratum-source form with P-mix | D-OIplus, D-sub | Without P-mix: finite reversible read-write dynamics "does not itself generate quantum state mixing" (:588) | `oiPlus_independence` | As R5 | Sufficient and necessary on F, within P-CK. P-mix is posited as "an empirical controllability resource". S9 |
| R7 | The present interface (D-nonneg), the affine class (V-OA1, V-OA2) or `G_SM` with its observers (V-OA3) | Operations preserve nonnegative entries; prepare–measure fragments are simplex-embeddable under the stated hypotheses | Without the affine restriction: Fredkin bijections supply control (V-OA1) | The classical simplex | [A-inf] Yes, where the fragment is classical | Fails coverage (kernel, for the present interface). Classical, not quantum |
| R8 | IC₂ (off main) | X-IC2 | Without the one-bit protocol in `Γ`: no exclusion | Classical-local and quantum-local references satisfy it | **Yes**, for fresh one-use PR, if the protocol is executable | Conditional discriminator only. Barred from C until the four conditions of #914 c.6883249235 item 4 are met. Necessity not claimed |
| R9 | RO-1 frame K-dyn … K-res (RO1-SPEC-r3) | — | — | An enlargement of the PR model, if one exists, meets it (RO1-SPEC-r3 §7.2) | **Not shown**; needs K-X | Not sufficient |

[A-inf] **Sufficiency and necessity, kept apart.**
- R5 and R6 are the only rows proved sufficient for coverage and soundness on a finite carrier. Their
  necessity is also proved, relative to complex matrix kinematics and the stated operational-theory
  rules: the characterizations are equivalences (D-comp, D-OIplus). They are characterizations of an
  extension, not consequences of the existing foundations, and they rest on P-CK and on P-mix.
- R3 is sufficient for excluding PR but fails coverage.
- No row is shown both necessary and physically sourced.

## 5. Embedded observation: what the premises give

| Aspect | What the existing premises give | What they do not give | Sources |
|---|---|---|---|
| Preparation | A common source law (P-iv, posited); exact point preparations on F | A physical preparation process selecting a carrier. [R, record on main] "a selected hidden carrier cannot be held together with its choice record, for every bijection" under μ-G with "held" a function of the present visible configuration; a ready-cell supply or a history-record convention resolves it classically (V-OA1 Gap 1) | :54, :724; OA-1 STATUS |
| Intervention | Whatever `φ` executes. On the present interface, nonnegative operations only | Coherent operations, phases, continuous state mixing (D-iv, D-nonneg, D-sub) | :80, :588; PROGRAMME.md |
| Access | `V ⊊ S`, finite per moment (P-L1, P-L2) | A limit on what is reconstructible over time (V-OA3); a limit on interventions (§2.1) | :46, :48 |
| Retention | C2-structural holds by reversibility in every bijective realization (:80) | Retention of coherence; open at #1032 (#1143 c.6692765618) | :74, :80 |
| Resources | A finite closed world bounds entropy: `H(A^m) ≤ log₂ |Ω|` (SEL-DISC-1 l. 79, reviewed, not merged) | A separator: "Scarcity alone is not a separator" (P5) | SEL-DISC-1 §4 |
| Repeated use | Fresh-cell use keeps PR no-signalling; same-seed reuse signals (X-PR) | Whether either is executable (#913, #866) | SEL-EXCL-1 §§3, 7 |
| Composition | (iii) inert spectators and (v) iterated composition are conditions of D-comp. The substratum-source form "supplies the structural architecture — closure under composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance, reversibility" (:588) | The two-wing Bell composite with local instruments on separate subsystems. Its relation to D-comp's ancilla levels is not stated (A) | :562, :588 |

[A-inf] Embedded observation, as the premises state it, constrains access per moment and the
observer's size. It does not constrain the operation repertoire, the correlation strength between
wings, or reuse. The constraints that would select QM sit in the operation repertoire (D-comp,
D-OIplus), not in embeddedness.

## 6. Soundness and coverage together

[P] The comparison uses RO1-SPEC-r3's structure-preserving correspondence `Θ` (§6.3 there; its
adoption is S8).

[A-inf] Every candidate in §4 falls into one of four groups:
- **Sound against PR, not covering.** R3: the quantum Bell value is excluded with PR. R7: classical
  fragments only.
- **Covering and sound, on F only.** R5 and R6, given P-CK, P-mix and access closure. Neither is
  sourced.
- **Neither shown.** R1, R2, R4, R9.
- **A test, not a restriction.** R8: it excludes fresh PR, given availability, and keeps the
  classical-local and quantum-local references. It is not a clause of C.

[A-inf] No combination of *established* premises keeps the required quantum preparations, coherent
operations, incompatible measurements, Bell correlations and compositions. Under the present interface
coherent operations are absent (D-nonneg), so coverage fails there before Bell is reached.

## 7. Verdict

**UNDETERMINED.**

**Why not SUFFICIENT.** [R, kernel, record on main] Under the presently sourced interface, coverage
fails: sourced operations preserve nonnegative entries, while phases and dense unitary control do not
(D-nonneg; D-iv on the two-state carrier). [A-inf] The combinations that are sufficient (R5, R6) add
P-CK and P-mix, which are not established premises: one is imported as a conditional input and the
other is posited as "an empirical controllability resource" (:588). Adopting either as physical is a
new premise (S9, S10).

**Why not INSUFFICIENT.** [A] No proof shows that one model satisfies every premise at once and has a
physically available supraquantum experiment.
- D-PR realizes PR on F, but no source shows it meets P-vii, P-x, P-M1B and P-HBell together.
- The PR gate `B ⊕ r ⊕ (x ∧ y)` is not linear over `F₂`. [A-inf] So the stated PR model fails global
  P-vii.
- SEL-EXCL-1's interface is "specified, not derived" (X-PR).

Combining separately built countermodels does not count.

**The first missing implication.** In the chain from the existing premises to quantum operational
behaviour, the first link that does not follow is this:

> *The existing premises, within one fixed model, imply a physically sourced operation supplying
> completion condition (iv), full reversible control, together with the phases.*

[A-inf] It is first because every later requirement presupposes it: coherent preparations,
incompatible measurements, composites under (iii) and (v), and the quantum Bell value. LEDGER §2.4
names the same step as the first missing step for QM (off-main record). It is refuted for the
presently stated interface (D-nonneg; D-iv) and open for any extension.

**Evidence that would settle it:**
- *Positive.* A physically sourced mechanism, in the same fixed substratum and interface, that
  executes a continuously tunable off-diagonal operation and the phases, with its preparation,
  record and resources stated. #866 owns this sourcing, and #1169 owns MECH successors.
- *Negative.* A proof that every interface meeting the existing premises preserves nonnegative
  entries. That would extend `frozen_sourcing_verdict` beyond the present interface, and coverage
  would then fail for the whole premise set.

**The second missing implication**, for soundness, once the first is supplied. [A-inf] The premises
must imply a bound on the remote-setting dependence of a wing's response, with CHSH strictly below 4
and the value 2√2 kept. This is K-X / `R*` of RO1-SPEC-r3 §7.3.

**Evidence that would settle it:**
- a derivation of such a bound from the premises; or
- one model shown to meet every premise at once, with an executable two-wing interface that
  realizes PR. That would be INSUFFICIENT, by the standard above. Constructing it is #1143's and
  #866's work.

## 8. Smallest missing premises or proof obligations

Only after the joint analysis of §§2–7. Each is named, not adopted. Adopting any is a new premise
(S10).

| # | Missing item | Kind | What it must deliver | Why it is the smallest found | Home |
|---|---|---|---|---|---|
| MP-1 | A physically sourced, continuously tunable off-diagonal operation with phases, in the fixed substratum and interface | Sourcing obligation for P-mix | Completion condition (iv) and the phases, with preparation, record and resource accounting | [R, kernel] With it, the substratum gives finite operational QM (D-sub). Without it, finite read-write dynamics "does not itself generate quantum state mixing" (:588). [A-inf] No smaller addition in the corpus reaches coverage | #866; #1169 |
| MP-2 | An independently justified restriction on remote-setting response dependence | Proof obligation or new principle | CHSH strictly below 4, the 2√2 value and classical contexts kept, under `Θ` | [A-inf] P-xiv with parameter independence is too strong (D-ceil); P-MD and P-HBell (i)–(ii) are too weak | #1060 (Q7, H-Bell); #1143 (an information principle) |
| MP-3 | Transfer of the finite-carrier results to the admitted carrier | Proof obligations | Replacements for recurrence, exact common return and P-indivisibility on I; P-iv and P-EM on I | RO-3 | #1055; #1169 EXACT |
| MP-4 | Resolution of C-1 | Owner-scoped test | A5 scoped to a reference class, with its controls (#914 c.6880010243 item 4) | — | #1234 |

[A-inf] **Whether one principle could supply MP-1 and MP-2 together is open.** The OI⁺ principles
supply both on F, through D-OIplus with access closure (R6). They are stated within imported complex
kinematics and with a posited mixing operation. Whether they may be a clause of C is S9.

## 9. Stops

| Stop | Where | Owner decision or open question |
|---|---|---|
| S5 | P-xiv (§1.1; §2.3) | Ledger Q8: is measurement independence admissible as a posit? |
| S9 | P-CK, P-OI⁺ (§§1.1, 4, 8) | May C use complex kinematics or the OI⁺ principles as a conditional input? |
| S10 | MP-1, MP-2 (§§7, 8) | Adopting any missing principle is a new premise, which this unit may not do |
| S2 / Q7 | MP-2 (§8) | Q7: H-Bell route, or exclusion stated on C directly. Not chosen |
| S1 / O11 | §§1.3 (V-B4), 4 | Model identity. Not resolved, and not needed for the verdict |
| S3 | §§4, 7 | Availability of setting, reuse, message and coherent operations: #866, #913 |
| S8 | §6 | Adoption of `Θ` |
| S11 | C-1 (§3) | Global A5 against the adopted Bell branch. The owner's Q2 direction scopes A5. Its test (#1234) is not authorized here |
| S12 | C-3 (§3) | Structure:872, :886 against Main:18, 554, 562: a manuscript correction candidate. Outside this unit |

No stop requires changing the scientific target.

## 10. What remains of the inventory

Not inventoried in r1, because the items bear on downstream branches rather than on sector C:
- **SM:** the gauge content and lattice posits beyond P-viii–xiii; H-link, H-cust, H-χ′, H-spin′;
  flavour values (LEDGER §§4–6).
- **GR:** the Einstein-equation route through Jacobson's relation (`papers/GR.md`:162); H-count,
  H-slope, H-frame, H-Hawking, G3; the deep-sector corollaries beyond GR:138.
- **Structure:** its hierarchy placements (LEDGER C-STR-7), except C-3 above.
- **Cosmology and black-hole information** premises.

Within C's scope, the following are listed but not traced to every dependency:
- the full hypothesis list of D-real's uniform-continuum theorem (:596–598);
- the composite rules (a)–(f) of D-comp's operational theory (:562), against the two-wing interface;
- the relation of the substratum-source architecture (:588; `papers/GR.md`:256) to the RO-1 frame's
  K-acc.

[P] **Next step, proposed.** Review r1. If the owner wants the inventory completed, a second pass
covers §10's downstream premises against A-REAL, and traces the three listed items.
