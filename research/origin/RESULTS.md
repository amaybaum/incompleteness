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
