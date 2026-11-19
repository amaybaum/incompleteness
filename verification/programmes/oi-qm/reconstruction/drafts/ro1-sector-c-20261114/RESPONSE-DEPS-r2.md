# Response to the independent review of RO1-DEPS-r2

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-DEPS-r2.md` (REVISE at `3b7d5aac`;
criteria 1, 3 and 4 MET, criterion 2 NOT MET). The changes are in `RO1-DEPS-r3.md`. `RO1-DEPS-r2.md`
is left unchanged (SHA-256 `01809afbba839b3fcc6aada8d54ddf17f6c2d463a16568659346d871f1d6545e`).

Each finding was checked at source before it was applied. Lean files were read and not built. No
finding was found to be wrong.

Unchanged, as the coordinator asked:
- the verdict UNDETERMINED;
- S6 and S7, restored;
- no claim of minimality;
- the separations between defined and executable, conditional and established, and first missing
  step and ultimate goal;
- no new premise, no computation and no manuscript edit.

## Required changes

| Finding | Check at source | Disposition | Where in r3 |
|---|---|---|---|
| **F1, track (c).** The named first step presupposes the interface, setting availability and C-1 | Confirmed. r2's own track-(c) table listed `Θ` (S8), the reading (S6), the typing (S7) and setting availability (S3) as unspecified assumptions, and recorded the dependence on C-1 | **Applied.** Track (c) is now an ordered chain: (1) C-1 resolved; (2) the two-wing interface specified (`Θ`, S7, S6, S3 and the "executes through `Obs`" criterion); (3) the bound `R*`; (4) the bound on the enlarged executable set (X4). The first open step is (2), given (1). The bound is third | §7.4; §7.6; OB-c0, OB-c1 |
| **F1, track (d).** The named first step restates INSUFFICIENT's condition | Confirmed. X-PR's interface is "specified, not derived" (SEL-EXCL-1 l. 46), and `T` writes no setting | **Applied.** INSUFFICIENT's condition is now the track's ultimate goal, not a step. The chain is: (1) a definition of "executable" (S3; RO1-SPEC-r3 S3), which is first; (2) the reading (S6); (3) a construction checked against every premise | §7.5; §7.6; OB-d1 |
| **F1, track (a).** Neither the carrier nor the typing is fixed | Confirmed (OB-T; S7) | **Applied.** The chain is: (1) the target's carrier, first; (2) the typing (S7), constrained by P-L3; (3) sourcing of (iv), given 1 and 2; (4) the co-requisites. It now says explicitly that (iv) is first *given* a carrier and a typing | §7.2; §7.6; OB-T, OB-S7, OB-a1 |
| **F1, track (b).** Name the precondition | Confirmed (#914 c.6880010243 item 4: "an independently defined reference class") | **Applied.** Step 1 is the reference class (OB-b0). Step 2 is C-1. Step 4 is the transfer of D-cone | §7.3; OB-b0 |
| **F2, X1.** P-super against P-iv and P-xiv; a non-aligned cut is not a preparation | Confirmed: P-iv is a measure on configurations (:54; :724 (iv)), and P-xiv is a distribution of `Ω` (:724 (xiv)) | **Applied.** Flagged as X1. Effect: adopting P-super would need P-iv replaced and P-xiv restated. The non-aligned-cut alternative depends on track (a)'s step 3, so OB-a3 is not an independent route. The verdict does not change | §7.7; OB-a3; P-super row |
| **F2, X2.** Track (a)'s evidence on I against track (b)'s scoped P-vii | Confirmed. OBL-RO3-2 §0 uses the posited linear rule; D-phaseQ concerns the finite-range update (:588) | **Applied.** Flagged as X2. Under the scoped reading, track (a)'s evidence on I covers the reference class only | §7.2 (Dynamics); §7.7 |
| **F2, X3.** Placement of the added operation against P-L3 | Confirmed: P-L3 (:54); "an empirical controllability resource" (:588) | **Applied.** Flagged as X3. The route is compatible with P-L3 only if the operation is typed into `Γ` or `Obs`. S7's row and OB-S7 carry the constraint | §7.7; §8.1; §8.2 S7 |
| **F2, X4.** The coverage operation enlarges what is executable under access closure | Confirmed: :582 ("non-quantum finite instrument families"); :360 (PR); #1169 c.6876591512 answer 4 | **Applied.** Flagged as X4. Tracks (a), (c) and (d) must be answered on one interface, and a coverage route that is not checked for soundness on the enlarged `Γ` does not advance SUFFICIENT. It is stated in the verdict summary, as track (c) step 4, in OB-c1 and in §5.1 | Header; §§5.1, 7.4, 7.7, 8.1 |
| **Central question.** Reuse with retention as the partial discriminator; the one-interface requirement | Confirmed. C2-structural by reversibility (:74, :80). Same-seed signalling, `b₂ = x₂` and `b₁ ⊕ b₂′ = x₂` (SEL-EXCL-1 §7, at `0ecfddeb`). The fresh-cell lemma (§3 there). "Scarcity alone is not a separator" (SEL-DISC-1 P5, l. 53) | **Applied.** A new §5.1 states the central question and its answer: limitations exclude both or neither; retention with reuse is the one partial discriminator, with its exact scope (it rejects the same-seed PR implementation only if that continuation is executable; fresh cells defeat it; it does not bear on coverage); the question moves to renewal and resources (#913, #866); and it must be answered on one interface (X4). The §5 "Repeated use" row and the closing paragraph of §5 are corrected | §5; §5.1 |

## Residues and minor findings

| Finding | Check at source | Disposition | Where in r3 |
|---|---|---|---|
| **R1.** "(iv) not supplied on F₂ under B" labelled [R, kernel] | Confirmed. The kernel states ¬`DenseUnitaryControl (permTheory (Fin 2))` (`FrozenSourcing.lean`:318–321). `DenseUnitaryControl` approximates every unitary by an available one up to a unit scalar (`DiscreteCompletion.lean`:45–48), so exact control gives dense control with `V = U`, `c = 1` | **Applied.** Marked [A-inf], with the one-step argument | §§2.5, 7.1, 7.2 |
| **R2.** "proved sufficient for coverage" | Confirmed | **Applied.** It now reads "sufficient for exact endomorphic coverage on Op, within P-CK" | §7.1 |
| **R3.** "does not constrain … reuse" too strong | Confirmed | **Applied.** Through §5.1 and the corrected §5 paragraph | §5 |
| **R4.** BH-02 is on `main` | Confirmed: `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:8 ("SUPPLIED marks a quantum ensemble, circuit or superposition chosen by the analyst") and :16 | **Applied.** Reclassified as support on main, in the P-super row and in §9 | §1.1; §9 |
| **R5.** (xiii) gives the transfer route for D-cone | Confirmed: :724 (xiii), "each `F_i` reading the current values at finitely many sites and each site read by finitely many `F_i`" | **Applied.** Named as a [P] route in D-cone, in track (b) step 4 and in OB-T. The transfer itself is not given | §§1.2, 7.3, 8.1, 10 |
| **R6.** Name the cone's kernel module | Confirmed: `QuasilocalAlgebra.lean`:1323–1328, "THE ALGEBRAIC CAUSAL CONE" | **Applied** | §1.2 (D-cone); §9 |
| **R7.** Pin RO-3's Main lines | Applied from RO-3's own citations: Main:113–127, :135–139, :141, :143, :155, :157 | **Applied** | §9 |

## Verdict

**UNDETERMINED**, unchanged. Correcting F1 changes which step is first on tracks (a), (c) and (d), not
the verdict. The four cross-track conflicts constrain routes and settling evidence. None shows
SUFFICIENT or INSUFFICIENT.
