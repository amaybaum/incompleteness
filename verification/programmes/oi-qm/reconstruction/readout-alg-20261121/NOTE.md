# READOUT-ALG: are OI's native readouts in the configuration algebra? (research note)

**WIP / UNVERIFIED. Paper and corpus reading only.** This note runs no computation, edits no
manuscript or reviewed record, adopts no premise and changes no status. It has not been reviewed.

- **Authority.** Owner decision #1169 c.7066541026, Decision 1: a corpus-grounded verification of
  R-READ, "not a new assumption", with every readout classified Proved, Conditional, Open or
  Counterexample, and "the definition of native readouts is not silently restricted to make the
  conclusion hold".
- **Tracking.** Issue #1512; draft PR to follow. The companion record `O1-RESTATEMENT.md` (Task B)
  is in this directory.
- **Base.** Corpus citations are against `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`.
  `Main:n`, `GR:n`, `Sub:n`, `Str:n` and `Comp:n` are lines of `papers/Main.md`, `papers/GR.md`,
  `papers/Substratum.md`, `papers/Structure.md` and `papers/Computation.md`. `EP:n` is line n of
  `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` (blob `d9d92e03`).
  Lean identifiers are in `verification/lean-mathlib/OIBridge/`, with `file:line` at the same base.
- **OPRES.** Cited read-only at `7669e511c4d5473f177444bc84de09081d375dc3` (#1511, reviewed;
  `verification/programmes/oi-qm/reconstruction/opres-20261121/NOTE.md` on that commit), as
  `OPRES §n`.
- **Layers.** K: a kernel definition or theorem on `main`, cited and not duplicated. X: exact algebra
  on paper. P: a paper argument or reading. R: a reviewed record, cited at its own status.

## 0. Outcome and the three questions

**Outcome.** No counterexample was found among the corpus's definitions of a native readout. Every
such definition gives effects in the configuration algebra: Proved on finite and countable carriers,
and Conditional on a named measurability hypothesis on measurable carriers. Every effect outside the
configuration algebra that the corpus contains enters through a named import, and in each such case
the readout primitive itself is a configuration readout. The import is a non-monomial step before
it, supplied instrument data, or an interface field whose native interpretation is an open
obligation. Six items are Open, because the corpus gives the readout as unspecified interface data or
as an unrun candidate extension (§3). The inventory covers the searched sources listed in §5 and is
evidence about those definitions only.

**Established.**
- The inventory of §2: 22 items, each classified under every reading of §1 that applies to it.
- **(N), P, with K forms cited.** Under readings R1 and R2 of §1, every native readout definition
  found is a function of the configuration, through the native dynamics, at finitely or countably
  many times. Its effects are therefore indicators of sets of configurations.
- **(I) on KIN, X.** In the Born-form representation these effects lie in ℓ^∞ (countable carriers)
  or L^∞ (measurable carriers, given the measurability hypothesis).
- **K, with X for the composite.** In each Lean interface structure the readout primitive is a
  configuration-basis projector. An effect outside the configuration algebra appears there only as
  U†PU after an available isometric step:
  - `readout_is_localLuders` (`OperationalAssembly.lean`:658);
  - `InstAvail.readout` with `readProj` (`ImplementationLocality.lean`:256, :268);
  - `fullInstruments_of_control` (`StinespringAssembly.lean`:197).
- **No silent restriction.** This conclusion does not restrict "native readout" silently. Readings R3
  and R4 are classified separately: items 14 to 18 contain effects outside the algebra, each with its
  import named.

**Assumed.**
- KIN, the Born-form representation on configurations, for every operator-level statement (OPRES §0).
- For measurable carriers, measurability of the dynamics and of the record map:
  - `Main:336` states it as a hypothesis;
  - `EP:100` requires it of every EP-schema model.

  Nonsingularity is not needed for the effect statement. It enters only the Koopman representation
  (OPRES Proposition D, U1′).
- The readings R1 and R2 of "native readout" (§1). These are readings of the corpus's definitions,
  not new premises.

