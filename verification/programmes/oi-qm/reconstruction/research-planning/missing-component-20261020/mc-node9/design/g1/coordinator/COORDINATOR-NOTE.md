# Coordinator check of G1-REPORT (2026-10-21): card correspondence and the lift ambiguity

Exploratory design evidence. **Provenance.** Corrected after independent review REVIEW-G1-8d90f77e, 2026-10-21; the
changes and the findings they answer are listed under Corrections, at the end. The arithmetic is exact: integer
amplitudes scaled by powers of √2 (numpy object arrays), and probabilities as Fractions. The scripts and outputs are in
this directory, and `run_all.sh` regenerates every output here (about 2 minutes). The reviewer's independent engine
and the scripts behind the alphabet and sub-family tables are in `../review/` (its own `run_all.sh`, about 3 minutes).
Both were run twice with byte-identical outputs (Python 3.13, numpy 2.5.3).

**Lift model.** For each of swap_A, swap_B and couple, the lifts are the 16 Pauli-frame twists P·H_A, P·H_B and P·CNOT.
These are the lifts that act trivially on C, unique up to inner automorphism, matching G1-REPORT §1(b); the review
confirms by brute force that they are all such lifts (`../review/lift_check.out`). Flips lift to Paulis. Reads are
Z-projections of the relevant system. The ℤ₄ C-inverting lifts are not modelled separately; item 3(d) shows they change
no conclusion.

1. **The report's 64/64/64/64 witness split reproduces** over the 16 × 16 (swap_A, couple) lift pairs (`lifts.out`).
2. **One example in G1-REPORT was wrong.** The report said replacing H by H·Z gives W6 = 0, but H_A·Z_A (= X_A·H_A),
   Z_A·H_A and every twist of swap_A supported on A give W6 = 1 (`lifts.out`). The witness changes only under swap_A
   twists with a factor on B, which are not local lifts of a local operation, or under the coupling twists CNOT·Z_B and
   Z_B·CNOT (`local2.out`). With the swap lifts restricted to A, the witness still depends on the couple twist
   (`local.out`). The review reproduces this (F1); G1-REPORT is corrected.
3. **Correspondence requirement, formulated after the enumeration (not preregistered).** The lifted theory must
   reproduce the existing card theory on every protocol up to length L. The protocols are words over {swap_A, swap_B,
   couple, the four flips, read_A, read_B}, starting from both visible cards at 0 and the hidden cards uniform, with the
   full outcome-record distribution compared exactly. L was chosen after the counts below were seen. Lift triples
   (swap_A, swap_B, couple) passing, out of 4096:

   | L | words of length ≤ L | triples passing | their W6 values | source |
   |---|---|---|---|---|
   | 2 | 90 | 256 | 128 give 1, 128 give 0 | `corr.out` |
   | 3 | 819 | 64 | 32 give 1, 32 give 0 | `corr.out` |
   | 4 | 7380 | 8 | all give 1 | `corr.out` |
   | 5 | 66429 | 4 | all give 1 | `corr3.out` (the L = 5 survivors are among the 8 L = 4 survivors, each checked there on all 59049 length-5 words) |
   | 6 | all | 4 | all give 1 | `../review/corr_main.out` (exact pair-BFS) |
   | 7 | all | 0 | — | `../review/corr_main.out` |

   - At L = 5, four of the eight L = 4 survivors fail first on `sA sB c sA rA` (`corr3.out`).
   - **The four survivors are ≡ standard QM on every word of every length (exact).** Each is Ad(W)∘std∘Ad(W)⁻¹ with
     W ∈ {I, Z_A, Z_B, Z_A Z_B}: (0,0,0) ↔ I, (12,0,0) ↔ Z_A, (0,3,8) ↔ Z_B, (12,3,8) ↔ Z_A Z_B. Each W fixes the |00⟩
     record group and the records ±Z_A, ±Z_B, and commutes with every flip, so it intertwines the two record automata
     and preserves every read probability (`../review/exact_e.out`; exhaustive already in `../d_witness.out`, lines
     39–40). Historical cross-check only: `corr2.out` compared them with standard QM on every length-5 word and on
     20,000 random length-7 words; that sample is not the support.
   - All four give W6 = W7 = 1, the quantum value; the cards give 0 (`survivors.out`).

   **(a) Alphabet dependence.** Triples agreeing with the cards on every word of length ≤ L (`../review/alph.out`;
   local rows `../review/extra.out`). "Local" restricts each swap's lift to its own system (256 triples).

   | alphabet | L = 5–6 | L = 7–9 | L = 10 | maximal agreement length, class |
   |---|---|---|---|---|
   | full | 4, QM | 0 | 0 | 6, QM |
   | no flips {sA, sB, c, rA, rB} | 4, QM | 0 | 0 | 6, QM |
   | no swap_B {sA, c, 4 flips, rA, rB} | 128: QM and a class with W6 = W7 = 0 | 64, non-QM, W6 = W7 = 0 | 0 | 9, non-QM |
   | minimal {sA, c, rA, rB} | 128: QM and a class with W6 = W7 = 0 | 64, non-QM, W6 = W7 = 0 | 0 | 9, non-QM |
   | each of the four, local lifts | QM only (4, or 16 where swap_B is idle) | 0 | 0 | 6, QM |

   - Without swap_B, the 16 swap_B lifts are idle, so 128 triples are 8 (swap_A, couple) pairs. The non-QM class has
     swap_A lift Z_B·H_A or XZ_A Z_B·H_A, both acting on B (`../review/ident.out`).
   - Coordinator re-check, exact, without swap_B (`nosb.py`, `nosb.out`): at L = 5 and 6, 8 surviving (swap_A, couple)
     pairs split 4/4 in W6 with any lifts; with A-local swap lifts, 4 survive, all with W6 = 1.
   - Standard QM's first disagreement with the cards is at length 7 in every alphabet.

   **(b) Sub-family correspondence, all lengths** (`../review/subfam.out`, `../review/extra.out`, `p41_local.out`).
   - P1 ∩ P2 ∩ P3 (single systems; coupling without swaps; local operations only) leaves 16 triples, W6 split 8/8. The
     Z-type twists of the coupling are invisible without swaps, and P3 has no coupling.
   - P4₁ (at most one coupling, any local operations) leaves exactly the 4 QM triples over the full alphabet, and
     standard QM ≡ cards on it. It has no free length. It fails without swap_B: 256 pass (64 ≡ QM) with any lifts, and
     32 pass (16 ≡ QM, 16 with W6 = W7 = 0) with local swap lifts, in both alphabets without swap_B.
   - P4₂ (at most two couplings) is unsatisfiable: standard QM already differs from the cards at `sA c sA c sA rA rB`.

   **(c) C-inverting lifts.** Every inverting lift is L∘κ, with L trivial on C and κ complex conjugation. κ fixes the
   real Pauli subgroup ⟨X_j, Z_j, −1⟩, which contains every reachable record group, so φ(S) = L(S) on every reachable
   state. Every count above is multiplied by exactly 8 (2048, 512, 64, 32, 32, 0 at L = 2, …, 7), and the conclusion is
   unchanged; the 32 survivors match G1-REPORT's 32 (`../d_witness.out`, line 29).
