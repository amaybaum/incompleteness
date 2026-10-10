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
| O1-T3 | Monomial envelope: for every class of submonomial operators (substratumClass, permClass, subclasses) every InstAvail branch commutes with Δ at every level; reachable states are diagonal; path dephasing (= fresh-record dephasing) is the identity on them; every sandwich has V = 0 for every protocol (ancilla, readout with feed-forward, coarse-graining, discard); DC is a linear subspace (dim d² + (d²−d)²), closed under mixtures and limits. | CONDITIONAL ([W] proof; branch commutation [D] pending CI, see LOG) | [K ImplementationLocality.lean:530, StructuralClosure.lean:231, SubstratumInterfaceAudit.lean:350] + [W] + [X] 60 protocols, 2304 exhaustive sandwiches, ranks 8 / 45 | NOTES-O1 §2; M3, M4a–d, M7 |
| O1-T4a | Ones-fixing is independent of mixing: all four cells populated; V = 0 exactly in the monomial cells. | CONDITIONAL ([W]; exact instances) | [X] | NOTES-O1 §3; M5a |
| O1-T4b | The landed ones-fixing architecture `onesClass` makes the conjugation by the gate flow of the site exchange at t = 1/2 (= √X: balanced, non-monomial, owner's witness exact) available in its generated theory. | CERTIFIED as a composition of landed declarations [K InstrumentRealization.lean:628 `onesClass_arch`, :833 `isometry_fixes_ones`, :508 `onesClass_gateFlow`; SubstratumSource.lean:103 `genTheory_avail_conj`; LiftAudit.lean:138 `gateFlow_half_entries`]; non-monomiality and the packaged statement CONDITIONAL ([D] pending CI) | [K] + [D] + [X] | NOTES-O1 §3; M5b–c |
| O1-T4c | The kernel's interference exposure (branches 3/2, −1/2) holds verbatim with the ones-fixing mixer √X in place of `hMat`. | CONDITIONAL ([X] exact; no kernel check) | [X] | M6 |
| O1-T4d | Correction of the rung-1 slogan: `permClass_onesFixing` + `instAvail_unitary_fixes_ones` exclude `hMat` and the quarter phase; the exclusion of every mixer from the sourced class is O1-T3 (monomiality). Non-monomiality is necessary (and with balance sufficient) for the witness; non-ones-fixing is neither. | CONDITIONAL (on O1-T2, O1-T3, O1-T4a at their status) | [K PhaseSource.lean:79, InstrumentRealization.lean:398] + [W] + [X] | NOTES-O1 §3 |
| O1-T5 | Passivity: if observe-and-forget is the identity on the reachable body, every sandwich has V = 0 whatever the mixers (drive, completion-valued operations, imported unitaries included); classical towers are passive (A5), also on the completed body; fresh-record dephasing is the identity on classical states. The Discrete witness requires invasive observation. | CONDITIONAL ([W] proof, no kernel check) | [W] + [A oistage A5] + [X] F1, F5, F9 (6336 + 6336 sandwiches; group of order 1344) | NOTES-O1 §4 |
| O1-T6 | Outcome determinism: if the extreme points give the frame readout 0/1 values, no reversible operation is a balanced pure mixer; with exchanges + passive readout + conditioning, point masses are reachable and are the extreme points. | CONDITIONAL ([W] proof, no kernel check) | [W] + [X] F2–F4, F6 | NOTES-O1 §4 |
| O1-T7a | Memory erasure fakes the witness: classical swap from (z=0, x uniform) gives 1 and 1/2 with the memory re-randomized or with the kernel recorder written into the memory; a blank-register record gives V = 0. The definition of path dephasing is load-bearing. | CONDITIONAL ([X] exact on the model) | [X] F6, F7, CCF3 | NOTES-O1 §5 |
| O1-T7b | Knowledge-balance readout (KB-D) turns the substratum swap into a balanced extreme mixer of an octahedral body and gives the exact witness; adding back the passive readout collapses it to the simplex. | CONDITIONAL (on KB-D, which is not in the stated access; [X] exact on the model) | [X] F8a–g, CCF1, CCF2; [L] Spekkens 2007 | NOTES-O1 §5 |
| O1-V | Verdict O1: within the stated access the envelope is complete on the configuration carrier (T3) and field-neutrally (T5, T6); its exact boundary is T7. | CONDITIONAL (on O1-T3, O1-T5, O1-T6 at their status) | as above | NOTES-O1 §0 |

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
| O3-T3 | Discrete ⇏ Continuous with the quarter phase only (⟨H, S⟩ and ⟨rot(π/4), S⟩ have order 24) and field-neutrally (KB-D octahedron, reversible group of order 24); the fixed-gate theory is not QM at any angle; an irrational fixed gate gives density without exactness and no exact witness. | CONDITIONAL ([X] exact; polytope ⇒ finite Aut [W]); the fixed-gate facts CERTIFIED [K DiscreteCompletion.lean:1929, 1933, 1948, 1522] | [X] C4, C5, C7 + [K] | NOTES-O3 §2 |
| O3-T4 | Lemma P: if the native readout is repeatable and passive, every pure state is outcome-deterministic for it; hence no balanced mixer and no drive through the native NOT, whatever operation data are added. Applies to every tower built by conditioning a classical substratum. | CONDITIONAL ([W] proof, no kernel check) | [W] + [X] C3a–c + [A oistage A5] | NOTES-O3 §3 |
| O3-T5 | The field-neutral Continuous Origin needs: finite rank of an infinite-substratum completion, an infinite-order stage-crossing datum with OFF (OPS-Γ), and invasive repeatable observation (Lemma P). | OPEN (all three unsourced) | [A drive F-D2, F-D3; oistage NG1, NG2; rank] + O3-T4 | NOTES-O3 §3 |
| O3-T6 | Once a drive is sourced at level one, what remains for `oiPlusMin_iff_qm` is its spectator extension to every level and the context stability of a generating class containing it; given the phase continuum this reduces to the spectator stability of one balanced mixer. | CONDITIONAL ([W]; spectator form exact [X] C6; context stability a theorem only for the monomial class [K StructuralClosure.lean:261]) | [K SubstratumInterfaceAudit.lean:654, :660; ImplementationLocality.lean:904] + [A stage 5 D5 N1c, row β] + [X] C6 | NOTES-O3 §4 |
| O3-D | Disguise test of the minimal added content: every matrix-level form known at L (layer flow, driven pair, state-mixing datum at every angle, balanced mixer by hypothesis) contains the balanced mixer in its interface; OPS-Γ passes syntactically but cannot be met through the native NOT on passive towers. | FAILED as a source (matrix forms); OPEN (OPS-Γ's source) | [K StateMixingCoupling.lean:511] + O2 G1–G4 + O3-T4 | NOTES-O3 §5 |

**Script ledger (O3).**

| script | sha256 (script) | sha256 (output) | result | replay |
|---|---|---|---|---|
| `o3_continuous.py` | `795cb274…40ffc7` | `b4e1e261…7e3cc8` | 11/11 checks, 4 countercontrols expected-false | byte-identical |
