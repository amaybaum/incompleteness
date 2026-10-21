# G1 hypothesis H-LOC: local lifts plus longest card agreement

**DRAFT — NOT FROZEN; design specification; no computation may run against it as a test.**

A candidate that a later node could preregister, for gap G1 only (a composition rule for joint records), drafted
2026-10-21 after review REVIEW-G1-8d90f77e and revised on the owner's corrections. Every result quoted was computed
before this draft and is therefore a control or a disclosed prior, not evidence for it.

Status tags: **[exact]** computed with exact arithmetic, file named; **[read-off]** read from a committed output, not
separately computed; **[arg]** algebraic argument, checked by the review; **[hyp]** part of the hypothesis, untested;
**[corpus]** a statement of `papers/Main.md`; **[open]** not available.

## Claim

[hyp] Within the declared package (central extensions E of V = F₂^{2n} by C ∈ {ℤ₂, ℤ₄} with commutator (|C|/2)·ω in
the recordable class; the lift set and read rule (c) of the Statement; the declared primitive alphabets and cost metric),
the selector **locality (B1) + longest card agreement** leaves exactly one lift class, and that class ≡ standard
real-stabilizer QM, at n = 2 (known) and n = 3 (new). The selector is the whole package; no part is credited alone.
- A success would establish only that this package selects the real-stabilizer class within that family; not that
  locality alone selects QM (the 256 swap-local triples at n = 2 are not one class, `review/extra.out` [exact]), and
  no OI implementation of the lifts or of locality, nothing for G2, and no full equivalence of OI with QM.

## Statement

Organized by the owner's declarations (`../../NOTES.md`, last section); the correspondence form is item 5 here.

1. **Dynamics and resource model.** [hyp]
   - *Systems.* n card systems (n = 2, and n = 3 for the new test), each a visible card q_j and a hidden card p_j.
     Card operations: swap_j (q_j ↔ p_j); couple_jk (q_k ^= q_j, p_j ^= p_k); flip q_j, flip p_j; read_j. Card side as
     in `g1lib.CardTheory` and `review/eng.py` (`Cards`) [exact, review F12].
   - *Records and lift set.* E as in the Claim [G1-REPORT §1(a)–(b): exact at n = 1, arg at n = 2; n = 3 open]. Lifts:
     every automorphism of E covering the card map, Ad(P·U) (trivial on C) and, for ℤ₄, the C-inverting Ad(P·U)∘κ,
     κ complex conjugation. Not taken from QM [review F12, exact for n = 2; F8].
   - *Locality (B1), defined on the full lift.* For a set τ of systems, R_τ = ⟨C, d(X_k), d(Z_k) : k ∈ τ⟩ ⊂ E is the
     record algebra of τ, composite records included (for ℤ₄, i·d(X_k)d(Z_k)); C lies in every R_τ, and R_∅ = C. A
     lift φ of an operation on σ is *local* iff φ is the identity on R_σ̄, σ̄ the untouched systems. At n = 2 this
     restricts the swaps only; at n = 3 it also restricts each coupling to its two systems.
     - ℤ₂: Aut(C) is trivial; Ad(P·U) is local iff P is the identity outside σ. Local lifts: 4 per swap, 16 per coupling.
     - ℤ₄: Ad(P·U) is local iff P is the identity outside σ (same counts). Ad(P·U)∘κ inverts C and sends each spectator
       record i·d(X_k)d(Z_k) to its value-1 partner, so it fails B1 whatever P is.
     - *Rule for κ.* κ acts on every system at once: it inverts the centre that every R_τ contains and has no
       restriction to a proper subset of systems. So no C-inverting lift is local, for any operation, including one
       that touches every system (the n = 2 coupling). The rule does not depend on n.
     - *B2, reported only.* A lift passes B2 iff it agrees with a B1-local lift of the same card map on every record
       group reachable over the declared alphabets. κ-type lifts with local P should pass B2 and fail B1: κ fixes the
       real subgroup holding every reachable record group [F8, arg], which hides what the complex algebra
       distinguishes. Locality is B1; B2 never substitutes for it.
   - *Fresh resources.* One fair bit per read, replacing the conjugate; nothing beyond the n systems and the outcomes.
