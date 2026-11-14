# EOI audit phase 2, cluster C1: the OI↔QM equivalence core (A1 quantum import, A5 matching level) — r3

**Revision.** r2 answered `REVIEW-C1.md` (verdict REVISE: B1–B6, N1–N9). r3 applies the four non-blocking items of `REVIEW-C1-r2.md` (ACCEPT WITH CHANGES); r2 is preserved as `AUDIT-C1-r2.md` (sha256 `230be89b…f0a8a`).
- r1 is preserved as `AUDIT-C1-r1.md` (sha256 `09bdac1c…0ab10`).
- The disposition table is at the end of this file.

**Scope and method.**
- Everything was read at `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`, using `git show` and `git grep`.
- The work was read-only and paper-only: no builds, no computations, and no repository writes. Line numbers refer to that commit.

**Abbreviations.**
- Papers: `papers/Main.md` (Main), `papers/GR.md` (GR), `papers/Substratum.md` (Sub), `papers/SM.md` (SM), `papers/Introduction.md` (Intro).
- Book: `book/The-Incompleteness-of-Observation-FULL.md` (FULL).
- Programme map: `verification/programmes/oi-qm/PROGRAMME.md` (PROG).
- Reconstruction records: `verification/programmes/oi-qm/reconstruction/` (RECON).
- Lean modules are under `verification/lean-mathlib/OIBridge/`.

**Outcome codes.** These apply to results.
- 1 = valid as stated.
- 2 = valid but conditional, with each import named together with the step that consumes it.
- 3 = requires new investigation.

**Class codes.** native, conditional, imported, and n/a (pure mathematics).

**Texts read too strongly** are listed separately from outcomes. No replacement wording is drafted.

**Two marked kinds of point.**
- **[audit derivation]**: my own paper or exact-algebra argument, not a corpus result.
- **[named question]**: a question with its cheapest check. Its outcome is not adopted (brief: "may name, may not adopt").

**Evidence layers are stated explicitly.** They are: kernel; exact-arithmetic probe; paper proof; source reading.

***

## 0. What the core objects actually are (shared by every claim below)

### `Q_fb` is a function of a Markov chain whose kernel is unistochastic

**The definition** (`Equivalence.lean:190-217`). `QfbReal` has four parts:
- a finite basis `Bas`;
- a matrix `U`;
- a real initial weight `init : Bas → ℝ`;
- a readout `read : Bas → V`.

`IsLaw` (`:201-202`) requires `U` to be unitary and `init` to be a probability vector. The dynamics enter only through the Born weight `born b b' = ‖U b' b‖²` (`:205`). This kernel is unistochastic, because Uᵀ is unitary. The law is `chain σ = init(σ0)·∏ born(σk, σk+1)` (`:209-210`), pushed forward through `read` (`:213-214`).

So `Q_fb` is a deterministic function of a time-homogeneous Markov chain on `Bas` with kernel |U|². It carries no state, no coherence and no update.
- "Measured projectively at every step" is the docstring's gloss on this product form (`:207-208`).
- In `D_imp_Qfb` the basis is `V × Hid` (`:297-299`).
- Main:16 and Main:552 ("initial state diagonal in it … the visible record a fixed function of each outcome") agree.

**Law-class identity.** The `D ⇒ Q_fb` witness is a permutation matrix, so its Born weights are indicators and the exponent plays no role (Main:556; `equivalence_recovery_probes.py`, check 6).
- Hence the laws of `Q_fb` data with permutation `U` form the same **law class** as `D`. This is an identity of law classes, via S. It is not a structural identity: `Bas` need not be `V × Hid`, and `read` is arbitrary.
- At the law-class level, the `Q_fb` leg adds nothing to `S⟺D` beyond D ⊆ Q_fb ⊆ S. This is CONFIRMING: the corpus says the same at Main:20 and Main:556.

**Downstream uses of the specific witness.** The corpus also uses the specific witness `U_φ`, with Ĥ = i log U_φ:
- Main:532-534, Main:554;
- GR:228 (the determination of ħ "uses only the fixed-basis representation");
- GR:134.

Those uses are likewise the Koopman representation of a classical bijection. They are examined under MQ-03 and TB-BA. The "adds nothing" statement above is a law-class statement and does not cover them unexamined.

**POSITIVE [audit derivation]: the full-basis access is not material to the class equality.** Let `Q_vis` be the variant that measures only the visible fibre projectors, by Lüders on `read⁻¹(v)`.
- `Q_vis ⊆ S`, because any finite quantum record is a stochastic law.
- `S ⊆ Q_vis`, via `S ⇒ D` with a permutation `U` and a diagonal initial state. Visible Lüders projection and permutation conjugation preserve diagonality.

So `Q_vis = S`, and the class identity does not rest on the quantum-side observer reading hidden coordinates.

### The kernel's `S ⇒ D` carrier pre-stores the whole visible trajectory

**The kernel construction.** The carrier is `Hid = Fin (K+1) × Traj V K` (`Equivalence.lean:364-365`). The initial law is `marg P ι` with `ι τ = (τ 0, (0, τ))` (`:426-428`, `:361`). The hidden state at time 0 is therefore the entire visible record, correlated with the root.

**What class (D) asks for.** The `RevReal` docstring (`:150-156`) says the class (D) initial law "is not required to factor". It says the stronger independent-prior form "is the manuscript's separate finite-horizon process-dilation theorem … and it is NOT what this theorem's class (D) asks for".

**Where the root-independent prior is proved, by layer.**
- **Multi-time joint law: paper proof only.**
  - The response-table construction, Main:520.
  - Main:522: "the independence of μ_H from the visible initial state rests on the construction above and the cited probes and is not formalized".
  - Egri et al. Prop. 16, an external input (Main:554).
  - I re-read the argument at Main:520 and find it sound at the paper layer.
- **First-order rooted family: kernel.** `pper_has_responseRealization` gives one finite realization whose single prior is shared by every root (Main:640; `track-i/arc-b-rooted-classification/result.md:50-56`). The qualifier is zero-prior padding (result.md:86-91).

### The two matching levels

**Multi-time, one protocol.**
- `S⟺D⟺Q_fb` concerns full finite-horizon trajectory laws (`Traj V K`).
- Each law is realized separately; the carrier and φ depend on the target and on K (Main:522).

**First-order rooted (M2).** The following are two-time families `Γ_t(a,j)` or `T_ij(t)`, with one unitary per time and conditioning time `T₀ = {0}`:
- the Definition (i) at Main:526;
- the Barandes tuple;
- Arc B (`C_OI = PPer`);
- Arc C (`Q*`);
- the Track B lifts.

