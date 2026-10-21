# Node 9, gap G1: exploratory design evidence on a composition rule for joint records

**Status.** Pre-preregistration design evidence for draft PR #885 (missing-component thread, node 9). No M0–M5 verdict;
not a preregistered run. Inputs: `incompleteness` at `59d2c858`, read through a detached worktree (removed afterwards).
Arithmetic is exact throughout: F₂ bitmasks, ℤ₂/ℤ₄ group tables, `fractions.Fraction`, and for QM Gaussian-integer
state vectors with exact normalized density-matrix keys. No floats enter any verdict. `run_all.sh` regenerates every
`.out` file. Two consecutive runs were compared byte for byte (see Bounds). Every statement below is scoped to the
declared construction: two card systems, the generator family {swap_A, swap_B, couple, four flips, read q_A, read q_B},
central extensions of V = F₂⁴ by C ∈ {ℤ₂, ℤ₄}, and the fixed read rule (c). Nothing here is a claim about OI in general,
and nothing here reconstructs QM. The QM side is calibration only.

**Conventions** (`g1lib.py`). A relation label u = (x|z) ∈ V reads the card functional x·p + z·q, so Z ↔ q (visible card)
and X ↔ p (hidden card). The card maps act on labels by Schrödinger push-forward. Computed:
- swap_j: X_j ↔ Z_j;
- couple: X_A → X_A X_B, Z_B → Z_A Z_B, with Z_A and X_B fixed.

These equal the Clifford conjugation labels of H_j and CNOT(A→B), and all are symplectic (`controls.out`).

***

## Controls (all green)

Provenance of the controls. The read rule (c), K-G1 and the card/QM calibrations were fixed before any enumeration. The
preserved-result controls P1–P3 were added during the session, after the first enumerations, so they are controls and not
preregistered. ERT was formulated by this session with QM known, which is one reason it is classed CONFIRMING (§1(d)).

