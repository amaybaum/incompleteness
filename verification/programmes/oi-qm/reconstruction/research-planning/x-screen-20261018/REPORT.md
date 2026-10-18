# Extension-X candidate screen against F2-reg gates G1–G8

Research only: no X adopted, no F, no status/theorem/branch change (consistency axis, §A.23). Saved by the coordinator from the screening agent's final report (the agent could not write files); text as delivered, except where S1–S3 and the source-claims list cite `op-fork/`, the OP-weak vs OP-strong fork and its independent audit.

Base main `b96662e6`; memo #859 `acfef447`; #832 `f48b11fd`, #833 `9fc5ec2e`, #836 `0e0b3ddc`, #820 `1d4606b2`, #831 `65b85147`; F2 threads H/I `804843f1`. Criteria: the memo's adopted A1 exact, B1 qubit-power registers (F2-reg), G1–G8 (§2.3), M1, applied as written. Tags: [AT] kernel on main (grep-checked), [CD] compiled design, [WA] written argument, [EC] exact computation in this screen, [EC-up] upstream exact replayed, [MP] manuscript exhaustive Python probe, [L] literature, [UP] unsourced.

Coordinator replay (2026-10-18): all five probes re-run with `python3 -I -B probes/<p>.py`, rc 0, outputs byte-identical to `runs/SHA256SUMS`. A first replay attempt used the wrong path (rc 2, file not found); its outputs are kept in `../xscreen-replay/run1-harness-error/`.

## Result: no candidate survives all eight gates

G2 blocks every candidate: each obtains coherence-level state–operation compatibility either by its own definition or by bare assertion. G4 also blocks the Γ-breakers (MI, PC: they add no operation). G3 also blocks the continuous-resource suppliers (OP, continuous reversibility, the static principles). G6 is OPEN for all; no independent prediction was found. Missing ingredient: an OI-internal, non-definitional source fixing how a native entangling bijection acts on coherence-level (off-diagonal) joint descriptions, plus a continuous phase resource that is not merely posited as available. Γ fixes every configuration-diagonal object [EC], so no principle whose content reaches only the substratum's ensemble level can pass G3.

## Intake

Rejected at intake:
- R1: E0 (a gate, flow or phase taken as premise) assumes the resource.
- R2: OI⁺-1, (b), IE1, H-OI_g/H-T and bare (T)/(T^ch) assume CNOT and continuous operations available and state-preserving.
- R3: LO and DT rename preservation.
- R4: PS, C = PSD by fiat, reachable closure define states so that preservation holds.
- R5: limit-closure of availability as a standalone X is, under strict A1, the dense endpoint relabelled, and cannot pass G4 alone (every barrier invariant is closed under limits). Kept only as a component.

Screened C1–C15:

| # | Candidate | Outcome |
|---|---|---|
| C1 | SP (Barnum–Müller–Ududec Postulate 1) | G3 FAIL [EC]; G4 FAIL |
| C2 | Self-duality / homogeneity (Jordan route) | G3 FAIL [EC]; G4 FAIL |
| C3 | Local tomography | G3 FAIL [EC]; G4 FAIL |
| C4 | No higher-order interference | G3 FAIL [WA]; G4 FAIL |
| C5 | Hardy / Masanes–Müller continuous reversibility | G4 conditional pass; G3 FAIL [EC] |
| C6 | Masanes–Müller interacting continuous pair group | G3 FAIL: Γ∘Ad_U∘Γ is an interacting continuous automorphism group of Γ(Q3) [EC] |
| C7 | OP, operational purification | survivor S1 |
| C8 | Dakić–Brukner | as C5/C6 |
| C9 | E1 / E1-L | fails G4 and M1; check B replayed byte-identically [EC-up] |
| C10 | E2 (contextual lift) | not screenable: no operation map stated |
| C11 | E4 / T, stroboscopic time on the configuration carrier | G4 FAIL [EC P4]: the Lie algebra of principal logs of all 24 native pair bijections has dimension 9 of 16 and is ones-fixing; a native local phase reaches 16 |
| C12 | E3 / E5 / E6 | fail the barrier invariants |
| C13 | PC, native-bijection preservation | G3 PASS [EC]; G4 FAIL; G2 FAIL |
| C14 | MI, measurement as interaction | survivor S2 |
| C15 | Time orientation used as preservation | G3 FAIL; spectral form OPEN [UP] |

