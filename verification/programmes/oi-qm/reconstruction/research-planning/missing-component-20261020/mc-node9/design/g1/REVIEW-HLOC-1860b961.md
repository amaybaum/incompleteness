> **Redaction note (committed copy).** The reviewer's session-scratchpad path has been replaced by `<reviewer scratchpad>` (1 occurrence). Nothing else is changed. Of the scratch scripts, `lifts_b1.py`, `restrict.py`, `kg1_local.py` and `nearmiss.py` are committed, with re-run outputs, in `review/` beside this file; their import line was changed from the scratchpad path to the script's own directory, and `eng.py` there is identical to the reviewer's copy.

# Independent pre-freeze review: H-LOC draft at 1860b961 (draft PR #885)

Reviewer: independent, read-only, using the §A.31 gem-finding mode with maximum skepticism toward the favourable reading.
- Worktree: detached at `1860b961d6f281ea769c1a2c1d68fddf41542432`, removed afterwards.
- File reviewed: `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/g1/G1-HYPOTHESIS.md`. Line numbers below are its lines, cited as `H:n`.
- Replay: `SHA256SUMS` (g1, 20 entries), `review/` and `coordinator/` all check OK.
- What was not run: the n = 3 prediction, any n = 3 word or distribution, and any re-costed metric at any n.
- Scratch scripts and outputs: `<reviewer scratchpad>/revhloc/`.

## Disposition: **REVISE (blocking)**

Would a successful run mean what the draft says? Not yet, for three reasons:
1. The n = 3 "new test" is largely implied by the n = 2 results. A restriction argument (F2) shows that on three of the five n = 3 alphabets the outcome depends only on how early three-qubit QM departs from the cards. That is a fact about QM, and the selector plays no part in it.
2. The robustness test D2 has no open content at n = 2. Its n = 2 outcome follows from committed outputs under every reading (F1). In the drafted form it survives only because the intersection mixes two metrics.
3. "≡ standard QM" is not operationally defined (F5).

Is the package fixed tightly enough? Not yet:
- There is a void-and-rerun path with no rule (F6).
- The compound sc is chosen asymmetrically at n = 3 (F3).
- The D2 refutation clause does not say whether an empty or multi-class result counts as "a different class" (F1).
- Several stated invariants have no checkpoint, and no control has a mutant (F4).

What does hold: all six owner requirements are addressed in substance, and every count I could check exactly is correct (4 lifts per swap, 16 per coupling, 16384 tuples, κ fails B1, the K-G1 local row).

## Findings

### F1 (blocking). D2 at n = 2 is settled by committed outputs; the drafted invariance holds there only by mixing metrics

Evidence: `H:112–119`, `H:137–138`. I derived this from committed base-metric outputs and algebra. No re-costed ℓ was computed for any tuple. Triples are indexed as in `review/eng.py` (P = PAULI[4a+b]).

- **(i) ℓ_QM = 4 under re-costing (a).**
  - Upper bound: W6 = (sc)³ r_B costs 4, and every QM-class tuple disagrees with the cards on W6 (`coordinator/survivors.out`).
  - Lower bound: a word whose expansion has base length m contains at least one read, so it holds at most ⌊(m−1)/2⌋ sc letters and costs at least m − ⌊(m−1)/2⌋. The QM class has base ℓ = 7, so m ≥ 7 and the cost is at least 4.
- **(ii) The four local near-miss triples also reach 4 under (a).** These are (0,0,8), (0,3,0), (12,0,8) and (12,3,0).
  - In the base metric they have ℓ = 5 on both the full and the no-flips alphabets (`review/extra.out`).
  - They fail first on `sA sB c sA rA` (`coordinator/corr3.out`). I re-checked that, and that `sB sA c sA rA` gives the identical distribution (`nearmiss.out`, exact). That word contains an adjacent sA, c pair, so it costs 4 under (a).
  - No cheaper word exists. A word of cost 3 or less needs base length at least 5, and must contain:
    - sB, because on sB-free words a near-miss acts as the QM triple with the same (sA, c), which agrees with the cards through length 6;
    - a read;
    - at least two sc letters.

    That is at least 4 letters, so ℓ^(a) = 4.
  - Every other local triple has base ℓ ≤ 4, so its ℓ^(a) is also at most 4.
