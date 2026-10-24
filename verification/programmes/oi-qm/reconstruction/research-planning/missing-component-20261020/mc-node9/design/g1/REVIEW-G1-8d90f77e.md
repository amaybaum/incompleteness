# Independent review: node 9 G1 design evidence at 8d90f77e (draft PR #885)

Reviewer: independent, read-only (§A.31, maximum skepticism on the favourable reading). Worktree: detached at
`8d90f77e916cc16c3b6f4d6bb64b22e6af6b6b76`, removed afterwards. Paths below are relative to
`verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/g1/`.
The reviewer engine is in `review/` in this directory (scripts copied there unchanged)
(`eng.py` and the scripts beside it). It imports neither `g1lib.py` nor the coordinator's scripts. The QM side uses
stabilizer groups of signed real Paulis, with conjugation tables derived from integer matrices. The card side uses
explicit Fraction distributions over (q_A, p_A, q_B, p_B). Equivalence is decided by exact pair-BFS over conditioned
states, which covers every word of every length. Length-bounded agreement is read off the BFS depth. All arithmetic is
exact.

## Dispositions

- **(R) G1-REPORT: ACCEPT WITH CORRECTIONS.** Every count and control I re-derived or replayed reproduces. One
  computational example is false (F1). One interpretive sentence overstates its evidence (F2). Three NEW labels should be
  downgraded or reworded (F9).
- **(C) Coordinator: ACCEPT WITH CORRECTIONS.** The counts 256/64/8/4 reproduce independently, and the length-7
  equivalence is now exact at all lengths. Including C-inverting lifts changes nothing. One correction blocks any use of
  the reading: in its current wording the reading does not survive the alphabet tests. With swap_B removed, length-bounded
  correspondence does not select QM. For L = 7–9 it selects a non-QM class carrying the cards' witness values (F4). The
  correspondence condition was also chosen after the enumeration, not stated in advance (F5).

## Numbered findings

**F1 (blocking for the sentence, (R)). The H·Z example is wrong; the coordinator is right.** At G1-REPORT.md:154 the
report says "Within the same generated theory, the lift H·Z gives W6 = 0". No output file computes this: grep finds no
H·Z case in any `.py` or `.out`. Reviewer check (exact):

| swap_A lift (couple = CNOT) | W6 | W7 |
|---|---|---|
| H_A·Z_A (= X_A·H_A) | 1 | 1 |
| Z_A·H_A | 1 | 1 |
| H_A·Z_B (Z on the other system) | 0 | 0 |

| couple lift (swap_A = H_A) | W6 | W7 |
|---|---|---|
| CNOT·Z_B (= Z_A Z_B·CNOT) | 0 | 0 |
| Z_B·CNOT | 0 | 0 |
| CNOT·Z_A | 1 | 1 |

Every A-supported twist of swap_A gives W6 = 1 (`lifts.out:2,6,10,14`). The report most plausibly meant H_A ⊗ Z_B, or
CNOT·Z_B. The first is not a local lift of a local operation; the second is a legitimate local-frame twist of the
coupling.

Replacement wording: "Within the same generated theory, the swap lift H_A·Z_B (which acts on B) or the coupling lift
CNOT·Z_B gives W6 = 0; every A-supported twist of swap_A leaves W6 = 1."

**F2 (non-blocking, (R)). "Partly conventional in QM itself" overstates the evidence.** At G1-REPORT.md:152–153 the
report says that "QM's value of W6" is "partly conventional in QM itself". In QM the circuit is a fixed unitary. The
freedom lies in the card-to-operation dictionary, and the coordinator's result, reproduced here, shows that agreement with
the cards on short protocols fixes that dictionary over the declared alphabet.

Replacement wording: "The principle alone leaves the Pauli frame of each lift free, and the frame decides W6. In QM the
frame is fixed by the calibration dictionary (ERT). Over the declared alphabet it is also fixed by agreement with the
card theory on short protocols (coordinator note), so the witness value is not a convention of QM."

**F3 (non-blocking, (R)). Scope the verdict to the principle alone.** At G1-REPORT.md:140 the verdict
"permits-with-k-choices" is correct for the principle alone. Add after line 151: "With an added card-correspondence
requirement over the declared alphabet, the choice is removed (coordinator note); that requirement was formulated after
this enumeration."