4. **Reading.** Within this construction, with the declared alphabet (both swaps, the coupling, flips optional, both
   reads), the principle plus agreement with the card theory on every protocol of length ≤ L, for L ∈ {5, 6}, leaves
   exactly the QM class (4 triples, one Pauli-relabelling class). Equivalently, QM is the unique lift class with maximal
   card-agreement length (6), the lift class closest to the cards over the full alphabet. The selection fails without
   swap_B: correspondence is then ambiguous at L ≤ 6, and at L = 7–9 it selects a non-local swap_A lift with the cards'
   witness values. Restricting each swap's lift to its own system restores the QM selection at L ∈ {5, 6} for every
   alphabet tested.
   - Locality of the lifts, not the length window, is the load-bearing extra condition. Locality is a new premise and
     was not stated in advance.
   - The condition is not circular: it uses only predictions of the card theory, and the lift set is the abstract lift
     set, not taken from QM (review F12, F13). QM enters earlier, through the principle's commutator ω.
   - L, and the correspondence requirement itself, were chosen after the counts were seen. That is post hoc, not
     preregistered as §A.29 asks. The result is **CONFIRMING** (consistency axis, §A.23), not a derivation.
   - A preregistration would have to freeze one correspondence form (maximal-length agreement or P4₁), the alphabets
     and the locality premise in advance. A draft is `../G1-HYPOTHESIS.md`; it is not frozen.
5. **Skepticism (§A.31).** The open points of the first version are settled as follows: the length bound against
   sub-families (3(b)); the alphabet (3(a)); the length-7 equivalence, now exact (item 3); C-inverting lifts (3(c)).
   Still open: a locality-based form tested on an alphabet or system count not yet computed (three systems); the
   literature check for G1-REPORT's H8. None of this addresses G2. K-STAB-GAP still holds: Bloch components are only 0
   and ±1 (`../controls.out`).

## Corrections (independent review REVIEW-G1-8d90f77e, 2026-10-21)

| finding | change |
|---|---|
| F4 | The reading (item 4) is replaced by the review's wording, and item 3(a) states the alphabet dependence: without swap_B, or with only {swap_A, couple, read_A, read_B}, two classes survive at L = 5–6, only the non-QM class at L = 7–9, none at L = 10; with local swap lifts QM is unique at L = 5–6 in all four alphabets. Added `nosb.py` / `nosb.out`, the coordinator's exact re-check without swap_B |
| F5 | Item 3 now says the requirement was formulated after the enumeration and L chosen after the counts were seen (post hoc, not preregistered); item 4 states the result is CONFIRMING, not circular, and that QM is the unique lift class closest to the cards over the full alphabet |
| F6 | Item 3(b) adds the sub-family result: P1–P3 leave 16 triples split 8/8; P4₁ leaves exactly the 4 QM triples over the full alphabet but fails without swap_B; P4₂ is unsatisfiable. The local-lift P4₁ figure (32, 16 ≡ QM) is re-checked in `p41_local.py` / `p41_local.out` |
| F7 | The 20,000-word sampled statement is replaced by the exact conjugation proof; the sample is kept as a labelled historical cross-check |
| F8 | "Invisible" is replaced by the argument of item 3(c): inverting lifts multiply every count by 8 and leave the conclusion unchanged |
| F11 | `survivors.out` regenerated from `survivors.py` exactly as it prints (it now carries the `passing at L<=4` line); the L = 5 count is cited to `corr3.out`; the words column is cumulative throughout; `run_all.sh` added; `SHA256SUMS` regenerated here and in `..` |
| F1 | Item 2 aligned with the review's statement of the correct variants |