- **(iii) Re-costing (b) is not a re-costing.** The expansion of flip p_j is a word over full∖{flip p} at its natural base length. So ℓ^(b) is just ℓ over the alphabet "full without the p-flips" at unit cost.
  - That alphabet sits between full and no-flips, so for every tuple ℓ_full ≤ ℓ^(b) ≤ ℓ_noflips.
  - At n = 2 the QM class has ℓ = 7 on both sides, and every other local triple has ℓ_noflips ≤ 5. So (b) is invariant at n = 2 from existing data.

**Consequences.**
- *Metric dependence is already shown at n = 2.* Under (a), Surv(full) contains at least the QM class and the near-miss class. This is exactly the "changed class" of owner requirement A2.
- *The drafted form passes only by masking.* In the draft, only the full alphabet is re-costed and the intersection is compared. The intersection stays the QM class only because the base-metric Surv(no flips) removes the near-miss tie.
- *The uniform form is refuted.* Suppose instead the metric is re-costed in every alphabet that contains sA and c. Then the near-miss class ties QM in full^(a) and in no-flips^(a), and it coincides with QM on every sB-free alphabet. The intersection can then never be exactly the QM class, so the invariance claim is refuted at n = 2.
- *Net effect.* Neither (a) nor (b) can refute H-LOC at n = 2 in the drafted form, so the n = 2 clause of `H:137–138` is empty. Whichever reading is frozen, its n = 2 result is now known.
- *The refutation wording is incomplete.* "D2 selects a different class" does not say whether an empty or multi-class D2 intersection counts.

**Required.**
- Move D2 at n = 2 into the disclosed priors, with the derived values.
- Fix the D2 claim on grounds that do not depend on any outcome. My recommendation is in Q2.
- State refutation as: "the D2 outcome is anything other than *forces* with the base-metric class."

Replacement for `H:115–119` (recommended scoped form):
> *Metric scope, stated beforehand.* H-LOC is a claim about the unit-cost primitive metric. The selection is known to
> depend on the metric at n = 2: with sc at cost 1 the QM class has ℓ = 4 and the four near-miss triples also reach 4,
> so Surv(full) under (a) holds at least two classes [arg from `review/extra.out`, `coordinator/corr3.out`; disclosed
> prior]. D2 is reported per alphabet and as an intersection at n = 3, with the compound family of F3 applied to every
> alphabet containing its constituents. D2 does not decide H-LOC. The verdict names the metric as part of the package.

Delete "or if D2 selects a different class at n = 2 or n = 3" from `H:137–138`.

### F2 (blocking). The n = 3 prediction is largely implied by the n = 2 results

Evidence: `H:124–128` ("the outcome is not implied by the two-system results"); owner declaration 5 (`NOTES.md`, last section).

**The restriction bound.**
- Under B1, every local n = 3 lift restricts to an n = 2 lift on AB and on BC.
- The AB and BC sub-alphabets of the n = 3 full alphabet are copies of the n = 2 full alphabet with the third system idle.
- Hence ℓ₃(t) ≤ min(ℓ₂(t|AB), ℓ₂(t|BC)) for every tuple t.

**Exact check** (`restrict.out`, lift algebra only):
- Of the 16384 local tuples, exactly 8 have both restrictions in the n = 2 QM class.
- Those 8 are exactly Ad(W) std₃ Ad(W)⁻¹ for W ∈ ⟨Z_A, Z_B, Z_C⟩.
- Every other local tuple restricts to a non-QM n = 2 triple, and every non-QM local n = 2 triple has ℓ ≤ 5 (`review/extra.out`). So every other tuple has ℓ₃ ≤ 5.

