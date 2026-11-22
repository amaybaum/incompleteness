# READOUT-ALG: are OI's native readouts in the configuration algebra? (research note)

**WIP / UNVERIFIED. Paper and corpus reading only.** This note runs no computation, edits no
manuscript or reviewed record, adopts no premise and changes no status.

Revision r2 answers the independent review of `0ba83cff` (#1513 c.7066721761, verdict REVISE) and
its addendum (c.7066739331). It also takes in the owner recommendations at #1169 c.7066723717 and
the owner's framing decision on #1169 (three levels kept separate; native non-DIO not declared
impossible; a sufficient classifying premise named for each open instrument and site). r2
has not been re-reviewed. r3 answers review c.7066821806 (the `Main:664` update for items 1, 4 and 22;
item 24's cause; the item count; premises sufficient in one direction only). r3 has not been
re-reviewed.

- **Authority.** Owner decision #1169 c.7066541026, Decision 1. It asks for a corpus-grounded
  verification of R-READ, "not a new assumption", with every readout classified Proved,
  Conditional, Open or Counterexample. "The definition of native readouts is not silently restricted
  to make the conclusion hold".
- **Tracking.** Issue #1512 and draft PR #1513. The companion record `O1-RESTATEMENT.md` (Task B) is
  in this directory.
- **Base.** Corpus citations are against `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`.
  - `Main:n`, `GR:n`, `Sub:n`, `Str:n` and `Comp:n` are lines of `papers/Main.md`, `papers/GR.md`,
    `papers/Substratum.md`, `papers/Structure.md` and `papers/Computation.md`.
  - `EP:n` is line n of `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`
    (blob `d9d92e03`).
  - Lean identifiers are in `verification/lean-mathlib/OIBridge/`, with `file:line` at the same
    base.
- **OPRES.** Cited read-only at `7669e511c4d5473f177444bc84de09081d375dc3` (#1511, reviewed), as
  `OPRES §n`. Its note is `verification/programmes/oi-qm/reconstruction/opres-20261121/NOTE.md` on
  that commit.
- **Layers.**
  - K: a kernel definition or theorem on `main`, cited and not duplicated.
  - X: exact algebra on paper.
  - P: a paper argument or reading.
  - R: a reviewed record, cited at its own status.

## 0. Outcome and the three questions

**Three levels, kept separate (owner, #1169).** No level is substituted for another.

| Level | What is established | Status |
|---|---|---|
| **Observable effects** E_o = Φ_o*(1) | For every readout procedure the corpus defines, under R1 and R2, the effects lie in 𝒜 (RA-1). This holds on countable carriers, and on measurable carriers within the scope of `Main:336` and `EP:100` only | Proved / Conditional |
| **Complete measurement instruments**, with their state updates | DIO for items 2, 3 (non-selective) and 5–10, where the corpus fixes monomial, diagonal or block-scalar Kraus operators (RA-1′). Items 11 and 12 have no update rule in the corpus. Items 1, 4 and 22 have one only for the diagonal sector (`Main:664`); for coherent inputs the update is assigned to imports. Whether **all** native instruments are DIO is not established | DIO for the listed items; **Open** in general |
| **Operationally accessible observable algebras** | The corpus *states* that the observable algebra is the full matrix algebra (`Str:742`, `Str:788`, `Main:722`, `GR:366`). It gives no implementable measurement for any non-diagonal element. A mathematically available observable algebra is not the same thing as a set of physically implementable measurements. What the sites mean operationally, and whether they are compatible with R-READ, is unresolved | **Open** |

**Whether bare OI supplies a non-DIO operation is Open.** This record does not declare native non-DIO
impossible. It finds no native readout in the corpus that supplies one.

**Outcome, by reading.**

1. **Defined readout procedures (readings R1 and R2).** The searched corpus contains no
   counterexample at the effect level.
   - Every readout procedure the corpus defines has its **effects** in the configuration algebra 𝒜.
     This is Proved on countable carriers. On measurable carriers it is Conditional on measurability,
     a hypothesis of the measurable setting (§1).
   - At the **instrument** level, including the state update, the procedure is DIO for items 2, 3
     (non-selective) and 5–10, and for item 26 when its step U is monomial. The corpus gives those
     items Kraus operators that are monomial, diagonal, or block-scalar on configuration blocks.
   - Items 1, 4, 11, 12 and 22 are established **at the effect level only**, so they are **Open for
     O1-D**. Items 11 and 12 have no update rule in the corpus. Items 1, 4 and 22 have `Main:664`'s
     update for the diagonal sector only, which assigns coherent inputs to imports.
2. **The declared observable algebra (reading R5).** The corpus declares, in its own voice and for
   bare OI, that the observable algebra is the full matrix algebra B(ℓ²(C_V)): `Str:742`, `Str:788`,
   `Main:722`, `GR:366` and their book mirrors. `Str:742` and `Str:788` name no import. `Main:722` and
   `GR:366` name none in the sentence itself.
   - Their operational meaning, and whether they are compatible with R-READ, are unresolved.
   - If these observables were operationally readable (R5a, an unresolved premise), they would be
     counterexamples to R-READ needing no import.
   - If they are a mathematical declaration of the algebra-channel pair, with no instrument (R5b),
     they are Open as to physical implementability.
   - The corpus defines no instrument for any of them, and `Str:788` allows a smaller preserved
     algebra. So the corpus alone does not settle R-READ. Owner question 3 (§7) asks which reading
     holds, and §3.1 names a sufficient premise for deciding each site.
3. **Interface and represented readouts (R3, R4).** Every **instrument** effect outside 𝒜 that a
   corpus structure defines through branch maps enters through a named import: a non-monomial step
   before a configuration readout, or supplied data (Proposition RA-2). None of these is a native
   readout.
4. **Open.** Six items remain Open (§2.2).
5. **Scope.** The inventory covers the sources listed in §5. It is evidence about those definitions
   only.

**Established.**
- The inventory of §2: 26 numbered items, plus four further kernel definitions checked in the
  bullets of §2.2, each classified under every reading of §1 that applies to it.
- **Theorem RA-1 (effects).** Under R1 and R2, every defined readout's outcome event is a set of
  configurations reached by the native dynamics. This statement is (N) about configuration
  functions. As an operator statement it is (I) on KIN, and its effects lie in 𝒜.
- **Proposition RA-1′ (instruments).** For items 2, 3 (non-selective), 5–10 and 26, the full
  branch maps are DIO: X, from the K forms cited.
- **Proposition RA-2 (narrowed; K, X).** Wherever a corpus structure defines an instrument whose
  effect lies outside 𝒜, the readout primitive is a configuration projector. The outside effect
  arises as U†PU after an imported isometric step (items 14, 15, 26), or from supplied data on a
  represented space (item 18). This covers instruments only. The declared full observable algebra
  (items 24, 25) is not an instrument and is classified separately.

**Assumed.**
- KIN for every operator-level statement (OPRES §0).
- **The measurable setting.** It is not a new clause of R-READ; it is a hypothesis of the setting in
  which R-READ is checked.
  - `Main:336` makes measurability of F a hypothesis of that corollary only.
  - `EP:100` requires the history events to be measurable, and only for EP-schema models.
- The readings of §1. They are readings of the corpus's own definitions, not new premises.

**Missing.**
- **Definitions (mathematics).**
  - The corpus states no readout procedure for the elements of the declared full observable algebra
    (items 24, 25).
  - It does not say whether the supplied-datum readouts (items 13, 19) satisfy `Main:42`, which
    defines an observation, not a readout.
  - It gives no update rule for items 11 and 12. For items 1, 4 and 22 it gives one for the
    diagonal sector only (`Main:664`), and assigns coherent inputs to the completion and the bridge,
    both imports.
  - The GPT track (item 17) has no configuration algebra.
- **Physical mechanism.** A native coherence detector is the earliest missing mechanism.
  - Under R1 and R2 the defined native readouts supply none at the effect level.
  - At the instrument level, the corpus does not settle whether they can for items 1, 4, 11, 12 and
    22.
  - Under R5a, the declared algebra would supply one only if a readout procedure for its
    non-diagonal elements were defined. No such procedure is defined.
  - Native non-DIO is not shown impossible. Whether bare OI supplies it is Open. §3.1 names the
    sufficient premise for deciding each open instrument and site, in one direction only.

## 1. What is checked, and the readings

**R-READ (OPRES §0, §8).** Every native readout effect lies in the configuration algebra 𝒜:
- 𝒜 = ℓ^∞(C) for a countable carrier C;
- 𝒜 = ℓ^∞(C_V) ⊗̄ L^∞(H) for a finite visible carrier and a standard measurable hidden carrier,
  acting by multiplication.

**Effect and instrument.**
- For an outcome o with branch map Φ_o, the effect is E_o = Φ_o*(1). Inclusion means E_o ∈ 𝒜.
- At the (N) level the corresponding statement is that "outcome o" is a measurable set of
  configurations at the protocol's start.
- An instrument is **DIO** when every branch satisfies Φ_o*(𝒜) ⊆ 𝒜, which is stronger than
  E_o ∈ 𝒜.
  - The two levels are not equivalent. A qutrit instrument with diagonal effects can have a non-DIO
    update (c.7066739331).
  - One direction does hold. An effect outside 𝒜 already makes the instrument, with its outcome
    recorded in a configuration register, non-DIO, because the record's diagonal then depends on
    off-diagonal input entries (X).

**The measurable setting.** R-READ is checked on measurable carriers under the setting's own
measurability hypotheses, exactly as the corpus states them:
- `Main:336`: F is measurable for 2^{C_V} ⊗ 𝓗, and the coincidence sets are measurable. This is a
  hypothesis of that corollary only. The coincidence sets and the injectivity in x are used for the
  channel, not for the effect.
- `EP:100`: the history events are well defined in the declared measurable model. This applies to
  EP-schema models only.
- For classical hidden laws, the effect statement needs nothing more. For coherent hidden states,
  the operator-level effect requires OPRES Proposition D's lift: nonsingularity and normality.

**Readings.** The corpus uses "readout", "record", "instrument", "observation" and "observable" in
these senses. They are kept apart, so that no restriction is silent.

| Reading | What counts as a native readout | Corpus sources |
|---|---|---|
| **R1** primitive | a readout operation the corpus defines: an observation of the visible sector, a register read, a record function | `Main:42`, `:46`; the readout fields and constructors of the Lean interfaces |
| **R2** composite native | any outcome-producing procedure built from the R1 primitives found in the corpus and native steps: histories, records, auxiliary registers, adaptive feedforward, stopping, coarse-graining, discard | `Main:490`, `:494`; `EP:92`; `InstAvail` constructors (`ImplementationLocality.lean`:268); `availExt_bind` (`OperationalAssembly.lean`:594). OPRES Lemma C is used only for the closure algebra, not as a definition of native readout. OPRES 𝒩 is not cited as a definition, since its (n3) presupposes R-READ |
| **R3** interface-available | any outcome family that a corpus interface structure makes available, whatever its native interpretation | `FiniteOperationalTheory`, `InstAvail`, `EmbeddedObservation`, OI⁺, `J_exact`, K∞ |
| **R4** represented | the effect of a supplied instrument on a represented space other than KIN's configuration span | the gluing realization (`Main:574–592`), D-W |
| **R5a** declared observable, operational | every element of the declared observable algebra 𝒜_V is a native readout: something the observer can read out | `Str:624` (Definition 9.1), `Str:742`, `Str:788`, `Main:722`, `GR:279`, `GR:366` and the book mirrors |
| **R5b** declared observable, declarative | 𝒜_V is a datum of the algebra-channel pair used for observational equivalence (`Str:624–628`; Definition 9.3, `Str:635`), with no claim that its elements are read by a native procedure | the same sources |

- **Counterexample** has one sense throughout: an admissible native readout, under the stated
  reading, whose effect lies outside 𝒜.
- Under R3 and R4 an outside effect is recorded as "outside 𝒜 via import X (not native)". It is a
  counterexample only if X is native.
- Under R5a the declarations carry no import, so they would be counterexamples if R5a held. R5a is
  an unresolved premise: a mathematically available observable algebra is not the same thing as a set
  of physically implementable measurements.

## 2. Inventory

### 2.1 Defined native readouts (R1, R2)

The column "Instrument" records whether the corpus fixes the full branch maps and whether they are
DIO.

| # | Item | Source | Effect | Class (effects) | Instrument | Label |
|---|---|---|---|---|---|---|
| 1 | Observation of the visible sector | `Main:42` (Definition: "finitely many distinguishable internal states"), `:46` (Lemma 1: C_V finite). Reading R1 takes the outcome to be the visible configuration; `Main:42` does not say this in those words | E_x = 1_{x} ⊗ 1 | **Proved** (R1) | `Main:664` gives an update only for the diagonal sector: the Lüders rule "transcribes Bayesian updating on the classical substratum (Lemma 3) for the represented diagonal sector". The general update for noncommuting interventions is assigned there to the instrument algebra under the operational completion conditions, and "its extension to arbitrary coherent density matrices belongs to the operational bridge". Both are imports. On coherent inputs the native update is not given: **Open for O1-D** | (N) as a configuration function; (I) KIN as an operator |
| 2 | Visible history and passive record words | `RecordFibreIdentification.record` (:21), `recordFibre` (:25); `Main:560`; `Sub:331` (Proposition 24.4) | E_w = indicator of {s : r(φ^j s) = w_j for all j} | **Proved** (R1, R2) | the process is the permutation channel, DIO (X; `isDiag_Phi`, `EquivalenceChain.lean`:253, K) | (N); (I) KIN |
| 3 | History readout on a measurable hidden carrier | `Main:336–338` | E_{t,b} = indicator of {(x, h) : A_t(x, h) = b}, a genuine measurable set | **Conditional** on the corollary's measurability hypothesis | non-selective: Kraus K_C = Σ_{x∈C} \|A_t(x,h)⟩⟨x\| is row-monomial, since A_t(·, h) is injective on C, so DIO (X from `Main:338`) | (I) KIN; measurable setting |
| 4 | Bell outcome | `Main:376`, `:390` | indicator of a configuration set on a finite site set | **Proved** (R1) | as item 1: an update for the diagonal sector only (`Main:664`), with coherent inputs assigned to imports: **Open for O1-D** | (N); (I) KIN |
| 5 | Classical intervention dilation | `Main:490`, `:494` | outcomes are visible configurations | **Proved** (R2) | bijections, monomial, DIO (X) | (N) |
| 6 | Native ancilla readout of `FiniteOperationalTheory` | field `readout` (`OperationalAssembly.lean`:594); `readout_is_localLuders` (:658); `localLuders` (:191) | E_k = 1 ⊗ \|k⟩⟨k\| | **Proved** for the kernel field; native status **Conditional** on `EP:25` (the field's native interpretation is an open obligation) | Kraus 1 ⊗ \|k⟩⟨k\|, diagonal, DIO (X) | (I): KIN and READ, a structure field (QOPS #1501) |
| 7 | Register readout in implementation locality | `InstAvail.readout` (`ImplementationLocality.lean`:268), `readProj` (:256); `CoherentLift.readProj` (`CoherentLift.lean`:133) | a reindexed diagonal projector | **Proved** (R1) | conjugation by a diagonal projector, DIO (X) | (I) KIN |
| 8 | The recorder | `recordInstr` (`InternalObserver.lean`:249), `recordInstr_apply` (:252) | E_a = E_aa ⊗ 1 (K) | **Proved** (R1) | Kraus operators with a single nonzero entry, DIO (X) | (I) KIN |
| 9 | Passive and internal observers | `IsBlockPassiveInstrument` (`CentralObservation.lean`:164); `central_classification` (:433); `kraus_block_vanish` (:207); `branch_scalar_on_block` (:392); `IsInternalObserver`, `internal_outcome_law` (`InternalObserver.lean`:68, :150); `IsPassiveInstrument`, `passive_branch_scalar` (`PassiveObservation.lean`:203, :215) | E_a = Σ_i c_{a,i} P_i with configuration projectors P_i (X from K). For an unblocked passive instrument, c·1 | **Proved** (R1) | Kraus operators block diagonal and scalar on each block, hence diagonal, DIO (X) | (I) KIN |
| 10 | Adaptive, coarse-grained and feedforward composites | `availExt_bind`, `avail_coarse`; `InstAvail.bind`, `.coarse`, `.discard`; `EP:92` | — | **Proved** (R2), when every step is one of items 2, 3, 5–9 | DIO is closed under these operations (OPRES Lemma C, used for the algebra only) | (N) as algebra; (I) KIN |
| 11 | EP-schema record law | `EP:92`, `EP:97`, `EP:100` | the event of h is a measurable set of seeds | **Proved** inside the schema | the schema fixes the outcome law, not a represented update: **Open for O1-D** | (N) relative to the schema; (I) KIN |
| 12 | Reviewed native-record assessments | F2-1 A★2 item 1 (`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md`:31–35), scope at :341; O-ACC P2-G (`verification/programmes/oi-qm/reconstruction/o-acc-native-record-20261117/O-ACC.md`:51) | indicator projectors of a measurable partition | **Proved** (R1), at the records' own scope | the induced operator is a positive unital Markov operator (A★2 item 2); no represented update: **Open for O1-D** | (N), P, R |
| 26 | Adaptive stopped readout (repeat until success) | `stopped` (`BridgeFiniteProtocol.lean`:33), `instAvail_stopped` (:63), `correctedReadout` (:182), `attempt_balanced_branch` (:194) | each round is a register `readProj` after `conjChannel U`, then a diagonal correction. With U = `balancedCircuit` (:153), which is non-monomial, the pulled-back effects are outside 𝒜 | the primitives are **Proved** (R1, item 7). The composite is outside 𝒜 via the imported step U, whose admissibility is a hypothesis (not native) | the stopped composite with a monomial U is DIO (X). The realized branch with `balancedCircuit` is (5/8)·Ad_`drivePhase`, a diagonal phase | (I) on the admissibility of U |

### 2.2 Readouts given as data, open readings, and the book mirror

| # | Item | Source | Class | Note |
|---|---|---|---|---|
| 13 | Supplied-datum readouts | `Sub:249`; `Str:720` | **Open** | The readout is an interface datum. The same datum includes "the coherent reduced-channel family" (`Sub:249`), which places the interface comparison at the operator level. `Main:42` defines an observation, not a readout, and the corpus does not settle whether these readouts satisfy it. Following the owner's recommendation (c.7066723717), they are not counted as native observations automatically |
| 17 | Effect availability in the GPT track | `round-eff-1-effect-space/result.md`; `round-k1-bridge-1-effect-availability/result.md` (both under `verification/programmes/oi-qm/reconstruction/`); `CompositeInterface.SharpReadout` (`CompositeInterface.lean`:393) | **Open** (R3); not applicable as typed | The track has no configuration algebra. Its four hypotheses are unsourced, and they are not attributed to OI |
| 19 | "Efficient measurement" in the conditional BQP model | `Comp:106` | **Open** (R3) | The basis is not stated. Operational closure is imported |
| 20 | The wave-operator lift (L3) | F2-1 A★ N8 (`A-star.md`:338–340) | **Open** | The lift "fails on the readout and on the native carrier" |
| 21 | PC-1 candidate coupling | `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md`:125–135 | **Open** | A preregistered candidate extension. Nothing was run |
| 22 | The book's fixed-basis readout | `book/glossary.md`:21; `book/ch01-observation.md`:159 | **Proved** (R1) at the effect level; **Open for O1-D** | It mirrors items 1 and 2, including item 1's diagonal-sector limitation of the update |

**Item 14 without a control hypothesis** is the sixth Open item (§2.3).

**Other kernel readout definitions.** These were checked; none changes the classification.
- `OrientationClosure.ReadoutSeparating` (`OrientationClosure.lean`:165) and `stationary_readout`
  (:171): the readout is the visible diagonal ρ_ii, in 𝒜, although it is stated through a spectral
  basis V_m.
- `CoherentLift.ReadoutIntertwining` (`CoherentLift.lean`:1512): a trace condition only, with no
  effect beyond 1.
- `ObservableMeasureReturn.measuredGamma` (`ObservableMeasureReturn.lean`:74): classical ratios of
  measures of visible cells.
- `EmbeddedObservation` (`EmbeddedObservation.lean`:123): an `avail` family, classified as item 14.

### 2.3 Interface and represented readouts (R3, R4)

| # | Item | Source | Class | Import |
|---|---|---|---|---|
| 14 | `FiniteOperationalTheory.avail` and `availExt`; `EmbeddedObservation` | `OperationalAssembly.lean`:594; `HasCompositeUnitaryControl` (:665); `fullInstruments_of_control` (`StinespringAssembly.lean`:197) | without control: **Open** (R3). With `HasCompositeUnitaryControl` and `FiniteIsometryExtensionSF`: **outside 𝒜 via import (not native)**. The branch conjugating by the projector onto H\|i⟩ has effect H\|i⟩⟨i\|H | composite unitary control; `EP:25` |
| 15 | OI⁺ and OI⁺min | `Main:594–598`; `GR:229–245`; `carrier_general_oiPlus` (`CarrierGeneralOIPlus.lean`:213); `oiPlusMin_iff_qm` (`MinimalRepertoire.lean`:569) | **outside 𝒜 via import (not native)** | reversible or phase-free richness; `GR:241` |
| 16 | The OI_Q region completion | `GR:279`; `GR:286` | **outside 𝒜 via import (not native)** under R3 and R5a; **Open** under R5b | continuous off-diagonal controllability (`GR:286`) |
| 18 | Gluing realization | `Main:574–592`, `:590` | on the realization's carrier: **Proved** (R1, R2). On the comparator space: **outside 𝒜 via import (not native)** (R4) | supplied instrument data; GATE-A r5 T-SUB′ (iv) (#1503 at `fd3cb064`) |

### 2.4 The declared observable algebra (R5)

| # | Item | Source | R5a (operational) | R5b (declarative) | Import |
|---|---|---|---|---|---|
| 23 | Definition 9.1, embedded observer | `Str:624–628`: 𝒜_V ⊆ B(𝓗_V) a declared von Neumann algebra of "visible-sector observables", with Φ†(𝒜_V) ⊆ 𝒜_V | **Open**: the algebra is arbitrary | **Open** | none |
| 24 | OI's finite algebra-channel pair | `Str:788` ("the full finite observable algebra is 𝒜_V^fin = B(𝓗_V^fin) … A smaller specified algebra can be used when it is preserved by the Heisenberg adjoint"); `Str:742` ("may be taken to be the full finite matrix algebra") | **Counterexample if R5a holds** (R5a is unresolved). For \|C_V\| ≥ 2, the projector onto (\|x⟩ + \|y⟩)/√2 lies in B(ℓ²(C_V)) and not in ℓ^∞(C_V) | **Open**. No instrument is defined. `Str:788` permits a smaller preserved algebra, and ℓ^∞(C_V) is preserved by Φ^fin† for any ρ_H, because the permutation-unitary channel is DIO (X) | **none**: the bare permutation realization with a supplied ρ_H |
| 25 | Finite-region observable algebra, stated in the framework's voice | `Main:722`, `GR:366` ("Its observable algebra on each finite region is the full matrix algebra on the region's configuration space"); `book/ch07-gravity.md`:199 and `book/The-Incompleteness-of-Observation-FULL.md`:2064 (mirrors) | **Counterexample if R5a holds** (R5a is unresolved) | **Open** | none in the sentences themselves. Their cross-references (`Main:722` to §3.4, `GR:366` to §3.3) lead to the completion statements at `Main:598` (in the OI⁺ paragraph) and at `GR:279`, which `GR:286` qualifies as OI_Q. The corpus leaves open which reading is intended. Both are kept |

**Corpus tension.** `book/ch03-structural-realism.md`:168 places the noncommuting observable algebra
"conditional on the coherent operational lift". Items 24 and 25 declare the full algebra without that
condition. This record does not resolve the tension; owner question 3 (§7) asks which statement
governs.

## 3. Results

**Theorem RA-1 (effects; (N) as configuration functions, (I) KIN as operators; P with K forms).**
- **Scope.** Items 1–12, 22 and the primitives of 26, under R1 and R2. For items 3 and 11 it holds in
  the measurable setting.
- **Statement.** Every outcome event is a set of configurations reached by the native dynamics,
  measurable in the measurable setting. Under KIN, every effect lies in 𝒜.
- **Proof.**
  - Each definition makes the outcome a function of a configuration reached by a bijection, a
    permutation instrument or a configuration-projector readout.
  - Composition, feedforward, stopping, coarse-graining and discard preserve this property.
  - Preimages of measurable maps are measurable. ∎
- **Grade.** The result is close to definitional.

**Proposition RA-1′ (instruments; (I) KIN; X from K).**
- **DIO.** For items 2, 3 (non-selective), 5–10, and 26 with a monomial U, the full branch maps are
  DIO. In each, the Kraus operators that the corpus fixes are monomial, row-monomial, diagonal, or
  scalar on configuration blocks.
- **Open for O1-D.** Items 1, 4, 11, 12 and 22 are established at the effect level only. Items 11
  and 12 have no update rule. Items 1, 4 and 22 have the `Main:664` update for the diagonal sector
  only, and DIO concerns coherent inputs. So RA-1 does not decide whether they are DIO.

**Proposition RA-2 (narrowed; K, X).**
- **Statement.** Wherever a corpus structure defines an instrument, through branch maps, whose
  effect lies outside 𝒜, the readout primitive is a configuration projector (items 6, 7). The outside
  effect arises as U†PU after an imported isometric step (items 14, 15, 26), or from supplied data on
  a represented space (item 18).
- **Scope.** The declared full observable algebra (items 24, 25) is outside 𝒜 without import, but it
  is not an instrument. The corpus defines no procedure that reads its non-diagonal elements.
  RA-2 does not cover it.
- No formal map between these structures is claimed.

### 3.1 A sufficient additional premise for classifying each open instrument or site

Each premise is named, not adopted. Each is **sufficient in one direction only**: the stated
classification follows from it by the cited algebra. No minimality is claimed, and the premise's
failure is not shown to give the opposite classification.

| Item | Open question | Sufficient additional premise | What it would give |
|---|---|---|---|
| 1 (observation, `Main:42`) | the state update | **UPD-C**: the observation's update is the substratum bijection followed by conditioning on the observed visible configuration, i.e. Kraus operators P_x U_φ with configuration projectors P_x, **on coherent inputs as well**. `Main:664` gives this form "for the represented diagonal sector" only, and assigns the extension "to arbitrary coherent density matrices" to the operational bridge, an import. UPD-C's clause on coherent inputs is therefore a premise that `Main:664` declines to supply, not one it supports | DIO (X): permutation and diagonal-projector Kraus operators |
| 4 (Bell outcome, `Main:376`) | the update of the readout region | **UPD-C** applied to the readout region R_A | DIO (X) |
| 11 (EP-schema record law) | the represented update of a model's maps | **REP-EP**: each deterministic map of the schema (ι, Φ, R) is represented by the channel with single-entry Kraus operators \|f(λ)⟩⟨λ\| on ℓ²(Ω) | DIO (X), whether or not the map is injective |
| 12 (A★2 records) | the represented update of the recording coupling | **REP-K**: the coupling on Reg × K is represented by its permutation lift, with K classical | DIO (X) |
| 22 (book mirror) | as item 1 | **UPD-C** | DIO (X) |
| 24 (`Str:742`, `Str:788`) | the operational meaning of 𝒜_V = B(ℓ²(C_V)) | To make it a source of non-DIO: **IMPL-R5**, an implementable native instrument realizing one non-diagonal effect, for example the projector onto (\|x⟩ + \|y⟩)/√2. To make it compatible with R-READ: **ACC-R5**, the operationally accessible algebra is ℓ^∞(C_V), with B(ℓ²(C_V)) kept as the mathematical algebra of the pair. `Str:788`'s smaller-algebra clause admits this (X) | IMPL-R5: a native coherence detector, so O1-D is met and R-READ fails. ACC-R5: R-READ holds at the accessible level |
| 25 (`Main:722`, `GR:366`, book mirrors) | as item 24, and also the referent | **REF**: fix whether the sentence refers to bare OI or to the OI_Q completion (`GR:286`). Then IMPL-R5 or ACC-R5 as for item 24 | under REF = OI_Q, the site is item 16 (outside 𝒜 via import). Under REF = bare OI, as item 24 |

**Open items.** Six items are Open: 13, 17, 19, 20, 21, and 14 without control. Under R5b, items 16,
23, 24 and 25 are Open as well.

## 4. Pressure test (§A.31)

1. **Visible configurations as superpositions.** `Main:42` and `Main:54` give finitely many
   distinguishable states and a bijection. No superposition is defined. This settles R1. It does
   not settle R5.
2. **Two-slice readouts.** These are functions on the pair carrier on which the update acts
   (`GR:290`).
3. **Hidden-sector readouts.** None is defined (`Main:48`).
4. **Continuous and coarse-grained readouts.** Their level sets are measurable.
5. **Singular dynamics and non-normal states.** These do not reach the effect statement for
   classical laws. For coherent hidden states they need OPRES D's lift (§1).
6. **Hidden non-monomial steps.** Composite procedures that contain one are treated separately as
   RA-2, not excluded silently.
7. **Effects versus instruments.** Diagonal effects do not give a DIO update. RA-1′ restricts the
   instrument-level claim to the items with defined Kraus operators.
8. **Declared observables.** The full-algebra declarations are recorded as R5, not explained away.
   If R5a governs, R-READ fails without import, although no procedure is yet given that realizes it.

## 5. Search record

- **Terms.** readout, read-out, record, instrument, observation, observable, observable algebra, full
  matrix algebra, outcome, measurement, pointer, detector, effect, Lüders. In Lean, definitions whose
  names contain Readout, Record, Instrument, Observ, Passive, Outcome, Luders or stopped.
- **Sources.**
  - `papers/*.md`, all twelve;
  - `book/The-Incompleteness-of-Observation-FULL.md`, `book/glossary.md` and `book/ch*.md`;
  - `verification/lean-mathlib/OIBridge/*.lean`, 245 files, by definition grep;
  - `verification/programmes/oi-qm/**`.
- **Read in context.**
  - `Structure.md` §9.1 (`Str:620–641`), §10.4 (`Str:786–792`) and `Str:742`;
  - the cited lines of Main, GR and Substratum;
  - the reviewed records named in §2;
  - QOPS-P2 (#1501 at `cd3672fa`) and GATE-A r5 (#1503 at `fd3cb064`).
- **Identified but not read line by line.** `measurement-record-formation`,
  `observer-access-20261106`, `apparatus-1-20261107`, `record-control-20261107` and
  `meas-q-20261120`.
- **The inventory is a finite search.** It is evidence about what was found.

## 6. Classification

| Item | Label | Layer | Class (§A.31) |
|---|---|---|---|
| RA-1 | (N) as configuration functions; (I) KIN as operators; measurable setting | P, K forms | CONFIRMING for R1 and R2, at the effect level |
| RA-1′ | (I) KIN | X from K | ELABORATING: instrument-level DIO for the items with defined Kraus operators |
| RA-2 | (I): the import named in each structure | K, X | POSITIVE, within instruments |
| R5 items 24, 25 | — | P | NEW relative to r1: a corpus declaration that contradicts R-READ under R5a, with no import |
| Open items | — | P | open |

**Bearing on OPRES.**
- OPRES §5's verdict holds for the defined native readouts at the effect level (RA-1). At the
  instrument level it holds for items 2, 3, 5–10 and 26 (RA-1′). It is open for items 1, 4, 11, 12
  and 22.
- It does not hold as stated if R5a governs. In that case the corpus declares non-diagonal
  observables for bare OI, and OPRES U2 shifts as described in owner question 3.

## 7. For owner decision (nothing adopted)

1. **Interface-datum readouts (items 13, 19).** The owner recommendation (c.7066723717) is to classify
   them separately, not to count them as native observations automatically, and not to modify
   `Main:42`. This record follows it. They stay Open.
2. **Measurability.** It is recorded in §1 as a hypothesis of the measurable setting, at its exact
   corpus scope: the `Main:336` corollary, and EP-schema models under `EP:100`. It is not a new
   clause of R-READ.
3. **Is OI's declared observable algebra the full B(ℓ²(C_V)) or the configuration algebra
   ℓ^∞(C_V)?** The alternative is that it contains only native-readout effects (`Str:742`, `:788`;
   `Main:722`; `GR:366`).
   - **Full algebra, with its elements readable (R5a).**
     - R-READ fails without import.
     - O1-D could be met by a native readout of a non-diagonal observable, once a procedure
       realizing that readout is defined. The corpus defines none.
     - OPRES §5's conditional verdict does not hold as stated. U2 becomes "a detector is declared and
       a coherence source is still needed" (OPRES §8). With a sharp, destructive readout in a basis
       unbiased with respect to the configurations, and a fixed |+⟩, CC-1 gives an exact H.
   - **Full algebra as a declaration only (R5b).**
     - R-READ stands for defined procedures at the levels of RA-1 and RA-1′.
     - O1-D needs a non-monomial step, or a readout the corpus does not define.
     - Items 24 and 25 then state representational data, not readable observables.
   - **Configuration algebra.**
     - R-READ holds for the declared algebra as well. `Str:788`'s smaller-algebra clause admits it
       (X).
     - The statements at `Str:742`, `Str:788`, `Main:722` and `GR:366` would then be inconsistent
       with the declared algebra. That is a manuscript matter outside this record.

## 8. What this note does not do

It edits no manuscript, reviewed record or Issue body other than its own. It runs no computation and
dispatches no workflow. It adopts no premise and posts nothing on #1169. It makes no broader
quantum-operational claim.
