# G1 hypothesis H-LOC: local lifts plus longest card agreement

**DRAFT — NOT FROZEN; design specification; no computation may run against it as a test.**

A candidate that a later node could preregister, for gap G1 only (a composition rule for joint records). Drafted
2026-10-21 after independent review REVIEW-G1-8d90f77e of `G1-REPORT.md` and `coordinator/COORDINATOR-NOTE.md`.
Nothing here has been tested against the hypothesis as stated. Every result quoted was computed before this draft and
is therefore a control or a disclosed prior, not evidence for it.

Status tags: **[exact]** computed with exact arithmetic, file named; **[read-off]** read from a committed output, not
separately computed; **[arg]** algebraic argument, checked by the review; **[hyp]** part of the hypothesis, untested;
**[corpus]** a statement of `papers/Main.md`; **[open]** not available.

## Statement

Organized by the owner's declarations (`../../NOTES.md`, last section). The owner's item 4 (family and convergence) is
answered by the scope, and item 5 (an independent consequence) by the consequences below; the correspondence form is
declared here as item 5 because it decides the outcome.

1. **Dynamics and resource model.** [hyp]
   - *Systems.* n card systems (n = 2, and n = 3 for the new test), each a visible card q_j and a hidden card p_j.
     Card operations: swap_j (q_j ↔ p_j); couple_jk (q_k ^= q_j, p_j ^= p_k); the flips of q_j and p_j; read_j. Card
     side as in `g1lib.CardTheory` and `review/eng.py` (`Cards`) [exact, review F12].
   - *Records.* Relation records form a central extension E of V = F₂^{2n} by C ∈ {ℤ₂, ℤ₄} with commutator
     (|C|/2)·ω, in the recordable class (real or complex Pauli) [G1-REPORT §1(a)–(b): exact at n = 1, arg at n = 2;
     n = 3 open].
   - *Lift set.* Every automorphism of E covering the card map: the lifts trivial on C and, for ℤ₄, the C-inverting
     lifts L∘κ. Not taken from QM [review F12, exact for n = 2].
   - *Locality.* The lift of an operation on a set σ of systems is supported on σ: it is Ad(P·U), or Ad(P·U)∘κ, with
     the Pauli frame P acting as the identity outside σ. For n = 2 this restricts the swaps only; for n = 3 it also
     restricts each coupling to its two systems.
   - *Fresh resources.* One fair bit per read, replacing the conjugate (read-with-reset). No reservoir, ancilla or
     memory beyond the n systems and the retained outcome sequence.
2. **One representation across every intervention.** [hyp] One lift per operation, fixed for every word; the flips act
   as value twists (inner automorphisms of E); one read rule for every read; no word-dependent or context-dependent
   choice.
3. **Coexisting records.** [hyp] A record state is an abelian S ⊂ E with |S| = 2ⁿ and S ∩ C = {1}; the read is rule
   (c) of G1-REPORT §1(c). Records in S coexist; a read randomizes the conjugate, so records of non-commuting relations
   do not. Every outcome is retained and every branch is kept. Copying: no primitive beyond couple. Reuse: none.
   Heralding and postselection: not allowed.
4. **Scope.** G1 only, on fixed finite constructions (n = 2, 3); not a completion, so no family or convergence
   criterion. The selected class is stabilizer-type, so K-STAB-GAP is expected to hold (gap ≥ 1/4,
   `../limit/LIMIT-DESIGN.md`, Lemma G). G2 and C5-P are out of scope; no outcome here bears on them.
5. **Correspondence, stated in advance, no free length.** [hyp] *Longest agreement*: let ℓ(t) be the length of the
   shortest word over the alphabet on which lift tuple t and the card theory give different joint record
   distributions (∞ if none). The admitted tuples are those that maximize ℓ.
   - *Why this form.* It has no parameter, and it is the ordinal form of the correspondence principle: the composite
     theory departs from the card theory only where it must. A fixed window L ∈ {5, 6} is rejected because L was chosen
     after the counts were seen [COORDINATOR-NOTE item 4].
   - *Why not P4₁ (at most one coupling).* P4₁ also has no free length, but it is already known to fail without
     swap_B even with local lifts: 32 pass, 16 ≡ QM and 16 with W6 = W7 = 0 [`coordinator/p41_local.out`, exact].
   - *Disclosure.* This choice is informed by known results on the two-system alphabets. Those results therefore
     carry no evidential weight for H-LOC; the weight rests on the consequences below.

## Fixed in advance

**Classes and survival.** Two tuples are in the same class iff they agree on every word over the largest declared
alphabet (exact pair-BFS). A tuple *survives* iff it maximizes ℓ in every declared alphabet, restricted to the
operations that alphabet contains.

**Preserved results (controls; each must be reproduced before any verdict prints).**
- P1, P2, P3: single systems, coupling without swaps, local operations only, each ≡ cards for the selected class, and
  standard QM ≡ cards on each [`controls.out`, `review/subfam.out`, exact].