**What this decides:**
- *Full alphabet.* Surv(full, n = 3) is the 8-tuple QM class whenever ℓ_QM,3 ≥ 6. ℓ_QM,3 is at most 7 and measures when three-qubit QM first departs from the cards; it involves no selection.
- *Without flips and without swap_C.* The same holds. The BC restriction of the no-swap_C alphabet is a copy of the n = 2 no-swap_B alphabet, whose non-QM local triples have ℓ ≤ 5.
- *K-G1 at n = 3.* Its outcome is identical to the n = 2 K-G1 local selection.
- *Without swap_B and swap_C.* This is the only alphabet where the selector has new content.
  - The BC words {cBC, flips, reads} cannot see the Z-type coupling twists: by P2, 4 coupling lifts are ≡ cards.
  - So the B1-local lifts CNOT_BC·Z_C and CNOT_BC·Z_B Z_C lie outside the QM class and are separated from it only by three-system words.
  - Such words exist: sA and cAB carry X_A into B, and cBC carries it into C.
  - This is also where locality of the couplings does its first real work.

Replacement for `H:127–128`:
> By restriction (K-RES), every local tuple outside the 8-tuple QM class has ℓ ≤ 5 on the full, no-flips and
> no-swap_C alphabets, so there the outcome depends only on whether three-system QM first departs from the cards at
> length ≥ 6, a property of QM and the cards. The selector-dependent content of the n = 3 test is the alphabet without
> swap_B and swap_C, where the coupling twists CNOT_BC·Z_C and CNOT_BC·Z_B Z_C are B1-local, outside the QM class, and
> separated from it only by three-system words. The K-G1 alphabet at n = 3 reproduces the n = 2 K-G1 selection. ℓ for
> the QM class is not predicted.

Add to the prediction: "the forced class consists of exactly the 8 local tuples Ad(W) std₃ Ad(W)⁻¹, W ∈ ⟨Z_A, Z_B, Z_C⟩."

The owner should then decide whether this residual content meets §A.29's requirement of an independent prediction. If it does not, add a three-system alphabet that the restriction bound cannot decide, generated by a stated rule (see N3) and fixed before freeze.

### F3 (blocking). The compound sc is asymmetric at n = 3

Evidence: `H:107–108` defines sc only as swap_A then couple_AB.
- QM's base-metric distinguishing words lie on AB, so (a) lowers QM's ℓ to at most 4.
- A competitor whose distinguishing words lie on BC is not compressed. For example, a tuple with QM-class AB restriction and near-miss BC restriction has ℓ₃ ≤ 5 through `sC sB cBC sB rB`-type words.
- So the choice of which pair to compound tilts (a) against QM in a predictable way. This is a free choice of the kind §A.29 rejects.

Replacement:
> sc_jk denotes swap_j then couple_jk, for every declared coupling (sc_AB at n = 2; sc_AB and sc_BC at n = 3), each
> represented by the composite of its constituents' lifts.

### F4 (blocking). §A.41: invariants without checkpoints, and no mutants

Evidence: `H:140–154`. Missing checkpoints:
- **K-E3**: E at n = 3 is built exactly for each C, with the right commutator and the recordable class. The class is unique at every n [arg]: for ℤ₂, q is fixed by q(X_j) = q(Z_j) = 0; for ℤ₄, q̄ = 0. Every declared map lifts.
- **K-ENG3**:
  - the trivial extension ≡ a direct three-card simulation on every word;
  - std₃ ≡ an independent exact three-qubit stabilizer simulator (the review engine extended) on every word over the full n = 3 alphabet.

  The engine controls in `H:91–92` are n = 2 only.
- **K-QM3**: the definition in F5.
- **K-RES**: ℓ₃(t) ≤ min(ℓ₂(t|AB), ℓ₂(t|BC)) for every tuple and alphabet, with the 8-tuple identity of F2. This is a free cross-check of the n = 3 engine against the n = 2 engine.
- **K-Z24**: the ℤ₂ and ℤ₄ engines give equal ℓ_A(t) for every trivial-on-C tuple and every alphabet. They are equal by the real-subgroup argument, so a disagreement is an engine error and voids the run. It does not count as a refutation "for either C".
- **Item 2** (one lift per operation, fixed across words): a check that each automaton is built from a single lift table per operation.