| control | result | file |
|---|---|---|
| **K-G1** cards: W6 = (swap_A, couple)³ then read q_B | 0 with certainty; W7 also 0, and the W7 state equals the initial state | controls.out |
| **K-G1** exact QM: (CNOT·(H⊗I))³\|00⟩ | 1 with certainty; W7 also 1 (exact Gaussian-integer arithmetic, replacing fb.py's floats) | controls.out |
| trivial extension (abelian, β = 0) engine vs direct ontic card simulation | **equivalent on every word** over the full alphabet (24 state pairs, 248 transitions) | controls.out |
| calibration extension, C = ℤ₂ real Pauli (β = z·x′) with ERT lifts, vs exact QM | **equivalent on every word** (24, 248) | controls.out |
| calibration extension, C = ℤ₄ complex Pauli (β = 2 z·x′) with ERT lifts, vs exact QM | **equivalent on every word** (24, 248) | controls.out |
| shortest word distinguishing cards from QM (product-automaton BFS) | length 7 (6 gates plus the read), and W6 is such a word | controls.out |
| preserved P1: single system, D₄ real class + ERT | ≡ cards (n = 1) and ≡ QM (n = 1) | controls.out |
| preserved P2: coupling plus flips plus reads, no swaps | ≡ cards | controls.out |
| preserved P3: two systems, local operations only | ≡ cards | controls.out |
| formula check: lift-existence criterion q∘S = q vs brute-force lift enumeration | agree on all 16 × 4 (class, map) cases per C (assertion) | b_lifts.py |
| formula check: Aaronson–Gottesman phase rules (H: r ^= xz; CNOT: r ^= x_a z_b(x_b ⊕ z_a ⊕ 1)) vs engine in the Hermitian section | reproduced on all 16 records, for every map | oi_real.out |
| formula check: real-section update g_swap = x z, g_couple = 0 | reproduced | oi_real.out |
| value twists (card flips) = inner automorphisms when the commutator is ω | true (assertion). In the abelian extension every inner automorphism is trivial, so flips are not inner there | controls.py |
| **K-STAB-GAP** | every reachable QM state (24) has single-qubit Bloch components in {−1, 0, 1} (exact). The passing extension engine has elementary-record expectations in {−1, 0, 1} by construction. G1 does not touch G2 | controls.out |
| (II) control: affine extension with the extra cell decoupled | ≡ cards, ≢ QM | oi_real.out |

Counts of the reachable family (full alphabet): 24 states, 168 gate transitions and 80 read branches, identical for
cards, QM and the trivial extension.

***

## 1(a) Classification of central extensions with commutator ω

Brute force at n = 1 covers every normalized cocycle. At n = 2, representatives are separated by the class invariant
(the squares of lifts), and their number is matched against |Ext(V, C)| = 2^{2n} (`a_classify.out`).

| n | C | cocycles with commutator (|C|/2)·ω | classes | isomorphism types | classes in which every elementary relation X_j, Z_j has an involutive lift ("recordable") |
|---|---|---|---|---|---|
| 1 | ℤ₂ | 8 (brute force) | **4** | 3 × D₄, 1 × Q₈ | 1: D₄ with squares (X, Z, Y) = (+, +, −), the real Pauli group. Q₈ has no recordable relation at all |
| 1 | ℤ₄ | 64 (brute force) | **4** | 1 × Pauli group (orders 1:1, 2:7, 4:8); 3 × a group with elements of order 8 | 1: the complex Pauli group |
| 2 | ℤ₂ | (representatives) | **16** | 10 × 2^{1+4}₊ (Arf 0), 6 × 2^{1+4}₋ (Arf 1) | 1: real Pauli, q(u) = x·z |
| 2 | ℤ₄ | (representatives) | **16** | 1 × Pauli (no element of order 8), 15 × with elements of order 8 | 1: complex Pauli |

- For C = ℤ₂ the classes are the quadratic refinements q of ω. For C = ℤ₄ they are the linear maps q̄ : V → ℤ₂ (squares
  mod 2), because a ℤ₄ coboundary absorbs the even part.
- The n = 2 completeness (no further classes) rests on the standard sequence Ext(V, C) → H² → Hom(Λ²V, C) [W]. It is
  brute-force verified at n = 1 only.
- Odd-order C admits no extension with commutator ω, since Hom(ℤ₂, C) = 0. So ℤ₂ is the minimal phase group carrying
  the principle.

## 1(b) Lifting the card dynamics (`b_lifts.out`)

Every lift was enumerated by brute force over generator images, with a homomorphism check on all pairs.

| maps required to lift | ℤ₂ classes admitting all | ℤ₄ classes admitting all |
|---|---|---|
| swap_A, couple (the K-G1 alphabet) | 2 (q on gens 0000, 0001) | 2 |
| swap_A, swap_B, couple | **1 (real Pauli)** | **1 (complex Pauli)** |
| + phase map p_A ^= q_A (S-type) | **0** | 1 |

- **Lift existence ⇔ the class is preserved** (q∘S = q, or q̄∘S = q̄). This agrees with brute force in every case.
- **The coupling excludes Q₈-type classes.** Q₈ admits swap but not couple.
- **Two independent routes select the class.** One is lift existence for {swap_A, swap_B, couple}. The other is the read
  rule's need for involutive lifts of Z_A, Z_B (the initial state) and X_A, X_B (reads after a swap). In the second
  admissible class for the K-G1 alphabet, z_B has no involutive lift, so no record state can hold q_B = 0 and the class
  is excluded by (c) (`d_witness.out`).
- **Uniqueness of the lift.** Each admissible map has exactly 16 lifts acting trivially on C, and they form one coset
  L₀∘Inn(E), with |Inn(E)| = 16. The lift is therefore unique up to inner automorphisms, i.e. up to the Pauli frame.
- **Inverting lifts.** With C = ℤ₄ there are 16 further lifts per map that invert C (the antiunitary type).
- **The phase map.** It has no lift in the real class, so with C = ℤ₂ the family {swap, couple, phase} is unsatisfiable.
  With C = ℤ₄ it lifts, but the ERT rule below is ambiguous for it (`predictions.out`).

## 1(c) Read rule (one rule, fixed in `g1lib.ExtTheory` before any run)

A record state is an abelian subgroup S ⊂ E with |S| = 2ⁿ and S ∩ C = {1}. Reading relation u, with value-0 lift d(u)
and z the order-2 central element:
- if d(u) ∈ S, the outcome is 0;
- if d(u)·z ∈ S, the outcome is 1;
- otherwise each outcome o has probability ½, and S′ = ⟨{g ∈ S : ω(πg, u) = 0}, d(u)·z^o⟩. This fixes u's sign and
  randomizes the conjugate.

The same text with β = 0 is the card read with fresh replacement (control above). Card flips act as value twists
(a, u) ↦ (a + ω(w, u)·|C|/2, u).

## 1(d) Witnesses and complete transition table under every admissible choice (`d_witness.out`)

Admissible class: real Pauli (ℤ₂) or complex Pauli (ℤ₄). Default dictionary.

**K-G1 over all 16 × 16 (swap_A, couple) lift pairs.** The ℤ₂ and ℤ₄ counts are identical when lifts act trivially on C.

| W6 | W7 | pairs |
|---|---|---|
| QM (1 certain) | QM (1) | 64 |
| QM | cards (0 certain) | 64 |
| cards | QM | 64 |
| cards | cards | 64 |

With ℤ₄ and C-inverting lifts also allowed: 256 / 256 / 256 / 256 out of 32 × 32 pairs.

**Complete transition table** (exact product-automaton equivalence on all words over the full alphabet):

| choice set | triples | ≡ QM | ≡ cards | other |
|---|---|---|---|---|
| ℤ₂, lifts trivial on C | 4096 | **4** | 0 | 4092 |
| ℤ₄, lifts trivial on C | 4096 | **4** | 0 | 4092 |
| ℤ₄, trivial or inverting on C | 32768 | **32** | 0 | 32736 |

- The 4 QM-equivalent triples are exactly the ERT triple conjugated by the value twists of Z_A^a Z_B^b. These are the
  relabellings that fix the preparation and the readouts (verified). The factor 8 for ℤ₄ comes from composing each map
  with complex conjugation, which is invisible on this all-real family.
- With the flips in the family, the operation group generated by (lifts + flips) is the same for every choice, order
  1152 = 16 × 72. Different lifts differ by inner automorphisms, which are products of flips; this was checked on a
  sample of 18 triples.
- **The elementary-record transport rule (ERT).** Each elementary record d(X_j), d(Z_j) is carried to the product of the
  elementary records of its image, with the card's value and no sign. Composite records then get their sign from the
  group law (H: XZ ↦ ZX = −XZ).
  - ERT is well-defined on all three maps and gives the QM table under **all 16 dictionaries** of value-0 lifts, for
    both C.
  - Among the 840 unordered bases of V, ERT is well-defined only on the card basis {X_A, Z_A, X_B, Z_B}. The other 839
    are ill-defined (non-commuting products) or contain a non-recordable element (ℤ₂).

### Hard-to-vary verdict (1): **permits-with-k-choices** at the level of the labelled operations

- **What the principle forces** (given C ∈ {ℤ₂, ℤ₄} and the generator family):
  - a unique extension class;
  - the generated operation group (the real-stabilizer one, never the card one: 0 of 4096 triples reproduce the cards);
  - lifts unique up to the Pauli frame.
- **What it leaves open.** Which element of that group is called "swap" or "couple" is not fixed. There are 16 lifts per
  map and 4096 triples, of which 4 (one relabelling class) reproduce the QM table. The witness splits evenly: W6 takes
  QM's value in 128 of 256 pairs, and (W6, W7) = (QM, QM) in 64 of 256.
- **What selects QM's labelling.** It is selected by ERT, an added rule, not by the principle. ERT is independently
  stateable from the card side ("change only composition; transport elementary card records exactly as the cards do"),
  and it is unique in the sense that it is well-defined on 1 of 840 bases and dictionary-independent.
- **Maximum skepticism.** ERT is the same convention that singles out the calibration circuit's H and CNOT, which
  conjugate X and Z with no sign. So "QM's value of W6" is partly conventional in QM itself. Within the same generated
  theory, the lift H·Z gives W6 = 0. ERT also does not extend to the phase map, where S and S† (which differ by a flip)
  remain a free choice. Classification: **CONFIRMING**, not a derivation.

***

## 2. OI-side realizability (`oi_real.out`, `oi_z4family.out`, `predictions.out`)

**(I) Record level.** A record is a cell block (u, r) with phase cell r ∈ C, and a map acts as (u, r) ↦ (Su, r + g_S(u)).

- **Theorem [W, verified exhaustively at n = 1].** Take any lift acting trivially on C of a map that exchanges u and v
  with ω(u, v) = 1, such as the swap. Then g(u+v) − g(u) − g(v) = β(v, u) − β(u, v) = −|C|/2 ≠ 0. So g is not additive
  in any section (coordinatization), and not bit-linear into ℤ₄ either. At n = 1 this covers all 8 ℤ₂ and all 64 ℤ₄
  cocycles, i.e. every section of every class, with every lift: **0** additive.
- **n = 2, ℤ₂, all 2¹⁵ sections.** No section gives an affine swap update (0 of 32768). The minimum over sections of the
  maximum ANF degree over (swap_A, swap_B, couple) is **2**. It is attained in the real section, where g_swap = x z
  (quadratic) and g_couple = 0. In the Aaronson–Gottesman Hermitian section the CNOT update is cubic.
- **Gem: the C-inverting loophole.** With C = ℤ₄, C-inverting (antiunitary-type) lifts of the swap alone can have an
  additive update (32 of 128 at n = 1; at n = 2, 64 sections f₁ complete). But no section makes any pair from {swap_A,
  swap_B, couple} additive simultaneously, nor the whole family, under any of the 8 trivial/inverting assignments
  (exact ℤ₄ elimination). The single-map controls are solvable, so the solver is not vacuous.
- **Consequence, scoped to the displayed realization.** Main.md:290's update is linear over F₂, and Lemma 2(iii) acts on
  Weyl operators "with no phase". Reproducing the G1 sign structure needs either a phase cell with a degree-2 update in
  the phase-space cells, which the displayed realization does not contain, or a ℤ₄ cell together with still-nonlinear
  dynamics.
- **What Main.md:320 covers.** Its ℤ_q is the cell alphabet:
  - Lemma 1 holds over ℤ_q;
  - the symplectic and Clifford arguments extend to prime q;
  - composite q (so ℤ₄) "is not covered".

  It provides no phase group.
- **Contrast at odd prime q** (q = 3, n = 1, exact over all of Sp(2, 3)). β = ω/2 has commutator ω and is invariant
  under every symplectic map, so every map lifts with zero phase update. The q = 2 obstruction is specific to
  characteristic 2.

**(II) Ontic level.** Take the card cells plus one extra F₂ cell h, with every card map extended affinely:
s′ = S s + t h, h′ = h + λ·s + k. That gives 272 bijective extensions per map. Initial h ∈ {0, 1, uniform}, and reads
either leave h alone or refresh it.
- 1491 to 5429 models (by variant) pass **both** K-G1 witnesses with QM's values.
- **0** are equivalent to QM on all words over {swap_A, couple, read q_A, read q_B}.

So within this one-cell affine class the sign structure is not realizable. The witnesses alone are easily matched by
tuning, which is exactly what §A.29 rejects, and the full-table comparison is the decisive control.

***

## 3. Alternative principles (`alt.out`)

- **Alt-1: associative and covariant, with minimal phase group, commutator not prescribed.**
  - The card group (order 72) preserves exactly 2 alternating forms, 0 and ω.
  - Minimal C (trivial) forces commutator 0, i.e. the cards.
  - The abelian ℤ₂ branch admits 1 class with 16 non-inner lifts per map. Over 4096 triples: 4 ≡ cards, 0 ≡ QM, 4092
    other, and the witnesses split 1024 / 1024 / 1024 / 1024.
  - Verdict: **permits**. If anything, minimality selects the cards, and QM must be chosen by hand.
- **Alt-2: commutator ω, and the lifts form a faithful copy of the card group (no new identities).**
  - 16 of 4096 lift triples are splittings, for both C.
  - **None ≡ QM, none ≡ cards.** (W6, W7) is (0, 1) or (1, 0), 8 each; never (1, 1).
  - The QM/ERT lifts generate order 1152 ≠ 72, so QM is not a splitting.
  - Verdict: **fails**, since it excludes QM.
  - The positive content (a postdiction): QM's composition makes the card-identity word (swap_A, couple)⁴ act as a flip
    of q_B's record (`predictions.out`). The cards return q_B = 0; QM gives 1.

## 4. Hidden assumptions (gem-finding, §A.31)

| # | assumption | test | finding |
|---|---|---|---|
| H1 | the choice of C | ℤ₂ vs ℤ₄; odd C | Same verdicts for ℤ₂ and ℤ₄. Odd C is impossible. ℤ₄ is needed only if the phase map is a generator (**NEW**: C = ℤ₂ and the p ^= q map are incompatible with the coupling) |
| H2 | dynamics act trivially on C | ℤ₄ inverting lifts | Witness counts ×4, QM-equivalent ×8 (invisible on the real family). Opens a single-map linear phase update, but not for any pair (**NEW**, bounded) |
| H3 | the same read rule across extensions | — | For nonabelian E the commutativity of S forces the centralizer rule. The involutive-lift requirement is itself class-selecting (**POSITIVE**: a second, independent route to the class) |
| H4 | the card operations are the right generators | drop swap_B; add phase | {swap_A, couple} alone leaves 2 classes (one killed by H3). The phase map kills ℤ₂ and makes ERT ambiguous (**ELABORATING**) |
| H5 | lift convention | all lifts; ERT; 840 bases | The principle fixes the lifts only up to the Pauli frame. QM's witness value enters through ERT, which coincides with the convention defining the calibration circuit (**NEW**: G1's "forcing" of the witness is convention-dependent; the generated theory is forced) |
| H6 | dictionary of value-0 lifts | all 16 | Irrelevant under ERT (**POSITIVE**) |
| H7 | witnesses as the decisive test | full table; (II) | K-G1 is necessary but weak. Thousands of tuned affine models and 64 lift pairs match both witnesses (**NEW**: the K-G1 pair must be paired with a full-table equivalence control) |
| H8 | composition lifts the card group faithfully | Alt-2 | Faithful lifts exclude QM. QM needs the kernel (flips generated by swap and couple) (**NEW**) |

## 5. Bounds

- n ≤ 2 systems; C ∈ {ℤ₂, ℤ₄}; central extensions only.
- Generators: {swap_A, swap_B, couple, flips, reads of q}, plus the phase map as a probe.
- n = 2 classification completeness is [W] beyond n = 1 brute force.
- The group-identity check is sampled (18 of 4096 triples), backed by an algebraic argument.
- (II) uses one extra cell, with the V-part fixed to the card map and the witness alphabet only.
- Two complete runs of `run_all.sh` give byte-identical outputs. Total runtime is about 2 minutes per run.