2. **One representation across every intervention.** [hyp] One lift per operation, fixed for every word; the flips act
   as value twists (inner automorphisms of E); one read rule for every read; no word-dependent or context-dependent
   choice. A compound letter is represented by the composite of its constituents' lifts.
3. **Coexisting records.** [hyp] A record state is an abelian S ⊂ E with |S| = 2ⁿ and S ∩ C = {1}; the read is rule
   (c) of G1-REPORT §1(c). Records in S coexist; a read randomizes the conjugate, so records of non-commuting relations
   do not. Every outcome and branch is kept. No copying beyond couple, no reuse, no heralding or postselection.
4. **Scope.** G1 only, on fixed finite constructions (n = 2, 3), within the package of the Claim; not a completion, so
   no family or convergence criterion. The selected class is stabilizer-type, so K-STAB-GAP is expected to hold
   (gap ≥ 1/4, `../limit/LIMIT-DESIGN.md`, Lemma G). G2 and C5-P are out of scope; no outcome here bears on them.
5. **Correspondence, stated in advance, no free length.** [hyp] *Longest agreement*: let ℓ(t) be the minimum cost of a
   word over the alphabet on which lift tuple t and the card theory give different joint record distributions (∞ if
   none). In the base metric every primitive costs 1, so ℓ is the shortest such length. The admitted tuples maximize ℓ.
   - *Why this form.* It has no parameter, and it is the ordinal form of the correspondence principle: the composite
     theory departs from the card theory only where it must. A fixed window L ∈ {5, 6} is rejected because L was chosen
     after the counts were seen [COORDINATOR-NOTE item 4].
   - *Why not P4₁ (at most one coupling).* P4₁ also has no free length, but it is already known to fail without
     swap_B even with local lifts: 32 pass, 16 ≡ QM and 16 with W6 = W7 = 0 [`coordinator/p41_local.out`, exact].
   - *What length means: scoped to the declared primitive alphabet.* One unit is one card primitive (one swap of one
     system, one coupling of one pair, one flip, one read). It is not tied to physical resources: no OI result assigns
     a cost to an operation, so "one use of a declared coupling" would assert an underived resource model. Naming a
     compound as one step changes the metric; the description controls test whether that changes the selection.
   - *Disclosure.* This choice is informed by known results on the two-system alphabets. Those results therefore
     carry no evidential weight for H-LOC; the weight rests on the consequences below.

## Fixed in advance

**Classes and survival.** Two tuples are in the same class iff they agree on every word over the largest declared
alphabet at that n (exact pair-BFS). For each declared alphabet A, Surv(A) is the set of tuples maximizing ℓ over A,
restricted to the operations A contains. A tuple *survives* iff it lies in every Surv(A) at its n. The K-G1 alphabet
is **required** in that intersection: without locality it selects a cards-equivalent class (ℓ = ∞) [`review/alph.out`,
`review/ident.out`, exact], so it is the sensitivity control that shows locality doing work.

**Declared alphabets.** n = 2: the five rows of the table below. n = 3: full {swap_A, swap_B, swap_C, couple_AB,
couple_BC, the six flips, read_A, read_B, read_C}; without flips; without swap_C; without swap_B and swap_C; K-G1
{swap_A, couple_AB, read_B} (system C idle). **Reporting:** per C, each Surv(A) (tuples, class labels, ℓ_max), then
the intersection, then the verdict generated from the printed intersection.

**Preserved results** (controls; each reproduced before any verdict prints).
- P1, P2, P3: single systems, coupling without swaps, local operations only, each ≡ cards for the selected class, and
  standard QM ≡ cards on each [`controls.out`, `review/subfam.out`, exact].