Mutants or sensitivity tests, one per control:

| control | mutant or sensitivity test |
|---|---|
| K-B1 | The record algebra without C must admit the κ-type lifts with local P: 4 per swap and 16 per coupling (computed, `lifts_b1.out`). A P with spectator support must be rejected. |
| K-D1 | An sc built from a lift other than the tuple's own must change some ℓ. sc at cost 1 must give ℓ_QM = 4. |
| K-κ | A ℤ₄ record group containing i·X_A Z_A, on which a κ-type lift and its partner differ. |
| K-REP | Altering one printed Surv must change the regenerated verdict. |
| K-RES | A non-local cAB (Z_C factor) must be refused by the restriction map. |
| K-W, K-KG1 | Already carry their sensitivity: cards ≠ QM, and the non-local K-G1 row. |

### F5 (blocking). "≡ standard real-stabilizer QM" is not defined at n = 3

Evidence: `H:17`, `H:126`, `H:134–137`. Replacement:
> ≡ QM means exact pair-BFS equivalence, on every word of every length over the full n = 3 alphabet, of the class
> representative with std₃ = (H_A, H_B, H_C, CNOT_AB, CNOT_BC) in the extension engine, cross-checked against an
> independent exact stabilizer simulator; the forced class must consist of exactly the 8 Z-frame conjugates (K-QM3).

Without this definition, a forced class that is equivalent to QM on some alphabets only, or up to a relabelling, could be read as "≡ QM".

### F6 (blocking). A void run has no rule, and the order of checks is not fixed

Evidence: `H:138`, "a red checkpoint voids the run, which then bears on nothing".
- K-D1 at n = 3 and K-EXACT print only after the n = 3 ℓ values exist. So a void can be declared after the outcome is visible, and nothing governs the rerun. This is a path from a negative outcome to a "void", then to a modified rerun.

Replacement:
> Order: K-PRES, K-W, K-KG1, K-E3, K-ENG3, K-B1, K-B2, K-κ and K-RES run and print before any n = 3 Surv is computed;
> a red one stops the run before selection. A void run is retained with all outputs. A rerun is admissible only for an
> implementation defect named with a failing mutant, through an append-only amendment that changes no frozen element;
> the void run's n = 3 outputs are published beside the rerun's, and any difference between their verdicts is reported.

### F7 (blocking, text). K-B1 must enumerate the lift set by brute force

Evidence: `H:150`. "Local sets by element-wise check on R_σ̄" does not say where the candidate set comes from. If it is generated from the Ad(P·U) formula, an error in that formula (Q5) cannot be caught. Replacement:
> The candidate lifts of each operation, for each C, are enumerated by brute force over generator images (every
> assignment of X_k, Z_k and, for ℤ₄, i to their fibres, kept iff it is a bijective homomorphism), independently of the
> Ad(P·U) formula, and compared with {Ad(P·U)} ∪ {Ad(P·U)∘κ} as sets. Expected at n = 3, both C: 64 lifts trivial on C
> per operation (and 64 C-inverting for ℤ₄); B1-local 4 per swap, 16 per coupling, 0 C-inverting; product 16384.

I ran this enumeration (`lifts_b1.out`, 15 s); every expected value holds.

### Non-blocking

- **N1. The κ rule's justification** (`H:39–43`). The conclusion is exact: no C-inverting lift is B1-local, for any operation, at n = 2 or 3. The stated reason needs tightening.
  - Under the mutant record algebra ⟨d(X_k), d(Z_k)⟩, which drops C, κ-type lifts with local P do pass. So the exclusion rests entirely on the composite record i·d(X_k)d(Z_k), equivalently on C ⊂ R_τ.
  - For the n = 2 coupling, which has no spectator, the exclusion rests on the stipulation R_∅ = C alone.

  Replacement for `H:41–43`:
  > *Rule for κ.* Every C-inverting lift moves i, and for a spectator k it fixes d(X_k), d(Z_k) only if it sends
  > i·d(X_k)d(Z_k) to its value-1 partner, so it fails B1 for every operation with a spectator. For an operation with no
  > spectator (the n = 2 coupling) the exclusion is the stipulation R_∅ = C. At n = 3 every declared operation has a
  > spectator. The rule rests on the single centre shared by all systems (the central-product form of E), which is
  > part of the package [assumption-watch].
