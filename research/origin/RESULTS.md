# RESULTS — research/origin

Every claim carries one label: CERTIFIED [K at L, file:line] / CONDITIONAL (on named items at their status) / CONJECTURE / FAILED / OPEN; evidence level [K]/[D]/[W]/[X]/[A]/[U]; and a pointer to its script, output and replay.

**Label convention used here.** CERTIFIED is reserved for statements that are landed kernel theorems at L (or the
direct composition of landed declarations, said so). A statement proved by a written argument [W] and checked by
exact computation [X], or kernel-checked only in a design run [D], is labelled **CONDITIONAL**, the named item
being *its own unkernelized step* ("[W] proof, no kernel check" or "[D], not certified"); a statement that also
rests on a named premise names that premise too. FAILED marks a mechanism that does not source the target, kept
with its evidence. Kernel paths are under `verification/lean-mathlib/OIBridge/` at L = `9f9f8257`. Scripts are
under `experiments/`; each has `.py`, `.out`, `.err` (exit marker), `.replay.out`, `.replay.err`
(byte-identical).

## O1 — the no-go envelope

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O1-T1 | For every linear map Φ: Φ∘Δ = Δ∘Φ ⟺ (non-generating ∧ non-detecting). For a unitary channel Ad U: non-generating ⟺ non-detecting ⟺ U monomial. | CONDITIONAL ([W] proof, no kernel check; non-generating half for monomials CERTIFIED [K SubstratumInterface.lean:126 `preservesDiag_conj_of_monomial`]) | [W] + [X] 15 unitaries (d = 2, 3) | NOTES-O1 §2; `o1_envelope` M1 |
| O1-T2 | Sandwich identity V = tr P M₂(id − Δ)M₁ρ₀; vanishes if M₁ non-generating or M₂ non-detecting. Qubit unitary with U†: V = 2\|a\|²\|b\|²; owner's witness (1, 1/2) ⟺ balanced (\|a\|² = 1/2). | CONDITIONAL ([W] proof, no kernel check) | [W] + [X] 11 qubit unitaries | NOTES-O1 §2; M2a–c |
| O1-T3 | Monomial envelope: for every class of submonomial operators (substratumClass, permClass, subclasses) every InstAvail branch commutes with Δ at every level; reachable states are diagonal; path dephasing (= fresh-record dephasing) is the identity on them; every sandwich has V = 0 for every protocol (ancilla, readout with feed-forward, coarse-graining, discard); DC is a linear subspace (dim d² + (d²−d)²), closed under mixtures and limits. | CONDITIONAL ([W] proof for the reachable-set and visibility steps; the branch commutation for substratumClass and permClass is [D]: `instAvail_substratum_dephase`, `instAvail_permClass_dephase`, `conj_dephase_of_submonomial`, green in run 38084486326 at dev commit c3f7fbb2, not certified) | [K ImplementationLocality.lean:530, StructuralClosure.lean:231, SubstratumInterfaceAudit.lean:350] + [W] + [X] 60 protocols, 2304 exhaustive sandwiches, ranks 8 / 45 | NOTES-O1 §2; M3, M4a–d, M7 |
| O1-T4a | Ones-fixing is independent of mixing: all four cells populated; V = 0 exactly in the monomial cells. | CONDITIONAL ([W]; exact instances) | [X] | NOTES-O1 §3; M5a |
| O1-T4b | The landed ones-fixing architecture `onesClass` makes the conjugation by the gate flow of the site exchange at t = 1/2 (= √X: balanced, non-monomial, owner's witness exact) available in its generated theory. | CERTIFIED as a composition of landed declarations [K InstrumentRealization.lean:628 `onesClass_arch`, :833 `isometry_fixes_ones`, :508 `onesClass_gateFlow`; SubstratumSource.lean:103 `genTheory_avail_conj`; LiftAudit.lean:138 `gateFlow_half_entries`]; non-monomiality and the packaged statement `onesFixing_class_carries_mixer` [D], green in run 38084486326 at dev commit c3f7fbb2, not certified | [K] + [D] + [X] | NOTES-O1 §3; M5b–c |
| O1-T4c | The kernel's interference exposure (branches 3/2, −1/2) holds verbatim with the ones-fixing mixer √X in place of `hMat`. | CONDITIONAL ([X] exact; no kernel check) | [X] | M6 |
| O1-T4d | Correction of the rung-1 slogan: `permClass_onesFixing` + `instAvail_unitary_fixes_ones` exclude `hMat` and the quarter phase; the exclusion of every mixer from the sourced class is O1-T3 (monomiality). Non-monomiality is necessary (and with balance sufficient) for the witness; non-ones-fixing is neither. | CONDITIONAL (on O1-T2, O1-T3, O1-T4a at their status) | [K PhaseSource.lean:79, InstrumentRealization.lean:398] + [W] + [X] | NOTES-O1 §3 |
| O1-T5 | Passivity: if observe-and-forget is the identity on the reachable body, every sandwich has V = 0 whatever the mixers (drive, completion-valued operations, imported unitaries included); classical towers are passive (A5), also on the completed body; fresh-record dephasing is the identity on classical states. The Discrete witness requires invasive observation. Scope: dephasing realized as which-path recording; the twirl reading is covered by O3-T4 (Lemma P). | CONDITIONAL ([W] proof, no kernel check) | [W] + [A oistage A5] + [X] F1, F5, F9 (6336 + 6336 sandwiches; group of order 1344) | NOTES-O1 §4 |
| O1-T6 | Outcome determinism: if the extreme points give the frame readout 0/1 values, no reversible operation is a balanced pure mixer; with exchanges + passive readout + conditioning, point masses are reachable and are the extreme points. | CONDITIONAL ([W] proof, no kernel check) | [W] + [X] F2–F4, F6 | NOTES-O1 §4 |
| O1-T7a | Memory erasure fakes the witness: classical swap from (z=0, x uniform) gives 1 and 1/2 with the memory re-randomized or with the kernel recorder written into the memory; a blank-register record gives V = 0. The definition of path dephasing is load-bearing. | CONDITIONAL ([X] exact on the model) | [X] F6, F7, CCF3 | NOTES-O1 §5 |
| O1-T7b | Knowledge-balance readout (KB-D) turns the substratum swap into a balanced extreme mixer of an octahedral body and gives the exact witness; adding back the passive readout collapses it to the simplex. | CONDITIONAL (on KB-D, which is not in the stated access; [X] exact on the model) | [X] F8a–g, CCF1, CCF2; [L] Spekkens 2007 | NOTES-O1 §5 |
| O1-V | Verdict O1: within the stated access the envelope is complete on the configuration carrier (T3) and field-neutrally (T5, T6); its exact boundary is T7. | CONDITIONAL (on O1-T3, O1-T5, O1-T6 at their status) | as above | NOTES-O1 §0 |

**Design module (O1).** `lean/OriginEnvelope.lean`, verbatim copy of `verification/lean-mathlib/OIBridge/OriginEnvelope.lean`
at dev commit `c3f7fbb21f32587ef3f00d156d58a3743d28ed53` (branch `dev-origin/envelope`, blob `1a529c36…`, sha256
`182af483…fa3288`); Mathlib bridge Build green in workflow run 38084486326, every declaration on
[propext, Classical.choice, Quot.sound]. The run's release gate failed on `lean-manuscript` (the design module has no
census disposition) and on `claims` and `duplicate` (hits in `research/archive/`, present at the branch base).
Run 38083822302 (dev commit 271ba177) failed to parse `ᴴ` (scoped notation not opened).