- The card single-system theory: dimension 3, diamond state space, read-with-reset [`../../NOTES.md`, owner result].
- K-G1, never tuned: W6 = (swap_A, couple)³ then read q_B, W7 = W6 with one more swap_A. Cards 0, QM 1 [`controls.out`].
- The engine controls of G1-REPORT (trivial extension ≡ cards; calibration extensions ≡ QM; the direct word-level
  control of `review/direct_ctrl.out`). K-STAB-GAP.

**Two-system alphabets** (all required; preserved-result controls, since the outcomes are known):

| alphabet | survivors, local lifts | survivors, without locality | source |
|---|---|---|---|
| full {sA, sB, c, 4 flips, rA, rB} | QM class, ℓ = 7 | QM class, ℓ = 7 | `review/extra.out`, `review/alph.out` [exact] |
| without flips | QM class, ℓ = 7 | QM class, ℓ = 7 | same [exact] |
| without swap_B | QM class, ℓ = 7 | non-QM class, ℓ = 10 | same, `coordinator/nosb.out` [exact] |
| minimal {sA, c, rA, rB} | QM class, ℓ = 7 | non-QM class, ℓ = 10 | same [exact] |
| K-G1 {sA, c, rB} | QM class, ℓ = 7 [read-off] | cards-equivalent class, ℓ = ∞ | `review/ident.out`, `review/alph.out` |

Hence locality is load-bearing within the package. Admitting the κ-type lifts (which fail B1) would multiply every
count by 8 and change no survivor class [review F8, arg].

**Description controls** (full alphabet, n = 2 and n = 3). Let sc denote one letter for swap_A then couple (couple_AB
at n = 3), represented by the composite of the tuple's two lifts (Statement item 2), so no new lift is chosen.
- *D1, correctness control: same cost, new notation.* Add sc at cost 2, the cost of its expansion. Every protocol then
  expands to one of equal behaviour and equal cost, so every tuple's ℓ and every Surv(A) must be unchanged. Any change
  is an implementation or accounting error: the run is void, and the change is never evidence about H-LOC.
- *D2, robustness test: different cost assignment.* Two declared re-costings, ℓ computed as exact minimum cost:
  (a) sc at cost 1; (b) the flips of p_j removed, so each costs its expansion swap_j, flip q_j, swap_j³ (cost 5)
  [arg: in the cards swap_j³ = swap_j; for each lift L = P·H_j, Ad(L)⁴ = id and L X_j L⁻¹ = ±Z_j].
- *Invariance claim, stated beforehand.* H-LOC claims that the intersection, with the full alphabet replaced by its
  re-costed form, selects the same class under (a) and under (b) as under the base metric. A different class refutes
  H-LOC. Why invariance rather than scoping: a selector whose output follows the cost given to a named compound can be
  refitted by choosing costs, the freedom §A.29 rejects, and scoping to the base metric would leave that freedom
  unpriced. The claim covers these two re-costings only, not arbitrary weights.
- Neither D1 nor D2 replaces the n = 3 prediction as the new test: D1 checks the engine; D2 tests a declared
  robustness claim of the package.

**Independent consequences beyond W6/W7.**
- *New test (primary): three systems.* [hyp] The n = 3 declared alphabets. Under B1 each swap has 4 lifts and each
  coupling 16, so 4³ · 16² = 16384 local tuples, for each C. Prediction: under the package, longest agreement leaves
  exactly one class, and that class ≡ standard three-qubit real-stabilizer QM (H_j, CNOT_AB, CNOT_BC). Here locality
  restricts the couplings for the first time, so the outcome is not implied by the two-system results. The value of ℓ
  for the QM class is not predicted and not computed.
- *Postdiction (weak).* The card identity word (swap_A, couple)⁴ flips q_B's record (cards 0, QM 1) [`predictions.out`,
  `d_witness.out`, exact]; implied by the full-table equivalence with QM, so not independent of the controls.

