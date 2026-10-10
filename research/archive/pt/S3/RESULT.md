# Thread S3 — COMP-CONS: a composition principle for four-copy coherence — RESULT (stage 2; research only)

Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, read-only at `pt/base/`. Governing texts:
`PROTOCOL.md` (`239dc123…`), amendment 1 (`b41aa0e7…`), amendment 2 (`2a2f78f3…`), `PROTOCOL-STAGE2.md` (`38603692…`),
hash-verified at start and end. Nothing here is adopted, frozen or governed; no git write, CI, GitHub access,
publication or agent. There is no Lean toolchain: the Lean text in §1.7 is UNBUILT. Running record: `NOTES.md`.

Evidence levels, kept apart throughout:
- kernel: **[K]** certified at L (`file:line` under `pt/base/verification/lean-mathlib/OIBridge/`; CD =
  CompositeDimension, CI = CompositeInterface, KG = K2Guard); **[D]** kernel-checked in the design run `ff9c3a35`, not
  certified (`pt/inputs/fourcopy/`);
- **[W]** written argument;
- **[X]** exact computation in `pt/S3/`, replayed byte for byte, stated for the instance it checks (`s1`–`s5`, check
  ids as printed);
- **[L, unverified]** literature or a standard result not re-derived; **[M]** Mathlib v4.33.0 source;
- **UNBUILT** Lean text.