**Missing.**
- **Mathematics.**
  - The corpus never ties its supplied-datum readouts (items 13 and 19) to the Definition at
    `Main:42`. That is a definitional link, not a theorem.
  - The GPT setting (item 17) has no configuration algebra in which to state inclusion.
- **Physical mechanism.**
  - For the non-DIO half of O1, no native readout supplies a coherence detector under R1 or R2.
  - A detector must come from a non-monomial step, or from a native readout that the corpus does not
    define: OPRES U2.

## 1. What is checked, and the readings of "native readout"

**R-READ (OPRES §0, §8).** Every native readout effect lies in the configuration algebra 𝒜:
- 𝒜 = ℓ^∞(C) for a countable configuration carrier C;
- 𝒜 = ℓ^∞(C_V) ⊗̄ L^∞(H) for a finite visible carrier and a standard measurable hidden carrier, acting
  by multiplication.

**Effect.** For an outcome o of a procedure with branch maps Φ_o, the effect is E_o = Φ_o*(1) on the
input carrier. For a history h of an adaptive protocol, it is the effect of the composed branch along
h. Inclusion means E_o ∈ 𝒜.

At the (N) level, without KIN, the corresponding statement is that the event "outcome o" is a
measurable set of configurations of the carrier at the protocol's start. This holds when the outcome
is a measurable function of configurations reached by the native dynamics. Under KIN the indicator of
that set is E_o.

**Readings.** The corpus uses "readout", "record", "instrument" and "observation" in four senses. They
are kept apart, so that no restriction is silent.

| Reading | What counts as a native readout | Where the corpus uses it |
|---|---|---|
| **R1** primitive | the readout operation itself: the observer registering its visible configuration, a register read, a record function | `Main:42`, `:46`; the readout fields and constructors of the Lean interfaces |
| **R2** composite native | any outcome-producing procedure built from native primitives: histories, records, auxiliary registers, adaptive feedforward, coarse-graining, discard | `Main:490`; `EP:92`; OPRES 𝒩 |
| **R3** interface-available | any outcome family that a corpus interface structure makes available, whatever its native interpretation | `FiniteOperationalTheory`, `InstAvail`, OI⁺, OI_Q, `J_exact`, K∞ |
| **R4** represented | the effect of a supplied instrument on a represented space other than the configuration span that KIN uses | the gluing realization (`Main:574–592`), D-W |

**What each reading means for R-READ.**
- R1 and R2 are the readings under which `Main:42` defines observation. They are what OPRES §5 means
  by "native readout and records".
- R3 and R4 are readouts only in the sense of an interface or a representation. A readout outside 𝒜
  under R3 or R4 refutes R-READ only if its import is itself native.
- This dependence is stated item by item in §2. It is not used to discard any item.

## 2. Inventory

Each row gives one class for each reading that applies to the item. **Proved** means inclusion
follows from the cited definitions or theorems. **Conditional** names the assumption it needs.
**Open** means the corpus does not settle inclusion. **Counterexample** gives an effect outside 𝒜,
with any import it needs.

### 2.1 Native definitions (readings R1 and R2)