**F4 (blocking for use of the reading, (C)). The selection depends on the alphabet.** It requires swap_B in the protocol
family, or a locality premise on the lifts. Full results are in the 1(c) table below. Removing the flips changes nothing.
Removing swap_B, or using only {swap_A, couple, read_A, read_B}, changes three things:

- At L = 5, 6 the survivors are two classes: QM (W6 = W7 = 1) and a class whose swap_A lift is Z_B·H_A or XZ_A Z_B·H_A,
  with W6 = W7 = 0.
- For L = 7, 8, 9 the unique survivor class is that non-QM class, with the cards' witness values.
- At L = 10 nothing survives.

So "maximal correspondence" selects the cards' value without swap_B. The non-QM class needs a swap_A lift that acts on
B. With swap lifts restricted to their own system, the unique QM class reappears at L ∈ {5, 6} in all four alphabets
tested. COORDINATOR-NOTE.md:33–40 must say this.

Replacement wording for COORDINATOR-NOTE.md:33–36: "Within this construction, with the declared alphabet (both swaps,
the coupling, flips optional, both reads), the principle plus agreement with the card theory on every protocol of length
≤ L, for L ∈ {5, 6}, leaves exactly the QM class (4 triples, one Pauli-relabelling class). Equivalently, QM is the
unique lift class with maximal card-agreement length (6). The selection fails without swap_B: correspondence is then
ambiguous at L ≤ 6, and at L = 7–9 it selects a non-local swap_A lift with the cards' witness values. Restricting each
swap's lift to its own system restores the QM selection at L ∈ {5, 6} for every alphabet tested."

**F5 (blocking for the §A.29 framing, (C)).** COORDINATOR-NOTE.md:16 calls the condition a correspondence requirement
"of the kind §A.29 already asks a revision to state in advance". It was not stated in advance:

- it was formulated after G1-REPORT's enumeration;
- L was fixed after the counts were seen;
- the sub-family form P1–P3 that G1-REPORT did state (G1-REPORT.md:23–25, 35–37) does not select QM (F6).

Replacement wording: "A correspondence requirement formulated after the enumeration (not preregistered): …". The result
sits on the consistency axis (§A.23). A future preregistration should freeze one form in advance: maximal-length
agreement, or single-coupling agreement P4₁, together with the alphabet and any locality premise on the lifts.

**F6 (non-blocking, both). P1–P3 do not select the QM class; the missing family is coupling combined with swaps.** At
all lengths, P1 ∩ P2 ∩ P3 leaves 16 triples, with W6 split 8/8. The Z-type twists of the coupling (CNOT times Z_A, Z_B
or Z_A Z_B) are invisible without swaps, and P3 has no coupling. Adding P4₁ fixes this: every protocol with at most one
coupling event, any local operations, all lengths. P4₁ alone leaves exactly the 4 QM triples, and standard QM ≡ cards
on P4₁. P4₂ is unsatisfiable: QM differs from the cards already at `sA c sA c sA rA rB`. P4₁ has no free length, but it
also fails without swap_B, even with local lifts (32 pass, of which 16 are QM and 16 have W6 = W7 = 0).

**F7 (non-blocking, (C)). The length-7 equivalence is now exact (point 1(e)).** The reviewer's pair-BFS finds all 4
survivors ≡ standard QM on every word, at every length, over the full alphabet. The exact algebraic proof:

- Survivor = Ad(W)∘std∘Ad(W)⁻¹, with (0,0,0) ↔ W = I, (12,0,0) ↔ Z_A, (0,3,8) ↔ Z_B and (12,3,8) ↔ Z_A Z_B (verified
  table by table).
- Each W fixes the |00⟩ record group and the records ±Z_A, ±Z_B, and commutes with every flip.
- So S ↦ Ad(W)S intertwines the two record automata and preserves every read probability.

G1-REPORT already had this, exhaustively: `d_witness.out:47–48`, "QM-equivalent triples == {ERT conjugated by Z_A^a
Z_B^b value twists}: True (4)". COORDINATOR-NOTE.md:30–31 should cite it and drop "20,000 random length-7 words" as the
support.

