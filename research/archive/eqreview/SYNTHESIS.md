# EQ threads A–E plus the balanced-n5 thread — combined synthesis (research-only, base `bcbc516f`)

Nothing here is adopted, frozen or governed. Nothing is kernel-checked except where a landed identifier is cited.
Thread results:

- `scratchpad/eq/{A,B,C,D,E}/RESULT.md`
- `scratchpad/bal/LEDGER.md`

My review record, with every replay and independent check: `scratchpad/eqreview/REVIEW.md`.

## 1. Status

| thread | question | headline classification | my verification |
|---|---|---|---|
| BAL | relT + frame + P± select d for a balanced NOT? | **Counterexample.** C7b at d = 7, and every d ≡ 3 mod 4. **Excluded:** d = 5 (`n5`) and d = 9. **Missing premise:** the −z corner identity | exact 33/33, 46/46, 20/20; replays identical |
| A | foundations (K∞-Stage/Seed/V4/Geom, the elementary scope) | **Theorem route:** ELEM2 + GEOM2 ⇒ relative strict convexity. GEOM2 holds in QM at every level. **Independent premises:** V4 and FiniteRank. **Equivalence:** FiniteRank ⇔ compactness (written) | replay 3/3 exact |
| B | sourcing the control gate; K∞-Act/Trans; K∞-Copy | **Counterexamples:** conditioning, a continuous interaction and role exchange each give a weaker gate (J/K flow through gC5). **Theorem route:** natural conditioning ⇒ relC, but it is relC restated. **Route to d = 3:** local SO(d) in the same connected group, via unverified literature. **Independent premises:** boundary purity and token-level K∞-Copy | replay 10/10 exact; independent 8/8 |
| C | the composite (K2) | **Theorem route:** an entangling gate or a continuous interaction, with LT and local SO(3)², gives the composite in {Q3, R_B Q3}. Continuous exchange (CX) gives exactly Q3. **Independent premises:** CX and IE₁ | replay 7/7 exact; independent 10/10 (dim V1 = 33, CX identity) |
| D | all finite dimensions (Kₙ) | **Independent premise:** a states-only subspace axiom does not lift operations; a transformation clause is needed. **Theorem route** with encode/decode. **Kernel form (Theorem A):** qubit drivability + Architecture + ContextStable + LabelInvariant ⇒ DrivesElementary everywhere. **Open:** the kinematic half | replay 6/6 exact; 15 citations verified; independent 37/37 on Theorem A's core |
| E | the converse; global consistency | **Converse:** a theorem route at qubit scope under an explicit identification. **Consistency:** no incompatible pair among landed premises. **Mis-scopes:** several, each with a QM witness. **Seams:** 12 | replay 8/8 exact; independent 10/10; 9 citations verified |

## 2. The forward route with candidate principles, as the threads leave it

1. **Elementary system (A).**
   - ELEM2: two pure states with an interior midpoint.
   - GEOM2: the face of a pair of pure states is relatively strictly convex.
   - Together these give relative strict convexity. Under TRB-1's hypotheses, boundary transitivity is relative strict
     convexity plus transitivity on pure states.
   - Still independent: V4 (seed-orbit availability; it follows from label-dual operations) and FiniteRank (it follows
     from operational compactness, which OI has not been shown to supply).
2. **Dimension (BAL, B, E).** relC's selector work splits into two independent halves:
   - the −z corner identity (CI), which the block reduction reads at RelcSelectBlock:95 → :103;
   - the parity half (TR), which only `dim_of_ctrlGate` reads, at :746.

   Two independent derivations agree on this split: BAL B4 (kernel reading plus witnesses) and EQ-B's CI ∧ TR. Each
   half alone is insufficient:
   - C7b has balance and fails CI;
   - gC5 has CI and fails balance and TR.

   Candidate sources:
   - "Natural conditioning" gives both halves, but it is relC re-expressed.
   - A continuous interaction with local SO(d) in the same connected group gives d = 3 through Krumm–Müller
     (literature, unverified).
   - Type covariance of the NOT (E, T2) replaces "identical copies' NOTs agree"; QM satisfies it, and the recorded
     non-quantum survivors violate it.