**Script ledger (O1).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o1_envelope.py` | `9390d8a5…7d9fd9` | `a161ea05…c8a695` | 14/14 checks, 6 countercontrols expected-false, VERDICT ENVELOPE-M HOLDS | byte-identical |
| `o1_fieldneutral.py` | `965eb41d…acd5d` | `0750e15c…2073` | 16/16 checks, 4 countercontrols expected-false, VERDICT ENVELOPE-F HOLDS | byte-identical |

## O2 — candidate mechanisms for a discrete mixer

Each mechanism: smallest exact model, induced visible operation, non-monomiality, sandwich, disguise test
(`experiments/o2_mechanisms.py`, classification rule fixed in the header before run 1).

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O2-A12 | A1–A2 (finite configurations, bijective dynamics, selectable permutations): the 24 bijections of {0,1}² induce only identity, flip, replace-by-uniform on the visible bit (all DC); composite sandwich V = 0. | FAILED (envelope; O1-T3) | [X] A12a–b, CC1 live detector; [K SubstratumInterface.lean:91] | NOTES-O2 §1 |
| O2-A36 | A3–A6 with the link coupling: a centre-independent, linear, link-coupled second-order rule (N = 3, K = 2, q = 2) is a bijection of the 4096 configurations, gauge-covariant under M → G M G⁻¹; hence monomial on the carrier; visible bit uniform after one step. The reconstruction's U(3)×U(2)×U(1) is complex representation theory downstream of the input E1. | FAILED (envelope; the complex route imports E1) | [X] A36a–d; Substratum.md:122, :162 | NOTES-O2 §1 |
| O2-PH | Phase interventions (Z, quarter phase, rational phases): monomial, DC, V = 0. | FAILED (envelope) | [X] PHa | NOTES-O2 §1 |
| O2-RW | Read-write coupling: at every knob value the coupling is 1 or the swap. | FAILED (envelope) | [X] RWa; [K ReadWriteControl.lean:96, CoherentContinuumSource.lean:292] | NOTES-O2 §1 |
| O2-ANC | Ancilla coupling with readback and feed-forward; record writing (`recordInstr`): DC; memory, not coherence; the recorder into a blank register leaves populations unchanged. | FAILED (envelope) | [X] ANCa; O1 M3, M4c–d; [K InternalObserver.lean:249, :290] | NOTES-O2 §1 |
| O2-TAV | Coarse-graining and time averaging: mixtures of permutations, DC, V = 0. | FAILED (envelope) | [X] TAVa | NOTES-O2 §1 |
| O2-CLO | The completion's closure: monomial group closed; DC a closed linear condition; passivity survives the completion. | FAILED (envelope) | [X] CLOa, O1 M7; [W] O1-T5 | NOTES-O2 §1 |
| O2-G1 | `HasAncillaQubitInterference`: passes (1, 1/2); the coherence is the hypothesis `availExt … (ancMix A)`. | FAILED (disguise) | [K AncillaInterference.lean:161–163] + [X] G1a | NOTES-O2 §2 |
| O2-G2 | `LayerFlowExecutable` / gate flow at t = 1/2: passes; coherence enters through the complex phase on the swap's −1 eigenspace; not derived by the substratum theory. | FAILED (disguise) | [K LiftAudit.lean:47, :200] + [X] G2a | NOTES-O2 §2 |
| O2-G3 | State-mixing datum `rot(π/4)` / `fixedGateTheory`: passes; a postulate; with one angle DerivedOI ∧ FixedGateSourced ∧ ¬QM. | FAILED (disguise) | [K StateMixingCoupling.lean:45, :50; DiscreteCompletion.lean:1929, 1933, 1948] + [X] G3a | NOTES-O2 §2 |
| O2-G4 | Unistochastic lift of the balanced transition: every lift is a balanced mixer, but its coherent predictions are not fixed by B (seven values found), and the substratum's own two-step statistic is the dephased 1/2. | FAILED (disguise) | [K BarandesTuple.lean:430] + [X] G4a–b, CC3 | NOTES-O2 §2 |
| O2-G5 | Knowledge balance: with all permutations, the counting measure and KB-D (reading z re-randomizes the memory), the substratum swap is a balanced extreme mixer of an octahedral toy bit; exact witness (1, 1/2). | CONDITIONAL (KB-D; [X] exact on the model) | [X] G5a, O1 F8; [L] Spekkens 2007 | NOTES-O2 §3 |
| O2-KB | No premise at L supplies KB-D; four candidate sources closed (recorder, bath relaxation, incompleteness of observation, native readout); the native Lüders readout and A5 passivity contradict it. | OPEN (sourcing of KB-D); ruled out on the stated access ([W] + [X] O1 F2, F7) | [K OperationalAssembly.lean:658]; [A oistage A5] | NOTES-O2 §3 |
| O2-V | Verdict O2: no mechanism from the stated resources sources a discrete coherent mixer; every passing construction either imports the coherence (G1–G4) or changes the observation law (G5). | CONDITIONAL (on O1-T3, O1-T5 at their status) | as above | NOTES-O2 §0 |

**Script ledger (O2).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o2_mechanisms.py` | `14caa86b…5be627` | `fce8a314…02f444` | 17/17 checks, 4 countercontrols expected-false, no CANDIDATE | byte-identical |