- **N2. D2(b)** is a sixth alphabet bounded between full and no-flips (F1(iii)). It is not a metric test. It is also asymmetric: it removes the p-flips but not the q-flips. See Q3.
- **N3. The n = 3 alphabet list follows no stated rule.** K-G1 at n = 3 copies n = 2. The n = 2 minimal alphabet {sA, c, rA, rB} has no flip-free n = 3 analogue. State a generating rule, for example images of the n = 2 alphabets under the AB and BC embeddings plus the two-coupling chains, and freeze the list from it.
- **N4.** The verdict's naming list (`H:133`) omits the declared alphabets. Owner requirement 2 names them as part of the package.
- **N5. B2's definition** (`H:44–47`): "reachable" needs a defined set, for example the union over all B1-local tuples and declared alphabets. Owner requirement 4 phrases B2 as indistinguishability under the restricted measurement menu. Either adopt that wording, or state that agreement on record groups implies it.
- **N6.** The ℤ₄ rows at n = 2 (`H:96–102`) come from the real-subgroup argument applied to the ℤ₂ engine. Tag them [arg] and have K-PRES compute them in a ℤ₄ engine.
- **N7. Surv wording** (`H:77`): ℓ_A(t) depends only on t restricted to A, so Surv(A) is already a union of whole cylinders. Replace "restricted to the operations A contains" with "(ℓ_A depends only on the lifts of operations in A)".
- **N8. Rhetoric** (`H:61–62`): "departs from the card theory only where it must" overstates. Replace with "it selects the lifts whose first departure from the card theory is latest".
- **N9. Runtime (§A.40).** The run is roughly 16384 tuples × 2 C × about 9 alphabet and metric variants of pair-BFS or Dijkstra at n = 3, twice. Estimate it, place it in CI, and freeze any symmetry reduction (for example the Z-frame quotient) as part of the engine with its own control.
- **N10.** "Element-wise (not generators only)" (`H:150`) is mathematically equivalent to a generator check; the counts agree (`lifts_b1.out`), so it is not a safeguard. The safeguards that matter are the brute-force enumeration (F7) and the C-free mutant (F4).
- **N11.** `H:104–105` says "multiply every count by 8". That holds at n = 2; at n = 3 the factor is 2⁵ = 32, giving 524,288. State both.
- **N12.** The ℤ₂ and ℤ₄ runs are not independent tests: they are equal by argument (K-Z24). Say so in `H:136`.
- **N13.** `H:31` says "n = 3 open". The recordable class is unique at every n given the classification sequence [arg], and K-E3 checks the n = 3 instance.
- **N14. K-G1 local row: confirmed exactly** (`kg1_local.out`).
  - Over the 64 local (sA, c) pairs, ℓ = 7 is the maximum, and exactly the 4 QM pairs reach it.
  - The next value is ℓ = 6, reached by 4 pairs with c ∈ {Z_B·CNOT, Z_A Z_B·CNOT}.
  - Change "[read-off]" to [exact], commit the output, and record the margin of 7 against 6.

## Answers to the author's questions

**Q2. Is invariance the right claim? Should D2 at n = 2 be computed before freeze?**
- *Should it be computed?* In the draft's framing, no. D2 at n = 2 is a declared refuter, and computing it would let the invariance clause be chosen after its outcome was seen. I did not compute it.
- *The question is now moot.* The outcome follows from committed outputs (F1), so D2 at n = 2 is a disclosed prior, not a test. "D2 can refute H-LOC already at n = 2" is false for the drafted form. It is also unnecessary to compute anything to check that the claim is well-posed:
  - ℓ under a cost assignment is a minimum-cost path in a finite pair automaton with positive integer costs, so it always exists;
  - what is needed is to fix the comparison object (per-alphabet and intersection), the tie rule, and which alphabets are re-costed.