## Survivors

### S1 — OP: operational purification (Chiribella–D'Ariano–Perinotti in OI terms)

Premise: every token state is the marginal of a pure joint description with an unobserved partner; any two such descriptions with the same marginal are related by a reversible procedure on the partner that is an automorphism of the joint cone; trivial-system clause. In the terms of `op-fork/PREREG.md` §2 this is OP-strong; the relation-only reading OP-weak drops the automorphism requirement and is insufficient alone as a standalone cone-selection condition under the tested premises (`op-fork/RESULT.md`). Motivation: OI's own thesis, that the observer's mixedness comes from incompleteness; the existence half has an in-house ingredient (Main.md:600 [MP]).

| Gate | Verdict | Evidence |
|---|---|---|
| G1 | PASS | stated without listing matrices |
| G2 | FAIL (strict) | uniqueness unsourced, and `fiber_freedom` [MP] refutes its substratum analogue; the automorphism clause is compatibility by definition, and P3 shows it alone excludes K(Z_F) |
| G3 | FAIL | Γ(Q3) satisfies OP via the native map Ad_{I⊗S̄} [EC P1] |
| G4 | PASS, conditional [WA] | transitivity on the token sphere forces a map \|+⟩ ↦ \|+i⟩, breaking NonnegBounded, the uniform ray and reality; whether OP contradicts `fiber_freedom` is OPEN. The pass rests on the automorphism clause and does not carry over to OP-weak (G4 OPEN, `op-fork/RESULT.md` gate table) |
| G5 | PASS | controls designed here |
| G6 | OPEN | no novel empirical confrontation |
| G7 | PASS | no branch, alphabet or prior parameter |
| G8 | PASS | A1/B1 fixed before screening |

Five distinctions:
- Source: partner procedures posited; cone given independently, in the domain SEP ⊆ K ⊆ maxCone.
- Preservation: definitional for the local procedures; silent on #831's readout, attach and discard fields and on CNOT.
- QM vs the partial-transpose alternative: does not separate [EC].
- M1: PASS for any conservative extension [WA]. Exact instance P5: the q = 3 leap protocol reproduces the monitored law in all 27 entries from diagonal and coherent starts; a re-randomizing readout and an inserted operation each change it (the test can fail).
- Drive: an uncountable closed local automorphism group on the preservation side. On availability it is posited, and exactness needs a closed available set. Strictly, OPEN.

Countercontrols:
- Q3 passes; Γ(Q3) passes.
- K_B fails existence: its pure states are products and B. The QM purification of diag(1/4, 3/4) is excluded by W = Γ(singlet + |00⟩⟨00|), pairing 1/4 − √3/4 [EC].
- K(Z_F) fails OP-strong uniqueness, the automorphism requirement; it satisfies relation-only uniqueness (U-weak) at every marginal (`op-fork/RESULT.md` N3). Each defect z has eigenvalues {½³, −½} and det −1/16. χ_ab = a|00⟩ + b|11⟩ lies in Q3 ∩ Z_F* for all a, b > 0, with an extremality certificate. Γ(χ_ab) has eigenvalue −ab, so a local congruence would have to map a continuum of PSD extreme rays onto at most 4 non-PSD ones [WA + EC].
- maxCone is not excluded by the stated clauses: it satisfies existence and both relation-only and automorphism uniqueness, and the trivial-system clause is not defined in the repository; its two tested readings hold for every domain cone, so neither excludes any cone [WA] (`op-fork/RESULT.md` N6, AW-OP2). maxCone fails PC [EC].
- SEP and the classical cone fail existence.

### S2 — MI: measurement as interaction

Premise: a native readout is the native read-write coupling (CNOT) to a meter in ready state |0⟩, and CNOT(ρ ⊗ |0⟩⟨0|) is a state. Motivation: OI's readout is an embedded coupling (`permClass_readWrite` [AT], `readout_is_localLuders` [AT]).