**F8 (non-blocking, (C)). ℤ₄ C-inverting lifts do not change the conclusion (point 1(g)).** Every inverting lift of a map
is L∘κ, where L is a lift trivial on C and κ is complex conjugation (X ↦ X, Z ↦ Z, i ↦ −i). κ fixes every element of
the real Pauli subgroup ⟨X_j, Z_j, −1⟩. Every reachable record group lies in that subgroup: the initial group, the lifts
Ad(P·U) with P and U real, the flips and the read update all preserve it. So φ(S) = L(S) on every reachable state, and
every count is multiplied by exactly 8: 2048 / 512 / 64 / 32 / 32 / 0 at L = 2…7. The 32 survivors ≡ QM, matching
G1-REPORT's 32 (`d_witness.out:37`). COORDINATOR-NOTE.md:8 should replace "finds them invisible" with this argument.

**F9 (non-blocking, (R)). The NEW labels at G1-REPORT.md:219–226.**

| row | finding as stated | disposition | reason and correction |
|---|---|---|---|
| H1 | NEW | **ELABORATING** | That the S-type map has no lift in the real class is the standard fact that S is not a real Clifford. NOTES.md:133 already names "the phase-group distinction between Spekkens' toy theory and qubit stabilizer QM". The wording "incompatible with the coupling" is also imprecise. With ℤ₂ at n = 1, the phase map lifts only where q(Z) = 1, i.e. where Z has no involutive lift, so the conflict is with the read rule (c). Q₈ is the class that admits swap and phase but not couple. Reword: "C = ℤ₂ and the p ^= q map are incompatible with a recordable Z (read rule (c))" |
| H2 | NEW, bounded | **ELABORATING** | A real closure of a loophole, but it has no observable consequence on this family (F8) |
| H5 | NEW | **NEW survives, narrowed** | Keep "the principle fixes the lifts only up to the Pauli frame, and the frame decides W6/W7". Replace "G1's 'forcing' of the witness is convention-dependent" with "the frame is fixed by ERT, or by a card-correspondence requirement over the declared alphabet (F4–F6), not by the principle" |
| H7 | NEW | **NEW (methodological) survives** | Independently confirmed here: 16 triples pass P1–P3 at all lengths, and 8 of them give QM's W6, but only 4 are QM-equivalent on the full table |
| H8 | NEW | **BORDERLINE** | Correct within the construction. Not checked against the literature on splitting of the Clifford extension (§A.31 step 4); keep the label only after that check |

**F10 (non-blocking, (R)). The other spot checks hold.**

- n = 1 classification, independent brute force:
  - ℤ₂: 8 normalized cocycles with commutator ω, 2 coboundaries, 4 classes. Three have 5 involutions (D₄), one has 1
    (Q₈).
  - ℤ₄: 64 cocycles, 16 coboundaries, 4 classes. One has element orders 1:1, 2:7, 4:8 (Pauli); three have elements of
    order 8.
- n = 2:
  - ℤ₂: 16 quadratic refinements of ω, 10 with Arf 0 and 6 with Arf 1, as reported.
  - The completeness argument is adequate. 16 representatives separated by an invariant give at least 16 classes, and
    the exact sequence 0 → Ext(V, C) → H²(V, C) → Hom(Λ²V, C) gives at most |Ext(F₂⁴, C)| = |C/2C|⁴ = 16 above each
    commutator form. For ℤ₂ it is also confirmed directly by the refinement count.
- "Never affine" (G1-REPORT.md:163–166):
  - For a lift (a, u) ↦ (a + g(u), Su), the homomorphism condition is g(u+v) − g(u) − g(v) = β(Su, Sv) − β(u, v). For
    S exchanging u and v this is β(v, u) − β(u, v) = −(|C|/2)ω(u, v), which is nonzero, in every section.
  - Bit-linearity into ℤ₄ fails because X_j and Z_j have disjoint bit support.
  - The argument covers maps that exchange such a pair (the swaps). The couple's update is additive (zero) in the real
    section, and the report says so (l. 168).
- Degree-2 minimum: the lower bound follows from non-affinity and the upper bound from the real section, so the 2¹⁵
  search is a consistent redundancy.
- q = 3: β = 2ω (mod 3) is bilinear, has commutator 4ω = ω and is Sp-invariant, so g = 0 lifts every map. The contrast
  holds for odd prime q.
- Main.md citations: l. 290 is the update; Lemma 2(iii) "with no phase" is at l. 300; the scope remark "is not covered"
  is at l. 320. All correct.
