**Superseded; kept as history.** This file is revision r2 of the #1062 OBS-EMERGE report, first recorded at commit `5fa09a08a54646575cdbf38435d46515a85cbb1e`. It is superseded, and the text below this notice is kept unchanged as research history. Its conclusions are not current and are not to be cited as results: later revisions corrected parts of it. The authoritative revision is `REPORT-r4.md` in this directory, and its correction record is `CHANGES-r4.md`. `CHANGES-r3.md` records the correction from r2 to r3.

# #1062 OBS-EMERGE: bare observer formation from native OI dynamics (paper-only assessment)

## Status, pin and sources

- **Standing.** Read-only, paper-only research record under the owner authorization quoted on #1062 (amaybaum, 2026-11-25). No file, git or GitHub writes. No computation, Lean build, probe, premise change or manuscript edit. Scratch copies of sources only.
- **Revision r2.** This revision resolves the five blocking findings R1–R5 of the independent non-author review (PR #1562 comment 7166647951), under the owner decision quoted in #1169 comment 7166845267 (2026-11-25T15:26:25Z): "#1562 | Resolve the five observer-emergence findings." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r2.md`. Text outside those findings and their propagation is unchanged from r1.
- **Pin.** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`. Off-main reports read: `origin/research/i1558-witten-everett-20261125` (head `f876c01b4`). They are cited as provenance only (§A.42 item 8).
- **Sources read.**
  - `papers/Main.md`: §1.1–1.5, Definition, Lemmas 1–3, the status Remark, C1–C4, §3.3 causal cone, §4.5 ledger, §4.6.
  - `papers/Substratum.md`: §1–2. `papers/SM.md`: :66–70 (site factorization). `papers/Methodology.md`: §§2–4. `papers/GR.md`: :40, :603.
  - Kernel modules: `StochasticInterface.lean`, `PhysicalC4Discharge.lean` (cut realization), `ObservabilityQuotient.lean`, `EmbeddedObservation.lean`, `InternalObserver.lean` (via the #1558 report), `RegionTower.lean` and `QuasilocalAlgebra.lean` (causal cone); the `StochasticInterface` entry of `verification/lean-manuscript-census.json`.
  - Audit records: `verification/audits/operational/stochastic-observer-interface-audit.md`; `.../rooted-observer-family-sourcing/result.md`; `verification/audits/manuscript/round-consc-2-observation-terminology/result.md`; `verification/audits/foundations/a1-05`, `a1-06`, `a1-08`, `a1-free-p12b`.
  - Reconstruction records: `verification/programmes/oi-qm/reconstruction/` `meas-q-20261120`, `natprep-1-20261119`, `univ-1-20261119`, `measurement-record-formation/preregistration.md`, `observer-access-20261106`, `observer-interface-obsmu-20261104`; `verification/programmes/gravity/drafts/g3-w1-20261120` (labelled WIP/UNVERIFIED).
  - #1558: REPORT-r2 §§3, 5.1, 5.4, 8.3–8.4; STAGE2-REPORT-r2 §4.
  - GitHub: #1062 and its comments; #914 c.6563412926 (matrix rev 2, rows O-OBS, O-REC, O-ACC, C-8) and c.6558926162 (self-measurement candidate); #903 (LOC-1).
- **Support classes used.** KC = kernel theorem. PP = paper proof. PP-rr = paper proof in a research record on `main` with model review, not kernel-checked. EFC = exact finite check. BS = bounded search. CJ = conjecture. OP = open. PP-here = an elementary argument written in this report, not reviewed.

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
- **Restricted access is graded.** The span of the K-horizon branch domain equals the functions that are constant on the itinerary classes `∼_K` (`branchDomain_span_eq_itineraryInvariant`). Whether a physical cut is informationally complete is explicitly undecided. **KC.**
- **Exclusion (§4.6).** Under (EM) and `τ_mix ≪ τ_S`, no bounded-diameter partition supports (C2-slow) in the iterated coarse-grained description. **PP, conditional.** This is a necessary condition, not formation. The coverage ledger lists it as a kernel GAP (per A1-05).
- **Dynamically selected regions do exist on two native members, but they are isolated.**
  - On U₂, the class partition of `cl₂(A_0)` is invariant. Classes never merge, split or move, and each evolves alone by a periodic bijection (NP1 N3.1–N3.2). **PP-rr + EFC.**
  - Under i.i.d. noise the closure filled the whole torus in every checked instance, giving one class (NP1 [EC T2b]).
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
  - Every result built on `(S, φ, V)` uses a time-independent partition: the marginalization `T_ij(t2,t1)` of §1.4 with fixed `Γ_V, Γ_H` (Main:84–90); C2 and C4 across windows; the lattice cut `cutRealization` with fixed `Vs`.
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

- **Fixed regions.** Persistence is trivial (sites persist) and access is restricted. C1–C4 at a lattice cut are a named open residual (KC for the cut and its periodicity; C4 OP). The region is a parameter, so (E0) fails by construction.
- **Q and U₂ (G4, NEW, bounded).** Wherever state plus rule select a region, the region is exactly isolated while it is selected:
  - isolation means no coupling, so the Definition's coupling clause and C1 relative to the exterior fail;
  - finite selected regions are periodic and erase records (MQ4, N3.1);
  - under an untuned i.i.d. law on U₂ the selection returned the whole torus, so there is no proper part.

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
  - Not every non-trivial cycle type admits C4. Counterexamples, by hand:
    - If `|S|` is prime, no product identification with `|C_V|, |C_H| ≥ 2` exists.
    - Let `C_V = C_H = {0,1}` and let `φ` have cycle type (2,2). Its conjugates are the three fixed-point-free involutions of the four states, that is, the three perfect matchings of `C_V × C_H`: flip `v` with `h` fixed; flip both; flip `h` with `v` fixed. In each, the next visible state is a fixed function of the present visible state. So every visible history ending in the same state induces the same next-step law, and C4 fails. C1 fails as well: no visible conditional depends on the hidden state (Main:72, which also records that C4 implies C1). This holds for every 2×2 identification, under the uniform prior and under any other preparation.
    - The independent review reports an exact enumeration that agrees: for 2×2 the cycle types without C4 are exactly the identity and (2,2); for 2×3 and 3×2 only the identity. That enumeration is the reviewer's check and is not reproduced here.
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
- MR-1's conditions R1–R5 presuppose a given `V`, a readout `ρ` and `Acc`. So O-REC is downstream of bare formation, as #914 records.
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
| 8 | Selected regions on U₂ and Q are isolated, periodic, record-erasing; untuned U₂ gives one class (G4) | PP-rr + EFC; joint reading PP-here | U₂; Q confined sector, prepared background |
| 9 | Persistent moving signals on Q, non-interacting | EFC; BS for negatives | pre-laid lines |
| 10 | Location not selectable by `(φ, μ_inv)` under translation symmetry (G2) | PP-here | A4, invariant `μ`, covariant criterion |
| 11 | Existential C1–C4 selection is a cycle-type condition (G3) | PP-here | uniform prior, unrestricted identifications |
| 12 | Not every non-trivial cycle type admits C4 (prime number of states; 2×2 with cycle type (2,2)); which types admit C4 is open | PP-here (hand argument) / OP | given the sizes of `C_V` and `C_H` |
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

S0 is stated as a posit, so it is not "unsupported", but S1 inherits it. Where S1 has partial instances (classes on Q and U₂), they fail at S3 (isolation) and at S5 (prepared background, or one class under noise).

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
- **Unreviewed arguments.** G1–G5 are unreviewed arguments written here. G2 and G3 are elementary but not checked by a non-author.
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
2. **Substratum.md:22.** It calls the hidden sector "beyond the observer's causal reach". That conflicts with the Definition's coupling clause and C1, under which the hidden sector influences `V` (and with the §4.6 neighbourhood `Σ_loc`). GR:40 uses the causal cut with a separate boundary layer; Main:26 says only that degrees of freedom beyond reach are hidden.
3. **Main.md:48 (Lemma 2).** "This partition is not a modeling choice but the definition of embedded observation." This conflates the constitutive existence of a proper part with the choice of a particular partition, which §1.4 treats as a datum ("the choice of partition specifies the visible process"). It is also labelled a lemma without a proof.
4. **Main.md:34 (selection condition).** "Satisfies the conditions C1–C4 below for some partition": the partition class is unspecified. Over unrestricted identifications, the structural conditions depend only on the cycle type of `φ` (G3), so the condition carries no spatial content without (viii) and a locality restriction.
5. **Main §3.3 (:368).** It uses `V` for the site set, clashing with the observer `V`. This is notational.