At this level "higher-order trajectory probabilities are not fixed" (`track-b/boundary-audit/result.md:22-25`).

**Neither level reaches system-level QM** (one quantum system with all of its protocols).
- A `D` realization's visible law does not depend on passive reading. One `Q_fb` system has different laws for "measure every step" and "measure only at the end".
- So one `D` realization reproduces one protocol, unless the protocol choice is a visible intervention label. That case is the gluing theorem (Main:566), which holds for finite menus to accuracy ε.
- The corpus says this at Main:556, 558 and 560. This is CONFIRMING.

***

## MQ-01: S ⟺ D ⟺ Q_fb at the finite observable-law level

**Statement.**
- Main:16-20 (abstract).
- The theorem at Main:548-552.
- Main:602: "(1) S⟺D⟺Q_fb — proved, all finite laws".

Mirrors: Sub:14, 22; GR:20, 709; FULL:64, 274-278, 345-349, 496, 514, 528, 820, 6644.

**Where proved (kernel).** `finite_horizon_equivalence` (`Equivalence.lean:462-468`) assembles three directions. None of them appears as a hypothesis (`:458-461`).
- `S_imp_D` (`:422`).
- `D_imp_Qfb` (`:294`), via `permMatrix_mem_unitaryGroup`.
- `Qfb_imp_S` (`:245`). Normalization of the Born rows is unitarity, `sum_born` (`:227-239`).

**Hypotheses, and where each enters.**
- Unitarity and the Born weight |U|² are part of `Q_fb`'s definition (`:201-205`).
  - They are used in `Qfb_imp_S`.
  - They are used in `D_imp_Qfb`, through permutation unitarity.
- The product-chain law (`:209-210`) is part of the definition.
- The hidden–visible correlated initial law enters `S_imp_D` (`:361`, `:426`).
- A finite horizon K, with the realization chosen per law.

**Outcome: 1.**

**Class.**
- The S⟺D direction is n/a (pure mathematics).
- The Q_fb leg is imported, as a comparison target. The owner's principle 1 permits this.
- No QM structure is derived. The representation exists for every finite stochastic law, OI-sourced or not.

**Texts read too strongly.**
- **Main:776** says "*equivalence of quantum mechanics and embedded observation* has a precise theorem-level meaning". The quantum side of the theorem is `Q_fb`, the object of §0.
- **FULL:266** says "Quantum mechanics is therefore an exact observer-level representation of the incomplete finite law".
- **FULL:64** (= `book/preface.md:3`) says "quantum mechanics is … the exact observer-level representation".
- **`verification/ROADMAP.md:48-52`** says "quantum structure is emergent from the observational architecture". This file is frozen, so a correction would go in a mutable record (§A.42 item 6).

What the proof supports in each case is the existence of a fixed-basis unitary/Born representation for every finite law.

***

## MQ-02: "QM emerges" (Main:68, title, §3 heading, book Preface)

**Statement.**
- Main:68: "These properties contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below."
- The subtitle "Quantum Reconstruction" (Main:2).
- The heading at Main:206.
- Main:682.
- FULL:244 and FULL:334.

**Two readings, each already decided by the corpus.**
- **Representation reading.** This is valid unconditionally, and C1–C4 are idle.
  - Main:72: "the equivalence of §3.4 quantifies over none of them".
  - Main:82(2): "C4 is not needed for the existence of a quantum representation".
  - The support is MQ-01, outcome 1. "Under the conditions below" adds nothing to this reading.
- **Operational reading: "operational QM emerges under C1–C4".**
  - **Refuted** at the operational-theory interface by the kernel counterexample `oi_alone_not_qm` (`GeneralCarrier.lean:160-163`). The witness is `diagTheory`, which realizes the sealed C1–C4 core and is not exactly quantum.
  - It appears boxed at GR:220-222: "a theory that never creates coherence realizes the OI core and is not quantum … bare finite OI ⇏ QM".
  - **Scope of the refutation.** It is stated on the `Fin 2` carrier, for one sealed C1–C4 core (`RealizesSealedOICore`, `OIRealization.lean:234-242`), at the `FiniteOperationalTheory` interface. Within that scope the reading is refuted, not open.
  - **The refutation runs in one direction only.** `oi_alone_not_qm` shows that C1–C4 do not entail QM. Every theory with full control also realizes the core (`realizesSealedOICore_of_control`, `OIRealization.lean:252-258`), so C1–C4 do not exclude QM either. C1–C4 neither entail nor exclude QM at this interface.
  - AGENTS.md ("a valid counterexample or disproof requires correction or withdrawal of the refuted claim") applies to the wording that carries this reading.

**Outcome.**
- The representation reading is 1.
- The operational reading is **refuted** by an existing kernel witness. This is a refuted text, not outcome 3.

**Class: imported.** Every route to quantum structure beyond Q_fb supplies the following as hypotheses:
- complex kinematics (GR:216);
- complex control or a complex drive (MQ-11 to MQ-13).

**Texts read too strongly, or carrying the refuted reading.**
- Main:68, Main:206, Main:682.
- FULL:244 and FULL:334.
- SM:1100: "where quantum mechanics is itself emergent".
- Sub:459.
- Main:684 (A5): "The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix". The corpus gives one `D` realization per configuration. A common realization exists only through the ε-gluing theorem, whose hidden register stores the digitized density matrix (Main:566).

**Internal tension.** FULL:684 ("Chapter 1 took a substratum … as input and developed the emergent quantum description from it") sits against FULL:690 (= `book/ch02-substratum.md:56`). The latter says "(E1) Unitary quantum mechanics … This is Chapter 1's framework input". The second can be read as naming the datum Chapter 1 accounts for; as written, it calls QM an input.

**F-1 [named question]: extended mechanisms, outside the class already ruled out.**

*Question.* Does some OI mechanism outside the classes covered by `oi_alone_not_qm` and `substratumGen_not_control` generate an operational theory with the five completion conditions? Those classes are:
- the sealed core;
- the generated theory of the monomial class on the two-state carrier (`StructuralClosure.lean:348-349`; GR:228, "on the two-state carrier").

Alternatively, does a no-go hold for a stated wider class?

