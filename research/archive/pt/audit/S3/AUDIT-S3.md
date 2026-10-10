# Coordinator's audit of thread S3 — COMP-CONS (stage 2)

Audited: `pt/S3/RESULT.md`, sha256 `80f362db7f34bee2ee2227b7a590a5fc437febcd383179a6f5efd86e062d1da7`. `pt/S3/` holds 31 files and no subdirectory.

## Integrity
- **Coordinator's check, 08:37Z.**
  - The `inputs`, `stage1` and `inputs2` manifests are OK.
  - `pt/base` HEAD is `9f9f8257…`; status is clean; there is no bytecode.
  - The four protocol files are unchanged.
  - No file outside `pt/S2/` and `pt/S3/` is newer than S3's start marker.
- **The start marker.** Its sha256 `4851b380…` matches RESULT §7. The time written inside the marker is 07:26:30Z, and the file mtime is 07:26:37Z.
- **Hashes.** Every script and output hash in RESULT §6 matches the files.

## Replays
Run as `python3 -I -B` from `pt/auditS3-replay/`, with the OIBridge path argument for s1 and s2. All five reproduce stdout and `.err` byte for byte:

| script | checks |
|---|---|
| `s1_ladder` | 33 |
| `s2_foils` | 27 |
| `s3_selfdual` | 13 |
| `s4_conditioning` | 11 |
| `s5_pairlevel` | 8 |

Afterwards the base status is empty and there is no bytecode. The recorded failed run (`s2_foils.run1`, 26/27, a harness error at C3) was not re-executed. Its record is consistent with RESULT §6.

## Independent check (no thread code)
`indep_checkS3.py`: sha256 `b2226fe7…`; output `aa4bef7c…`; the replay is identical. **42/42 CONFIRMED**, verdict `INDEP-S3-CONFIRMED`.

**Run 1** (kept as `indep_checkS3.run1.*`) printed the same 42 check lines, all CONFIRMED, then failed at the final tally: some results were sympy booleans, which cannot be summed. The fix coerced each result to `bool` and changed nothing else. The check lines of runs 1 and 2 are identical.

The checks use my own implementations. `cnot` is built as conjugation by the CNOT unitary, control on the first qubit, and is compared with the landed sign and permutation tables only as a cross-check.

- **Primitives (P1–P6).**
  - `cnot` (CNOT conjugation) equals the landed tables; it is an ipW-orthogonal involution.
  - `ipW` is 4 × the trace pairing, and products lie in Q3.
  - `phiW = cnot(prodState e1 e3) = diag(1,1,−1,1)`, and `idW = actT reflY phiW = I`.
  - `sing4` is the singlet table, and `L' = diag(1,−1,1,−1)`.
  - `actT reflY` is an orthogonal involution, so twin is self-dual.
- **Cross-pairing (X1–X5)**, all symbolic in generic tables:
  - `<prodA X Y, prodB E F> = fourVal X Y E F`, and its famII analogue;
  - the four Lemma-B2 sub-identities;
  - naturality of σ12, with a countercontrol;
  - **a symmetry the thread does not state:** `fourVal X Y E F = fourVal E F X Y`. So famI and famII coincide for uniform cones, and the uniform-`K_gen` and uniform-`K_gen*` witnesses are the same number with the roles of states and effects exchanged.
- **Orders (O1–O4).**
  - No linear order makes both A and B contiguous.
  - **Every linear order leaves at least one KT4 pair non-adjacent** (O2): three adjacencies, four pairs.
  - The cycle 0-1-3-2 is the only cyclic order in which A and B are both non-crossing.
  - Coboundaries are exactly the 8 even patterns, with a countercontrol.
- **The foils (K1–K7).**
  - `cnot E0 = E0`.
  - `E0 ∈ maxCone`, by the singular values of its bilinear part (`MᵀM` has eigenvalues {0, 1, 1}). This route is independent of the thread's Lagrange identity.
  - `E0 ∉ Q3`: `pauliW E0` has eigenvalue −1/4.
  - `G` is a pure state.
  - `fourVal phiW phiW E0 G = −1` (uniform `K_gen`) and `fourVal E0 G phiW phiW = −1` (uniform `K_gen*`), with a countercontrol.
  - IE1 fails for `K_gen*`. My own deterministic scan of the 24 octahedral rotations against the 36 generated tables `cnot(prodState a b)` found its first negative pairing at side C, R = [[1,0,0],[0,0,1],[0,−1,0]], a = b = −e₂, value −1. This is the witness the thread reports. The identity rotation gives no negative value, as the countercontrol requires.