- The card single-system theory: dimension 3, the diamond state space, read-with-reset [`../../NOTES.md`, owner
  result, coordinator-checked in part].
- K-G1, never tuned: W6 = (swap_A, couple)³ then read q_B, W7 = W6 with one more swap_A. Cards 0, QM 1
  [`controls.out`].
- The engine controls of G1-REPORT (trivial extension ≡ cards; calibration extensions ≡ QM; the direct word-level
  control of `review/direct_ctrl.out`).
- K-STAB-GAP.

**Alternative operation sets it must pass** (two systems). Under locality the outcomes are already known, so these
are preserved-result controls:

| alphabet | survivors of longest agreement, local lifts | source |
|---|---|---|
| full {sA, sB, c, 4 flips, rA, rB} | QM class, ℓ = 7 | `review/extra.out` [exact] |
| without flips | QM class, ℓ = 7 | `review/extra.out` [exact] |
| without swap_B | QM class, ℓ = 7 | `review/extra.out`, `coordinator/nosb.out` [exact] |
| minimal {sA, c, rA, rB} | QM class, ℓ = 7 | `review/extra.out` [exact] |
| K-G1 {sA, c, rB} (not required) | QM class, ℓ = 7 | `review/ident.out` [read-off] |

Without locality, the without-swap_B and minimal alphabets select a non-QM class (ℓ = 10), and the K-G1 alphabet a
cards-equivalent class (ℓ = ∞) [`review/alph.out`, exact]. That contrast is what makes locality the load-bearing
premise. C-inverting lifts multiply every count by 8 and change no survivor class [review F8, arg].

**Independent consequences beyond W6/W7.**
- *New test (primary): three systems.* [hyp] Systems A, B, C; alphabet {swap_A, swap_B, swap_C, couple_AB,
  couple_BC, the six flips, read_A, read_B, read_C}, and the same alphabet without flips, without swap_C, and without
  swap_B and swap_C. Under locality each swap has 4 lifts and each coupling 16, so 4³ · 16² = 16384 tuples trivial on
  C. Prediction: longest agreement leaves exactly one class, and that class ≡ standard three-qubit real-stabilizer QM
  (H_j, CNOT_AB, CNOT_BC). Here locality restricts the couplings for the first time, so the outcome is not implied by
  the two-system results. The value of ℓ for the QM class is not predicted and not computed.
- *Postdiction (weak).* The card identity word (swap_A, couple)⁴ acts on records as a flip of q_B: the cards return
  q_B = 0, QM gives 1 [`predictions.out`, `d_witness.out`, exact]. It is implied by the full-table equivalence of
  the selected class with QM, so it is not independent of the controls.

**Decision rule** (outcomes printed only over green controls; verdict text generated from the measurements).
- *Forces*: the survivors form exactly one class. A separate line reports whether that class ≡ standard QM and gives
  W6 = W7 = 1; H-LOC predicts both.
- *Permits*: the survivors form more than one class.
- *Fails*: no tuple survives in every declared alphabet.
- Two-system declared alphabets: forces, QM class [known, controls]. Three-system: to be measured.
- H-LOC is refuted for G1 if the three-system outcome is permits, fails, or forces a class that is not ≡ QM.

**Hard-to-vary statement.** Frozen together, with no fallback: the lift set, the locality definition (support on the
operation's systems, couplings included), the longest-agreement form, the declared alphabets, the class and survival
definitions, and the decision rule. After a failure none of these is adjusted: no switch to P4₁ or to a length window,
no exemption of couplings from locality, no dropped alphabet, no added operation. An outcome that any of those
adjustments would rescue is a refutation of H-LOC as stated.

## What H-LOC needs from OI and does not yet have

- *A quadratic phase-cell update.* At q = 2 a lift of the swap is never affine in any section, and the minimum degree
  over sections is 2 (real section: g_swap = x z, g_couple = 0) [G1-REPORT §2(I), exact for n ≤ 2; arg, review F10].
  Main.md's displayed update is linear over F₂ (Main.md:290) and Lemma 2(iii) acts "with no phase" (Main.md:300)
  [corpus]. The displayed realization does not supply the update [open].
- *Or the q = 3 route.* At odd prime q every symplectic map lifts with zero phase update [G1-REPORT §2, exact for
  q = 3, n = 1], and Main.md:320 extends the symplectic arguments to prime q [corpus]. That route needs a q = 3 card
  theory and its own composition witness, neither of which exists here [open].
- *A ℤ₄ cell.* The other option (Main.md:320: composite q "is not covered") still needs nonlinear dynamics
  [G1-REPORT §2, exact for n ≤ 2].
- *A physical reading of locality.* That a lift's Pauli frame stays on the systems the operation touches is natural
  for a local substratum update, but no OI result yet derives it [open].