*Merged records already pursuing it* (owner's symmetry rule). None of them adopts a premise.
- RECON `quarter-phase-native-20261107/` (Q-A: "a native source for the 8-point quarter-phase mechanism"), with `DESIGN.md` and `PROOF-RECOVERY.md`.
- RECON `mechanism-2-20261108/DESIGN.md` (MECH-2: the state-dependent coupling graph `G(x)` at q = 2, its encoded operations and their classical model).
- RECON `oi-qm-ext-1/two-mode-drive.md`. It gives a conditional continuous unitary family, under the added real-mode and controller resources. Its §1 states that "Neither statement derives the required physical real-mode/control/access resources from the finite substratum".
- PROG:40, on F2: "assuming the resource as a premise states it without sourcing it".

*Cheapest check.* Per candidate mechanism, check the analogue of `diagGen_not_control` / `substratumGen_not_control` on its generated theory. That is: does every available conjugation preserve a property that the target unitary breaks? I propose no new check beyond those the cited records already set.

***

## MQ-03: the Definition label, and "establishes Hilbert space, unitary dynamics, Born"

**Statement.**
- Main:526: the Definition "*mathematically equivalent to unitarily evolving quantum mechanics*". It asks for a unitary U(t) per time on dimension ≤ n³ with a fixed ρ_anc, "with no composition law or fixed generator required".
- Main:530: "This definition captures the Hilbert space, unitary dynamics, and the Born rule."
- Main:648: "The characterization theorem establishes the Hilbert space, unitary dynamics, and Born-rule transition probabilities."

**Where proved.**
- **One-step ancilla lemma** (Main:212-216; paper proof plus `tdilate_probes.py`, exact). It gives the Definition's form, on dimension n², for every stochastic T(t), at each t separately.
- **Condition (i).** It is "Imported ([11, 12])" (Main:732). (i) does not imply (ii) (Main:634).
- **Fixed-Ĥ lemma** (Main:532-534; paper proof plus `review4_probes.py` P-F, exact). It gives `U_φ`, the Koopman permutation unitary of a realization.

**Hypotheses.**
- The Definition *is* the Born-and-unitary form, with an ancilla in a fixed ρ_anc.
- The one-step lemma uses a pure a₀ (an A4 idealization at the representation level).
- The data are first-order two-time data (M2).

**Outcome: 1.**

**Class.**
- The label is imported: QM form by stipulation, satisfied universally.
- The fixed-Ĥ lemma is n/a: it is the Koopman representation of a classical bijection.

**Texts read too strongly.**
- **Main:526**, the label itself. The property it names is universal.
- **Main:530 and Main:648**, "establishes … unitary dynamics, and Born-rule transition probabilities". Under (i) there is one unitary per time and no dynamics. Under (Q2) the dynamics is the permutation of the classical bijection. The Born exponent is not selected (Main:556).
- **Main:656**, "it is a theorem that the mathematical structures are identical". The theorem gives a many-to-one embedding; Main:218(i) itself says the correspondence "does not single out a unique quantum system".
- **FULL:6207**, "structurally equivalent to a unitary quantum dynamics on a Hilbert space via Stinespring dilation".

***

## MQ-11: the five-condition operational characterization

**Statement.**
- Main:564: "On any nonempty finite carrier, the operational theories whose available families … are exactly the normalized finite Kraus instruments are precisely those satisfying (i)–(v) … so that what the OI architecture must supply is named condition by condition."
- GR:218-228, with boxes at GR:222 and GR:226.

**Where proved (kernel).**
- `exactAll_iff_physical_general` and `general_characterization` (`GeneralCarrier.lean:100-111`).
- `main_result` (`:188`).
- `oi_compatible_classification` (`:168-173`), on `Fin 2` only.
- `oi_alone_not_qm` (`:160`).

**Hypotheses, and where each enters (both directions).**

The setting `FiniteOperationalTheory` (`OperationalAssembly.lean:594-640`) supplies:
- **Complex matrix kinematics**: operations are ℂ-linear maps on `Matrix A A ℂ` and on `Matrix (A×Fin n) (A×Fin n) ℂ`. This is the A1 import, and it is disclosed at GR:216 and Main:564.
- **`prepAvail_uniform`**: a uniformly mixed ancilla of any size.
- **A native readout**, forced into Lüders form by `readout_is_localLuders`.
- **Partial-trace discard**, rule (f).

The fresh uniform ancilla of any size and the free discard are A3/A4 observer-capability idealizations. They are not quantum content as such:
- The kernel's `diagTheory` meets the setting rules and is not QM (GR:220; `GeneralCarrier.lean:157-163`).
- (The corpus phrase "carries no quantum content", Main:590 and GR:276-280, is said of the *typed* interface. It is not cited here for the endomorphic setting, which rests on `diagTheory` alone.)

Condition (iv), `HasCompositeUnitaryControl`, supplies every unitary at every level.

The OI clause is idle. `realizesSealedOICore_of_control` (`OIRealization.lean:252-258`) proves that control implies the OI core.

**Outcome.**
- The kernel theorem is **1**. It states "with the complex matrix kinematics … taken as given", and GR:228 says "a classification … not a derivation".
- The reading "what the OI architecture must supply is named condition by condition" is **2**. OI would also have to supply:
  - the complex kinematics, which is named as open;
  - the A3/A4 setting capabilities: uniform ancillas of every size (rule (d)), partial-trace discard (rule (f)), and a spectator-independent readout at every level (rule (e)). These are not named as items to be supplied.

**Class: imported**, through complex kinematics and condition (iv).

**Texts read too strongly.**
- **Main:564**, as above.
- **GR:226 with GR:228.** The box "OI-compatible … ⟺ finite operational QM" is stated "for every nonempty finite system". Its OI-compatibility qualifier has kernel content only on `Fin 2`. On general carriers, the cited `main_result` (i) has no OI clause (cf. GR:244).

***

## MQ-12: OI⁺ ⟺ exact finite endomorphic operational QM, and `oiPlusMin_iff_qm` one direction at a time

**Statement.**
- Main:586-590.
- GR:230-244, box at GR:240.
- The primitive-source box at GR:256.
- The typed form at GR:276-280.

**Where proved (kernel).**
- `carrier_general_oiPlus`, with `qm_of_oiPlus` and `oiPlus_of_qm`.
- `oiPlus_independence`.
- `carrier_general_oiPlusMin` (`MinimalRepertoire.lean:578-582`).
- `oiPlusMin_iff_qm` (`MinimalRepertoire.lean:569`).

**`oiPlusMin_iff_qm`, checked one direction at a time (§A.34; the review's N9 confirmed this check).**
- **Forward, `qm_of_oiPlusMin` (`MinimalRepertoire.lean:552-560`).** It consumes three hypotheses.
  - `ImplementationLocality` (`ImplementationLocality.lean:370-372`). Availability is `InstAvail` (`ImplementationLocality.lean:260-292`): conjugation by an admissible isometry; Lüders readout by admissible projectors; coarse-graining; feed-forward; discard of a uniformly attached ancilla.
  - `PhaseFreeRichness` (`MinimalRepertoire.lean:423-428`). One pair is driven by `conjChannel (flow (transition a b) t)`, with `flow H t = exp(−itH)` (`ReachabilitySeam.lean:95-96`) and `transition = E_ab + E_ba` (`LieRankSource.lean:199`). Every exchange is also available.
  - `EmbeddedObservation` (`EmbeddedObservation.lean:123-124`).
  - The flow is consumed by `control_of_phaseFree` (defined at `MinimalRepertoire.lean:529`; invoked at `:559`, inside `qm_of_oiPlusMin`, `:552-560`).
- **Reverse, `oiPlusMin_of_qm` (`:562-567`).** It is immediate from full control.
- **Neither direction uses an OI object.**

`RECON oi-qm-ext-1/two-mode-drive.md:11` cites the result "within their given complex operational interface", and is correctly scoped.

**Outcome.**
- The kernel statements are 1.
- **The statements as made (GR:250, GR:256, Main:590) are 2.** Two imports must be named, each with its consuming step:
  - (a) complex matrix kinematics, in the setting;
  - (b) the drive generator `−i(E_ab+E_ba)`. This is a complex flow, consumed by `control_of_phaseFree` through `flow (transition a b) t`.

  The prose of the principle ("phase-free richness … no phase operation enters") does not state (b).

**ELABORATING (not NEW; credit to the corpus).** The corpus already locates the imaginary direction in the drive.
- GR:250: "two drives sharing a state bracket to the imaginary transition on the third pair". Also "the quarter phase supplying the imaginary partner of a transition directly", for the elementary form.
- GR:258: on even carriers, one drive and one full cycle generate "a conjugate of the real antisymmetric matrices".
- `MinimalRepertoire.lean:13-25`: `bracket_XX` supplies "the imaginary transition … which the quarter phase used to supply". `colourAlg` records that "the colour phase Λ = diag(i,1) carries every such drive into the real antisymmetric matrices".
- `LieRankSource.lean:36-43`: the control Lie algebra contains `−iX_pq` and `−iY_pq`.
- Intro:129: the reason operations are complex matrices at all is open.
- RECON `oi-qm-ext-1/two-mode-drive.md:54`: "Multiplication by i is exactly the zero-coupling quarter-turn J", with a phase-reference obligation at `:145-147`.

**The narrower residual point.** "No phase operation enters" holds for the primitive list, but not for what the primitives generate. On a carrier with D ≥ 3, take a pair (a, b):
- `flow(X_ab, π/2) · swap_ab = diag(−i, −i, 1, …)` [audit derivation, exact algebra; confirmed by the reviewer's sympy check]. This is a relative quarter phase between the pair and the remaining states.
- The real-rotation flow `exp(t(E_ab − E_ba))` = `flow (transitionY a b) t` (`LieRankSource.lean:201-203`) has the same single-pair Born matrix `[[cos², sin²], [sin², cos²]]`. Its quarter-period composite with the swap is `diag(1, −1, 1, …)`.
- On D = 2 the complex composite is the global phase `−i·I`, which is consistent with `not_hControl_two`.

The prose of the principle does not state that the phase relation between the drive and the exchange basis is load-bearing.

**Class: imported.**

**Texts read too strongly.**
- The principle names "observational independence", "observer recursion" and "embedded observation" (GR:232-236, GR:252; Main:590). They name closure properties of families of complex-matrix theories, not properties of OI's (S, φ, V). This is mild.
- **GR:242, "the physically rephrased form of completed OI": downgraded and not pressed.** The same passage (GR:244) discloses that the core conjunct is redundant (`completedOI_iff_physical`), and `oiPlus_iff_completedOI` is a valid kernel equivalence.

***

## MQ-13: "substratum + controllability ⟺ QM"

**Statement.**
- GR:262 (box): "current OI substratum + continuous off-diagonal controllability ⟺ exact finite endomorphic operational QM".
- GR:264: "quantum mechanics is obtained exactly when that one physical resource is added".
- Main:590 mirrors it.

**Where proved (kernel).**
- Forward: `substratum_plus_control_qm` (`StructuralClosure.lean:414-418`).
- Reverse: `qm_generated_by_substratum_extension` (`:423-430`).
- Closure of the substratum class: `substratumClass_structurallyClosed` (`:316`).
- The residual: `substratum_residual` (`:383-392`), which shows the substratum class is a classical (monomial), structurally closed class with no control.

**Hypotheses, one direction at a time.**
- **Forward.**
  - **The binder `(_ : ExtendsSubstratum 𝓘)` is anonymous and unused.** This is confirmed by the review. `git grep` shows `ExtendsSubstratum` is defined at `:401`, bound at `:409` and `:415`, produced at `:419` and `:425`, and consumed nowhere.
  - The proof is `genTheory_qm_of_quantumArchitecture ⟨hc.arch, hc.context, hc.label, hc.dagger, hd⟩` (`:417`).
  - It consumes `hc : StructurallyClosed 𝓘`, the closure of the extended class, and `hd : DrivesElementary 𝓘` (`SubstratumSource.lean:77-82`). `hd` is every flow, every swap, and `phaseGate` on every state.
- **Reverse.** The witness is `fullClass` (`:427-430`).
- **The substratum class.** It is `IsMonomial`, with arbitrary complex `d` (`SubstratumInterface.lean:75-83`). The phases are stipulated, and GR:260 says so.
- **The generic nature of the four closures is a kernel result, not mine.** `diagClass_arch`, `diagClass_contextStable`, `diagClass_labelInvariant` and `diagClass_daggerStable` (`LieRankSource.lean:87-119`), together with `diagGen_not_control` (`:146`), show this. `SubstratumSource.lean:37-46` states: "a substratum could supply a fully stable implementation architecture and still fail to be quantum". r1's "[audit derivation]" label for this point is withdrawn.

**Outcome.**
- The kernel statements are 1.
- **The statements as made (the GR:262 box, GR:264, Main:590) are 2.** Two imports or steps must be named:
  - **(a) An unformalized step.** Swaps and quarter phases are monomial, so `ExtendsSubstratum` would put them in `𝓘`, and flows alone would then complete `DrivesElementary`. The kernel theorem neither states nor uses this step. It assumes the full `DrivesElementary` in `hd`, consumed at `:417`.
  - **(b) The closure hypothesis `hc` on the extension.** It is disclosed at GR:260 ("a structurally closed extension … is a quantum architecture exactly when it drives …"), but it is missing from the GR:262 box, from GR:264 and from Main:590.

**What is not an over-reading (review B3).** "Supplies every structural requirement … but not continuous state-mixing controllability" (GR:264) states a necessary condition, and GR:264 denies sufficiency. The closure assumption is disclosed at GR:260.

**Class: imported.** The imports are complex kinematics, stipulated complex phases, and the complex drive.

**Texts read too strongly.**
- The GR:262 box, GR:264 ("obtained exactly when that one physical resource is added") and Main:590, for (a) and (b).
- PROG:80, "supplies the structural closure properties needed". This is accurate as a necessary condition; it is noted only for the same missing (a) and (b).

***

## MQ-27: GR:40, "The universality of the observed quantum mechanics follows from all sub-c observers sharing the same causal structure."

**Support.**
- The only proved support is MQ-01 (outcome 1), and that representation is universal for every finite law whatever the causal structure.
- The scoped form is GR:565, conditional on (C4) at the cosmological cut.
- The operational reading falls under the refutation recorded at MQ-02, in its scope.

**Classification.** This is a text that reads MQ-01 too strongly. It is not a separate result awaiting investigation. The text is GR:40.

**Class: imported.** "The observed quantum mechanics" is E1.

***

## MQ-28: Sub:389, "Both are emergent. … Both are derived rather than fundamental."

**Support.** The quantum side rests on MQ-01 alone (outcome 1). The surrounding text is scoped:
- Sub:26 and Sub:371 say "the reduced description admitting the quantum representation".
- Sub:554 conditions the synthesis on "G3 and the operational completion".

**Classification.** This is a text that reads MQ-01 too strongly. The texts are:
- Sub:389, "derived rather than fundamental";
- Sub:459;
- GR:346, "QM is emergent".

**Class: imported.**

***

## MQ-29: Sub:126, Stage-1 output, "The observed quantum dynamics is the reduced description obtained by tracing out S∖V from the deterministic evolution under φ."

**Where proved.**
- Sub:137 applies Main's `S ⇒ D` "for each finite experimental context".
- Sub:141 gives the status: "Theorem for the scoped finite dilation datum".

**Hypotheses.**
- E1 (Sub:76) as the comparison input, which the owner permits.
- M1-T.
- A hidden prior independent of the visible initial state, for the multi-time law (Sub:137). This is paper-only (Main:520-522, §0); the kernel `S_imp_D` correlates the prior with the root.
- A per-context realization (Main:522).
- Coverage of several contexts in one realization, only per finite menu to ε (Main:566, 598). In that construction φ_a is built from the quantum instruments, and the hidden sector holds "the unnormalized digitized branch matrix (a density register)" (Main:566).

**Outcome: 2.**

**Class, by part.**
- Per context: conditional, on paper-level prior independence and M1-T.
- Per menu: imported, through the density register.

**Texts read too strongly.**
- Sub:126: "the observed quantum dynamics", singular and unqualified.
- Sub:137: "record persistence is required for the non-Markovian returns that produce quantum interference".

***

## MQ-32: FULL:6409, "The framework reproduces Bohmian's … statistical-predictions content without the pilot wave's structural cost."

**Support.**
- MQ-01, per law.
- The ε-gluing theorem (Main:566) and the uniform continuum theorem (Main:598). In both, the realization runs genuine quantum instruments in a hidden density register: "every R-protocol runs genuine quantum instruments (net members)" (Main:598(ii)).
- Bell agreement holds only conditionally on H-Bell.
- No fixed finite carrier reproduces a qubit's full theory (Main:560).

**Outcome: 2.**

**Class: imported.**

**Texts read too strongly.**
- FULL:6409.
- FULL:4920: "exact in its predictions for any embedded observer's empirical access". This is against Main:560 and the ε scope.
- FULL:6417: "the structural foundation of why these epistemic descriptions take the specific form they do".

***

## MQ-42: SM:22, "The present paper consumes only the emergent quantum description and its Born-rule statistics."

**What Main supplies.**
- Q_fb (MQ-01).
- The per-time ancilla form (MQ-03).
- Operational QM, only conditionally (MQ-11).

**What SM uses beyond that.**
- A staggered Dirac operator (SM:286).
- Induced gauge dynamics from the fermion determinant (SM:699).
- RG running (SM:428), and "the unitary QFT that an embedded observer reports after the trace-out of [Main]".

**Outcome: 2.** SM is conditional on an imported QM/QFT layer that SM:22 does not name as such.

**Class: imported.**

**Texts read too strongly.**
- SM:22 ("only").
- SM:428.
- SM:1100.

SM:509 is carefully scoped.

***

## PROG: PROGRAMME.md, the F1 reading insofar as it concerns positive equivalence

**Statement.**
- PROG:23 and PROG:25 give the F1 form `OI + C <-> operational quantum mechanics`, "where C is an explicit set of physical conditions … derived … or clearly identified as additional principles".
- PROG:40: F1 retired; F2 is the objective, and "assuming the resource as a premise states it without sourcing it".
- PROG:521 and PROG:634.

**Positive-equivalence content.**
- §2 (PROG:44-64) correctly separates A (representation), B (operational) and C (full physical).
- §3.11 (PROG:208) is scoped: "a representation result and nothing more".

**Gap.**
- §3.1 (PROG:72) summarizes MQ-11 and MQ-12 without naming complex matrix kinematics or the complex drive generator.
- The file mentions neither: a grep for "complex matrix", "kinematics" or "Lüders" over PROG returns no match.
- So an F2 result proved sufficient under the existing interface would leave these imports unnamed, against PROG:23-25.

**Outcome.** n/a: PROG is a strategic map that controls nothing (PROG:7, PROG:15). What it summarizes has these outcomes:
- MQ-11: 1;
- MQ-12 and MQ-13: 2 for the statements as made.

**Class: imported**, for the F2 sufficiency route as it is framed.

**Texts read too strongly.**
- PROG:72, by omission.
- PROG:80 (see MQ-13).

The F1 retirement is a sourcing negative (marker M4), which belongs to the no-go cluster.

***

## TI-B: Arc B, `C_OI(V) = PPer(V)`

**Statement.** `track-i/arc-b-rooted-classification/result.md:13`; Main:640.

**Where proved (kernel, both directions).**
- `finiteRootedRealizable_iff_pper`.
- Forward: `pper_of_finiteRootedRealizable`.
- Reverse: `pper_has_responseRealization` (result.md:42-58).

**Hypotheses.**
- One hidden prior, shared by every root and independent of it. This is M1, kernel-realized (result.md:52-54).
- Zero-prior padding, which is proved necessary (result.md:86-91).
- Response-table carriers, M7 (result.md:60).
- Finite V (result.md:80-84).
- Exact step count.
- First-order Γ only (M2). The all-time multi-time-law question is open (Main:640 (a)).

**Outcome: 1.**

**Class: n/a.**

**Texts read too strongly.** `verification/programmes/oi-qm/amendments/amendment-1.md:19` says "the exact visible stochastic boundary for finite reversible OI under the inherited realization interface", and PROG:195 is similar. "Visible stochastic boundary" can be read as all visible statistics, while the theorem covers the rooted first-order family. This is minor.

***

## TI-C: Arc C, RC1 proper overlap of `C_OI` and `Q*`, and the ROADMAP:51 reading

**Statement.** `track-i/arc-c-quantum-representation/result.md:12-37`.

**Where proved (kernel).**
- `qStar_not_subset_finiteRootedRealizable`.
- `qStar_inclusion_iff_nonempty`.
- `qStar_of_finiteRootedRealizable`.

In all, 46 named kernel results (result.md:142-146).

**Hypotheses.**
- `Q*` is `QfbData` with the product-chain law (result.md:156-158).
- One common prior (result.md:110-115).
- First-order Γ only, with the seam at the final-coordinate marginal (result.md:66-68).

**CONFIRMING, stated in the record itself (result.md:84-90).** The witness for strictness is a non-periodic, fully mixing classical chain; any two-state rotation would serve. So `C_OI ⊊ Q*` at `Fin 2` means "non-periodic stochastic families are not rooted families of a finite bijection". It does not mean that quantum structure exceeds OI.

**Outcome: 1.**

**Class: n/a.** `Q*` is a comparison target.

**Texts read too strongly.** `verification/ROADMAP.md:48-52` (frozen). PROG:208 is scoped.

***

## TB-BA: Barandes boundary audit, and GR:134

**Statement.** `track-b/boundary-audit/result.md:8`, Outcome B: "rooted/conditional stochastic data suffice".

**Where established.** By primary-source reading (result.md:12-37). The representation datum is first-order Γ, and "higher-order trajectory probabilities are not fixed by those minimalist ingredients" (result.md:22-25). This is the origin of marker M2.

**Outcome: 1**, as an audit.

**Class: n/a.**

**Texts read too strongly.** GR:134: "Since $T_{ij}(t)$ determines the emergent quantum description (… Barandes correspondence)". Two places in Main contradict "determines":
- Main:218(i): the correspondence is many-to-one, and Θ is "not unique";
- Main:646: distinct coherent lifts of one visible family.

Uniqueness up to gauge holds only under the phase-locking hypotheses (G1)–(G4), for an undilated $e^{-iHt}$ with continuous-time data (Main:230), and GR:134 does not invoke them.

***

## TB-01: act 1, (BD3, BR3), and Main:210

**Statement.** `track-b/act-01-indivisibility/result.md:18-26`.
- **BD3.** Barandes's "indivisible stochastic process" is a tuple class that contains Markov chains.
- **BR3.** Failure of divisibility is not a hypothesis of the representation theorem; it is used only downstream, for interference.
- **Q8 (result.md:372-411).**
  - Our datum supplies Γ.
  - The initial distribution p is undetermined.
  - T₀ = {0} makes the divisibility axiom vacuous (result.md:403-406).
  - The prior is "not claimed to be sourced from bare OI" (result.md:408-410).

**Where established.** By a definition-level audit.

**Outcome: 1.**

**Class: n/a.**

**Main:210** reads correctly at the representation level.

**Texts read too strongly.**
- Main:656: "the mathematical structures are identical".
- Main:218: "the framework's use of the correspondence to obtain Born-rule statistics and unitary evolution". What it obtains is a per-time representation, with no intermediate propagator at T₀ = {0} (act 4, MP4).

***

## TB-06: act 6, (TI1, UB2)

**Statement.** `track-b/act-06-tuple-instantiation/result.md:17-31`.

**Where proved (kernel).** `BarandesTuple.lean`, 24 named results.

**Hypotheses.**
- T₀ = {0} (result.md:54).
- p0 is supplied by hypothesis (result.md:71-73).
- The UB2 witness is realized by a response table (M7; result.md:163-170).
- Γ level only.

**Outcome: 1.**

**Class: n/a.**

**CONFIRMING.**
- TI1 proves the translation hypothesis (T) for all of PPer, whereas Main:530 checks it at three sizes.
- At T₀ = {0} the source theorem yields only per-time dilations. That is the one-step lemma plus the n³ bound, consistent with Main:658's "interpretive apparatus — and nothing else".

***

## M2/M3: the Track B lift object (acts 7–45; act 14; book ch01, ch19)

**The object.**
- `AdmissibleDilationAt G a₀ U` means U is unitary on V×A and `G i j = Σ_a ‖U(i,a)(j,a₀)‖²` (`DilationChoice.lean:134-136`).
- `CoherentLift` means that holds at every t (`CoherentLiftGauge.lean:124-125`).

This is Main:526 per time, with a pure input ancilla a₀ (M3). The fit is first-order (M2).

**Act 14** (`act-14-threading-observability/result.md:40-51`): the verdict depends on the carrier, and "No carrier is adopted as the physical one".

**Act 45** (`act-45-fixed-basis-image/result.md`), separated by evidence layer.
- **(a) Kernel (the verdict `A45-BRIDGE-PROVED`, result.md:3-5, 11-26).** Take a trivial-ancilla admissible dilation and the fixed-basis datum with uniform initial law and identity readout. Its root-conditioned trajectory laws are fixed by the slice, also after `permClass` interventions on either side. Rooted families agree exactly when the slices are equal.
- **(b) Exact-arithmetic probe, not kernel and not in the verdict (result.md:5, 30-39).**
  - The CI-replayed probe `fixed_basis_ancilla_probe.py` exhibits two dilations of one slice "that share every column entering the slice".
  - These are separated at two steps when the ancilla is carried between steps as hidden basis states.
  - An ancilla attached as a tensor factor leaves the rooted family equal to `Gᵗ`, so it does not separate them. This tensor-factor fact also has a kernel anchor, `padData_rooted` (`OperationalSourcing.lean:476`, cited at Main:646).
  - The record: "They are not kernel statements, and the verdict does not contain them."
- **Main:646** states the separation tagged "(exact computation)", and the tensor-factor invisibility tagged "(kernel: `padData_rooted`)". That is the correct layering.

**Outcome: 1.** These are representation mathematics, and the records say so.

**Class.** Imported by design. This is legitimate unless the results are read physically.

**Texts read too strongly.**
- **`book/ch01-observation.md:187` (= FULL:522) and Main:646**, "each reproducing the visible law at every time". Here "visible law" means the rooted family Γ_t. Elsewhere it means the multi-time trajectory law (Main:99, 552). The probe witness in (b) exhibits lifts of one slice that a two-step law separates.
- **`book/ch19-open-problems.md:289-291`** states the carried-ancilla separation with no evidence-layer qualifier. Main:646 carries "(exact computation)". This is the R-I2 text point.
- **`book/ch19-open-problems.md:302`**, "None of this makes embedded observation and quantum mechanics inequivalent". The sentence presupposes an equivalence that is proved only with Q_fb. The proof supports the clause that follows it: "none of it narrows S⟺D⟺Q_fb".

***

## Summary (≤ 25 lines)

1. **Theorems.** Every kernel theorem in C1 is valid as a kernel statement (S⟺D⟺Q_fb; five-condition, OI⁺, primitive-source and substratum characterizations; Arc B/C; TI1/UB2; Track B lifts). Sub:141's Stage-1 paper theorem is 2 (MQ-29).
2. **Refuted reading.** The operational reading of Main:68 ("QM emerges under C1–C4") is refuted by the kernel witness `oi_alone_not_qm` (GR:220-222), in scope `Fin 2`, one sealed C1–C4 core, `FiniteOperationalTheory` interface; one direction only, since full control realizes the core (`realizesSealedOICore_of_control`), so C1–C4 neither entail nor exclude QM. The representation reading is valid, with C1–C4 idle (Main:72, 82(2)).
3. **No result in C1 derives quantum structure.** Q_fb is a function of a Markov chain with kernel |U|²; at the law-class level its leg adds nothing to S⟺D. Operational characterizations take complex kinematics and complex control/drives as hypotheses (imported); their other setting rules are A3/A4 idealizations that `diagTheory` also meets.
4. **Outcome 2, statements as made.**
   - MQ-12 (GR:250, 256; Main:590): the complex drive generator is unnamed; `control_of_phaseFree` consumes it (`MinimalRepertoire.lean:552-560`).
   - MQ-13 (GR:262 box, GR:264, Main:590): (a) unformalized swaps-and-phases step; (b) closure hypothesis `hc` missing from the box. `ExtendsSubstratum` is unused (`StructuralClosure.lean:414-417`).
   - MQ-29, MQ-32, MQ-42; and MQ-11's "what OI must supply" reading (Main:564).
5. **ELABORATING (not NEW).** The source of i is already in the corpus (GR:250, 258; `MinimalRepertoire.lean:13-25`; `LieRankSource.lean:36-43`; Intro:129; `two-mode-drive.md:54`). Residual: "no phase operation enters" holds for the primitives, not for what they generate: `flow(X_ab,π/2)·swap_ab = diag(−i,−i,1)` on D ≥ 3.
6. **Act 45, by evidence layer.** Kernel: with a trivial ancilla, fixed-basis laws are fixed by the slice. Exact-arithmetic probe only (not kernel, not in the verdict): two dilations sharing every column entering the slice separate at two steps with a carried ancilla, not with a tensor-factor ancilla. ch19:289-291 omits the layer; Main:646 states it.
7. **Texts read too strongly.** Emergence: Main:68, 206, 682, 684; FULL:244, 334; SM:1100; GR:40; Sub:389, 459. MQ-01: Main:776; FULL:64, 266; ROADMAP:48-52 (frozen). MQ-03: Main:526, 530, 648, 656; FULL:6207. Also GR:134; ch19:302; FULL:684 vs FULL:690.
8. **F-1 [named question].** Extended mechanisms beyond the ruled-out classes; already pursued by Q-A, MECH-2, `two-mode-drive.md`, PROG:40. Cheapest check: the `diagGen_not_control` analogue per mechanism.
9. **A5.** Γ-level matching (T₀ = {0}): Barandes, Definition (i), Arc B/C, Track B. Whole-law matching per protocol: S⟺D⟺Q_fb. Multi-protocol: only per finite menu to ε, via hidden quantum simulation.
10. **POSITIVE [audit derivation].** Q_fb's full-basis access is not material: the visible-only Lüders variant gives the same class.

## Cross-cluster assumption-watch markers

- **W1 (A1).** Q_fb, QfbData and Q* are functions of Markov chains with kernel |U|². An "agreement with QM" whose quantum side is one of them compares against such an object.
- **W2 (A1) [named question, ELABORATING].**
  - *Question.* In a candidate operational mechanism, is the phase relation between the drive generator and the exchange basis physically sourced?
  - *Why it matters.* The prose label "phase-free" states that no phase operation is a primitive. It does not cover what the primitives generate.
  - *Cheapest check.* Compute `flow(drive, π/2)·swap`. A relative quarter phase indicates the complex direction is present.
  - *Decisive form.* The analogue of `diagGen_not_control` (`LieRankSource.lean:18-25`, `:146`). Show that every available conjugation in the generated theory preserves real matrices, so control fails.
  - A zero-diagonal Lie-algebra lemma is not decisive, because `HControl` is not claimed necessary (`ReachabilitySeam.lean:71-72`).
  - `two-mode-drive.md:54, 145-147` already treats the matter for its candidate.
- **W3 (A1, with A3/A4 tagged separately).**
  - The import is complex matrix kinematics. It is disclosed at GR:216 and Main:564.
  - The setting rules — uniform ancillas of every size, partial-trace discard, a readout at every level — are observer-capability idealizations. They are not quantum content: `diagTheory` meets them (GR:220; `GeneralCarrier.lean:157-163`). The corpus phrase "carries no quantum content" (GR:276-280; Main:590) concerns the typed interface and is not used for this endomorphic claim.
  - PROG's F2 summary names neither the kinematics nor the drive.
- **W4 (idle hypotheses).** For each "OI + X ⟺ QM" box, check whether OI does logical work in each direction.
  - `ExtendsSubstratum` is unused in `substratum_plus_control_qm`.
  - The OI clause is idle via `realizesSealedOICore_of_control`.
  - `oi_compatible_classification` holds on `Fin 2` only.
- **W5 (A3, narrowed per review B5).**
  - For rooted first-order families, a shared root-independent prior is kernel-proved by `pper_has_responseRealization`, with zero-prior padding as its scope (Arc B result.md:86-91).
  - Only the multi-time joint-law form with a root-independent prior is paper-only (Main:520-522; Egri Prop. 16). The kernel `S_imp_D` correlates the hidden state with the root and stores the trajectory.
  - Consumers that need the multi-time form are Main:137, as applied to realized laws, and Sub:137.
- **W6 (A1/A5).** The ε-gluing and uniform-continuum realizations run quantum instruments in a hidden density register (Main:566, 598). Every "reproduces QM predictions" reading inherits this.
- **W7 (text).** "Visible law" names both Γ and the multi-time law (Main:99, 552 against Main:646 and ch01:187). An exact-arithmetic probe witness (act 45, not kernel) exhibits two lifts of one slice that a two-step law with a carried ancilla separates.

***

## Disposition of review findings (r1 → r2)

| Finding | Change in r2 |
|---|---|
| **B1** Act 45 evidence layer | **Accepted.** The M2/M3 section now splits (a) the kernel verdict from (b) the exact-arithmetic probe ("not kernel statements … verdict does not contain them", result.md:38-39). It quotes "share every column entering the slice" and adds the tensor-factor non-separation. W7 is now existential, at the probe layer. Main:646's "(exact computation)" tag is recorded. The R-I2 text point moves to ch19:289-291 and ch01:187. New summary item 6. |
| **B2** drive i | **Accepted.** Reclassified ELABORATING, crediting GR:250, GR:258, `MinimalRepertoire.lean:13-25`, `LieRankSource.lean:36-43`, Intro:129 and `two-mode-drive.md:54/145-147`. "Hides" is dropped. The narrow point is primitives versus what they generate, with the identity `flow(X,π/2)·swap = diag(−i,−i,1)` (D ≥ 3), `diag(1,−1,1)` for the real rotation, and global `−i·I` on D = 2. The decisive form is the `diagGen_not_control` analogue; the zero-diagonal lemma is marked non-decisive (`ReachabilitySeam.lean:71-72`). "Real QM" is replaced by "real-matrix-preserving; no control". The check is tied to the narrow sub-claim, not to F-1. |
| **B3** substratum box | **Accepted.** "ExtendsSubstratum unused" is kept. The diagonal counterexample is credited to the kernel (`LieRankSource.lean:87-119`, `SubstratumSource.lean:37-46`, `substratum_residual`), and the r1 audit-derivation label is withdrawn. The over-reading is restated as (a) the unformalized swaps-and-phases step and (b) the closure hypothesis missing from the GR:262 box, GR:264 and Main:590. The necessary-condition reading and the GR:260 disclosure are acknowledged. |
| **B4** outcome 3 misapplied | **Accepted.** MQ-02's operational reading is recorded as refuted by `oi_alone_not_qm` (GR:220-222), with its scope stated (`Fin 2`, sealed core, `FiniteOperationalTheory`). MQ-27 and MQ-28 are reclassified as texts reading MQ-01 too strongly. Summary items 1–2 are corrected. F-1 is kept as a separate named question on extended mechanisms, citing Q-A (with PROOF-RECOVERY.md), MECH-2, `two-mode-drive.md` and PROG:40. The scope of `substratumGen_not_control` is stated precisely. |
| **B5** W5 | **Accepted.** W5 is narrowed: the rooted form is kernel-proved by `pper_has_responseRealization` (zero-prior padding scope), and only the multi-time joint-law form is paper-only. §0 is updated to match. |
| **B6** MQ-12/13 outcomes | **Accepted.** Kernel statements stay 1. The statements as made go to 2, with the imports and consuming steps named: `control_of_phaseFree`, `MinimalRepertoire.lean:552-560`; `hc`/`hd`, `StructuralClosure.lean:417`. |
| **N1** citations | **Fixed.** `MinimalRepertoire.lean:423-428`. The full path `verification/programmes/oi-qm/amendments/amendment-1.md:19`. F1 form at PROG:23/25. |
| **N2** misattributed quote | **Fixed.** The `RevReal` docstring phrase is reattributed to the independent-prior form (§0). |
| **N3** structural equality | **Fixed.** Now "the same law class as D", with the non-structural caveat. |
| **N4** classical-chain / "adds nothing" | **Accepted.** "Function of a Markov chain" wording is adopted. A cross-reference is added for the downstream `U_φ` / ħ uses (Main:532-534, 554; GR:134, 228). |
| **N5** W3 overstatement | **Accepted.** Kinematics is tagged as the A1 import. Rules (d)–(f) are re-tagged A3/A4. The corpus counter-claim (GR:276-280, Main:590) and `diagTheory` are cited. MQ-11 is updated to match. |
| **N6** class/summary consistency | **Fixed.** MQ-29's class is split per context (conditional) and per menu (imported). Summary item 1 now separates kernel theorems from Sub:141 (outcome 2). |
| **N7** GR:242 | **Downgraded.** It is noted, with the GR:244 disclosure and `oiPlus_iff_completedOI`, and not pressed. |
| **N8** overreach | **Fixed.** "Gem (NEW)" and "decisive because it shows" are removed. W2 and F-1 are phrased as [named question] with their cheapest checks, and nothing is adopted. |
| **N9** §A.34 check | No change; the reviewer confirmed the direction-by-direction treatment. |

## Disposition of re-review items (r2 → r3)

| Item | Change in r3 |
|---|---|
| 1 | `control_of_phaseFree` is now cited at `MinimalRepertoire.lean:529` (defined) and `:559` (invoked), replacing `:106`. |
| 2 | "Carries no quantum content" is attributed to the typed interface (MQ-11, W3). The endomorphic claim now rests on `diagTheory` alone. |
| 3 | The tensor-factor fact is anchored at `padData_rooted` (`OperationalSourcing.lean:476`, cited at Main:646). |
| 4 | The `oi_alone_not_qm` refutation is stated as one direction only: `realizesSealedOICore_of_control` means C1–C4 neither entail nor exclude QM (MQ-02, summary item 2). |