## O3 — the Continuous Origin

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O3-K | Relative to the baseline the substratum theory satisfies (`DerivedOI ∧ SubstratumAvail`), exact finite QM ⟺ one executable layer flow ⟺ phase-free richness; the substratum theory executes no layer flow. | CERTIFIED [K LiftAudit.lean:812 `derivedOI_qm_iff_layerFlowExecutable`, :783, :200; RouteB.lean:161, :290; LiftAudit.lean:750; MinimalRepertoire.lean:569] | [K] | NOTES-O3 §1 |
| O3-T1 | With the substratum's phase continuum (every diagonal unitary, `diagonal_avail`), one exactly available balanced mixer on a moved pair at every level yields the transition flow at every angle; so, relative to the same baseline, exact finite QM ⟺ one balanced mixer per level (T-O3a). The one-parameter family comes from the stipulated phase continuum; the missing content is one non-monomial operation per level. | CONDITIONAL ([W] proof incl. B = D₁HD₂ and B† = EBE; no kernel check) | [W] + [X] C1a (6 unit Gaussian rationals), C1b (three points, gate flow + S) + [K LiftAudit.lean:754, :770; RouteB.lean:161] | NOTES-O3 §1 |
| O3-T2 | Continuous ⇒ Discrete: the drive's member at π/4 is a balanced mixer with the owner's witness; any drive whose NOT swaps two pure frame states with a complemented readout passes through a balanced pure state. | CONDITIONAL ([W] intermediate-value argument; [X] exact instances) | [X] C2a, C2b on `ball3Drive`'s geometry [K KInfFoundations.lean:449] | NOTES-O3 §2 |
| O3-T3 | Discrete ⇏ Continuous field-neutrally (KB-D octahedron, reversible group of order 24) and for exactness without the phase continuum (the fixed-gate theory is not QM at any angle); on the qubit level, ⟨H, S⟩ and ⟨rot(π/4), S⟩ have order 24; an irrational fixed gate gives density without exactness and no exact witness. | CONDITIONAL ([X] exact; polytope ⇒ finite Aut [W]); the fixed-gate facts CERTIFIED [K DiscreteCompletion.lean:1929, 1933, 1948, 1522] | [X] C4, C5, C7 + [K] | NOTES-O3 §2 |
| O3-T7 | Skeptical pass on O3-T3: without the phase continuum, finiteness is level-dependent. On three states two balanced mixers on overlapping pairs, and at level three the fixed-gate datum `mixImage 3 (π/4)` with one exchange conjugate, generate elements of infinite order (eigenvalues not roots of unity: norm-polynomial factors not monic over Z, e.g. λ² − (3/2)λ + 1); at level two the factors are cyclotomic. So the closure of what a balanced mixer generates contains a one-parameter subgroup; full dense control at the balanced angle is not checked. | CONDITIONAL ([X] exact certificates; closure ⇒ one-parameter subgroup [W + L]); density at π/4: OPEN | [X] `o3_density` E1–E3, CC1–CC2 | NOTES-O3 §2 |
| O3-T4 | Lemma P: if the native readout is repeatable and passive, every pure state is outcome-deterministic for it; hence no balanced mixer and no drive through the native NOT, whatever operation data are added. Applies to every tower built by conditioning a classical substratum. | CONDITIONAL ([W] proof, no kernel check) | [W] + [X] C3a–c + [A oistage A5] | NOTES-O3 §3 |
| O3-T5 | The field-neutral Continuous Origin needs: finite rank of an infinite-substratum completion, an infinite-order stage-crossing datum with OFF (OPS-Γ), and invasive repeatable observation (Lemma P). | OPEN (all three unsourced) | [A drive F-D2, F-D3; oistage NG1, NG2; rank] + O3-T4 | NOTES-O3 §3 |
| O3-T6 | Once a drive is sourced at level one, what remains for `oiPlusMin_iff_qm` is its spectator extension to every level and the context stability of a generating class containing it; given the phase continuum this reduces to the spectator stability of one balanced mixer. | CONDITIONAL ([W]; spectator form exact [X] C6; context stability a theorem only for the monomial class [K StructuralClosure.lean:261]) | [K SubstratumInterfaceAudit.lean:654, :660; ImplementationLocality.lean:904] + [A stage 5 D5 N1c, row β] + [X] C6 | NOTES-O3 §4 |
| O3-D | Disguise test of the minimal added content: every matrix-level form known at L (layer flow, driven pair, state-mixing datum at every angle, balanced mixer by hypothesis) contains the balanced mixer in its interface; OPS-Γ passes syntactically but cannot be met through the native NOT on passive towers. | FAILED as a source (matrix forms); OPEN (OPS-Γ's source) | [K StateMixingCoupling.lean:511] + O2 G1–G4 + O3-T4 | NOTES-O3 §5 |

**Script ledger (O3).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o3_continuous.py` | `795cb274…40ffc7` | `b4e1e261…7e3cc8` | 11/11 checks, 4 countercontrols expected-false | byte-identical |
| `o3_density.py` (run 2) | `62c92e54…a31a688` | `ea8f3633…a3766` | E1, E2 infinite order certified, E3 finite; 2 countercontrols expected-false; VERDICT DENSITY | byte-identical |
| `o3_density.run1.py` (run 1, kept) | `9cdb7585…a6c14` | `aef01c50…baa77` | VERDICT VOID: both countercontrols failed (defective cyclotomic comparison; characteristic polynomial over Q(√2) tested as if over Q) | — |

## O4 — the dependency between Origin and the composite-action bridge

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O4-I1 | The bridge's missing assumption (stage 6 §5: (b) for `ball3Drive`'s flow R_z and its J-conjugate R_x on one token) is equivalent to (b) for R_z(t) for all t together with (b) for the single discrete operation J = cyc3, since J = R_z(π/2)R_x(π/2) and J R_z(t) J⁻¹ = R_x(t). | CONDITIONAL ([W] proof; group identities [X]) | [X] D1, D2, CC1, CC3; [K KInfFoundations.lean:425, :427, :449]; [A stage 6 §5] | NOTES-O4 §1 |
| O4-J | J is a discrete balanced mixer for the frame z (pure e_z ↦ pure balanced e_x; owner's witness with J⁻¹; order 3); its unitary lift is non-monomial and balanced. J is the Discrete target in the bridge's vocabulary. | CONDITIONAL ([X] exact) | [X] D3, D4, CC2 | NOTES-O4 §0 |
| O4-I2 | Matrix reduction: if a generating class contains the substratum class and the spectator forms of one balanced mixer B, it contains the spectator forms of the drive. | CONDITIONAL ([W]; Kronecker identity [X]) | [X] D5; [K StructuralClosure.lean:261] | NOTES-O4 §1 |
| O4-D | Mutual, non-discharging dependency: the bridge needs SRC (availability of the mixer from a premise passing the disguise test) from Origin; Origin needs SPEC (spectator stability of the sourced mixer: matrix form = what remains for `oiPlusMin_iff_qm`; pair form = (b)) from the bridge; neither supplies the other. | CONDITIONAL (on O3-T6, O4-I1 at their status); SRC and SPEC each OPEN | [A stage 5, stage 6] + NOTES-O3 §4 | NOTES-O4 §0, handoff-proposals/O4-origin-bridge-dependency.md |

**Script ledger (O4).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o4_dependency.py` | `a68db000…49c64` | `8121ece5…580160` | 5/5 checks, 3 countercontrols expected-false | byte-identical |

## Verdicts by node

| node | verdict | label |
|---|---|---|
| O1 | The no-go envelope is dephasing covariance (monomiality), not ones-fixing; within the stated access every sandwich has visibility 0 on the configuration carrier and field-neutrally; its exact boundary is memory erasure (not a path dephasing) and the knowledge-balance readout KB-D. | CONDITIONAL (O1-T3, T5, T6 [W] + [X]; T4b CERTIFIED as a composition) |
| O2 | No mechanism from the stated resources (A1–A6, link coupling, ancilla readback, record writing, coarse-graining, time averaging, closure) sources a discrete coherent mixer; the four that pass the witness carry the coherence in their input; the KB-D toy passes with monomial input but changes the observation law. | FAILED (every stated-resource mechanism); FAILED by disguise (G1–G4); CONDITIONAL on KB-D (G5); sourcing of KB-D OPEN |
| O3 | Matrix level: relative to the substratum theory's availability, exact QM ⟺ one executable layer flow ⟺ one balanced mixer per level (via the stipulated phase continuum); field-neutral: Lemma P forbids a drive through the native NOT on passive towers, so an observation-side change is needed; once a level-one drive is sourced, what remains is its spectator stability. | CERTIFIED (O3-K); CONDITIONAL (O3-T1, T2, T4, T6, T7); OPEN (O3-T5, the field-neutral source) |
| O4 | Origin and the bridge meet at one discrete balanced mixer (the bridge's J); SRC is Origin's open premise, SPEC the bridge's; neither discharges the other. | CONDITIONAL (O4-I1, I2, D); SRC, SPEC OPEN; handoff proposal O4-1 |

## O5 — KB-D: source it or close it (round 2)

Script `experiments/o5_kbd.py` (decision rule in the header before run 1; one pre-run edit, the normalization
control the header names; run 1 `VERDICT NO-GO-ON-STATED-ACCESS`, 5 countercontrols expected-false; replay
byte-identical). Design module `lean/OriginPassive.lean` (verbatim copy of `verification/lean-mathlib/OIBridge/OriginPassive.lean`
at dev commit `aef5d4463a604601dc5cbe2da89fa02a8b67bdbc`, branch `dev-origin/passive`, blob `9ef2a18d…`, sha256
`8fac1f7f…17bf978`): Mathlib bridge Build green in workflow run 38090594001, all eleven declarations on [propext,
Classical.choice, Quot.sound]; release gate red only on `claims`, `duplicate`, `lean-manuscript` (by construction).

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O5-T1 | Sharpened Lemma P (classical carrier): on a body of probability vectors whose cell readouts are passive and repeatable (observe-and-forget decomposition into a state reading the cell surely and another body state, at every state with cell mass in (0, 1)), every extreme point is outcome-deterministic for every cell, so none is balanced; with cells separating the configurations every extreme point is a point mass. | CONDITIONAL ([W] proof; [D] `lemmaP_extreme`, `extreme_cellMass_det`, `extreme_not_balanced`, `pointMass_of_cells`, `extreme_pointMass_of_passive`, green in run 38090594001 at dev commit aef5d446, not certified) | [W] + [D] + [X] A1 (11 posteriors, extreme points = the 4 point masses, deterministic for all 15 partitions), A6 (passive decompositions everywhere on the simplex body; none at x⁺ on the KB-D body; separation control) | NOTES-O5 §1 |
| O5-T1a | Exclusivity: with the exchanges and any one passive repeatable readout of any nontrivial partition of {0,1}², every point mass is reachable and the body is the simplex whatever further instruments are added, KB-D's included (14/14 partitions); the reaching protocol is the kernel's pure-seed pattern (read, feed-forward correction, forget). KB-D's octahedron requires removing every passive readout, which contradicts the native readout of every `FiniteOperationalTheory`. | CONDITIONAL ([W] + [X]); the kernel facts CERTIFIED [K OperationalAssembly.lean:658 `readout_is_localLuders`, :675 `pureSeedPrep_available_of_swap`] | [X] A2, A3 (7 posteriors, octahedron, x⁺ repeatable and not passive), A4, A5 | NOTES-O5 §1 |
| O5-KB1 | KB-D splits: the instrument KB-D1 = forget_x ∘ Lüders_z exactly, branch by branch (native pieces: Lüders readout, ancilla discard, uniform attach); the exclusivity KB-D2 is what the toy body needs and is excluded on the stated access (O5-T1a). | CONDITIONAL ([X] D1, D2; composite availability [W]) | [X] D1 on 11 reachable states; [K OperationalAssembly.lean:492, :515, :649, :658] | NOTES-O5 §4 |
| O5-a | Candidate (a), incompleteness as a memory bound: procedures with a one-bit memory prepare point masses; embedded (posteriors given the memory), 18432 of the 40320 bijections of (z, x, m) give a point-mass posterior; the witness frequencies stay classical (V = 0) and the memory-conditioned 1/2 is the which-path record overwriting the preparation record (memory erasure, O1-T7a); a fresh blank bit gives 1. | FAILED (as a source of KB-D) | [X] B1, B2pm, B3 | NOTES-O5 §2 |
| O5-a′ | With affine (linear) dynamics and a one-bit memory, every embedded posterior is uniform on a pair or on all of Ω, and all six pair states occur: memory bound + linear dynamics supply the knowledge-balanced posteriors (the toy bit's epistemic half), not its disturbance. | CONDITIONAL ([X] exhaustive over AGL(3, 2), 1344 maps; one-bit, one-elementary-system scope) | [X] B2aff | NOTES-O5 §2 |
| O5-b | Candidate (b), the kernel recorder under a finite-memory bound: passive on the system when written into a separate register; erasure to a known value (x := z, point-mass posteriors) when written into the memory; no reversible dilation writes a perfect record into a non-blank register (0 of 576), and the 16 perfect records into a blank register keep x as a known relabeling. | FAILED (as a source of KB-D) | [X] C1, C2; [K InternalObserver.lean:249 `recordInstr`, :290 `recordInstr_not_passive`] | NOTES-O5 §3 |
| O5-d | Candidate (d), symplectic couplings: among affine record couplings of (z, x, q, p) (z′ = z, q′ = z from a blank pointer), all 32 symplectic ones re-randomize x when the pointer conjugate p is uniform (kickback x′ = x + p), none keeps x; 128 non-symplectic ones keep x; with p known none re-randomizes. The substratum's second-order linear rule is symplectic iff its coupling is symmetric. | CONDITIONAL (on SYMP: every coupling symplectic, the observer's included; and UPC: pointer conjugates unknown); UPC is KB-D2 relocated to the pointer (on one elementary system ASp(2, F₂) = S₄), so circular as a source; SYMP restricts A2's available bijections | [X] E1 (GL(4, 2), 20160 maps); [W] hand derivation and MᵀJM = [[0, I], [−I, F − Fᵀ]]; Substratum.md:158 | NOTES-O5 §4 |
| O5-V | Verdict O5: KB-D is not sourced; on the stated access its exclusivity is excluded by the native passive readout (sharpened Lemma P); candidates (a), (b) FAILED, (c) sources the instrument only, (d) CONDITIONAL on SYMP + UPC with UPC circular. | CONDITIONAL (on O5-T1, O5-T1a at their status); sourcing of KB-D OPEN | as above | NOTES-O5 §0 |

**Script ledger (O5).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o5_kbd.py` | `a662d9ab…ddcc4f` | `2aca6e8c…f87797` | 15/15 items True, 5 countercontrols expected-false, normalization control True, VERDICT NO-GO-ON-STATED-ACCESS | byte-identical |

## O6 — the stage-crossing generator against O3-T5's three requirements (round 2)

Script `experiments/o6_tower.py` (decision rule in the header before run 1; one pre-run edit, K9's nonnegativity
made an exact identity; run 1 `VERDICT EXCLUSIVE-ON-PASSIVE-JOINT-ON-INVASIVE`, 5 countercontrols expected-false;
replay byte-identical). Design module `lean/OriginPassive.lean` now the verbatim copy at dev commit
`c2484cca3107085e360c461167095262dba45444` (blob `4fc0c2a5…`, sha256 `5da5a6d4…eacc36`; adds Section D to the
`aef5d446` version, no other line changed): Mathlib bridge Build green in workflow run 38091462366, all thirteen
declarations on [propext, Classical.choice, Quot.sound]; release gate red only on `claims`, `duplicate`,
`lean-manuscript` (by construction), `lean-axioms` PASS.

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O6-K | An infinite-order reversible datum on the chart body is not stage-preserving (F-D3 kernelized): the generator crosses stages. | CERTIFIED [K CompositionOrder.lean:378 `not_stagePreserving_of_infiniteOrderOn`, :348 `finiteOrderOn_of_stagePreserving`] | [K] | NOTES-O6 §1 |
| O6-T1 | Passive towers: with FiniteRank, passive and repeatable native observation and reversible data, every extreme point of the completed chart body is outcome-deterministic for every protocol effect; there are at most 2^d of them; every reversible datum respecting affine relations, stage-crossing or not, has finite order on the chart body; no OPS-Γ datum, no drive. On passive towers finite rank and an infinite-order datum are mutually exclusive. | CONDITIONAL ([W] for the tower step (i): Lemma P at extreme points and induction along protocols, with DRIVE §2.2's coordinatizing labels [A]; steps (ii)–(iv) [D] `extremePoints_finite_of_binary`, `finiteOrderOn_of_finite_extremePoints`, `finiteOrderOn_chartBody_of_binary`, `not_infiniteOrderOn_chartBody_of_binary`, green in run 38091462366 at dev commit c2484cca, composed with the landed `chartBody_isCompact`, `chartBody_convex` [K TransitiveBody.lean:109, :80], `preservesBody_inducedEquiv` [K CompletionAction.lean:352], `exists_return`, `exists_common_period` [K CompositionOrder.lean:149, :171]; not certified) | [W] + [D] + [K] pieces; instances [X] P1 and O5 A1 | NOTES-O6 §1 |
| O6-T2 | What the generator must do to the frame readout: an infinite-order datum on a finite-rank body forces infinitely many pure states, all but at most 2^d of them outcome-random for some protocol effect; its infinite orbits contain infinitely many outcome-random pure states; with a repeatable readout, observation is invasive at each of them. Invasive observation is necessary, not sufficient (KB-D octahedron: invasive, reversible group of order 24). | CONDITIONAL ([W]; [D] finite-order step; Γ2 [A drive] and Cartan [L] for the circle reading) | [W] + [D] + [X] K5, O3 C4 | NOTES-O6 §2 |
| O6-I | Smallest exact instance meeting all three requirements: circle substratum, half-circle readout with the cosine re-preparation law (Kochen–Specker density): response (1 + cos(u − ψ))/2 exactly; rank 3 at every stage n = 1…10 (single and two-step readouts); the rotation by a (cos a = 3/5) has infinite order (minimal polynomial 5x² − 6x + 5) and crosses stages; the readout is repeatable and invasive; the pure states ρ_{ka} are frame-random; the owner's witness is exact for the closure member R(π/2) and never for a stage datum (V_k = sin²(ka)/2 < 1/2, k ≤ 200). The sphere version: response (1 + ψ·u)/2, rank 4, OFF-Γ′ for g = R_z(a), J = R_x(π/2), m ≤ 60. | CONDITIONAL (on the re-preparing law, outside the stated access; [X] exact) | [X] K1–K7; [L] Kochen–Specker 1967 | NOTES-O6 §3 |
| O6-L | Finite rank constrains the invasive law: on the dyadic grids passive conditioning and uniform re-preparation give table ranks 3, 5, 9, 17, 33, 65 (= 2^m + 1, growing); the cosine law gives 3; at degree one, repeatability and two outcomes force the response (1 + cos β)/2; finite rank alone does not (a repeatable degree-3 response with density (3/4)cos³t ≥ 0 has rank 5). | CONDITIONAL ([X] exact; rank = number of Fourier modes on uniform grids [W]) | [X] P1, K8, K9 | NOTES-O6 §4 |
| O6-V | Verdict O6: O3-T5's three requirements are mutually exclusive on passive towers (O6-T1) and jointly satisfiable, with a repeatable readout, on an invasive re-preparing tower (O6-I); the invasive law needed is a measure-and-re-prepare law — KB-D in continuous form — whose exclusivity the stated access excludes (O5-T1a): O5 and O6 meet at one premise. | CONDITIONAL (on O6-T1, O6-I at their status); the source of the re-preparing law OPEN | as above | NOTES-O6 §0 |

**Script ledger (O6).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o6_tower.py` | `1abb0a69…bdfd1f2` | `3e8e9fbc…f680ef4` | 10/10 items True, 5 countercontrols expected-false, VERDICT EXCLUSIVE-ON-PASSIVE-JOINT-ON-INVASIVE | byte-identical |

## O7 — density at the balanced angle (round 2)

Script `experiments/o7_density.py` (decision rule in the header before run 1; no edit after writing; run 1
`VERDICT DENSE-AT-THE-BALANCED-ANGLE`, 3 countercontrols expected-false; replay byte-identical).

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O7-D1 | On three states, the kernel's balanced datum `rot(π/4)` on the overlapping pairs (0,1) and (1,2) generates a group dense in SO(3): U = R01R12 has 2 cos θ = √2 − 1/2 (minimal polynomial x² + x − 7/4), so infinite order, and R01 moves its axis off its line. | CONDITIONAL (certificate [X]; closure step [W] + [L] classification of closed subgroups of SO(3)) | [X] D1, CC2 | NOTES-O7 §1 |
| O7-D2 | The Hadamard pair H01, H12 (reflections; audit X5) has an infinite-order product (2 cos θ′ = −3/2) but both generators fix its axis: the group is infinite dihedral and its closure is the stabilizer of one vector, a proper closed subgroup (a copy of O(2)). | CONDITIONAL ([X] exact fixing; dihedral structure [W]) | [X] D2, CC1 | NOTES-O7 §2 |
| O7-D3 | With the exchanges (the six permutation matrices) both pairs generate groups whose closure is O(3). | CONDITIONAL ([X] axis moved, det −1 present; [W] + [L]) | [X] D3 | NOTES-O7 §0 |
| O7-D4 | As unitaries all these groups are real, so their closures lie in O(3), proper in U(3), and do not give dense control even up to phase; with the quarter phase on one state the closure is {U : det(U)⁴ = 1}, containing SU(3): dense control up to phase on three states, without exactness (countable group). | CONDITIONAL ([X] Ad(S0) check; [W] maximality of so(3) in su(3); [L] Cartan) | [X] D4, CC3; [K DiscreteCompletion.lean:1522, :1948] for comparison | NOTES-O7 §3 |
| O7-C | Correction of reading for O3-T7: its one-parameter-subgroup statement stands for both pairs; density at the balanced angle holds for the rotation datum (and with the exchanges for both), not for the Hadamard pair alone. O3-T7's row is not altered; this row narrows how it is read. | CONDITIONAL (on O7-D1, O7-D2) | as above | NOTES-O7 §2 |
| O7-O | At the kernel's level three (six states, o3_density E2), density of the closure in SO(6), and SU(6) with the quarter phase, is not decided here. | OPEN | method recorded | NOTES-O7 §4 |

**Script ledger (O7).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o7_density.py` | `c3968310…ac23649` | `81a8e440…f4589` | 4/4 items True, 3 countercontrols expected-false, VERDICT DENSE-AT-THE-BALANCED-ANGLE | byte-identical |

## O5-SRC — the SRC side of HO-5's joint statement (round 2)

Script `experiments/o5_src.py` (decision rule in the header before run 1; two pre-run cleanups before any run; run 1
`VERDICT SRC-KB-TOKEN-ONLY`, 2 countercontrols expected-false; replay byte-identical).

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O5-SRC1 | If KB-D were SRC's source, the premise is SRC_KB(J): all configuration permutations on a token and an exclusive KB-D frame readout. Under it J = cyc3 is available as the unique configuration permutation inducing cyc3 on the toy bit's pure states (order 3, a rotation), mapping z⁺ to the balanced pure state x⁺, with the exact witness (1, 1/2). Disguise test: the operation is monomial and passes the owner's letter; the non-classicality is carried by KB-D2, which removes the stated access's native readout (O5-T1a). | CONDITIONAL (on KB-D2, excluded on the stated access; [X] exact) | [X] S1, S2, CC1; [K KInfFoundations.lean:425, :427] | NOTES-O5 §8 |
| O5-SRC2 | Every composite of such tokens built from product registers with local readouts has \|S_CHSH\| ≤ 2 (attained), so it realizes no candidate pair cone (each contains phiW with S = 14/5, HO-3 v1): SRC via KB-D is token-only and cannot serve SPEC's target. | CONDITIONAL ([X] exact over the 16 joint configurations; HO-3 v1 items 1–2 at their labels) | [X] S3, CC2; HO-3 v1 (received) | NOTES-O5 §8 |

**Script ledger (O5-SRC).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o5_src.py` | `c7c5bfd6…f7c7908` | `96e052e7…d41683` | 3/3 items True, 2 countercontrols expected-false, VERDICT SRC-KB-TOKEN-ONLY | byte-identical |

## O7 (extension) — level three at the balanced angle (round 2)

Script `experiments/o7_level3.py`: run 1 kept as `o7_level3.run1.{py,out,err}` (its LEVEL3-PROPER verdict superseded:
the rule's inference used permutation invariance only); run 2 with the corrected method and rule fixed before it,
`VERDICT LEVEL3-DENSE`, 3 countercontrols expected-false; replay byte-identical.

| id | statement | label | evidence | where |
|---|---|---|---|---|
| O7-L3 | Supersedes O7-O. At the kernel's level three (six states), the closure of ⟨`mixImage 3 (π/4)`, permutations⟩ contains SO(6) (O(6) with odd permutations); with the single-state quarter phase it contains SU(6): the balanced fixed-gate theory has dense unitary control up to phase at level three, without exactness. The permutation-only algebra is exactly so(5) of the all-ones hyperplane; Ad(M1) completes it to so(6). | CONDITIONAL ([X] exact Lie-algebra dimensions 10 → 15 over Q(√2); [W] circle generator and so(6) maximal in su(6); [L] Cartan's closed-subgroup theorem; class membership from [K StateMixingCoupling.lean:56–59, LieRankSource.lean:209, DiscreteCompletion.lean:1926, SubstratumSource.lean:103]) | [X] L1–L4, CC1–CC3 | NOTES-O7 §6 |
| O7-L3r1 | Run 1 of `o7_level3`: measurement dim L = 10 (permutation conjugates only) correct; its LEVEL3-PROPER verdict is not supported by the method and is superseded by O7-L3. | FAILED (as a verdict; kept with its files) | `o7_level3.run1.*` | NOTES-O7 §6 |

**Script ledger (O7 extension).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o7_level3.py` (run 2) | `e8f35239…446995c` | `53c31acd…52d611e` | dim L = 10, dim L′ = 15, L4 True, 3 countercontrols expected-false, VERDICT LEVEL3-DENSE | byte-identical |
| `o7_level3.run1.py` (run 1, kept) | `3580b297…fc860c5` | `54dfe42f…88eb762` | dim L = 10; VERDICT LEVEL3-PROPER, superseded (inference outside the method) | — |

## Verdicts by node (round 2)

| node | verdict | label |
|---|---|---|
| O5 | KB-D is not sourced. It splits into an instrument (Lüders ∘ forgetful map: sourced) and an exclusivity (no passive readout of any partition: excluded on the stated access by the native readout; sharpened Lemma P with a design module). Memory bound and recorder FAILED; symplectic couplings force KB-D's form only with unknown pointer conjugates (the exclusivity relocated). If KB-D were SRC's source, SRC would be token-only: product-register composites are Bell-local. | CONDITIONAL (O5-T1, T1a [W] + [X] + [D]); FAILED (O5-a, O5-b); CONDITIONAL (O5-d, O5-SRC1, O5-SRC2); source of KB-D OPEN |
| O6 | On passive repeatable finite-rank towers every reversible datum, stage-crossing or not, has finite order: O3-T5's requirements are mutually exclusive there. On an invasive re-preparing tower (circle and sphere substrata, cosine law) they hold together with a repeatable readout, the exact witness belonging to the closure. The field-neutral Continuous Origin and the source of KB-D are one premise: an exclusive measure-and-re-prepare readout. | CERTIFIED (O6-K, F-D3 at L); CONDITIONAL (O6-T1 [W] + [D], O6-T2, O6-I, O6-L); the re-preparing law's source OPEN |
| O7 | At the balanced angle: on three states the kernel's rotation datum on overlapping pairs is dense in SO(3) (O(3) with the exchanges; containing SU(3) with the quarter phase); the Hadamard pair alone is a proper O(2); at the kernel's level three the generated group's closure contains SO(6), and SU(6) with the quarter phase — density without exactness. | CONDITIONAL (O7-D1–D4, O7-L3: [X] + [W] + [L]); O7-O superseded by O7-L3; O7-L3r1 FAILED as a verdict (kept) |