3. **Composite (C).** LT + admissible + convex + local SO(3)² (IE₁) + an entangling gate or a continuous interaction
   gives the composite in {Q3, R_B Q3}. CX removes the twist.
   - CX holds in QM for every number of copies.
   - The twist is a twist only relative to a fixed copy identification (the K∞-Copy question again).
4. **All carriers (D).** The face principle needs a transformation clause (FP-O, encode/decode). In kernel terms the
   repertoire half reduces to qubit drivability (Theorem A). The kinematic half needs systems/faces vocabulary that the
   kernel lacks.
5. **Operations (K3).** These are kernel-landed (`genTheory_qm_of_quantumArchitecture`, `typed_determined_iff`,
   `oiPlus_iff_qm`). The typed converse lacks a quantum instance (E, T3).

## 3. Convergences and tensions across threads

- **Continuous reversibility recurs.**
  - B: continuous reversibility yields K∞-Act-type data and pure-state transitivity; with local SO(d) it gives d = 3.
  - C: CX, and a continuous interaction, fix the composite.
  - A/B: boundary purity is not supplied by it. The qutrit has continuous reversibility and fails K∞-Trans.

  A single "continuous reversible dynamics with continuous exchange and local transitivity" principle is a natural
  candidate to examine next. No thread showed that it supplies boundary purity at capacity two (B's open wall).
- **Copy identification recurs** in three threads:
  - B: K∞-Copy is independent in token form;
  - C: the twist exists only relative to a fixed copy identification;
  - E: universal agreement fails in QM, while type covariance holds.

  The convergent proposal is type covariance, or type-level availability of the NOT.
- **The elementary scope converges.** A's ELEM2, E's "capacity two" and D's frame faces describe the same scope.
  - E: K∞-Trans lacks an elementary-scope note in the ROADMAP; a manuscript-side observation, not acted on.
  - A: every geometric seam presupposes that the completed body is the system's full state space. That reading is
    nowhere named (the C4 marker).
- **No contradiction was found between threads.** E's single two-qubit model satisfies the landed premises jointly.

## 4. Open walls (named)

- **K2:** C's Theorems A and B are written proofs on exact inputs. The 33-dimensional foundation is independently
  verified. They depend on Yamabe and a prior cone-uniqueness step; the matching literature is unverified.
- **Kₙ:** the kinematic half has no kernel vocabulary.
- **FiniteRank:** a compactness source is needed.
- **Boundary purity at capacity two:** B's wall.
- **Balanced dimensions:** d ≡ 1 mod 4 with d ≥ 13 (BAL).
- **Deterministic generalized port-based teleportation:** D's wall without a closure premise.
- **Literature:** unverified throughout, because egress blocked the primary sources.

## 5. Candidate formal rounds (suggestions only; any proposal returns for separate review)

Cheapest kernel items first.

| item | source | status today |
|---|---|---|
| `drivesElementary_of_qubit` | D T1 | exact at Fin 1–7; written proof uniform in the carrier |
| relC ⇔ CI ∧ TR and `blockData_of_cornerGate` | B T1/T2 | aligns with BAL B4 |
| `k1_quantum_witness` | E T1 | composable from landed lemmas |
| twist transport and `swap_not_twistedUnitary` | C T1/T7 | `transpose_not_inner` is landed |
| C7b at d = 7 as a signed-permutation gate | BAL | balance + frame + relT + P± ⇏ d ∈ {1,3} |
| `BoundaryTransitive ⇔ RelStrictConvex ∧ ExtremeTransitive` | A T2 | needs a separate witness for each direction (§A.34) |