- *Is invariance right?* Three options:
  - **(A)** Uniform invariance, with every alphabet re-costed. This is false at n = 2 by F1, so it cannot be frozen as an untested claim.
  - **(B)** The drafted form, with only the full alphabet re-costed. It holds at n = 2 only because a base-metric alphabet in the same intersection removes the tie. That mixes metrics, which is not principled.
  - **(C)** Scope H-LOC to the unit-cost primitive metric, disclose that the metric dependence is already shown at n = 2, and report D2 at n = 3 per alphabet and as an intersection, using the symmetric compound family.

  I recommend (C). Owner requirement 3 allows it, provided it is stated beforehand. It narrows the claim rather than rescuing it. The cost is that the n = 3 primary prediction becomes the only refuter, which makes F2 more pressing.

**Q3. Are the n = 3 K-G1 alphabet and D2(b) well-motivated, or arbitrary?**
- *K-G1 at n = 3 ({swap_A, couple_AB, read_B}, C idle)* is motivated by requirement 1. It is not arbitrary, but at n = 3 it carries no information: its selection is identical to n = 2. If K-G1 should do work at n = 3, declare a three-system analogue by a stated rule, for example {sA, cAB, cBC, rC}.
- *D2(b)* has a sensible motivation: operations on hidden cards are reachable only through swaps. But it is an alphabet deletion bounded between full and no-flips. It is invariant at n = 2 from existing data, and at n = 3 it can only differ when ℓ_QM differs between the full and no-flips alphabets. It also treats p-flips and q-flips asymmetrically. Reclassify it as an alphabet ("full without hidden flips") or drop it; it is not a metric test.

**Q4. Is K-κ as a structural check adequate?**
Yes, provided three conditions hold:
1. It verifies that every record group reachable over every declared alphabet, for every local tuple, lies in the real subgroup. The pair-BFS enumerates these groups anyway.
2. It states the algebraic facts that κ commutes with the flips and the read update.
3. It carries the mutant of F4.

That is a proof that every κ-type tuple runs the same automaton as its partner, so rerunning the 524,288 tuples would add nothing. Since B1 excludes these lifts, K-κ supports only the ×32 disclosure and the B2 report. Merge it with K-B2, or cross-reference the two.

**Q5. Is K-B1 enough to catch an error in the ℤ₄ n = 3 counts?**
Only with the brute-force candidate set of F7; as worded, it is not. With brute force it suffices, and the counts are correct:

| n | C | lifts per operation (trivial on C / C-inverting) | B1-local | tuples |
|---|---|---|---|---|
| 2 | ℤ₂ | 16 / 0 | swaps 4, coupling 16 | 256 |
| 2 | ℤ₄ | 16 / 16 | swaps 4, coupling 16, C-inverting 0 | 256 |
| 3 | ℤ₂ | 64 / 0 | swaps 4, couplings 16 | 16384 |
| 3 | ℤ₄ | 64 / 64 | swaps 4, couplings 16, C-inverting 0 | 16384 |

**Q6. Is reading the K-G1 local row off `review/ident.out` acceptable?**
As a disclosed prior, yes, and the reading is correct. `ident.out` lists every pair with ℓ ≥ 5 or ∞. The local pairs among them are 4 at ℓ = 6 and the 4 QM pairs at ℓ = 7; no local pair is ≡ cards. The histogram shows every remaining pair has ℓ ≤ 4.

It should not stay a read-off. A wrong frozen expectation in K-KG1 would void the run and open the F6 path. I recomputed the row exactly (`kg1_local.out`, under a second). Commit such an output before freeze, and have K-KG1 recompute it in the run.

## Other checks requested