Notation. Tokens 0–3; grouping A = 01|23, grouping B = 02|13; pair cones `K_p ⊆ W 3`; `dualW` the Euclidean dual for
`ipW`. Four-token tables `W4 = R^{4^4}`: `prodA X Y = (X_ab Y_cd)`, `prodB L L' = (L_ac L'_bd)`, composed pairing
`<Om, Om'> = Σ Om_abcd Om'_abcd`; `min_A = cone(prodA K01 K23)`, `max_A = {Om : effA e f Om ≥ 0 ∀ e ∈ dualW K01,
f ∈ dualW K23}`, likewise for B. SEP = cone of products; `K_gen = SEP + cnot SEP` (A's native closure, C's `K_c`);
`K_gen* = dualW K_gen = maxCone ∩ cnot(maxCone)`. `E0 = E00 + E13 − E22` (C's witness), `G` the table with
`pauliW G = ψψᵀ`, `ψ = (1,−1,−1,−1)/2`; `L' = actT reflY sing4 = diag(1,−1,1,−1)`. Pair hypotheses ("the pair
hyps"): hcls ∧ hadm ∧ hcl ∧ hgate of `kt4_forward_ie1` [D].

## 0. Answer

**Target: FCC** (`FourCopyCoherent K01 K23 K02 K13`; under hadm equivalent to H = ∃ `KT4Core`, stage 1 [D + X]).
Relative to L it stays **INDEPENDENT**. The stage-1 models are unchanged. Two more are checked here: uniform `K_gen`
(C's `K_c`, recomputed) and the new uniform `K_gen*`. Both satisfy the pair hyps and fail FCC at −1 [X s2 G5, H1].

- **Label: CONDITIONAL** on **SDC, self-duality under composition**: (P3) independent preparations of the four tokens
  are states of one four-token system in either grouping (`min_A ∪ min_B ⊆ K4`); (OVL4) any two four-token states
  have nonnegative overlap for the composed pairing (`K4 ⊆ K4*`); (CSD2) every pair effect is a pair state
  (`dualW K_p ⊆ K_p`). **Sufficiency proved** [W, two lines, over the exact cross-pairing identity
  `<prodA X Y, prodB E F> = fourVal X Y E F`, X s1 B2.7]; no pair hypothesis is used.
  - **Renaming test: passed.** No clause of SDC states that one grouping's product effects are nonnegative on the
    other grouping's product states, or a restriction of that. Without CSD2 its cross-term content is state–state
    cross positivity, which is logically incomparable with FCC on admissible closed cones [X s2 G5, M1].
  - **Strength:** strictly stronger than FCC on admissible closed cones (uniform `maxCone`: FCC and CSD2 hold, and
    P3 forces two states with overlap −2 into any K4 [X s3 X1]). Relative to the pair hyps it is existentially
    equivalent to FCC [W over D, W + L, X s3 T1–T2]. Every quantum-compatible sufficient principle has that
    equivalence (§1.6), so it is not a renaming signal.
  - Each conjunct is independently motivated: the elementary ball is self-dual at L [K CD:869, 877, 916, 930, 1015,
    1590, 1679], and SDC asks that pairs and the four-token system inherit this for the composed pairing.
    **Whether OI's composition supplies SDC is UNRESOLVED**: L defines no pair and no four-token system.
- **Sufficiency proved, not a source:** C's N0 ∧ N1 ∧ N2 (stage 1; FCC renamed, per the owner); two-sided conditioning
  C1 ∧ C2 relative to the pair hyps on aligned gates [W over D, W + L, X s4], a restriction of FCC.
- **Route refuted by exact models** (each satisfies the pair hyps unless stated): ordered associativity (M_tok cones,
  −1/8 [X s1 A3]); the induced pairs of a one-grouping composite (−2 [X s1 I4]; not a pair-hyp model); every
  conjunction of chart-invariant single-pair principles (self-duality, either half, homogeneity, Jordan structure)
  without uniformity (M_tok [X s2 C1–C5]); uniformity with `K ⊆ dualW K` (uniform `K_gen`, −1) or with
  `dualW K ⊆ K` (uniform `K_gen*`, −1) [X s2]; token orientation coherence alone, equivalently all-generated
  conditioning (`K_gen`, `K_gen*`) [X s4]; one-sided conditioning C1 (`K_gen`), C2 (`K_gen*`) [X s4]; entanglement-
  swapping consistency (`K_gen*`) [X s4 S3]; four-token no-restriction with P3 (M_tok).
- **Survives the tested models; sufficiency not established (UNRESOLVED):** uniformity with full pair self-duality,
  and pair self-duality with token orientation coherence. Each is sufficient iff every self-dual, admissible, closed
  pair cone preserved by an N-CLASS gate is Q3 or twin (for `cnot` with identity locals: is Q3) — the exotic-cone gap. Lorentz-type cones are excluded exactly [W + X s5], and
  orthogonal images of Q3 up to an [L] step; no exotic cone is exhibited. Purification is also UNRESOLVED.

**Associativity versus cross-pairing.** No fixed token order makes 01|23 and 02|13 both contiguous [X s1 L2,
exhaustive]. So ordered associativity never reads `K02`, `K13` and does not imply FCC [X s1 A3]. Cross-pairing has two
parts:
- a free state-level part: both groupings' independent preparations are states;
- an effect-level part that is exactly famI ∧ famII [X s1 B2.3, B2.4].

C's N0 ∧ N1 ∧ N2 is the full step. Its effect part is COMP-1's `prodEff_effect` on the shared body.

**The owner's central question, as far as this thread reaches.** The state side of cross-pairing is free.
Preparing four tokens independently is one preparation however they are grouped. The whole constraint (FCC) sits on
the effect side, where neither associativity nor any principle about one pair at a time reaches it. The most
explanatory non-renaming principle found:
- Combined systems are systems of the same kind as the elementary ball, in that each is self-dual for the composed
  pairing.
- That state–effect duality turns the free state-level regrouping into the effect-level one.
- Relative to the pair hypotheses, its existential form is no weaker and no stronger than FCC.
- Its observer-native source is the open gap.

## 1. Routes and countermodels, node by node

### 1.1 S3.1 — the associativity / cross-pairing ladder (decisive for the owner's separation)

Fix admissible pair cones. Rungs, for a four-token cone K4 in W4 (four-copy local tomography is built into W4,
as in the package's Lemma B2; the abstract-carrier forms are in 1.3 and C's §1.A):

| rung | condition | satisfiable for every quadruple? | reads `K02`, `K13`? | evidence |
|---|---|---|---|---|
| R1 one-grouping composite | `min_A ⊆ K4 ⊆ max_A` | yes: K4 = `min_A` (`effA e f (prodA X Y) = ipW e X · ipW f Y`) | no | [X s1 B2.1] + [W] |
| R1′ ordered associativity (order 0,1,2,3) | every contiguous block cone (01, 12, 23, 012, 123, 0123) is a composite of each contiguous binary split | yes (minimal composites at every block; for Q3 pairs also the quantum chain, PSD at every block, Kronecker products of PSD being PSD [M Analysis/Matrix/Order.lean:213]) | no | [W] |
| R2 state-level cross-pairing | `min_A ∪ min_B ⊆ K4` | yes: K4 = `cone(min_A ∪ min_B)` | yes, no constraint | [W] |
| R3 effect-level cross-pairing | `K4 ⊆ max_A ∩ max_B` | yes alone (K4 = {0}) | yes | [W] |
| R2 ∧ R3 (cross-pairing consistency) | one K4 is a composite in both groupings | iff FCC | — | below |

Verdicts, each direction with its own witness (§A.34):
1. **No linear order supplies cross-pairing** [X s1 L1–L2, exhaustive over 24 orders]. Each order makes exactly one
   pairing contiguous, and none makes both A and B contiguous. Ordered associativity is therefore blind to the
   pairs 02 and 13. Exact model: the M_tok cones (Q3, Q3, Q3, twin), aligned gates (cnot, cnot, cnot, cnotTw), with
   the quantum chain as the ordered-associative structure. All pair hyps hold, and FCC fails at
   `fourVal phiW phiW (phiW/4) (L'/4) = −1/8` [X s1 A2–A3; countercontrol A3c gives +1/4]. **Route refuted:**
   "ordered associativity + pair hyps ⇒ FCC".
2. **What associativity implies about pair 02.** An A-composite induces an admissible pair on 02 and on 13:
   - the 02-marginal of `prodA X Y` is `(X_a0 Y_c0)`, a product of token marginals [X s1 I1; countercontrol I1c];
   - the induced 02 state cone of `min_A(Q3, Q3)` is SEP, with effects `maxCone` [W].

   The induced pairs need not compose. The B-product of the induced effects `idW`, `sing4` (both in `maxCone`
   [X s1 I2, I3]) takes `fourVal phiW phiW idW sing4 = −2` at an A-product state [X s1 I4; countercontrol I4c]. The
   failure is on the effect side. With K4 = PSD16 the induced pairs compose. So the property belongs to K4, not to
   associativity. (This model is not a pair-hyp model: SEP fails hgate. It shows only that associativity plus
   induced subsystems does not give cross-pairing.)
3. **Cross-pairing consistency ⟺ FCC** (Lemma B2).
   - (⇒) `effB E F (prodA X Y) = fourVal X Y E F` and `effA e f (prodB L L') = g2 e f L L'` [X s1 B2.3, B2.4]. If
     K4 contains both products and the four-token effects are nonnegative on K4, famI and famII hold.
   - (⇐) K4 := {Om : all `effA`, `effB` of dual factors ≥ 0} contains both products, by B2.1, B2.2 and FCC through
     B2.3, B2.4 [W s1 B2.W]. This is the package's `exists_kt4Cone_of_fourCopyCoherent` [D statement].

   Its four sub-identities (`effA_prodA`, `effB_prodB`, `effB_prodA`, `effA_prodB`) are `sorry` in
   `FourCopyPackage` A.2. Here they are exact symbolic identities [X], not kernel proofs.
4. **The precise content of the cross-pairing step.** Given R1 (or R1′), the passage to R2 ∧ R3 adds exactly the two
   inclusions `min_A ⊆ max_B` (famI) and `min_B ⊆ max_A` (famII). R2 is free. **All of the constraint is R3 given
   R2.**
5. **The minimal extra structure to state it.** A token identification across groupings is needed: the exchange
   σ12 of tokens 1 and 2, natural on products (`σ12 (prodA L L') = prodB L L'` [X s1 B2.8; countercontrol B2.8c]).
   Equivalently, in the cyclic order 0-1-3-2 both groupings are non-crossing matchings and 03|12 is the crossing
   one [X s1 L3–L6]. The four KT4 pairs are the edges of the cycle 0-1-3-2-0, and the one-click rotation of that
   cycle maps A onto B [X s1 L5, L6]. EvenCycle is the Z₂ holonomy around this same cycle (1.4).
6. **Where N0, N1, N2 sit** (C, audited; abstract carrier).

   | conjunction | rung, in carrier terms | satisfiable for every quadruple? | model |
   |---|---|---|---|
   | N0 alone | R1 for each grouping, with separate bodies | yes | — |
   | N0 ∧ N1 | one body, no token identification | yes, vacuous | the anchor sum |
   | N0 ∧ N2 | token identification, separate bodies | yes, vacuous | SEPH |
   | N0 ∧ N1 ∧ N2 | R2 ∧ R3 | ⟺ FCC under hadm | each direction witnessed by C: B1 [D] + A2; MSIG [X + W] |

   The effect-level part R3 is N0's COMP-1 field `prodEff_effect` [K CI:228] applied to the shared body. That field
   is the cross clause, which is why the owner reads N0 ∧ N1 ∧ N2 as FCC renamed.

### 1.2 S3.2(a) — pair-level structural principles

1. **Single-pair chart obstruction** (exact obstruction for a class) [X s2 C1–C5 + W].
   - `actT reflY` is an ipW-orthogonal involution [C1]. It maps products to products [C2] and `maxCone` onto
     `maxCone` [C3]. It conjugates `cnot` to the N-CLASS gate `cnotTw` with locals (I, reflY, I, reflY) [C4], and
     carries `dualW Q3` onto `dualW twin` [C5].
   - So every predicate of one pair's data (cone, gate and locals) that is invariant under this transport holds at
     `(twin, cnotTw, …)` iff it holds at `(Q3, cnot, I, …)`.
   - Such predicates include self-duality and each half of it, homogeneity, symmetric-cone (Jordan / Koecher–Vinberg)
     structure, closedness, admissibility and gate invariance.
   - Every conjunction of such predicates therefore holds on M_tok whenever it holds on the quantum data, and FCC
     fails on M_tok. **Route refuted** for all of them without uniformity.
   - This complements the narrowed B3, which stays exactly as AUDIT-C records it: B3 holds for chart-invariant
     conditions on the cones and gate *maps* of at most three of the four pairs; it does not hold, as stated, for
     conditions that may read the supplied locals. A single pair's locals carry no cross-pair information, so the
     one-pair obstruction may read them.
2. **With uniformity, each half of self-duality is refuted.**
   - `K ⊆ dualW K`: uniform `K_gen`. All pair hyps hold (A, C, audited). `K_gen ⊆ Q3 = dualW Q3 ⊆ dualW K_gen`
     [X s2 D1–D4 + W, with PSD self-duality [K JordanClassification.lean:84]]. FCC fails:
     `fourVal phiW phiW E0 G = −1`, with `E0 ∈ dualW K_gen` [X s2 G1–G3, Lagrange] and
     `G ∈ Q3 ⊆ dualW K_gen` [G4, G5; countercontrol G5c].
   - `dualW K ⊆ K`: **uniform `K_gen*`, a new foil from above.**
     - It is a closed convex cone containing Q3, lying in `maxCone` and `cnot`-invariant [W s2 H.W, D2]. So it
       satisfies hcls, hadm, hcl and hgate.
     - `dualW K_gen* = closure K_gen ⊆ Q3 ⊆ K_gen*`.
     - FCC fails: `fourVal E0 G phiW phiW = −1`, with E0 and G as *states* and `phiW = cnot(prodState xplus z3)`
       as effects [X s2 H1, H2; countercontrol H1c].
     - IE1 fails by an octahedral witness [X s2 H3, H4; countercontrol H4c].
3. **Full self-duality with uniformity: UNRESOLVED (the exotic-cone gap).**
   - By the theorem [D] and the classification [W + L], "uniform + `K = dualW K` + pair hyps ⇒ FCC" holds iff every
     self-dual, admissible, closed, N-CLASS-gate-invariant cone is Q3 or twin. The same gap governs "pair
     self-duality + token orientation coherence" (1.4) and "pair self-duality + all-generated conditioning".
   - Partial exact results [s5]:
     - (a) No ipW-self-dual cone linearly isomorphic to a Lorentz (spin-factor) cone contains SEP. The averaging
       identity (36 axis products of norm 2 average to E00) contradicts the 45° aperture [X A1, A2; countercontrol
       A2c; W LOR.W with a standard fact on Aut(L)].
     - (b) An ipW-orthogonal Ψ with `SEP ⊆ Ψ(Q3)` fixes E00 and sends pure products to rank-one states [X A1–A4;
       countercontrol A3c; W ORTH.W]. That only Q3 and twin arise this way rests on a Wigner-type classification
       [L, unverified].
     - (c) Reducible self-dual cones are not settled.
   - An equivariant Barker–Foran extension would produce an exotic `cnot`-invariant self-dual cone containing
     `cone(K_gen ∪ {E0})`. That theorem is [L, unverified]: the symmetrized step can stall, s5 BF.W. No label rests
     on it.
4. **What pair-level principles can do, and their residue.** Under the pair hyps on {Q3, twin}⁴ the twist bits equal
   the gate orientation bits (AUDIT-C, [W + X]), and FCC holds exactly at the 8 coboundary patterns (C B2). A pair
   principle can at most restrict each cone to {Q3, twin}, which is not established for self-duality (item 3). The
   residue is then the parity: a 4-pair Z₂ holonomy that no one-pair principle sees (item 1) and no three-pair cone
   or gate-map principle sees (narrowed B3).

### 1.3 S3.2(a′) — self-duality under composition (the source found)

**Statement** (W4 form). There is a four-token cone K4 with the three conjuncts of §0: P3, OVL4 and CSD2. With full
self-duality at every level (SD2: `K_p = dualW K_p`; SD4: `K4 = K4*`) this is the natural principle: **every system
is self-dual for the composed pairing**. Only the halves CSD2 and OVL4 are consumed.

**Derivation of FCC** [W, exact ingredient X s1 B2.7]:
- famI: let `X ∈ K01`, `Y ∈ K23`, `E ∈ dualW K02 ⊆ K02` and `F ∈ dualW K13 ⊆ K13` (CSD2). Then `prodA X Y` and
  `prodB E F` lie in K4 (P3), so `fourVal X Y E F = <prodA X Y, prodB E F> ≥ 0` (OVL4).
- famII is the same with `<prodA e f, prodB L L'> = g2 e f L L'`.

No hadm, gate, closedness or operation is used.

**Satisfiability with FCC.**
- Uniform Q3: K4 = PSD16.
  - `pauli4(prodA X Y) = pauliW X ⊗ pauliW Y` and `pauli4(prodB L L') = Π(pauliW L ⊗ pauliW L')Πᵀ`
    [X s3 Q2, Q3; countercontrol Q3c].
  - The W4 pairing is 16 times the trace pairing [X s3 Q1 + W].
  - Kronecker products of PSD matrices are PSD [M Analysis/Matrix/Order.lean:213]. PSD self-duality is landed:
    `psd_iff_trace_nonneg` [K JordanClassification.lean:84], `psd_trace_mul_nonneg` [K OperationalRigidity.lean:917].
- Every even twist pattern τ = δε, with K4 = chart4 ε (PSD16), the partial transpose on the qubits with ε_i = 1.
  - It is orthogonal, hence self-dual.
  - It carries `prodA`/`prodB` of the charted cones [X s3 T1, T2 + W T.W].

**Each conjunct cannot be dropped** (insufficiency of the rest only, not necessity):

| dropped | model | evidence |
|---|---|---|
| OVL4 | M_tok cones; P3 and CSD2 hold; any K4 containing both groupings' products holds `prodA phiW phiW` and `prodB phiW L'`, whose overlap is −2 | [X s3 D1] |
| P3 | M_tok cones with K4 = PSD16: OVL4 and CSD2 hold; `prodB phiW L' ∉ PSD16` | [X s3 D2] |
| CSD2 | uniform `K_gen` with K4 = PSD16: P3 and OVL4 hold; `E0 ∈ dualW K_gen \ K_gen`; FCC fails at −1 | [X s3 D3; countercontrol D3c] |

**Strength.** Strictly stronger than FCC on admissible closed cones [X s3 X1 + landed F.max]. Relative to the pair
hyps the two are existentially equivalent:
- (⇒) the derivation above;
- (⇐) FCC + pair hyps ⇒ IE1 ∧ EvenCycle [D] ⇒ cones `twistQ3(τ)` with even τ [W + L, AUDIT-C] ⇒ chart4 ε (PSD16).

**Abstract-carrier form** (no four-copy local tomography, no COMP-1 effect field) [W s3 C.W; X s3 C1, C2]. Replace
P3 by:
- N1 ∧ N2 at the state level (one body containing both groupings' product states; TPS on token products);
- bi-affine product data [K CI:210];
- a multiplicative inner product on grouping A.

The cross inner product on bodies is then `fourVal`, by the token-product identity [C1] and spanning [C2, det 256].
In the place of C's route, SDC replaces N0's effect field (the cross clause) by self-duality.

**Independence assessment** (renaming test fixed in NOTES N2):

| conjunct | statement | alone | motivation | renames FCC? |
|---|---|---|---|---|
| P3 | both groupings' product states are states of one system | satisfiable for every quadruple | independent preparation is grouping-blind | no (no positivity) |
| OVL4 | `<Om, Om'> ≥ 0` on K4 | satisfiable (PSD16) | overlaps of states are probabilities; the ball has `Lor ⊆ Lor*` [K CD:877] | no (no grouping) |
| CSD2 | `dualW K_p ⊆ K_p` | satisfiable; per-pair, so it cannot exclude M_tok | every test is a state's test; the ball's effects are its states up to scale [K CD:930, CD:916, CD:1015, CD:1590] | no (one pair) |

Verdict: **sufficiency proved; independently motivated; not a restatement**. FCC is CONDITIONAL on SDC. Caveat
(recorded, not hidden): when the pairs are self-dual, OVL4 restricted to the cross products is FCC's cross clause
verbatim. SDC derives that clause from a grouping-blind property instead of positing it.

### 1.4 S3.2(b) — token-level orientation coherence

- **Statement:** each token carries one orientation bit ε_i, and each pair's gate orientation bit (a gate invariant,
  D T2) is ε_i ⊕ ε_j.
- **Equivalence with EvenCycle** [X s4 O1; countercontrol O1c]. Two directions:
  - coboundaries are even (inclusion ⊆ of O1);
  - every even pattern is a coboundary (inclusion ⊇).

  EvenCycle is part of the audited theorem's conclusion.
- **Not FCC renamed** (a Z₂ frame principle with no cone or inequality). On the classified family {Q3, twin}⁴ with
  the pair hyps it is equivalent to FCC (twist = orientation, AUDIT-C; C B2).
- **Route refuted alone:**
  - uniform `K_gen` and uniform `K_gen*` (all orientation bits false) satisfy it and fail FCC [X s2 G5, H1].
- **What it needs to apply:** a reason the cones lie in {Q3, twin}. That reason is IE1 (forbidden), or pair
  self-duality if the exotic-cone gap closes (1.2 item 3).
- **Operational form** [X s4 O2–O4, G1–G2 + W AG.W]:
  - On aligned gates, all-generated conditioning (AG: FCC with every argument a gate image of a product or a
    product) holds exactly for the even patterns.
  - AG reads only the gates. It is the operational content of orientation coherence and carries none of the IE1
    content.

### 1.5 S3.2(c, d) — conditioning, no-restriction, entanglement swapping

Slot analysis on aligned gates. Each argument of famI, famII ranges either over the full cone or full dual (F) or
over generated tables (g).

| principle | slots | M_tok | uniform `K_gen` | uniform `K_gen*` | uniform Q3 | verdict |
|---|---|---|---|---|---|---|
| AG | all g | fails (−2, G1–G2) | holds | holds | holds | = EvenCycle; refuted alone |
| C1 | states F, effects g | fails | holds [W] | fails (−1, s4 S1) | holds | refuted (`K_gen`) |
| C2 | states g, effects F | fails | fails (−1, s4 S2) | holds [W] | holds | refuted (`K_gen*`) |
| ESC | states g, measured effect g, conditioned-pair effect F | fails | fails (−1, s4 S3) | holds [W] | holds | refuted (`K_gen*`) |
| C1 ∧ C2 | both one-sided families | fails | fails | fails | holds | sufficient relative to the pair hyps, aligned gates [W over D, W + L] |
| FCC (no-restriction everywhere) | all F | fails | fails | fails | holds | target |

- **Answer to S3.2's conditioning question.**
  - An operational formulation that does not presuppose the full duals (AG) is strictly weaker than FCC. It carries
    exactly the parity.
  - One-sided no-restriction is refuted in both directions:
    - full states against generated effects excludes `K_gen*` but not `K_gen`;
    - full effects against generated states excludes `K_gen` but not `K_gen*`.
  - **Exposed hidden assumption (NEW):** the IE1 content of FCC needs no-restriction on both the state side and the
    effect side of the target pairs. The design proof reads exactly this: famI with full target states against Bell
    effects, and famII with link states against full target effects (FourCopyIE1 `cross_rel`, `inv_*`; C c4).
  - C1 ∧ C2 contains every instance the design proof reads. So relative to the pair hyps it gives IE1 [D], then the
    {Q3, twin} cones [W + L], then EvenCycle via AG ⊆ C1, then FCC (C B2).
  - C1 ∧ C2 is still a restriction of FCC's cross clause, so it is a strength result, not a source.
  - Self-duality makes C1 and C2 coincide (famI and famII exchange roles when effects are states).
- **Four-token no-restriction** (four-token effects = `K4*`) with P3 does not reach FCC. M_tok with
  `K4 = cone(min_A ∪ min_B)`, all four-token effects allowed, satisfies both and fails FCC [X s1 A3]. The
  load-bearing no-restriction is the pair-level one above.
- **Purification** (every pair state is the marginal of a pure four-token state): **UNRESOLVED**.
  - It is a state-level principle.
  - No derivation of the effect-level part from it was found.
  - No exact model of purification with marginal consistency and P3 on the M_tok or foil cones was built.

### 1.6 S3.3 — independence and obstructions

- **Classes with exact obstructions:**
  - (O1) chart-invariant single-pair principles (1.2 item 1);
  - (O2) uniform one-sided self-duality: `K_gen` against `K ⊆ K*`, `K_gen*` against `K* ⊆ K`;
  - (O3) one-sided conditioning, by the same two foils (1.5).
- **Renaming meta-obstruction** [W over D, W + L]. Let P be any principle with
  - (i) `∃Ω.P` + pair hyps ⇒ FCC, and
  - (ii) `∃Ω.P` true on every configuration whose cones are `twistQ3(τ_p)` with τ even, for any gates satisfying the
    pair hyps.

  Then, relative to the pair hyps, `∃Ω.P ⟺ FCC`: FCC + pair hyps ⇒ IE1 ∧ EvenCycle (theorem [D]) ⇒ cones
  `twistQ3(τ)`, τ even (classification [W + L], AUDIT-C) ⇒ (ii). So **equal strength relative to the pair hyps cannot
  distinguish a source from a renaming**. The renaming test must read statement content, as fixed in NOTES N2. SDC
  and N0 ∧ N1 ∧ N2 are both existentially equivalent to FCC there. Only N0 ∧ N1 ∧ N2 contains the cross clause.
- **Exposed hidden assumption in C's candidate table (row 17, symmetric monoidal composition)** [W]. In such a
  category the effect side of cross-pairing comes from one of two places:
  - the passive requirement that the four-token object is a composite in both groupings, which is N0 ∧ N1 ∧ N2,
    i.e. FCC renamed;
  - functoriality applied to the braiding: σ12 on tokens 1, 2 idly extended to tokens 0, 3 is a state map, i.e. an
    operation on part of a larger composite ((o)-type, forbidden as a premise).

  Either way it is not a non-renaming, non-forbidden source.

### 1.7 UNBUILT Lean statement (design only; not compiled; not a kernel proof)

```lean
-- UNBUILT. Names follow the design modules at ff9c3a35 (FourCopyPackage W4, prodA, prodB).
def ip4 (Ω Ω' : W4) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, Ω a b c d * Ω' a b c d

structure SDC (K01 K23 K02 K13 : Set (W 3)) (K4 : Set W4) : Prop where
  prodA_mem : ∀ X ∈ K01, ∀ Y ∈ K23, prodA X Y ∈ K4          -- P3
  prodB_mem : ∀ L ∈ K02, ∀ L' ∈ K13, prodB L L' ∈ K4        -- P3
  ovl : ∀ Ω ∈ K4, ∀ Ω' ∈ K4, 0 ≤ ip4 Ω Ω'                     -- OVL4
  csd01 : dualW K01 ⊆ K01  -- CSD2, and likewise csd23, csd02, csd13

-- needs: ip4 (prodA X Y) (prodB E F) = fourVal X Y E F  (exact identity, s1 B2.7)
theorem fourCopyCoherent_of_sdc (h : SDC K01 K23 K02 K13 K4) : FourCopyCoherent K01 K23 K02 K13 := sorry
```

## 2. The ledger (certified versus added)

| premise | used by | class | anchor | note |
|---|---|---|---|---|
| `W 3`, `prodState`, `hom`, `maxCone`, `cnot`, `phiW` | all | [K] definitions | CD:97, 161, 186, 775, 1220 | the two-copy carrier encodes two-copy LT, K2 [A, OPEN] |
| ball self-duality: `Lor`, `lor_hom`, `lor_eq_smul_hom`, `lor_ehom`, `isEffectOn_affOf`, `lor_pair_bound`, `lor_of_forall_pair` | SDC motivation only | [K] | CD:869, 1679, 1590, 930, 916, 877, 1015 | not used in any derivation |
| `ProductData` (bi-affine product states) | SDC abstract form | [K] definition | CI:210 | asserting it of four tokens is part of [N] |
| PSD self-duality | satisfiability of SDC (uniform Q3), `dualW Q3 = Q3` | [K] | JordanClassification.lean:84; OperationalRigidity.lean:917 | model verification, not a premise |
| `Matrix.PosSemidef.kronecker` | satisfiability (PSD16 contains products) | [M] | Analysis/Matrix/Order.lean:213 | — |
| `FourCopyCoherent`, `fourVal`, `KT4Core`, `NClass`, `orient`, `EvenCycle`, `gateOf`, `cnotTw` | statements | [D] definitions | FourCopyDefs:56–98; FourCopyCore:30, 99–157, 177–180 | not certified |
| `kt4_forward_ie1`, Lemma B1, `cross_rel`, `link_mem`, `parity_witnesses` | strength results (§1.3 ⇐, §1.5 C1 ∧ C2, §1.6) | [D] | FourCopyHeadline:120; FourCopyBridge:269; FourCopyIE1:155, 286, 528 | not certified |
| `KT4Cone`, Lemma B2 | S3.1 | [D] statement; its four sub-identities `sorry` | FourCopyPackage:83–138 | sub-identities exact here [X s1 B2.1–B2.4] |
| classification `hcls ∧ hadm ∧ hgate ∧ IE1 ⇒ {Q3, twin}` | strength results only | [W + L] | landed KT4-PREM-1 Q1-NEC | one Lie-theory input |
| AUDIT-C: twist = orientation on {Q3, twin}; narrowed B3; C's B2 and models | §1.2, 1.4, 1.5 | stage 1, audited [W + X] | `pt/audit/C/AUDIT-C.md` | cited as recorded |
| **P3** state-level regrouping | SDC | **[N]** | — | satisfiable for every quadruple; independently motivated |
| **OVL4** four-token overlap positivity (composed pairing) | SDC | **[N]** | — | independently motivated; not a renaming |
| **CSD2** pair effects are states | SDC | **[N]** | — | independently motivated; per-pair |
| W4 carrier (four-copy LT) | SDC W4 form, S3.1 | [N] setting | as Lemma B2 | avoided by the abstract form (§1.3) |

No premise of SDC is IE1, IE2, Q3/PSD, the region tower, an (o) step or operation-level idle extension. Neither
flagged route is used.

## 3. Candidate table

Codes:
- **S**: sufficiency proved;
- **R**: route refuted (candidate holds, FCC fails);
- **n**: the candidate fails on that model;
- **✓**: candidate and FCC hold;
- **U**: unresolved.

Models: M_tok; uniform `K_gen`; uniform `K_gen*`; uniform `maxCone` (fails hgate); uniform Q3.

| # | candidate | M_tok | `K_gen` | `K_gen*` | `maxCone` | Q3 | verdict | renames FCC? |
|---|---|---|---|---|---|---|---|---|
| 1 | ordered associativity (fixed order) | R | R | R | ✓ | ✓ | refuted | no |
| 2 | induced pairs of an A-composite | — | — | — | — | — | refuted on its own model (`min_A(Q3, Q3)`, induced SEP pairs, −2) | no |
| 3 | N0 ∧ N1 ∧ N2 (C) | n | n | n | ✓ | ✓ | S | yes (cross clause in N0) |
| 4 | chart-invariant single-pair principles, no uniformity | R | — | — | — | ✓ | refuted (class) | no |
| 5 | uniform + `K ⊆ dualW K` | n | R | n | n | ✓ | refuted | no |
| 6 | uniform + `dualW K ⊆ K` | n | n | R | ✓ | ✓ | refuted | no |
| 7 | uniform + `K = dualW K` (also strong self-duality, symmetric cone) | n | n | n | n | ✓ | U (exotic-cone gap) | no |
| 8 | token orientation coherence = EvenCycle | n | R | R | ✓ | ✓ | refuted alone | no |
| 9 | pair self-duality + orientation coherence | n | n | n | n | ✓ | U (same gap) | no |
| 10 | AG (all generated) | n | R | R | ✓ | ✓ | refuted; = EvenCycle | restriction |
| 11 | C1 (full states, generated effects) | n | R | n | — | ✓ | refuted | restriction |
| 12 | C2 (generated states, full effects) | n | n | R | — | ✓ | refuted | restriction |
| 13 | ESC (entanglement swapping) | n | n | R | — | ✓ | refuted | restriction |
| 14 | C1 ∧ C2 | n | n | n | — | ✓ | S relative to the pair hyps (aligned gates) | restriction |
| 15 | four-token no-restriction + P3 | R | — | — | — | ✓ | refuted | no |
| 16 | purification | — | — | — | — | ✓ | U | no |
| 17 | symmetric monoidal composition (C row 17) | n | n | n | — | ✓ | S, but via the cross clause or an (o)-type idle extension | yes, or forbidden |
| 18 | **SDC = P3 ∧ OVL4 ∧ CSD2** | n | n | n | n | ✓ | **S**; no conjunct can be dropped (D1–D3) | **no** |

Notes on the table:
- Rows 1 and 4 use the M_tok cones with their aligned gates.
- Row 2's model is not a pair-hyp model.
- "✓" in the `maxCone` column means FCC holds there (landed F.max) and the candidate holds; `maxCone` fails hgate.
  "—" means not evaluated on that model.
- Row 7 (n on `maxCone`): `maxCone ≠ SEP = dualW maxCone`.
- Row 18 fails on `maxCone`: X1.

## 4. Cross-thread notes

- **S2 (pair system).** The two foils bracket the generated pair cone from both sides.
  - `K_gen` is too small: no-restriction makes its dual too large.
  - `K_gen*` is too large.
  - Both satisfy S2's three premises: `hadm`, `hcl` and `hgate`, with `cnot`.
  - With states `K_gen` and effects restricted to the generated ones, the four-copy condition for those effects holds
    (C1 and AG hold on uniform `K_gen`), while FCC with the full duals fails. The choice "effects = full dual"
    versus "effects = generated" is exactly where IE1 enters (§1.5).
  - CSD2 is a pair-level principle S2 could adopt: "the pair's effects are its states".
- **Stage 1, thread C.** N0 ∧ N1 ∧ N2 stands as a sufficient principle that renames FCC. SDC keeps its state part
  (N1 ∧ N2) and replaces N0's effect field. Row 17 of C's table carries an (o)-type ingredient (§1.6).
- **Stage 1, thread B.** The C2 foil `K_gen*` satisfies `hgate` in both directions (`cnot` is an involution). So gate
  preservation does not repair the failure from above, as `K_gen` already showed from below.
- **Stage 1, thread D / AUDIT-C.** All-generated conditioning reads only the gate orientations, consistent with D's
  T2 (orientation is a gate invariant) and the narrowed B3.
- **Integration (K2).** The composite-cone obligation splits, on this route, into:
  - local tomography (two-copy, in `W 3`; four-copy only in the W4 form of SDC);
  - the pair hyps;
  - self-duality of composites for the composed pairing (SDC), whose elementary instance is certified.

## 5. What is not claimed

- **No DERIVED claim.** L defines no pair system and nothing with three or more tokens. FCC stays INDEPENDENT of L.
- **No adoption.** SDC is a candidate principle. Nothing says OI's composition makes composites self-dual.
  INDEPENDENT relative to L does not mean SDC or FCC must stay independent principles forever.
- **Necessity.** No conjunct of SDC is claimed necessary. Drop-one models show insufficiency of the rest only.
  Existential equivalence relative to the pair hyps rests on [D] and [W + L].
- **Exotic cones.** Not claimed to exist and not claimed not to exist. The equivariant Barker–Foran remark is
  [L, unverified] and supports no label.
- **Scope of [X].** Each computation holds for the tables, symbols or finite sets it names. The slot analysis (§1.5)
  is for aligned gates (`cnot`, `cnotTw`). Universal statements rest on the named [W] arguments.
- **Kernel status.** The route is not kernel-checked. §1.7 is UNBUILT. The audited theorem, B1 and the design
  lemmas are [D]. The classification is [W + L]. Lemma B2's four sub-identities are exact identities here, not
  kernel proofs.
- **Narrowed B3** is cited as recorded and not generalized. The one-pair obstruction (§1.2) is a separate exact
  statement.
- **Bands.** Consistency-axis work. Bands unchanged.

## 6. Evidence log

`python3 -I -B`, Python 3.11.15, sympy 1.14.0, run from `pt/S3/`. `<OIB>` = `../base/verification/lean-mathlib/OIBridge`
(read-only; s1 and s2 check their transcription of the landed tables against it). Each decision rule was fixed in the
script header before the first run, and pre-run edits are recorded in NOTES N4. Nothing nondeterministic is printed.
Each `.err` holds only the appended exit line. The `exit=0` file has sha256 `19eaf438…f50f061`. Every replay
(`.replay.out`, `.replay.err`) is byte-identical to its run (`cmp`). Base status was empty and there was no
`__pycache__` under `base/` after the replays.

| script | sha256 (script) | output sha256 | checks | verdict | runs; replay |
|---|---|---|---|---|---|
| `s1_ladder.py <OIB>` | `7609665c5b23ff2de9ce1104f379a9c1b3fd8cc298f6020fff2289cd636825d2` | `7a46682dc732b66608623c308cdacd552bd770fc19a2672cb51eb0e25c464775` | 33/33 | `S1-LADDER-EXACT` | 1; identical |
| `s2_foils.py <OIB>` | `b98de540f114caf195765041fa7ff982685c2efe96db97643810fa7d5c360d71` | `fe2b067d42e79f69842b516857cdc46a6fd97adf568a26e832affa887ecf3717` | 27/27 | `S2-FOILS-EXACT` | 2 (run 1 failed, kept); identical |
| `s2_foils.run1.py` (failed run, kept) | `ef06b607af0a21d073330a7f945fb21c6437754702e06f336562d94ef3f3a417` | `f35115762066f9cd22ae9be392e20cf2d1ab081aaf55c72db014a26a0969f5cf` (`.err` `cf205dbb…`, `exit=1`) | 26/27 | FAILED (C3, harness error) | 1; not replayed |
| `s3_selfdual.py` | `e73d337b87b7d6d842804ed97dde27ad703bfed026478c8759346842e59824d2` | `bafd40fdedf8ea88bdba1f28e25401ffcccae4c85d1ab3ad4b7a4c07fe92e27f` | 13/13 | `S3-SELFDUAL-EXACT` | 1; identical |
| `s4_conditioning.py` | `4c5aa9455441fae6177562ef46bf0101cbb79ecd2b7bf70d520a3804e8e01f83` | `2782e6e1865ffe7571ab63d97cf67c197c0fda2fc15d1f615490d47559d02e01` | 11/11 | `S4-CONDITIONING-EXACT` | 1; identical |
| `s5_pairlevel.py` | `0af44511e2cbdb0404b78402a67db76ef75ce3ef6a8d5368143b777d1e3e6fa9` | `b0562444eb18fdeebc1dde76179591f5bb84a65cc2a63ac5ead5e8de9c59d1d1` | 8/8 | `S5-PAIRLEVEL-EXACT` | 1; identical |

**The failed run.** `s2_foils` run 1 failed one check, C3, on a harness error: a 1×1 sympy Matrix, not its entry, was
compared with 0. The one-line fix touched only that check, and every other line of run 2's output is identical to run
1's. The fact C3 checks (reflY on the second token preserves the Lorentz form) was never in question.

Checks by kind: s1 identity 11, witness 5, enumerate 6, source 5, countercontrol 6; s2 identity 14, witness 7,
enumerate 1, source 2, countercontrol 3; s3 identity 3, witness 5, enumerate 3, countercontrol 2; s4 witness 4,
enumerate 5, countercontrol 2; s5 identity 2, witness 2, enumerate 2, countercontrol 2.

## 7. Integrity

- **Start** (`.start_marker`, sha256 `4851b380…fe38`, written 2026-10-10T07:26:30Z before any other file; `pt/S3/` was
  empty):
  - the `inputs`, `stage1` and `inputs2` manifests passed `sha256sum -c --quiet` (rc 0);
  - base HEAD was `9f9f8257a980a1819fbbc1dc0019917cf8678626`, with empty status;
  - the four protocol files matched their recorded hashes.
- **During the run:** no file appeared in `pt/S3/` that this thread did not write. Nothing was written outside
  `pt/S3/`. No quarantine was needed.
- **End** (2026-10-10T08:33:29Z, after the last script run and before §6–§7 were written):
  - the three manifests passed (rc 0);
  - base HEAD was `9f9f8257a980a1819fbbc1dc0019917cf8678626`, with 0 status lines and no `__pycache__`/`.pyc` under
    `base/`;
  - PROTOCOL.md `239dc123…`, amendment 1 `b41aa0e7…`, amendment 2 `2a2f78f3…` and PROTOCOL-STAGE2.md `38603692…`
    were unchanged.
  - `pt/S3/` held 31 files, all written by this thread, and no subdirectory:
    - `.start_marker`, `NOTES.md`, `RESULT.md`;
    - for each of s1–s5: `.py`, `.out`, `.err`, `.replay.out`, `.replay.err`;
    - `s2_foils.run1.{py,out,err}`.
- **Integrity events:** none.