- The ontic (II) result and Alt-1/Alt-2 are correctly scoped. They were not re-derived here.
- Line 129–131: "same group for every choice" follows exactly, because the flips generate Inn(E). State that argument
  rather than "checked on a sample of 18".

**F11 (non-blocking, (C)). Provenance and replay defects.**

- `coordinator/survivors.out` is not byte-reproducible from `survivors.py`. The script re-executes the prefix of
  `corr2.py`, which prints `passing at L<=4: [...]` first, and the committed output lacks that line.
- `corr.out` has no L = 5 row. The note's L = 5 count (COORDINATOR-NOTE.md:27) follows from `corr3.out`, because the
  L = 5 survivors are a subset of the L = 4 survivors. Cite it that way.
- The "words" column mixes cumulative counts (90, 819, 7380) with an increment (+59049).
- The coordinator directory has no `run_all.sh`.
- The scripts depend on numpy object arrays (exact integers); numpy 2.5.3 was used here.

**F12 (non-blocking, (C)). Lift model and card semantics are faithful (points 1(a), 1(b)).**

- For each of swap_A, swap_B and couple, brute force over generator signs gives exactly 16 automorphisms of the signed
  real Pauli group that cover the card map and fix −1. They equal {Ad(P·U) : P ∈ 16 Paulis} as sets. This is
  G1-REPORT's set of 16 lifts per map. The ℤ₄ case has the same 16, since lifts trivial on C differ by Hom(V, C[2]) ≅
  F₂⁴.
- `corr.py` matches `g1lib.CardTheory`:
  - the read records q_j and refreshes p_j with a fair bit, on both branches;
  - the flips are xA ↔ flipq_A (X Pauli) and zA ↔ flipp_A (Z Pauli);
  - the initial state is q = 0 with p uniform;
  - couple is (q_B ^= q_A, p_A ^= p_B).
- The comparison is equality of full joint distributions over outcome sequences, as dicts with exact Fractions.
- The reviewer's word-level control (L ≤ 3, every word, 4096 triples) agrees with the BFS-depth method on every triple:
  256 at L ≤ 2 and 64 at L ≤ 3.

**F13 (point 1(f), non-blocking, analysis).**

- *Circularity.* The correspondence condition uses only predictions of the card theory, and the lift set is the
  abstract lift set, not taken from QM (F12). So it is not circular. QM enters earlier, through the principle (commutator
  ω, formulated with QM known; G1-REPORT.md:25), and the alphabet decides the outcome (F4).
- *Is the window tuned?* The window {5, 6} is not fitted. Its lower edge is where the lift ambiguity resolves, and its
  upper edge is QM's first departure (7). Its existence is a computed fact: QM is the unique lift class closest to the
  cards over the full alphabet. Choosing L = 5 after seeing the counts is still a post hoc choice. Two parameter-free
  forms exist:
  - maximal-length agreement;
  - P4₁ single-coupling agreement, whose k-window is exactly {1}: k = 0 leaves 64 triples, k ≥ 2 none.

  Both select QM over the full alphabet. Both fail without swap_B. Maximal-length agreement then selects the cards'
  witness value.
- *Classification.* The swap_B and locality dependence is what keeps this CONFIRMING (consistency axis), not a
  derivation. swap_B is part of the generator family declared beforehand (G1-REPORT.md:8–9), so it was not added to
  produce the result. Locality of lifts would be a new premise and would have to be stated in advance.

**F14 (point 5, scope).**

- Neither document claims anything about OI in general or a reconstruction of QM (G1-REPORT.md:9–10).
- G2 is untouched, and K-STAB-GAP holds (`controls.out`, replayed byte-identically).
- The coordinator's hedges ("within this construction", "needs independent review", the open points at l. 41–48) are
  appropriate in kind. Its reading (l. 33–40) needs the F4/F5 scope before it is used.

## Result tables

### 1(c) Alphabet dependence

Each cell is the number of lift triples, out of 4096, that agree with the cards on every word of length ≤ L. "QM" means
every survivor ≡ standard QM over that alphabet. "max" is the largest L with survivors, and which class that is.