- **R_τ and composite records.** R_τ = ⟨C, d(X_k), d(Z_k) : k ∈ τ⟩ is the full preimage of V_τ, asserted for every operation, n = 2, 3, both C. For ℤ₄ it contains i·X_k Z_k. It covers every composite record on τ.
- **"No C-inverting lift is local."** Correct within B1, with the qualification of N1. It was checked exactly at n = 2 and n = 3 by brute force, and the C-free mutant shows what the exclusion rests on.
- **"4 per swap, 16 per coupling", 16384.** Correct at n = 2 and n = 3 for both C (Q5 table). At n = 2 the coupling has no spectator, so all 16 of its lifts are local.
- **Decision rule.** The outcomes "forces", "permits" and "fails" partition the possible sizes of the intersection, so they are mutually exclusive and exhaustive. This requires the intersection to be a union of classes; it is, since every alphabet is contained in the full alphabet and the compounds expand into it.

  Paths by which a negative result could be re-read as a success:
  - void, then modified rerun (F6);
  - the choice of D2 reading and its incomplete wording (F1);
  - the undefined "≡ QM" (F5);
  - a divergence between ℤ₂ and ℤ₄ that is ambiguous between an engine bug and a refutation (K-Z24).

  Changes of alphabet, lift set, metric or B2 are blocked by `H:156–160`.
- **Overclaim and register.** The Claim's attribution to the whole package is correct and well bounded (`H:17–21`). The overclaims are the independence sentence (F2), D2 described as a "robustness test" (F1), and `H:61–62` (N8). §A.32 and §A.33 do not apply, since this is not `papers/`. The "What H-LOC needs from OI" section is accurately scoped.

## Exact checks run (scratch directory above)

| script | what it checks | result |
|---|---|---|
| `lifts_b1.py` → `lifts_b1.out` | Brute-force automorphisms over each card map, n = 2, 3, ℤ₂ and ℤ₄; B1 element-wise; generator-only check; C-free mutant; R_τ = preimage; Y_k ∈ R_τ | All draft counts hold; κ-type B1-local = 0; under the mutant, κ-type local = 4 per swap and 16 per coupling (ℤ₄) |
| `restrict.py` → `restrict.out` | Which of the 16384 local tuples have both 2-system restrictions in the n = 2 QM class | 8, equal to the Z-frame conjugates of std₃ |
| `kg1_local.py` → `kg1_local.out` (uses `review/eng.py`) | n = 2 K-G1 alphabet with local swap_A lifts | ℓ_max = 7, the 4 QM pairs only; next ℓ = 6, 4 pairs |
| `nearmiss.py` → `nearmiss.out` | Base metric only: the n = 2 local triples with ℓ ≥ 5, and the reordered witness word | 4 near-miss triples at ℓ = 5; `sB sA c sA rA` distinguishes them, with a distribution identical to `sA sB c sA rA` |

None of these computes an n = 3 word, an n = 3 distribution or a re-costed metric. Total runtime is about 25 s.

## Freeze checklist

- [ ] F1: D2 at n = 2 moved to the disclosed priors with the derived values. D2 claim fixed (recommended: scoped form (C)); refutation wording covers empty and multi-class results; the list of re-costed alphabets is stated.
- [ ] F2: the restriction bound and its consequence stated in advance; the selector-dependent alphabet named; the 8-tuple class predicted; the owner's judgement on §A.29 independence recorded, with a rule-generated three-system alphabet added if needed.
- [ ] F3: symmetric compound family sc_jk.
- [ ] F4: K-E3, K-ENG3, K-QM3, K-RES, K-Z24 and an item-2 check added; a mutant column filled for every control.
- [ ] F5: "≡ QM" defined operationally.
- [ ] F6: run order and void-and-rerun rule.
- [ ] F7: K-B1 brute-force candidate set, with the expected numbers frozen.
- [ ] N1–N14 text fixes, especially the κ-rule wording (N1), B2 definition (N5), K-G1 row as [exact] with a committed output (N14), and the runtime estimate with CI placement (N9).
- [ ] After revision: a fresh independent review of the revised text before the owner designates F.
