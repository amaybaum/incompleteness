# Coordinator check of G1-REPORT (2026-10-21): a correspondence requirement removes the lift ambiguity

Exploratory design evidence; unreviewed. The arithmetic is exact: integer amplitudes scaled by powers of √2, and
probabilities as Fractions. The scripts and outputs are in this directory.

**Lift model.** For each of swap_A, swap_B and couple, the lifts are the 16 Pauli-frame twists P·H_A, P·H_B and P·CNOT.
These are the lifts that act trivially on C, unique up to inner automorphism, matching G1-REPORT §1(b). The ℤ₄
inverting lifts are not modelled; G1-REPORT finds them invisible on these real states. Flips lift to Paulis. Reads are
Z-projections of the relevant system.

1. **The report's 64/64/64/64 witness split reproduces** over the 16 × 16 (swap_A, couple) lift pairs (`lifts.out`).
2. **One example in G1-REPORT is wrong.** The report says replacing H by H·Z gives W6 = 0, but H·Z, Z·H and every
   twist supported on A alone give W6 = 1 (`lifts.out`). The witness changes only under twists with a factor on B.
   For swap_A, such a twist is not supported on A, so it is not a local lift of a local operation. With the swap lifts
   restricted to A, the witness still depends on the couple twist (`local.out`, `local2.out`).
3. **Correspondence requirement**, of the kind §A.29 already asks a revision to state in advance: the lifted theory must
   reproduce the existing card theory on every protocol up to length L. The protocols are words over {swap_A, swap_B,
   couple, the four flips, read_A, read_B}, starting from both visible cards at 0 and the hidden cards uniform, with the
   full outcome-record distribution compared exactly. Lift triples (swap_A, swap_B, couple) passing, out of 4096
   (`corr.out`):

   | L | words | triples passing | their W6 values |
   |---|---|---|---|
   | 2 | 90 | 256 | 128 give 1, 128 give 0 |
   | 3 | 819 | 64 | 32 give 1, 32 give 0 |
   | 4 | 7380 | 8 | all give 1 |
   | 5 | +59049 | 4 | all give 1 |

   - At L = 5, four of the eight L = 4 survivors fail first on `sA sB c sA rA` (`corr3.out`).
   - The four L = 5 survivors equal standard QM on every length-5 word and on 20,000 random length-7 words
     (`corr2.out`). This agrees with G1-REPORT's count of 4 triples ≡ QM, one relabelling class.
   - All four give W6 = W7 = 1, the quantum value; the cards give 0 (`survivors.out`).
4. **Reading.** Within this construction, two requirements together fix the theory and the witness value without taking
   the lift from QM:
   - the stated principle (records form a central extension with commutator ω, and the dynamics lift to it);
   - preservation of the card theory's predictions on every protocol of length ≤ 5.

   QM's first disagreement with the cards is at length 7 (G1-REPORT), so any L of 5 or 6 gives the same unique class,
   and L ≥ 7 is unsatisfiable. The free choice the report calls a convention (ERT) is the one the correspondence
   requirement selects.
5. **Skepticism (§A.31).**
   - The outcome is favourable, so it needs independent review before it is used.
   - Open points:
     - whether a length bound is the right form of correspondence, as against the sub-families P1–P3 of G1-REPORT;
     - whether the result depends on the alphabet, for example including the flips;
     - that the length-7 equivalence is sampled rather than exhaustive;
     - that only lifts trivial on C are modelled.
   - None of this addresses G2. K-STAB-GAP still holds: Bloch components are only 0 and ±1.