| # | Item | Source | Effect | Class | Label |
|---|---|---|---|---|---|
| 1 | Observation: the observer registers its visible configuration | `Main:42` (Definition), `:46` (Lemma 1: C_V finite) | outcome x ∈ C_V; E_x = 1_{x} ⊗ 1 | **Proved** (R1) | (N) as a configuration function; (I) KIN as an operator |
| 2 | Visible history and passive record words | `RecordFibreIdentification.record` (:21), `recordFibre` (:25); `Main:560` (Q_fb: "the visible record a fixed function of each outcome"); `Sub:331` (Proposition 24.4, deterministic passive readout r : Ω → 𝒜) | E_w = indicator of {s : r(φ^j s) = w_j for all j} ⊆ S; the dual of a permutation unitary maps diagonal to diagonal (X); channel-level counterpart `isDiag_Phi` (`EquivalenceChain.lean`:253, K) | **Proved** (R1, R2) | (N); (I) KIN as an operator |
| 3 | History readout on a measurable hidden carrier | `Main:336–338` (Corollary, measurable hidden carrier) | E_{t,b} = indicator of {(x, h) : A_t(x, h) = b}. This is a genuine measurable set, so the null-set ambiguity of a singular T does not arise. No nonsingularity is used | **Conditional** on measurability of F for 2^{C_V} ⊗ 𝓗, a stated hypothesis of the Corollary (R1, R2) | (I) KIN; the named hypothesis is measurability |
| 4 | Bell outcome | `Main:376` (a ±1-valued function of the state on a readout region R_A); `Main:390` | indicator of a set of substratum configurations on a finite site set | **Proved** (R1) | (N); (I) KIN as an operator |
| 5 | Classical intervention dilation | `Main:490` (Theorem), `:494` ("classical action labels, permutation instruments") | outcomes are visible configurations; instruments are bijections, monomial, hence DIO (OPRES Lemma C, X) | **Proved** (R2) | (N) |
| 6 | Native ancilla readout of `FiniteOperationalTheory` | field `readout` (`OperationalAssembly.lean`:594); `readout_is_localLuders` (:658) gives id ⊗ ℒ_k; `localLuders` (:191) | E_k = 1 ⊗ \|k⟩⟨k\|, diagonal (X from the K form) | **Proved** (R1) for the field | (I): KIN and READ, the field (QOPS #1501 records READ as a structure field); `EP:25`: the field's native interpretation is an obligation |
| 7 | Register readout in implementation locality | `InstAvail.readout` (`ImplementationLocality.lean`:268), `readProj` (:256); `CoherentLift.readProj` (`CoherentLift.lean`:133) | `Matrix.reindex e e (readProj …)` with e an equivalence of index types, so a permutation of a diagonal projector, hence diagonal (X) | **Proved** (R1) | (I) KIN |
| 8 | The recorder | `recordInstr` (`InternalObserver.lean`:249), `recordInstr_apply` (:252) | tr(F_a X) = Σ_b X_{(a,b),(a,b)}, so E_a = E_aa ⊗ 1 (K) | **Proved** (R1) | (I) KIN |
| 9 | Passive and internal observers | `IsBlockPassiveInstrument` (`CentralObservation.lean`:164); `central_classification` (:433); `IsInternalObserver`, `internal_outcome_law` (`InternalObserver.lean`:68, :150) | The kernel states the law on block-diagonal inputs only. For general inputs: `kraus_block_vanish` (:207) makes every Kraus operator block diagonal, and `branch_scalar_on_block` (:392) makes each branch c_{a,i}·id on block i. So E_a = Σ_i c_{a,i} P_i (X from K), and P_i is a configuration projector because the blocks come from blk : S → I | **Proved** (R1) | (I) KIN |
| 10 | Adaptive, coarse-grained and feedforward composites | `availExt_bind`, `avail_coarse` (`OperationalAssembly.lean`:594); `InstAvail.bind`, `.coarse`, `.discard` (`ImplementationLocality.lean`:268); `EP:92` ("feed-forward and repeated record reads") | if every step is DIO, the composite is DIO (OPRES Lemma C, X). This holds in particular for steps in OPRES 𝒩 | **Proved** (R2) for native steps | (N) as algebra; (I) KIN as an operator |
| 11 | The EP-schema record law | `EP:92` (record maps R extract H_M(λ, π) from the same Φ); `EP:97` (p_M(h \| π, p) = μ_p({λ : H_M(λ, π) = h})); `EP:100` ("All terms must be well-defined in the declared measurable model") | the event of h is a measurable set of seeds, pulled back through ι and Φ to configurations of Ω. This holds whatever carrier E declares (`EP:73`), because the history law is a law over λ | **Proved** (R1, R2) inside the schema | (N) relative to the schema's definition; (I) KIN as an operator |
| 12 | Reviewed native-record assessments | F2-1 A★2 item 1 (`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md`:31–35: "The register value it records is a measurable function of the joint state … the indicator basis of a measurable partition"), scope at :341; O-ACC P2-G (`verification/programmes/oi-qm/reconstruction/o-acc-native-record-20261117/O-ACC.md`:51, current-slice functions) | indicator projectors of a measurable partition | **Proved** (R1), at the records' own scope: classical couplings that record set membership | (N), P, R |

### 2.2 Readouts given as data, open readings, and the book mirror

| # | Item | Source | Class | Note |
|---|---|---|---|---|
| 13 | Supplied-datum readouts | `Sub:249` ("The observational datum must specify the visible/hidden interface, the admissible preparations and the readouts"); `Str:720` ("the declared preparation and readout") | **Open** | The readout is an interface datum. No definition places it in 𝒜, and none places it outside. Read as an observation in the sense of `Main:42`, it is item 1, and so Proved. Identifying the two is the definitional link named under Missing |
| 17 | Effect availability in the GPT reconstruction track | `verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/result.md` (`fullEffects_subset_avail`, `sharpFamily_subset_avail`); `round-k1-bridge-1-effect-availability/result.md` (`k1b_core`) | **Open** (R3) | The carrier is the ball `eball d`, with no configuration algebra, so inclusion in 𝒜 cannot be stated. Its four hypotheses (body preservation, K∞-Seed, K∞-Trans, K∞-V4) are unsourced, and the round "attributes none of these hypotheses to OI" |
| 19 | "Efficient measurement" in the conditional BQP model | `Comp:106` | **Open** (R3) | The measurement basis is not stated. Operational closure ("all admissible operations … are standard quantum instruments") is an imported premise |
| 20 | The wave-operator lift (L3) | F2-1 A★ N8 (`A-star.md`:338–340: "fails on the readout and on the native carrier") | **Open** | No native readout of field amplitudes as quantum amplitudes is defined |
| 21 | PC-1 candidate coupling | `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md`:125–135 | **Open** | A candidate F2 extension. It must break one of A★2's premises, among them (ii) the indicator readout. It is a preregistration only, and nothing was run |
| 22 | The book's fixed-basis readout | `book/glossary.md`:21 (Born rule); `book/ch01-observation.md` | **Proved** (R1) | It mirrors items 1 and 2. No distinct definition was found |

### 2.3 Interface and represented readouts (readings R3 and R4)

| # | Item | Source | Class | Import that places the effect outside 𝒜 |
|---|---|---|---|---|
| 14 | `FiniteOperationalTheory.avail` and `availExt` in general | `OperationalAssembly.lean`:594; `HasCompositeUnitaryControl` (:665); `fullInstruments_of_control` (`StinespringAssembly.lean`:197) | Without a control hypothesis: **Open** (R3). The field is abstract and unconstrained. With `HasCompositeUnitaryControl` and the explicit hypothesis `FiniteIsometryExtensionSF` of `fullInstruments_of_control`: **Counterexample** (R3). Every finite endomorphic instrument is available, including one whose branch is the conjugation by the projector onto H\|i⟩, whose effect H\|i⟩⟨i\|H is not diagonal | `HasCompositeUnitaryControl`, a composite-control (FLOW-type) import. The readout field stays diagonal (item 6), and the effect leaves 𝒜 through `conjChannel U` |
| 15 | OI⁺ and its primitive-source form OI⁺min | `Main:594–598`; `GR:229–245`; `carrier_general_oiPlus` (`CarrierGeneralOIPlus.lean`:213); `oiPlusMin_iff_qm` (`MinimalRepertoire.lean`:569) | **Counterexample** (R3) | Reversible richness, or phase-free richness (a continuously driven transition, which is non-monomial). The register readout is item 7. `GR:241`: "an axiomatic completion theorem, not a derivation of the additional principles from bare OI" |
| 16 | Observables of the OI_Q region completion | `GR:279` ("the observable algebra is the full matrix algebra on the region's finite configuration space"); `GR:286` (OI_Q = "the current OI substratum together with continuous off-diagonal controllability") | **Counterexample** (R3) | Continuous off-diagonal controllability. The corpus names these elements observables, not readouts, and gives no readout procedure for them |
| 18 | The gluing realization and the single controlled dynamics | `Main:574–592`; `Main:590` ("Quantum mechanics enters as the instrument data and as the state held in the hidden register") | On the realization's carrier: **Proved** (R1, R2). The outcome is written to the visible record by a reversible step. On the comparator space: **Counterexample** (R4). The effects are arbitrary supplied instrument data | Supplied instrument data, on a represented space that is not KIN's configuration span. A detector in this sense is not a detector in OPRES's sense. GATE-A r5 T-SUB′ clause (iv) (#1503 at `fd3cb064`) excludes such simulator access ("an apparatus running a simulator of a stored state does not count as access") |

## 3. Result

**Theorem RA-1 (corpus inclusion; (N) as a statement about configuration functions, (I) on KIN as an
operator statement; P with the K forms cited).**
- **Scope.** The native readout definitions of §2.1, items 1 to 12, under readings R1 and R2.
- **Statement.** Every outcome event is a set of carrier configurations at the protocol's start:
  - finite or countable when the carrier is;
  - measurable when the carrier is measurable and the dynamics and record maps are measurable
    (item 3, `EP:100`).
- **Consequence under KIN.** Every effect lies in 𝒜.
- **Proof.**
  - Each definition makes the outcome a function of a configuration reached by the native dynamics:
    a bijection, a permutation instrument, or a configuration-projector readout.
  - Composition, feedforward, coarse-graining and discard preserve this property (OPRES Lemma C;
    item 10).
  - The preimage of an outcome under a measurable map is measurable. ∎
- **Grade.** The inclusion is close to definitional: `Main:42` and Lemma 1 make the outcome a visible
  configuration. What the inventory adds is that no definition in the searched corpus departs from
  this, including those with histories, records, registers, adaptive protocols and coarse-graining.

**Proposition RA-2 (where non-configuration effects enter; K and X).** In every corpus structure in
which an effect outside 𝒜 is available (items 14, 15, 16), the readout primitive is a
configuration-basis projector (items 6 and 7). The outside effect arises only as U†PU, after an
available non-monomial isometric step whose availability is the named import. In item 18 it arises on a
represented space, from supplied data.
- This is the interface counterpart of OPRES Corollary C1.
- No formal map between these structures is claimed.

**Open (§2.2).** Items 13, 17, 19, 20 and 21, and item 14 without a control hypothesis, are Open.

- None of them supplies a native readout outside 𝒜. None is shown to be inside 𝒜 either, except by
  identifying it with item 1.
- They are where a native coherence detector could still be defined. Defining one would be a new
  physical premise. This record does not propose or adopt one.

**No counterexample under R1 or R2.** No admissible native readout outside 𝒜 was found. The
counterexamples of §2.3 each need a named import, and none of those imports is native in the corpus:
- `EP:25`: the native interpretation of the interface fields is an obligation;
- `GR:241`: OI⁺ is not derived from bare OI;
- `GR:286`: OI_Q is not bare OI;
- `Main:590`: in the gluing realization, quantum mechanics enters as supplied data.

## 4. Pressure test of the favourable reading (§A.31)

The outcome favours OPRES's conditional verdict, so each reading that could break it was checked.

1. **Could a visible configuration be a coherent superposition?** No.
   - `Main:42` speaks of "finitely many distinguishable internal states", and `Main:54` makes φ a
     bijection on S.
   - KIN places configurations in a basis. It does not place them in arbitrary vectors.
2. **Two-slice or phase-space readouts.** These include SM's second-order update and the O-ACC
   two-slice access.
   - A function of the pair of slices is a configuration function on the pair carrier, and that pair
     carrier is the one the reversible update acts on (`GR:290`, `leap_eq_swap_shear`).
   - This stays inside 𝒜 provided that KIN is taken on the pair carrier. If KIN were taken on
     single slices while the dynamics acts on pairs, the representation would not be the bijection's
     permutation lift. The corpus does not do that.
3. **Readouts of the hidden sector.** The corpus defines no observer readout of H. Lemma 2
   (`Main:48`) makes H the inaccessible complement. Proposition D's hidden configuration readouts
   are countable partitions in 𝒜, and OPRES records that a normal Lüders instrument for a continuous
   hidden PVM does not exist.
4. **Continuous or coarse-grained readouts.** A measurable function of configurations has
   indicator level sets in L^∞. Coarse-graining sums indicators.
5. **Singular dynamics or non-normal hidden states.** The effect statement concerns genuine
   measurable sets. It does not depend on Koopman unitarity or on the normality of the hidden state,
   so U1′ does not reach R-READ.
6. **Composite procedures that hide a non-monomial step.** These are excluded from R2 by definition
   only when the step is not native. That is exactly the condition under which OPRES places the
   creator and detector in the step, and not in the readout. The exclusion is therefore not a
   restriction of the readout notion; it is Proposition RA-2.

None of the six checks found a native readout outside 𝒜. The remaining risk is a native readout that
the corpus has not yet defined. That is OPRES U2, a physical question, and it is not settled by
reading the corpus.

## 5. Search record

- **Terms.** readout, read-out, record, instrument, observation, outcome, measurement, pointer,
  detector, effect, Lüders. In Lean, also definitions whose names contain Readout, Record,
  Instrument, Observ, Passive, Outcome or Luders.
- **Sources searched.** `papers/*.md` (all twelve), `book/glossary.md` and the `book/ch*.md` chapters
  by grep, `verification/lean-mathlib/OIBridge/*.lean` (245 files) by definition grep, and
  `verification/programmes/oi-qm/**` by directory listing and grep.
- **Reviewed records read in part.**
  - the `oi-qm-ext-1` endpoints;
  - O-ACC, F2-1 A★, PC-1, EFF-1 and K1-BRIDGE-1;
  - QOPS-P2 (#1501 at `cd3672fa`);
  - GATE-A r5 (#1503 at `fd3cb064`).
- **Records not read in full.** Records under `oi-qm/reconstruction/` other than those named. Their
  directory names were checked for readout and record topics. `measurement-record-formation`,
  `observer-access-20261106`, `apparatus-1-20261107`, `record-control-20261107` and
  `meas-q-20261120` were identified but not read line by line.
- **The finding is a finite search.** It is evidence about the definitions found, not a theorem
  about every readout the corpus could later define.

## 6. Classification

| Item | Label | Layer | Class (§A.31) |
|---|---|---|---|
| Theorem RA-1 | (N) as configuration functions; (I) KIN as operators; the measurable case is conditional on measurability | P, with K forms | CONFIRMING (R-READ under R1 and R2) |
| Proposition RA-2 | (I): the named import in each structure | K, X | POSITIVE: it locates every non-configuration effect at a non-monomial step or in supplied data |
| §2.2 open items | — | P | open; candidate locations of a native detector |
| §2.3 counterexamples | (I): composite control; reversible or phase-free richness; off-diagonal controllability; supplied data | K, P | not native, so not counterexamples to R-READ under R1 or R2 |

**Bearing on OPRES.**
- OPRES §5's verdict was conditional on R-READ. For the native readout definitions of §2.1 that
  condition is met: Proved on countable carriers, and Conditional on measurability on measurable
  carriers.
- It is not met for the open items of §2.2. Those remain the place where a native coherence detector
  could be defined (OPRES U2).

## 7. For owner decision (nothing adopted)

1. Whether readouts given as interface data (`Sub:249`, `Str:720`), and the native interpretation of
   `J_exact` labels (`EP:47`), are required to be observations in the sense of `Main:42`. If they
   are, items 13 and 19 become Proved. If not, they remain Open, and they are where a native
   non-DIO readout could be defined.
2. Whether the measurability hypothesis of `Main:336` is to be stated as part of R-READ on measurable
   carriers. `EP:100` already requires it of EP-schema models.

## 8. What this note does not do

It edits no manuscript, reviewed record or Issue body other than its own. It runs no computation and
dispatches no workflow. It adopts no premise and posts nothing on #1169. It makes no broader
quantum-operational claim.