| alphabet | L=2 | 3 | 4 | 5 | 6 | 7 | 8–9 | 10 | max |
|---|---|---|---|---|---|---|---|---|---|
| full {sA,sB,c,4 flips,rA,rB} | 256 | 64 | 8 | **4 QM** | **4 QM** | 0 | 0 | 0 | 6, QM |
| no flips {sA,sB,c,rA,rB} | 256 | 64 | 8 | **4 QM** | **4 QM** | 0 | 0 | 0 | 6, QM |
| {sA,c,rA,rB} | 512 | 256 | 256 | 128 mixed (64 QM + 64 W6=W7=0) | 128 mixed | 64 non-QM (W6=W7=0) | 64 non-QM | 0 | 9, **non-QM** |
| no sB {sA,c,4 flips,rA,rB} | 512 | 256 | 256 | 128 mixed | 128 mixed | 64 non-QM | 64 non-QM | 0 | 9, **non-QM** |
| K-G1 {sA,c,rB} (extra) | 1024 | 512 | 256 | 256 | 128 mixed | 64, ≡ cards on all words | 64 | 64 | ∞, cards |
| full, swap lifts local (256 triples) | 64 | 16 | 8 | 4 QM | 4 QM | 0 | 0 | 0 | 6, QM |
| {sA,c,rA,rB} or no sB, swap lifts local | 64 | 32 | 32 | 16 QM | 16 QM | 0 | 0 | 0 | 6, QM |

Notes on the table:
- In alphabets without sB, the 16 swap_B choices are idle, so 64 triples are 4 (swap_A, couple) pairs.
- The non-QM class has swap_A lift ∈ {Z_B·H_A, XZ_A Z_B·H_A} and couple ∈ {CNOT, Z_A·CNOT}.
- Standard QM's first disagreement with the cards is at length 7 in every alphabet.
- Answer: with flips removed, the unique QM class survives at L ∈ {5, 6}, unchanged. With {swap_A, couple, read_A, read_B}
  or swap_B removed, it does not, at any L, unless swap lifts are required to be local.

### 1(d) Sub-family correspondence

Each row counts the triples that agree with the cards on all words of the sub-family, at all lengths (exact BFS).

| family | triples ≡ cards | std QM ≡ cards on it | selects QM class? |
|---|---|---|---|
| P1a single system A {sA,xA,zA,rA} | 2048 | yes | no |
| P1b single system B {sB,xB,zB,rB} | 2048 | yes | no |
| P2 coupling without swaps {c,flips,rA,rB} | 1024 | yes | no |
| P3 local operations only {sA,sB,flips,rA,rB} | 64 | yes | no |
| **P1 ∩ P2 ∩ P3** | **16** (W6: 8 give 1, 8 give 0) | yes | **no** |
| P4₀: no coupling (= P3 with both systems) | 64 | yes | no |
| **P4₁: at most one coupling, any local ops** | **4 = QM class** | yes | **yes** |
| P4₂: at most two couplings | 0 | **no** (`sA c sA c sA rA rB`) | unsatisfiable |
| P4₁ without sB (all lifts / local lifts) | 256 (64 QM) / 32 (16 QM) | yes | no |

The 16 P1–P3 survivors are swap_A ∈ {H_A, XZ_A·H_A}, swap_B ∈ {H_B, XZ_B·H_B} and couple ∈ {CNOT, Z_B·CNOT, Z_A·CNOT,
Z_A Z_B·CNOT}. The missing sub-family is a coupling combined with swaps: the Z-type coupling twists show up only after a
swap.

### Exactness status of the length-7 equivalence

It is exact. Pair-BFS over the full alphabet shows the 4 survivors ≡ standard QM on all words of all lengths. The
algebraic proof is Pauli conjugation by W ∈ ⟨Z_A, Z_B⟩, which fixes the preparation, the readouts and the flips (F7).
The same result is already exhaustive in `d_witness.out:47–48`.

### Replay

| item | result |
|---|---|
| `SHA256SUMS` (g1, 19 entries) | 19/19 OK |
| `coordinator/SHA256SUMS` (14 entries) | 14/14 OK |
| `controls.py`, `b_lifts.py`, `predictions.py`, `a_classify.py` | byte-identical to the committed `.out` |
| `coordinator/lifts.py`, `local.py`, `local2.py` | byte-identical |
| `coordinator/corr.py 2` | byte-identical to the L = 2 lines of `corr.out` |
| `coordinator/survivors.py` | **differs**: an extra first line, `passing at L<=4: [...]`, which the committed `.out` omits (F11) |
| reviewer controls | cards vs standard QM: first disagreement at length 7; 24 reachable stabilizer states. Both match G1-REPORT |