- **maxCone, M_tok and the induced pairs (M1–M6).**
  - Memberships of `idW`, `sing4`, `phiW` and `L'` in maxCone.
  - The induced-pair value −2.
  - The strictness value −2 on uniform maxCone.
  - M_tok: −1/8, with `L' ∈ twin` (since `actT reflY L' = sing4`).
  - The drop-OVL4 overlap: −2.
  - Drop-P3: `<v| pauli4(prodB phiW L') |v> = −1/2`, with v = Φ⁺ on qubits (0,2) ⊗ Φ⁺ on (1,3). This is computed from the definition of `pauli4`, not through the thread's Π identity. The countercontrol (`phiW` in place of `L'`) gives 1.
- **Entanglement swapping (S1–S2).**
  - `fourVal X Y E F = ipW E (X F Yᵀ)` holds symbolically.
  - With S3's generated triple, the ESC value on uniform `K_gen` is −1.
- **The rest.**
  - Lorentz-exclusion ingredients (L1–L2): the 36 axis products have norm 2 and average `E00`, and each lies outside the 45° cone about `E00`.
  - The abstract-carrier identities (C1, C2): the token-product identity, and |det| = 256 for the 16 token products.
  - The charts (T1): transpose acts on the Pauli basis by the signs (1,1,−1,1), and every token chart carries `prodA` and `prodB`.

## Design-source check of the slot claim
I read the FCC consumption sites in `pt/inputs/fourcopy/` to test RESULT §1.5's claim that "C1 ∧ C2 contains every instance the design proof reads".

| site | family and form | arguments | contained in |
|---|---|---|---|
| `cross_rel` | `upper` | full target states X ∈ K, Y ∈ K′ against Bell effects (FourCopyIE1:166) | C1 |
| `cross_rel` | `lower` | Bell states against full target effects (:171) | C2 |
| `inv_left/right_ctrl`, `inv_left/right_partner` | `lower` | a rotated link and a Bell table against full effects (:315, :329, :343, :363) | C2 |
| parity (`kt4_parity_of_witnesses`, `kt4_parity_aligned`) | `famI` | four gate images (FourCopyIE1:448, FourCopyParity:237) | C1 |

The 02-target versions arise by exchanging the roles of the two families.

Bell tables and rotated links are gate images of products: AUDIT-B confirmed that `link_mem` and `bell_mem` obtain them from `hgate` applied to products. **The claim is consistent with the design source.** This is a source read over [D], not a kernel proof.

## Written steps reviewed
- **SDC ⇒ FCC.**
  - Correct. It takes two lines over the exact cross identity (X1, X2) plus CSD2, and uses no pair hypothesis.
  - The drop-one models show only that the remaining conjuncts are insufficient, as the thread says.
  - Satisfiability with FCC holds for uniform Q3 with PSD16 and for every even twist pattern via `chart4 ε` (T1 + Q.W).
- **Strength.**
  - Strictly stronger than FCC *on admissible closed cones*: uniform maxCone satisfies FCC (landed F.max) and CSD2 but not P3 ∧ OVL4. maxCone fails `hgate`, so this is not a pair-hypothesis model; the thread states that scope correctly.
  - Existentially equivalent to FCC relative to the pair hypotheses [W over D, W + L].
- **The meta-obstruction (§1.6)** is sound and is the thread's most useful structural point. Relative to `hcls ∧ hadm ∧ hcl ∧ hgate`, every quantum-compatible sufficient principle is existentially equivalent to FCC, because:
  - FCC plus the pair hypotheses gives IE1 ∧ EvenCycle [D];
  - IE1 ∧ EvenCycle gives even-twist {Q3, twin} cones [W + L];
  - on those cones any quantum-compatible principle holds.

  So logical strength cannot separate a source from a renaming. The renaming judgment must read statement content, which is what the thread's frozen test (NOTES N2) does.
- **Renaming test: passed in its frozen form.**
  - No clause of SDC is cross-positivity of one grouping's product effects on the other grouping's product states.
  - My reading, recorded beside the thread's own caveat: the load-bearing new content is **OVL4 across the two groupings**. Every four-token state overlaps nonnegatively with every other under the composed pairing; equivalently, the self-dualizing pairing composes multiplicatively.
  - With CSD2 and P3, OVL4 restricted to cross products is FCC's cross clause written for states.
  - SDC therefore derives the cross clause from properties of single systems and from grouping-blind state-level regrouping, instead of positing it. That is a genuine re-sourcing, but it does not explain *why* composites are self-dual for the composed pairing.
  - **Whether OI supplies SDC is UNRESOLVED**: L defines no pair and no four-token system.
- **The single-pair chart obstruction** is correct: transport by `actT reflY` preserves products, maxCone, self-duality and the N-CLASS form (P6 here; C1–C5 there). It is kept separate from the narrowed B3, which is cited verbatim and not generalized.
- **The exotic-cone gap.**
  - (a) Lorentz exclusion: a complete argument, given the standard structure of Aut(L) [W + X; L for Aut(L)].
  - (b) Orthogonal images of Q3 send pure products to pure states [W + X]. The Wigner-type step is [L, unverified], as stated.
  - Purification and reducible self-dual cones remain open.

## Corrections (wording; no label changes)
1. **Necessity overstated in §1.5 and in s4's SLOT note.** The text says "the IE1 content of FCC needs no-restriction on both the state side and the effect side" and that a sufficient conditioning principle "must let full (no-restriction) arguments enter on BOTH sides".
   - What the two foils establish: restricting *either* side to generated arguments loses FCC (`K_gen` and `K_gen*`). So a sufficient conditioning principle must admit, on each side, arguments outside the generated set: at `K_gen`, effects outside Q3; at `K_gen*`, states outside Q3.
   - That *full* no-restriction on both sides is sufficient relative to the pair hypotheses is shown [W over D].
   - That it is *necessary* is not shown.

   This is a necessary-versus-sufficient boundary. The finding itself, that two-sided non-generated arguments are needed, stands.
2. **BF.W (s5) stall condition.**
   - The symmetrized Barker–Foran step stalls when every candidate y ∈ K*∖K has *negative* overlap `<y, cnot y> < 0` and also `y + cnot y ∈ K`. Zero overlap is harmless.
   - Supporting the thread's caution: no equivariant extension theorem holds for every orthogonal involution. For g = −id, a g-invariant cone is a subspace S, S* = S^⊥, and no nonzero space has a g-invariant self-dual cone. So any such argument must use properties of `cnot`.
   - No label rests on BF.W.
3. **Ordered associativity is refuted as written for the order 0,1,2,3.** By O2, every linear order leaves a KT4 pair non-adjacent. Placing the twin at that pair, with the quantum chain on the contiguous blocks, refutes ordered associativity in every fixed order [W + C's 16-pattern classification].
   - R1′'s "satisfiable for every quadruple" is [W], not re-checked here.
   - No label depends on it.

## Verdict for integration
- **FCC relative to certified L: INDEPENDENT.** This rests on the stage-1 models plus the two uniform foils, `K_gen` and the new `K_gen*`, both confirmed here exactly.
- **FCC: CONDITIONAL on SDC = P3 ∧ OVL4 ∧ CSD2.**
  - Sufficiency is proved [W over the exact identity X1/X2].
  - Strictly stronger than FCC on admissible closed cones.
  - Existentially equivalent to FCC relative to the pair hypotheses.
  - Not a restatement under the frozen renaming test; its new content is the multiplicativity of the self-dualizing pairing.
  - Its observer-native source is UNRESOLVED.
- **Associativity versus cross-pairing.** Answered as the owner asked.
  - Ordered associativity in any fixed order is blind to at least one KT4 pair and does not imply FCC.
  - Cross-pairing splits into a free state-level part and an effect-level part that is exactly famI ∧ famII.
- **Routes refuted by exact models:**
  - ordered associativity;
  - chart-invariant single-pair principles without uniformity;
  - uniform one-sided self-duality, both halves (`K_gen`, `K_gen*`);
  - orientation coherence alone, which equals all-generated conditioning;
  - one-sided conditioning, C1 and C2;
  - entanglement-swapping consistency;
  - four-token no-restriction together with P3.
- **UNRESOLVED:**
  - uniform full self-duality, and self-duality with orientation coherence (the exotic-cone gap);
  - purification;
  - the OI source of SDC.
- **Evidence levels.**
  - [K]: ball self-duality anchors (CompositeDimension :869, :877, :916, :930, :1015, :1590, :1679, spot-checked to the named declarations); PSD self-duality (JordanClassification :84, OperationalRigidity :917); `cnot`, `phiW`, maxCone. Mathlib `PosSemidef.kronecker` is at Order.lean:213.
  - [D]: the theorem and the design lemmas.
  - [W + L]: the classification.
  - [X]: instance-scoped.
  - §1.7 is UNBUILT Lean.
- **Bands:** unchanged. This is consistency-axis work.