**Decision rule** (outcomes printed only over green checkpoints; verdict text generated from the measurements and
naming the package: B1 locality, longest agreement, the extension family, lift set, read rule and base metric).
- *Forces*: the intersection is exactly one class. A separate line reports whether that class ≡ standard QM and gives
  W6 = W7 = 1; H-LOC predicts both. *Permits*: more than one class. *Fails*: the intersection is empty.
- n = 2: forces, QM class [known, controls]. n = 3: to be measured, for ℤ₂ and ℤ₄ separately.
- H-LOC is refuted for G1 if, for either C, the n = 3 outcome is permits, fails, or forces a class not ≡ QM; or if D2
  selects a different class at n = 2 or n = 3. A void D1 or a red checkpoint voids the run, which then bears on nothing.

**Invariant → checkpoint** (§A.41).

| invariant asserted | checkpoint |
|---|---|
| preserved results reproduce (P1–P3, card theory, engine controls, K-STAB-GAP) | K-PRES |
| K-G1 witnesses untuned: cards 0, QM 1 | K-W |
| item 1: K-G1 in every intersection; its local row (QM, ℓ = 7) and non-local row (cards-equivalent, ℓ = ∞) reproduced exactly | K-KG1 |
| item 2: verdict names the whole package; the n = 2 without-locality rows printed beside it | K-ATTR |
| item 3, D1: ℓ and every Surv(A) unchanged with sc at cost 2; otherwise void | K-D1 |
| item 3, D2: the expansion of flip p_j exact in the cards and every local tuple; intersection under (a), (b) compared with base | K-D2 |
| item 4, B1: local sets by element-wise check on R_σ̄ (not generators only), ℤ₂ and ℤ₄ separately, counts as stated; engine tuple set equals their product | K-B1 |
| item 4, B2: lifts passing B2 and failing B1 printed per C; never used for selection | K-B2 |
| item 4, κ: each κ-type lift with local P acts as its trivial-on-C partner on every reachable record group at n = 3 (F8) | K-κ |
| item 5: every Surv(A) and the intersection printed per C; verdict regenerates from them | K-REP |
| exact arithmetic; two complete runs byte-identical | K-EXACT |

**Hard-to-vary statement.** Frozen together, with no fallback: the extension family, lift set, B1 definition and κ
rule, longest-agreement form, base metric, declared alphabets (K-G1 included), class and survival definitions, D1, D2
and the invariance claim, and the decision rule. After a failure none is adjusted: no P4₁ or length window, no
exemption of couplings from locality, no B2 in place of B1, no dropped alphabet, no added operation, no change of cost.
An outcome that any such adjustment would rescue refutes H-LOC as stated.

## What H-LOC needs from OI and does not yet have

- *A quadratic phase-cell update.* At q = 2 a swap lift is never affine in any section; the minimum degree is 2 (real
  section: g_swap = x z, g_couple = 0) [G1-REPORT §2(I), exact for n ≤ 2; review F10]. Main.md's update is linear over
  F₂ (Main.md:290) and Lemma 2(iii) acts "with no phase" (Main.md:300) [corpus], so it does not supply it [open]. A ℤ₄
  cell (composite q, "not covered", Main.md:320) still needs nonlinear dynamics [G1-REPORT §2, exact for n ≤ 2].
- *Or the q = 3 route.* At odd prime q every symplectic map lifts with zero phase update [G1-REPORT §2, exact for
  q = 3, n = 1; Main.md:320, corpus]; it needs a q = 3 card theory and composition witness, absent here [open].
- *A physical reading of locality.* That a lift is the identity on every untouched system's record algebra, and that
  a centre-inverting map is never local, is natural for a local substratum update, but no OI result derives it [open].

## Closing

The open question is whether this reviewed, fixed package makes the n = 3 prediction. No adjustment after the run
recovers it, and the frozen rule is never revised to fit the outcome.
