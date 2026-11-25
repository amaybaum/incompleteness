# #1062 OBS-EMERGE: bare observer formation from native OI dynamics (paper-only assessment)

## Status, pin and sources

- **Standing.** Read-only, paper-only research record under the owner authorization quoted on #1062 (amaybaum, 2026-11-25). No file, git or GitHub writes. No computation, Lean build, probe, premise change or manuscript edit. Scratch copies of sources only.
- **Revision r2.** This revision resolves the five blocking findings R1–R5 of the independent non-author review (PR #1562 comment 7166647951), under the owner decision quoted in #1169 comment 7166845267 (2026-11-25T15:26:25Z): "#1562 | Resolve the five observer-emergence findings." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r2.md`. Text outside those findings and their propagation is unchanged from r1.
- **Revision r3.** This revision applies nits 1–3 of the independent delta review of r2 (PR #1562 comment 7167101212), under the owner decision quoted in #1169 comment 7167242160 (2026-11-25T15:41:53Z): "#1562 — Observer emergence | Apply nits 1–3." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r3.md`. All other text is unchanged from r2.
- **Revision r4.** This revision replaces the collective provenance label for the off-main reports with a per-reference trace (§8), cites `InternalObserver.lean` directly on `main`, and adds the preservation and verification status (§9), under the owner decision quoted in #1169 comment 7167657546 (2026-11-25T16:10:25Z): "#1062 | Replace the collective provenance classification with a per-reference trace." and "Both | Add the preservation rationale and remediation plan required by §A.46 item 8." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r4.md`. No result, conclusion or classification of r3 is changed. All other text is unchanged from r3.
- **Revision r5.** This revision corrects in the body the statements that the delta review of r4 found overstated, incorrect or misattributed (R6, R10, R11, §6's review status and T17), reduces G3's report of the reviewer's enumeration to what the hand argument establishes, completes the §8 trace and tightens T16's search-scope wording, under the owner decision quoted in #1169 comment {{ID:c29}} (2026-11-25T16:29:44Z): "#1062 — Observer emergence | Narrow the cycle-type result to what the hand argument establishes. Apply all four body corrections, correct the R10 labels, complete the reference trace, tighten the search-scope wording and add the superseded notice to REPORT-r3.md." "For #1062, correct the unsupported statements directly in the report. A later qualification does not repair an earlier false assertion." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r5.md`. All other text is unchanged from r4.
- **Pin.** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`. Off-main reports read: `origin/research/i1558-witten-everett-20261125` (head `f876c01b4`). Each off-main reference in this report is classified, by the claim it is attached to, in §8 (§A.42 item 8).
- **Sources read.**
  - `papers/Main.md`: §1.1–1.5, Definition, Lemmas 1–3, the status Remark, C1–C4, §3.3 causal cone, §4.5 ledger, §4.6.
  - `papers/Substratum.md`: §1–2. `papers/SM.md`: :66–70 (site factorization). `papers/Methodology.md`: §§2–4. `papers/GR.md`: :40, :603.
  - Kernel modules: `StochasticInterface.lean`, `PhysicalC4Discharge.lean` (cut realization), `ObservabilityQuotient.lean`, `EmbeddedObservation.lean`, `InternalObserver.lean` (`verification/lean-mathlib/OIBridge/InternalObserver.lean`, on `main` at the pin), `RegionTower.lean` and `QuasilocalAlgebra.lean` (causal cone); the `StochasticInterface` entry of `verification/lean-manuscript-census.json`.
  - Audit records: `verification/audits/operational/stochastic-observer-interface-audit.md`; `.../rooted-observer-family-sourcing/result.md`; `verification/audits/manuscript/round-consc-2-observation-terminology/result.md`; `verification/audits/foundations/a1-05`, `a1-06`, `a1-08`, `a1-free-p12b`.
  - Reconstruction records: `verification/programmes/oi-qm/reconstruction/` `meas-q-20261120`, `natprep-1-20261119`, `univ-1-20261119`, `measurement-record-formation/preregistration.md`, `observer-access-20261106`, `observer-interface-obsmu-20261104`; `verification/programmes/gravity/drafts/g3-w1-20261120` (labelled WIP/UNVERIFIED).
  - #1558: REPORT-r2 §§3, 5.1, 5.4, 8.3–8.4; STAGE2-REPORT-r2 §4.
  - GitHub: #1062 and its comments; #914 c.6563412926 (matrix rev 2, rows O-OBS, O-REC, O-ACC, C-8) and c.6558926162 (self-measurement candidate); #903 (LOC-1).
- **Support classes used.** KC = kernel theorem. PP = paper proof. PP-rr = paper proof in a research record on `main` with model review, not kernel-checked. EFC = exact finite check. BS = bounded search. CJ = conjecture. OP = open. PP-here = an elementary argument written in this report, model-reviewed, with no author-independent verification.

***

## 1. Record assessment

### 1.1 What is stipulated

| Item | Where | Class |
|---|---|---|
| The observer `V ⊊ S` is a datum of the triple `(S, φ, V)`, with finite capacity and coupled to `H` | Main:42 (Definition) | definition |
| "Lemma 2" restates `V ⊊ S`. It has no proof | Main:48 | definitional restatement |
| A persisting locus is an input to the successor relation, and so to `φ` itself | Main:36; Methodology:136 ("Rung 5 takes ... succession and persistence of the locus as inputs") | stipulated input |
| Site factorization: "the dynamics alone has not been shown to select the identification". Coupling-degree minimization does not select it (normal-mode counterexample) | ledger (viii), Main:736; SM:68 | posit, with a PP counterexample |
| Visible finiteness: the finite-capacity clause, "stipulated, not derived" | Main:46, :712 | stipulated |
| The selection condition: our universe is "observer-admitting", meaning C1–C4 hold "for some partition" | Main:34 | domain commitment, existential |
| "Admitted observer" = a partition satisfying C1–C4 | CONSC-2 result | terminology |
| Bounded diameter of `V` | Main §4.6 Scope (i) | assumption, "motivated" |

### 1.2 What is established, and its scope

- **The region is a parameter in the kernel.** The cut realization of the wave substratum takes the region and the prior as arguments. Its rooted maps are row-stochastic and its visible law is periodic (`latticeCut_rootedMap_stochastic_periodic`). C4 at a lattice cut is only a named residual (`LatticeCutReadback`); it is not proved. **KC.**
- **No region is selected, and no ensemble is determined.**
  - Maps out of `Substratum.Conf` exist only parameterized by a declared region; none is selected. `cutRealization` (`PhysicalC4Discharge.lean`, RD5-a) is such a map: it splits `Conf` into a declared region `Vs` and its complement. The census records the observation-map leg "by census rather than by a nonexistence claim" (`lean-manuscript-census.json`, `StochasticInterface` entry).
  - The read-write structure admits a family at every pair of states, and at two pairs at once (`readWriteFamily_exists`, `readWriteFamily_exists_two`). The witness is the constant reference coupling. These theorems concern pairs of states, not the choice of a region `V ⊂ Λ`.
  - Invariance leaves the ensemble undetermined under A5, because the zero configuration is a fixed point (`waveSubstratum_stochastic_interface_gap`).
  - Class: **KC** for these theorems and for the region entering `cutRealization` as a parameter; census for the observation-map leg. That no criterion selects a region rests on the corpus search of §1.3, a negative claim under §A.19, not on a kernel theorem.
  - The rooted audit fixes the scope: a declared observer cut does exist at the realization layer, but it is primitive/declared, not derived. Its "no observer map" gloss holds only for the reduced A1–A5 layer (`rooted-observer-family-sourcing/result.md`:158).
- **Causal cone.** A region's state after `k` steps depends only on the ball `B(V,k)` (Main §3.3, :368). The kernel proves this for an abstract update with a coupling graph: `iterate_dependsOnlyOn_ball` (`RegionTower.lean`:283), with `site_iterate_dependsOnlyOn` (:297) and `readout_unaffected_outside_ball` (:304); `heis_iterate_emb` (`QuasilocalAlgebra.lean`:1330) gives the algebraic cone for reversible dynamics of finite range. The site set and the coupling graph enter as data, so the result holds relative to (viii). **KC.**
- **Restricted access is graded.** The span of the K-horizon branch domain equals the functions that are constant on the itinerary classes `∼_K` (`branchDomain_span_eq_itineraryInvariant`), **KC**. The module's header comment lists as undecided whether the actual SM/GR cut is informationally complete (`ObservabilityQuotient.lean`:53); that is a statement of scope, not a theorem.
- **Exclusion (§4.6).** Under (EM) and `τ_mix ≪ τ_S`, no bounded-diameter partition supports (C2-slow) in the iterated coarse-grained description. **PP, conditional.** This is a necessary condition, not formation. The coverage ledger lists it as a kernel GAP (per A1-05).
- **Dynamically selected regions do exist on two native members, but they are isolated.**
  - On U₂, the class partition of `cl₂(A_0)` is invariant. Classes never merge, split or move, and each evolves alone by a periodic bijection (NP1 N3.1–N3.2). **PP-rr + EFC.**
  - Under i.i.d. noise the closure filled the whole torus in each of the 14 seeded instances checked, at the stated densities: eight at (ρ, n) = (0.06, 16) and three each at (0.02, 24) and (0.01, 32), giving one class in each. A sparse instance at ρ = 0.0005 does not fill (NP1 `RESULT.md`:359–362 [EC T2b]).
  - On the rounded rule Q, with a uniform background `c ∈ {1,…,q−2}`, support closure and class isolation hold while the inner boundary layer stays in `[c−1,c+1]` (MEAS-Q MQ2). **PP-rr + EFC**, one-tick windows.
  - Finite confined classes are periodic and erase their records (MQ4).
  - Use outside a class needs a breach (MQ3). Under full-support noise, breaching symbols destroyed the background within 20 ticks (BS).
- **Persistent moving structures exist, but none interacts.** Q has signals W1 and W2 moving at speed 1/3 along pre-laid lines, plus period-4 frozen-line memory (UNIV-1, **EFC**). No turn, gate or fan-out was found (BS). Every verified block is non-interacting.
- **Conserved structure.**
  - Linear members conserve a quadratic invariant and split energy shells into many cycles (Main ledger (v)).
  - On Q, every low-degree conserved additive quantity in the certified classes is trivial (G3-W1: WIP/UNVERIFIED, EFC within its classes).
  - Linear members are not Turing-universal (UNIV-1 Theorem L, PP-rr).

### 1.3 Negative findings (searches)

- **No manuscript claims observer emergence.** I searched `papers/`, `book/ch*`, `book/appendix*` for emerge/arise/form near "observer"; the only hit, Structure:1301, is unrelated.
- **Name collision.** `EmbeddedObservation.lean`'s "embedded observation" is an operational-theory principle (regrouping, relabelling, ambience) that is equivalent to finite QM inside OI⁺. It is not physical observer formation.
- **No dynamical criterion for selecting `V` exists anywhere in the corpus.** None states what selecting `V` from `(φ, μ or state)` would mean. Moving or derived partitions are recorded as undecided (O-RET routes SOURCES:31; #914 O-ACC row: "need not transfer to a derived or moving partition"). GR uses a time-dependent partition for black holes, but with supplied causal geometry (GR:40, :603).
- **The self-measurement label `S = (A, B, E)`** has no development. The matrix records it as "missing in all five threads".

***

## 2. Questions

### Q1. What would "emergence" of a bare observer mean, in checkable form?

**A preliminary scoping finding (G1, ELABORATING, scoping).**
- OI's foundation uses a persisting locus to introduce `φ` (Methodology rung 5; Main:36).
- So "emergence from the native dynamics" cannot be a derivation from nothing. It is a self-consistency (closure) condition: the dynamics built from a persisting locus must contain a dynamically distinguished persistent subsystem that can play that locus.
- This is a consistency-axis question (§A.23).
- Main:36 already makes the proper-part locus constitutive of the primitive, and the rooted audit classifies the cut as primitive. G1 elaborates these; it is not a new structural finding.
- Pressure test.
  - The locus enters through the successor relation (Main:36: "A successor relation uses successive moments and a locus persisting across them"; Methodology:136).
  - The record-preservation sentence is also at Main:36 ("If the dynamics preserves registered records, states differing in those records have distinct successors") and in ledger item (iii) (Main:736), where the record-preservation argument grounds injectivity. Lemma 3 (Main:54) states determinism, reversibility and the measure selection; it has no record-preservation clause.
  - Every result of Main built on `(S, φ, V)` uses a time-independent partition, as does the kernel's lattice cut (GR's black-hole partition is time-dependent, GR:40, :603): the marginalization `T_ij(t2,t1)` of §1.4 with fixed `Γ_V, Γ_H` (Main:84–90); C2 and C4 across windows; the lattice cut `cutRealization` with fixed `Vs`.
  - The closure reading therefore has a cost. A moving `V_t` meeting (E0)–(E5) below does not by itself inherit Main's fixed-partition results. #914 (O-ACC row) records that fixed-region results "need not transfer to a derived or moving partition".
  - The G1 conclusion, that emergence is posed as a self-consistency condition, does not depend on the pressure test.

**Proposed criteria.** Fix in advance:
- the native data `N`: the site set `Λ`, the alphabet, the second-order rule `φ` (ledger (xiii)) and the symmetry group `G`;
- a law `μ`: counting, or an accounted preparation;
- a horizon `K`.

A bare observer is a family `V_t ⊂ Λ` (more generally a coarse-graining `π_t`) such that:

- **(E0) Selection.** `V_t = Sel(φ, s or μ, t)` for a criterion fixed before outcomes and covariant under relabelling and `G`. The criterion must be discriminating: it is not met by every region or every orbit.
- **(E1) Carrier persistence and identity.**
  - `V_t` exists on `[0,T]` with `T ≫ τ_S`.
  - `V_{t+1}` is computed from `V_t` and the state within `B(V_t,1)`.
  - Identity is a label-free invariant (a pattern class up to `G`), not a site name.
- **(E2) Boundary.** Approximate autonomy. The self-predictive information `I(V_t; V_{t+1})` dominates the exterior contribution `L_t = I(ext_t; V_{t+1} | V_t) ≤ ε`, an individuality criterion in the sense of Krakauer et al. 2020 [background].
- **(E3) Coupling** (the Definition's clause, C1). `L_t > 0` at some accessible step. Together, (E2) and (E3) require a window `0 < L ≤ ε`.
- **(E4) Restricted access.** The `∼_K` classes are not all singletons on the support. Finiteness and the cone hold automatically for a finite region.
- **(E5) Formation, not preparation.** The structure arises with accounted, non-negligible probability under the stated law. A designed or tuned pattern is a prepared observer (PREP-REGRESS/NP1 accounting).

Exclusions: no quantum rule and no record mechanism (O-REC) may be inserted.

Scope: (E1) admits a moving `V_t`. Such a family does not by itself inherit the fixed-partition results of Main (G1 pressure test).

### Q2. Do the native dynamics admit persistent subsystems that satisfy OI's observer conditions?

**Conclusion: open. No record exhibits a native structure meeting (E0)–(E3) jointly.** The bounded facts:

- **Fixed regions.** Persistence is trivial (sites persist) and access is restricted. At a lattice cut the kernel names only C4's readback clause as an open residual (`LatticeCutReadback`, `PhysicalC4Discharge.lean`:633); it does not name C1–C3 at the cut (KC for the cut and its periodicity; C4 OP). The region is a parameter, so (E0) fails by construction.
- **Q and U₂ (G4, NEW, bounded).** Wherever state plus rule select a region, the region is exactly isolated while it is selected:
  - isolation means no coupling, so the Definition's coupling clause and C1 relative to the exterior fail;
  - finite selected regions are periodic and erase records (MQ4, N3.1);
  - in the 14 seeded instances of an untuned i.i.d. law on U₂ checked at the stated densities (§1.2), the selection returned the whole torus, so they have no proper part.

  Class: PP-rr + EFC for the cited theorems; the joint reading is PP-here. It applies only to U₂ and to Q in its confined sector with a prepared uniform background. Q's background must be prepared, so (E5) fails there too.
- **An elementary fact behind G4 (PP-here).** If `V` is exactly closed, so that `φ = φ_V × φ_H` on a product identification, then under any product preparation the visible process is a deterministic permutation and C1 fails. Exact dynamical closure therefore cannot be the selection criterion. Only approximate closure with nonzero bounded leakage can be.
- **Moving signals on Q.** They have persistence and a label-free identity, but they are non-interacting and run on pre-laid lines (EFC). Interaction with an exterior is not shown.
- **Main's selected linear model (A5).** No record studies localized persistent structures for it. CJ: localized data disperse under the linear wave rule [background, unverified]. OP.

Skepticism (§A.31): G4 is unfavourable to emergence, but it is still scoped. It does not cover other criteria, other members, or approximate-closure notions, and it is not a no-go.

### Q3. Can the dynamics select the partition, or must it be stipulated?

- **Status: stipulated in the corpus. Dynamical selection is open, not refuted.**
- **Layer 0.** Any region criterion inherits site factorization (viii), and the dynamics does not select it (SM:68, PP counterexample; #903 LOC-1, unexecuted). In the kernel, the read-write structure distinguishes no pair of states, and the region enters the cut realization only as a parameter (KC).
- **G2 (ELABORATING, PP-here): symmetry obstruction to location.**
  - Assume `φ` commutes with translations (A4, up to gauge, with a gauge-invariant criterion) and `μ` is translation-invariant (the counting measure of Lemma 3).
  - Then any criterion `Sel(φ, μ)` that is covariant under relabelling selects a union of translation orbits.
  - So the location of an observer cannot come from `(φ, μ_inv)`. It must be carried by the microstate or the preparation.
  - This ties bare formation to the measure and readiness legs O-OBSMU/O-RDY, and to the low-entropy-background issue that Substratum §2 leaves open.
- **G3 (ELABORATING, PP-here): conjugation invariance.**
  - Under the uniform prior, the visible law of `(φ, β)` for a product identification `β : S ≅ C_V × C_H` depends only on `βφβ⁻¹`.
  - So "C1, C3, C4 and C2-structural hold for some partition" over unrestricted identifications is a property of the cycle type of `φ` alone.
  - The selection condition of Main:34 therefore carries no spatial or boundary information unless the partition class is restricted (to (viii) regions of bounded diameter). That restriction is stipulated.
  - Not every non-trivial cycle type admits C4. A counterexample, by hand:
    - Let `C_V = C_H = {0,1}` and let `φ` have cycle type (2,2). Its conjugates are the three fixed-point-free involutions of the four states, that is, the three perfect matchings of `C_V × C_H`: flip `v` with `h` fixed; flip both; flip `h` with `v` fixed. In each, the next visible state is a fixed function of the present visible state. So every visible history ending in the same state induces the same next-step law, and C4 fails. C1 fails as well: no visible conditional depends on the hidden state (Main:72, which also records that C4 implies C1). This holds for every 2×2 identification, under the uniform prior and under any other preparation.
    - The review reports an exact enumeration for 2×2, 2×3 and 3×2. It is not reproduced on `main`, and no conclusion uses it.
  - If `|S|` is prime, no product identification with `|C_V|, |C_H| ≥ 2` exists. This is the absence of a product identification, not a cycle type without C4, and is not a counterexample.
  - Which cycle types admit C4 for given `(|C_V|, |C_H|)` is open.
- **Causal boundaries.** Given a seed region `V` and a window `k`, the dynamics fixes a three-way split: `V`, the boundary layer `B(V,k)∖V`, and a deep sector decoupled within `k` (KC: the Main §3.3 cone, `iterate_dependsOnlyOn_ball` and `readout_unaffected_outside_ball`). This selects the boundary given `V`, not `V` itself. The horizon partition uses supplied GR causal geometry (GR:40).
- **Conserved structures.** Linear members have a global quadratic invariant, which defines no region. On Q, no low-degree conserved additive quantity was found (G3-W1, WIP). Neither supplies a selector.
- **Mathematical existence versus physical justification.**
  - A partition satisfying C1–C4 exists for suitable `φ`. This is existential, and by G3 it is cycle-type information.
  - A dynamically selected partition (E0) has not been exhibited in any coupled form.
  - The only selections on record (classes on Q and U₂) are decoupled.

### Q4. Where does bare formation end and recording (O-REC) begin?

**G5 (PP-here, definitional): the line falls between carrier persistence and content persistence.**

- **Bare formation** requires (E0)–(E5): a selected, persistent carrier with identity and a coupled boundary.
  - The coupling clause already yields R1-type correlation (MR-1 §3.2) of `V`'s later state with some exterior property, given a preparation that puts positive mass on differing hidden states.
  - Operational C4 can then hold with only one-way exterior-to-`V` influence. A pre-sampled hidden variable revealed by the history satisfies it (Main C4, response-table construction).
- **Recording begins** at three points:
  - a designated property `P`, instead of "some" correlation;
  - R2 (persistence of that correlation under policies that do not act on its support);
  - R3 (a native readout, no private decoder).

  These concern an accessible record of a property `P` of the carrier, held in a readout `r_t = ρ(φ^t s)`. C2-structural and C4 (Main:74, :78) concern a hidden record of the visible history, read back into `V`. The two differ in direction and in where the record sits, and this report does not identify them.
- MR-1's conditions R1–R5 presuppose a given `V`, a readout `ρ` and `Acc`. So O-REC is downstream of bare formation. #914 records that bare formation has no prerequisite, that a recording observer needs O-REC, and that O-REC's prerequisite O-ACC presupposes a declared `V`.
- MQ4 shows that carriers persisting by exact closure cannot hold records beyond their period.

***

## 3. Classification table

| # | Conclusion | Support class | Conditions |
|---|---|---|---|
| 1 | `V` is a datum; locus persistence is an input to `φ` | source reading | Main:42, :36; Methodology:136 |
| 2 | Emergence well-posed only as self-consistency (G1) | PP-here (scoping) | the foundation as stated |
| 3 | Checkable criteria (E0)–(E5) | proposal (definition) | criterion fixed in advance |
| 4 | The region is a parameter of the lattice cut realization; lattice C4 open | KC / OP | wave substratum |
| 5 | Read-write structure distinguishes no pair of states; maps out of `Conf` exist only parameterized by a declared region, none selected; ensemble undetermined | KC + census; "none selected" rests on the corpus search (§1.3) | A5, alphabet > 1 |
| 6 | Site factorization not selected by the dynamics | PP (counterexample) | (viii) |
| 7 | Exact closure implies C1 fails | PP-here | product preparation |
| 8 | Selected regions on U₂ and Q are isolated, periodic, record-erasing; untuned U₂ gives one class in the 14 seeded instances at the stated densities (G4) | PP-rr + EFC; joint reading PP-here | U₂; Q confined sector, prepared background |
| 9 | Persistent moving signals on Q, non-interacting | EFC; BS for negatives | pre-laid lines |
| 10 | Location not selectable by `(φ, μ_inv)` under translation symmetry (G2) | PP-here | A4, invariant `μ`, covariant criterion |
| 11 | Existential C1–C4 selection is a cycle-type condition (G3) | PP-here | uniform prior, unrestricted identifications |
| 12 | Not every non-trivial cycle type admits C4 (2×2 with cycle type (2,2)); which types admit C4 is open | PP (independent review's hand argument, restated) / OP | given the sizes of `C_V` and `C_H` |
| 13 | Exclusion from fast-mixing regions | PP, conditional | (EM), `τ_mix ≪ τ_S`, bounded diameter |
| 14 | Coupled, dynamically selected, persistent native observer | OP | — |
| 15 | Bare/recording line at R2/R3 plus designation (G5) | PP-here (definitional) | MR-1 §3.2 |
| 16 | Localized persistent structures under linear A5 | OP (CJ: dispersion [background]) | — |

***

## 4. Earliest unsupported step

The chain (this report's construct):
- **S0:** site identification. Posited, ledger (viii).
- **S1:** a criterion by which dynamics, state or law selects `V`.
- **S2:** carrier persistence and identity.
- **S3:** a coupled boundary with `0 < L ≤ ε`.
- **S4:** restricted access.
- **S5:** formation under an untuned law.
- **S6:** recording (O-REC).

**The earliest unsupported step is S1.** Its support has two parts:
- No criterion is stated anywhere in the corpus. This is the search of §1.3, a negative claim under §A.19.
- In the kernel `V` is a parameter: maps out of `Conf` exist only parameterized by a declared region (`cutRealization`); none is selected. The census records the observation-map leg by census, not by a nonexistence theorem.

This is not a kernel result that no selection exists.

S0 is stated as a posit, so it is not "unsupported", but S1 inherits it. Where S1 has partial instances (classes on Q and U₂), they fail at S3 (isolation) and at S5 (prepared background, or one class in the 14 seeded noise instances at the stated densities).

***

## 5. Smallest discriminating next step (proposed only; needs separate authorization)

1. **Paper step, no computation.**
   - Question: on Q, can a class whose boundary breaches re-enter the MQ2 regime (re-confine), with its post-breach content depending on the exterior?
   - Such a "breach-then-reconfine" event would be the first native instance of (E0) + (E3) + (E1): a selected, persistent, intermittently coupled subsystem.
   - Attempt a proof or an obstruction from MQ1–MQ3.
2. **If the paper step is inconclusive: a bounded exact search, preregistered with the decision rule only.**
   - Use the existing MEAS-Q check infrastructure on small boxes of Q at `c ∈ {1, 2^15, q−2}`.
   - Count configurations that breach and re-confine within a horizon `K`, and measure `L` across the event.
   - Controls: (a) isolated classes give `L = 0` exactly; (b) a designed coupling gadget gives `L > 0`; (c) the U₂ countercontrol (no merges) gives no events.
   - The rule discriminates: existence of the window implies S1–S3 are instantiable on Q; absence within bounds is a bounded negative only.

***

## 6. Limitations

- **Corpus coverage.** Book chapters were grep-searched, not read in full. Some records were read at summary level: NP1, UNIV-1, MEAS-Q beyond the cited sections, the O-OBSMU analysis.
- **Model-reviewed arguments.** G1–G5 are arguments written here, reviewed by two model reviews (§9.3); no author-independent verification exists. G2 and G3 are elementary.
- **Research records used as evidence.** The records used (MEAS-Q, NP1, UNIV-1, G3-W1) are research records. G3-W1 is unreviewed. Under §A.46 item 7 they serve here only as evidence for an open-status assessment, not as premises of established claims.
- **Literature [background], not retrieved or verified:**
  - Krakauer, Bertschinger, Olbrich, Flack, Ay, "The information theory of individuality" (Theory Biosci. 2020);
  - Beer, gliders and autopoiesis in the Game of Life (Artif. Life 2004, 2014);
  - Biehl, Pollock, Kanai, a critique of Markov blankets (Entropy 2021);
  - Zanardi, "Virtual quantum subsystems" (PRL 2001), and Zanardi, Lidar, Lloyd (PRL 2004);
  - Cotler, Penington, Ranard, "Locality from the spectrum" (CMP 2019);
  - Carroll and Singh, "Quantum mereology" (PRA 2021);
  - Kolchinsky and Wolpert, "Semantic information, autonomous agency ..." (Interface Focus 2018);
  - Fredkin–Toffoli conservative logic and Margolus reversible CA.

  None is used as a premise.
- **What this report does not do.** It establishes no no-go and does not touch O-REC construction beyond locating its start.

***

## 7. Manuscript inaccuracies found (listed, not edited)

1. **Main.md:768 (§4.6, observer-selection corollary).** "Within that description, observers exist where (C1)–(C4) ... are satisfiable."
   - Read as existence, this is the converse the theorem does not supply (matrix guard Z6, "Main:758's converse").
   - Read strictly it is definitional (the CONSC-2 "admitted observer").
   - Narrower wording: "can occur only where". No mirror hit in papers or book.
2. **Substratum.md:22.** It calls the hidden sector "beyond the observer's causal reach". That conflicts with the Definition's coupling clause and C1, under which the hidden sector influences `V` (and with the §4.6 neighbourhood `Σ_loc`). GR:40 carries the same wording ("Γ_V is the region in causal reach and Γ_H its complement"), with no boundary layer; Main:26 says that degrees of freedom beyond causal reach are hidden.
3. **Main.md:48 (Lemma 2).** "This partition is not a modeling choice but the definition of embedded observation." This conflates the constitutive existence of a proper part with the choice of a particular partition, which §1.4 treats as a datum ("the choice of partition specifies the visible process"). It is also labelled a lemma without a proof.
4. **Main.md:34 (selection condition).** "Satisfies the conditions C1–C4 below for some partition": the partition class is unspecified. Over unrestricted identifications, the structural conditions depend only on the cycle type of `φ` (G3), so the condition carries no spatial content without (viii) and a locality restriction.
5. **Main §3.3 (:368).** It uses `V` for the site set, clashing with the observer `V`. This is notational.

***

## 8. Off-main references (§A.42 item 8)

Each reference this report makes to content not on `main` is classified below by reading the claim it is attached to: **provenance** (the claim does not use the referenced content), **support on `main`** (the content the claim uses is on `main` and supports the claim as it stands there), or **support off `main`** (a gap). Every check was made against `main` at the pin `e2e2a623265187a28ebec604ab8bcc672742888f`. No reference is classified support off `main`.

| # | Reference | Where cited | Claim it is attached to | Class | Check |
|---|---|---|---|---|---|
| T1 | Branch `origin/research/i1558-witten-everett-20261125`, head `f876c01b402352b05029dddbc5f47ed51b6edfc5` | Status (Pin) | That the #1558 reports were read | provenance | No conclusion in §§1–7 cites the branch or its head. |
| T2 | #1558 `REPORT-r2.md` §3 (table O1–O18 of OI definitions and results) | Sources | No conclusion | provenance | Wherever this report uses an item that table also lists (Main:36, :42, :46, :712, :736; Methodology:136), it cites that item directly from `main` at the pin, where the r1 review verified the cited lines as stated. No conclusion uses the table itself. |
| T3 | #1558 `REPORT-r2.md` §5.1 (Track 1: Witten's measurement and records compared with OI's) | Sources | No conclusion | provenance | No conclusion here concerns Witten's construction. §2 Q4 rests on MR-1 §3.1–3.2 (`measurement-record-formation/preregistration.md`) and Main:74, :78, all on `main`. |
| T4 | #1558 `REPORT-r2.md` §5.4 (observation versus knowledge) | Sources | No conclusion | provenance | This report draws no conclusion about knowledge. The access statements of §1.2 and (E4) rest on `branchDomain_span_eq_itineraryInvariant` (`ObservabilityQuotient.lean`:270, on `main`). |
| T5 | #1558 `REPORT-r2.md` §8.3 (trace of Axiom 1) | Sources | No conclusion | provenance | The locus-input and record-preservation statements of §1.1 and G1 cite Main:36, Main:736 and Methodology:136 at the pin. Main:36 and Methodology:136 carry the quoted text (checked for this trace). The delta review of r2 confirmed Main:736. No conclusion uses §8.3's trace or its conclusion. |
| T6 | #1558 `REPORT-r2.md` §8.4 (possible manuscript errors concerning CLPW) | Sources | No conclusion | provenance | The §7 candidates concern other passages (Main:768, :48, :34, :368; Substratum:22). None uses §8.4. |
| T7 | #1558 `STAGE2-REPORT-r2.md` §4 (observation versus knowledge; Wigner's friend) | Sources | No conclusion | provenance | No conclusion concerns knowing or Wigner's friend. |
| T8 | `InternalObserver.lean`, which r3 listed as read "via the #1558 report" | Sources | No conclusion | on `main` | The module is `verification/lean-mathlib/OIBridge/InternalObserver.lean` at the pin (OI-N5) and is now cited there directly. No conclusion here uses its theorems. |
| T9 | #1062 comment 7163939024 (owner authorization, amaybaum, 2026-11-25T13:33:02Z), quoted: "#1062 - OBS-EMERGE. Authorize paper-only research into bare observer formation. Keep recording-observer construction blocked on O-REC. Confirm High tier." | Status (Standing); §2 Q1 "Exclusions" | The record's authorization; the exclusion of record mechanisms from the criteria | provenance | This is governance. The O-REC exclusion fixes the report's scope and is not a scientific claim that uses the comment. The other comments on #1062 are planning records and no conclusion uses them. |
| T10 | #1169 comments 7166845267, 7167242160, 7167657546 and {{ID:c29}} (owner decisions) | Status (revision lines) | The authority for r2, r3, r4 and r5 | provenance | Owner decisions, quoted with author and time (§A.42 item 7). No scientific claim uses them. |
| T11 | PR #1562 comment 7166647951 (independent review of r1) | Revision r2 line; §2 Q3 G3 (the 2×2 counterexample and the reviewer's enumeration); §3 row 12; §9 | (a) Row 12 and the G3 counterexample; (b) the sentence noting that the review reports an enumeration; (c) the review record in §9 | provenance | (a) The hand argument is written out in full in §2 Q3 and uses only Main:72 on `main`. The comment is cited as attribution, and the claim uses nothing from it beyond that restatement. (b) The sentence states only that the review reports an enumeration and gives none of its results. No conclusion uses it, including row 12 and §9.6 row 6, and row 12 leaves the general question open. (c) This is a record of review, quoted in §9 with its verdict, poster and time. It supports no scientific claim. |
| T12 | PR #1562 comment 7167101212 (delta review of r2) | Revision r3 line; §9 | The authority for r3's nits; the review record | provenance | Same as T11 (c). |
| T13 | The independent delta review of r3 at `f89d6861f2dabe095e2d5a6836d7fd6a32188b28` (ACCEPT), PR #1562 comment {{ID:1562-r3}} | §9 | The review record | provenance | Same as T11 (c). |
| T14 | #914 comment 6563412926 (matrix rev 2), O-ACC row: "A fixed-region verdict need not transfer to a derived or moving partition (O-OBS; S4)" | §1.3 ("No dynamical criterion …") | Moving or derived partitions are recorded as undecided | provenance | The claim rests on `verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/SOURCES.md`:31, on `main`: "Moving or derived partitions remain undecided." The #914 quote is verbatim and corroborates. |
| T15 | The same O-ACC row | §2 Q1, G1 pressure test | A moving `V_t` does not by itself inherit Main's fixed-partition results | provenance | The claim rests on the analysis in the preceding bullet, on `main`: the §1.4 marginalization with fixed `Γ_V, Γ_H` (Main:84–90), C2 and C4 across windows, and `cutRealization` with fixed `Vs` (`PhysicalC4Discharge.lean`:582). The difference: #914's sentence concerns the fixed-region verdict of the O-ACC audit, and this report applies the same point to Main's results through its own analysis. |
| T16 | #914 comment 6563412926, self-measurement row (classed "a label (J7)", status "missing in all five threads"), and comment 6558926162 (the candidate) | Sources; §1.3 | The self-measurement label `S = (A, B, E)` has no development | provenance | The claim is a negative claim about the corpus (§A.19). For this trace, `papers/`, `book/` and `verification/` were searched at the pin for `(A, B, E)`, `(𝖠, 𝖡, 𝖤)`, "self-measur" and "its own sub-states". No development was found. The only "self-measurement" hits cite Breuer's 1995 bound (GR, Computation, book chapters 7 and 12, FULL), or are audit records of those passages, not the label. The matrix quote is verbatim and corroborates. |
| T17 | #914 comment 6563412926, rows O-OBS (3′) and O-REC (3), and ordering item 3 | Sources; §2 Q4 ("#914 records that bare formation has no prerequisite …") | O-REC is downstream of bare formation; what #914 records | provenance | The claim rests on MR-1 §3.1–3.2 on `main`: R1–R3 are defined for a given `V`, a readout `ρ` and `Acc`. #914 records that bare formation has no prerequisite (row 3′), that a recording observer needs O-REC (row 3′; ordering item 3), and that O-REC's prerequisite O-ACC presupposes a declared `V` (rows 1 and 3). §2 Q4 attributes to it only these statements and draws the downstream conclusion from MR-1. |
| T18 | #914 comment 6563412926, row C-8 | Sources | The §4.6 exclusion (§1.2, row 13) | provenance | The claim rests on Main §4.6 and on the A1-05 record, both on `main`. |
| T19 | #914 comment 6563412926, guard Z6 ("Main:758's converse") | §7 item 1 | Main:768 read as an existence claim | provenance | The candidate rests on reading Main §4.6 at the pin (the corollary is at line 768; the matrix's 758 is an earlier line number). The r1 review judged the candidate not an inaccuracy (§9.5). |
| T20 | #903 (LOC-1) | Sources; §2 Q3 "Layer 0" | The dynamics does not select site factorization | provenance | The claim rests on SM:68's normal-mode counterexample on `main`. #903 is an open Issue whose LOC-1 preregistration is on a draft branch and has not been executed, as the report says. |
| T21 | #1169 comment 7166418469 (owner decision, amaybaum, 2026-11-25T15:10:24Z: independent reviews are performed by Claude reviewer agents, with the stated limitation) | §9.3 | The reviewers were launched by the coordinating session that wrote the work and belong to the same model family | provenance | A governance record stating the review arrangement and its limitation. No scientific claim uses it. |
| T22 | Head commits of r1 `6e2caec0acccc4efd060d335dfd1ff3b3bc204af`, r2 `5fa09a08a54646575cdbf38435d46515a85cbb1e`, r3 `f89d6861f2dabe095e2d5a6836d7fd6a32188b28` and r4 `18867ffc17ce7f06f8c89c38c0a0914f3e9164e6` | §9.3 | Which revision each review examined; the base of r5 | provenance | No scientific claim uses them. They are on branch `research/i1062-obs-emerge-20261125` and not reachable from `main` at the pin; they become reachable from `main` only if PR #1562 lands as a merge commit, not by squash or rebase. |
| T23 | The same four commits, named in the superseded notices of `REPORT.md`, `REPORT-r2.md`, `REPORT-r3.md` and `REPORT-r4.md` | Those notices | Where each superseded revision was first recorded | provenance | Same as T22. |
| T24 | The independent delta review of r4 at `18867ffc17ce7f06f8c89c38c0a0914f3e9164e6` (REVISE) | Status (r5 line); §9.3 | The review record; the findings r5 applies | provenance | Same as T11 (c). |

The literature listed in §6 consists of external publications, not repository content. None is used as a premise.

***

## 9. Preservation and verification status (§A.46 items 4 and 8)

### 9.1 Substantive, nonredundant result

The result is open and partly negative. It is not a no-go, and it shows no observer emergence. It contains:
- a checkable statement of what bare observer emergence would mean: the closure reading (G1) and the criteria (E0)–(E5), fixed in advance as §A.29 requires;
- a scoped negative structural finding (G4, with row 7): on U₂, and on Q's confined sector with a prepared background, every dynamically selected region on record is exactly isolated while it is selected, and so fails the coupling clause;
- two obstructions: location is not selectable by `(φ, μ_inv)` under translation symmetry (G2), and existential C1–C4 selection over unrestricted identifications is cycle-type information (G3), together with the 2×2 counterexample of cycle type (2,2);
- S1 as the earliest unsupported step, with a discriminating next step (§§4–5);
- the line between bare formation and recording (G5).

No record on `main` states these (search of §1.3). #914 carries the question only as the open obligation O-OBS.

### 9.2 Scope and limits of the evidence

- The work is paper-only and pinned to `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`. This report ran no computation and no Lean build.
- Scope is stated per conclusion in §3. G4 covers U₂ and Q's confined sector only. G2 assumes A4, an invariant `μ` and a covariant criterion. G3 assumes the uniform prior and unrestricted identifications, given the sizes of `C_V` and `C_H`. Main's selected linear member (A5) is open.
- The negative claims (§1.3; S1's support; T16) rest on corpus searches at the pin. The book was searched by grep only.
- Research records serve only as evidence for open status (§A.46 item 7). Further limits are stated in §6.

### 9.3 Independent reviews

Each review was by a Claude reviewer agent with a fresh context that wrote none of the reviewed work. The reviewers were launched by the coordinating session that wrote the work and belong to the same model family (#1169 comment 7166418469). A model's acceptance is evidence of review, not independent mathematical verification, and it does not change any evidence layer (§A.46 item 8).

| Revision | Record | Posted | Verdict |
|---|---|---|---|
| r1 at `6e2caec0acccc4efd060d335dfd1ff3b3bc204af` | PR #1562 comment 7166647951 | amaybaum, 2026-11-25T15:18:58Z | REVISE: blocking R1–R5, non-blocking R6–R11, five nits |
| r2 at `5fa09a08a54646575cdbf38435d46515a85cbb1e` (delta) | PR #1562 comment 7167101212 | amaybaum, 2026-11-25T15:36:23Z | ACCEPT-WITH-NITS: R1–R5 resolved; nits 1–5 |
| r3 at `f89d6861f2dabe095e2d5a6836d7fd6a32188b28` (delta) | PR #1562 comment {{ID:1562-r3}} | {{TIME:1562-r3}} | ACCEPT |

The r4 changes were §8, this section, the r4 status line, the Pin line and the `InternalObserver.lean` source entry. The independent delta review of r4 at `18867ffc17ce7f06f8c89c38c0a0914f3e9164e6` returned REVISE. r5 applies its findings 1–3 and 5, and its finding 4 is met by the superseded notice on `REPORT-r3.md`, under the owner decision of #1169 comment {{ID:c29}}. The r5 changes go to a bounded independent review, and this section does not record its outcome. The §A.42 item 8 trace is §8.

### 9.4 Accountable Issue

#1062 (OBS-EMERGE), High tier, confirmed by the owner (T9).

### 9.5 Verification status by claim class

| Class | Conclusions | Evidence on `main` | Status |
|---|---|---|---|
| KC | Rows 4 and 5 (theorems); §1.2 cone and restricted access | The Lean modules cited, at the pin. The reviewers checked the statements, `#print axioms` and `sorry` counts. | Kernel-verified for the statements as made. The reading "none selected" (row 5) rests on the §1.3 search, which is partially verified (see 9.6, item 4). |
| Source reading, definitions, proposal | Rows 1 and 3 | The cited lines | Verified at the cited lines by the r1 review. The thresholds for (E2) and (E5) are not fixed (R8). |
| PP (manuscript) | Rows 6 and 13 | SM:68; Main §4.6 | As proved in the manuscripts. Row 13 is conditional, and its coverage entry is a kernel gap. |
| PP-rr + EFC; BS | Row 8 (the cited theorems); row 9 | MEAS-Q, NP1 and UNIV-1 with their check scripts and results | Partially verified: model-reviewed records with reproducible exact checks. G3-W1 is WIP/UNVERIFIED (exploratory). Used for open status only. |
| PP-here | Rows 2, 7, 8 (joint reading), 10, 11, 15 | The arguments in this report | Partially verified: model review only, with no author-independent mathematical or formal verification. The r1 review's verdicts: G1's conclusion holds; G2 holds; G3 holds with qualifiers; G4 holds within its scope, subject to R6 and R7; G5 partly holds (its conflation was removed in r2); the row 7 fact holds under every preparation (R7). |
| PP (review's hand argument) | Row 12, first part | §2 Q3; Main:72 | Partially verified: checked by two model reviews. |
| OP, CJ | Row 12 (second part); rows 14 and 16 | — | Open. These are stated open questions, not verification gaps. |
| Manuscript candidates | §7 items 1–5 | The cited lines | Listed, not edited. Review verdicts: items 1 and 4 are not inaccuracies; items 2, 3 and 5 are valid (mild or notational). Item 2 covers GR:40 as well (R11). |

### 9.6 Remediation plan

| # | Gap | Current evidence level | Missing verification | Accountable Issue | Evidence or decision that would resolve it |
|---|---|---|---|---|---|
| 1 | G1–G5 and the row 7 fact | Paper arguments, model-reviewed | Independent mathematical verification. For G2, G3 and the row 7 fact, a kernel proof is feasible in principle. | #1062 | An independent verification record on `main` or kernel proofs, or an owner decision that model review suffices for this record's open-status use |
| 2 | R7 (scope wording of G4's heading and of the row 7 fact) | Non-blocking review finding; the statements hold within the scope stated beside them | — | #1062 | A bounded revision, or an owner decision to leave it |
| 3 | R8, R9; nits 4–5 of the r2 delta review; the r1 review's nits on the standing line, MEAS-Q's range of `c`, the §5 breach selector and the row 6 class | Non-blocking review findings | — | #1062 | The same bounded revision, or an owner decision to leave them |
| 4 | Negative search claims (§1.3; S1's support; T16) | Author searches at the pin; book searched by grep; reviewer grep check | A reproducible search recipe with its expected result (§A.42 item 1) | #1062 | Landing that recipe and result, or an independent repeat |
| 5 | Research-record evidence: MEAS-Q, NP1 and UNIV-1 (model-reviewed); G3-W1 (WIP/UNVERIFIED) | Partially verified; exploratory | Independent verification of those records | #1062, for this report's use of them | Review of those records in their own programmes. Until then, the conclusions that use them keep open status (§A.46 item 7). |
| 6 | Row 12: which cycle types admit C4 | Open; (2,2) on 2×2 fails C4 (§2 Q3). | A proof, or a preregistered exact enumeration landed on `main` | #1062 | Separate owner authorization (no computation is authorized) |
| 7 | S1 and rows 14 and 16 | Open | Not a verification gap | #1062 | The §5 paper step, then the bounded search, each separately authorized |
| 8 | §7 candidates | Candidates | A §A.25 correction decision | #1062 | An owner decision whether to open a manuscript correction |

A remediation plan authorizes no work (§A.45 rule 3).

### 9.7 Preservation rationale

- The record is a scoped, nonredundant assessment of a High-tier obligation (#1062; #914 row O-OBS) that no other record on `main` addresses.
- Its negative findings (G4, G2, G3) close specific routes, so later work need not repeat those searches.
- Its criteria are fixed in advance for a later test.
- It locates the earliest unsupported step (S1) and keeps the review trail that corrected it.
- Preservation establishes no claim (§A.46 item 1) and raises no evidence class. Merging needs a separate recorded owner decision (§A.45 rule 7), which this section does not record.
- `REPORT.md` (r1), `REPORT-r2.md`, `REPORT-r3.md` and `REPORT-r4.md` carry superseded notices naming this revision. `REPORT-r4.md` is r5's base, and `CHANGES-r5.md` records the r5 changes.