| Gate | Verdict | Evidence |
|---|---|---|
| G1 | PASS | OI terms: readout, meter, coupling |
| G2 | FAIL (borderline) | a restricted preservation clause whose Γ-breaking content is off-diagonal, which OI's diagonal-level sourcing does not reach [UP] |
| G3 | PASS | CNOT(\|+⟩\|0⟩) = Bell ∉ Γ(Q3); with \|+i⟩ the output lies outside K_B [EC] |
| G4 | FAIL | adds no operation |
| G5 | PASS | — |
| G6 | OPEN | — |
| G7 | PASS | coupling and ready state fixed by OI's read-write |
| G8 | PASS | — |

Five distinctions:
- Source: operations OI's own [AT]; state constraint [UP].
- Preservation: CNOT on product-with-ready-meter inputs only; fills no #831 primitive field fully.
- QM vs the partial-transpose alternative: separates [EC].
- M1: PASS (conservative extension) [WA, EC P5].
- Drive: none.

Insufficient alone: K(Z_F) and maxCone both satisfy MI [EC] (CNOT permutes K(Z_F)'s four defects exactly). On the domain SEP ⊆ K ⊆ maxCone, PC implies MI for every cone, since ρ ⊗ |0⟩⟨0| ∈ SEP ⊆ K [WA; EC instance in `op-fork/audit-931d5eda/AUDIT.md` F7]; maxCone satisfies MI and fails PC, so MI is strictly weaker than PC there, and adding MI to PC gives no further discrimination.

### S3 — OP-strong ⊕ PC: the strongest composite

PC: the native CNOT preserves the pair cone. OP is read as OP-strong throughout S3: L = Q3 ∩ Z_F\* and K(Z_F) satisfy OP-weak ⊕ PC (and MI, which PC implies on the domain) and are not Q3 [EC + WA, `op-fork/`].

Sufficiency [WA, unformalized]:
1. On K ⊆ maxCone, every pure product is extreme.
2. OP-strong uniqueness on pure-marginal purifications makes the closed local automorphism group transitive on the token sphere.
3. By the closed-subgroup classification (Montgomery–Samelson), that group contains SO(3), giving hA: the `rotLin` flow and `cycEquiv`.
4. PC gives hH2.
5. The adopted `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153 [AT]) then gives K = Q3. This is an implication, not an iff.

Gates: G1, G3, G5, G7, G8 PASS; G4 PASS (conditional); G6 OPEN; G2 FAIL (two compatibility clauses, one definitional — OP's automorphism clause — and one a bare assertion, PC).

Drop-one controls, both exact:
- Drop PC: Γ(Q3) remains [EC].
- Drop OP: K(Z_F) remains. It satisfies PC [EC] but fails OP-strong uniqueness [WA + EC] and the flow (#820's −1/16 witness).
- Weaken OP to OP-weak: L and K(Z_F) remain [EC + WA, `op-fork/`].

What it establishes: at most CONDITIONAL(OP-strong, PC); compatibility stays unsourced (G2 FAIL). The availability side of A1 is still OPEN.

Pressure test (§A.31): the favourable reading "OP sources hA" reduces to "transitive local maps + LO for them"; downgraded accordingly.

## Decisive countercontrols

All exact, replayed twice byte-identical, rc 0, no disk failures.
- P1 (22 checks): Γ is an involutive, trace-preserving, self-adjoint Hilbert–Schmidt isometry; it fixes all diagonal matrix units and satisfies the symbolic local-covariance identity; it transports SP frames, OP and an interacting continuous automorphism group. Only the native CNOT separates: Γ(CNOT Γ(B) CNOT) has eigenvalues {½³, −½}. Mutations: S in place of S̄ fails; a local U stays product; with the full transpose in place of Γ, Bell stays included.
- P2: main finding, exactly 8 of 24 native permutations preserve Γ(Q3), namely the local/swap subgroup (CP or co-CP certificates); the 16 entangling permutations fail, each with a rank-one witness. Positive controls: Q3 and the classical cone are preserved by all 24. Refutation-path controls: with Γ replaced by the identity or the full transpose, all 24 preserve. MI separates Q3 from Γ(Q3) and from K_B.
- P3 (27 certificates): the fixture tables above. The decisive new fact: K(Z_F) satisfies relation-only (weak) uniqueness at its I/2 pair via Ad_u∘T, which sends χ_ab to a matrix with det −(ab)⁴ < 0, so it is not an automorphism. OP's exclusion power on K(Z_F) lies entirely in its compatibility clause.
- P4: dimension 9, ones-fixing; the other log branch gives a different flow but the same algebra, so G7 bears on the flow statement, not this verdict.
- P5: as under S1's M1 distinction.
- Replays: #859 Fact B green; check B byte-identical to upstream digest `634e1639…`.

## Recommended next investigation: the OP-weak vs OP-strong fork

On the domain SEP ⊆ K ⊆ maxCone with the retained premises: does relation-only purification uniqueness exclude every cone other than Q3 and Γ(Q3)?

Preregistered rule:
- Keep OP if a written argument shows OP-weak ⇒ OP-strong; then attempt to source OP from the lifted substratum purification (Main.md:602's open lift), with `fiber_freedom` as the kill test.
- Retire OP as an X component if an exact domain cone other than Q3 or Γ(Q3) satisfies OP-weak and existence at every marginal. A closed route is progress (§A.29).

First node already computed: K(Z_F) satisfies OP-weak at its I/2 pair [EC]. Remaining: its full pure-state classification, and existence at non-diagonal marginals.

## Assumption-watch markers

- AW-X1 (NEW): every literature reconstruction screened takes state–operation compatibility from the definition of an operational theory (composition closure), exactly what OI's X-4 forbids obtaining by definition. Bears on #832, #836.
- AW-X2 (NEW): Γ is invisible to any configuration- or ensemble-level source [EC], so G3 content must be coherence-level, which the substratum does not source.
- AW-X3: on a closed cone, the pair theorem's hA weakens to local transitivity on the token sphere [WA].
- AW-X4: exactness is asymmetric — closure is free for preservation, but countability theorems [AT] block it for availability.
- AW-X5: the stroboscopic-time algebra is branch-independent and ones-fixing.
- AW-X6: `fiber_freedom` [MP] threatens any substratum-sourced OP uniqueness.
- AW-X7: K(Z_F) is Q3 ∩ Z_F* plus Γ-images of four entangled stabilizer projectors that CNOT permutes, which explains PC-pass/flow-fail. This screen gives an exact certificate for its CNOT invariance; its historical status is unchanged.

## Gate ambiguities (screened strictly)

- A1 vs limit closure: treated as the dense endpoint relabelled; not admitted.
- G2 vs the GPT convention that a local operation acts on every composite: treated as "defined so that preservation holds".
- G3's "fixed identification": read as the native CNOT and native local maps fixed. Native product tests and local permutations are Γ-compatible [EC], so only entangling native operations can separate.

## Status of source claims relied on

- [AT] (grep-checked at `b96662e6`): `pairCone_eq_Q3_of_drive_maxCone`, `driveInvariant_of_eq_Q3`, `pairCone_eq_Q3_iff_drive_maxCone`, `obsTheory_nonnegBounded`, `permClass_readWrite`, `readout_is_localLuders`, `dict_cnot`, `Q3_cnot`, `finite_protocol_spectator` (availability conditional on balanced-circuit membership, not in permClass), `onesTheory_not_qm`, `countable_not_pairFlowSourced`, `mixTheoryR_not_qm`, `fixedGateTheory_not_qm`, `sourcedOI_qm_iff_phaseFree`, `permTheory_not_phaseFree`, `typed_determined_iff`, `instAvail_fullClass_of_krausFamily`.
- [CD], not re-run: #829, #831.
- [EC-up]/[WA], not re-run: the #820 witnesses; the #832 results.
- [UP]: #833, #836 (planning only).
- [MP]: Main.md:600, `fiber_freedom`.
- This screen's new arguments: OP-strong ⊕ PC ⇒ Q3, OP-strong ⇒ local SO(3), and the fixture failures are [WA] with [EC] certificates; none is formalized.

## Boundaries

Nothing pushed or dispatched; no PR, comment or status changed; no branch or worktree touched, nor #829's candidate F. The only repository operation was a read-only `git fetch` of seven branches, read with `git show`. Writes only inside xscreen.
