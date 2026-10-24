# G1 hypothesis H-LOC: local lifts plus longest card agreement

**DRAFT — NOT FROZEN; design specification; no computation may run against it as a test.**

**Deferred (owner, 2026-10-21).** The n = 3 run is not to be dispatched. Without an explicit map from the card/record
interface to an operational carrier, its selection bears on labelling only and not on which operations are available
(`../map/MAP.md`). Node 9 works on sourcing a non-monomial gate first (NOTES, "Direction after the map").

A candidate that a later node could preregister, for gap G1 only (a composition rule for joint records), drafted
2026-10-21 after review REVIEW-G1-8d90f77e and revised on the owner's corrections. Revised again after the pre-freeze
review `REVIEW-HLOC-1860b961.md` (committed beside this file), on the owner's choice (a): H-LOC is scoped to the
unit-cost metric. Every result quoted was computed before this draft and is therefore a control or a disclosed prior,
not evidence for it.

Status tags: **[exact]** computed with exact arithmetic, file named; **[read-off]** read from a committed output, not
separately computed; **[arg]** algebraic argument, checked by the review; **[hyp]** part of the hypothesis, untested;
**[corpus]** a statement of `papers/Main.md`; **[open]** not available.

## Claim

[hyp] Within the declared package (central extensions E of V = F₂^{2n} by C ∈ {ℤ₂, ℤ₄} with commutator (|C|/2)·ω in
the recordable class; the lift set and read rule (c) of the Statement; the declared primitive alphabets; the unit-cost
primitive metric), the selector **locality (B1) + longest card agreement** leaves exactly one lift class, and that
class ≡ standard real-stabilizer QM in the sense defined under "Fixed in advance": at n = 2 (known), and at n = 3
exactly the 8 Z-frame conjugates of std₃ (new). In addition, at n = 3 the alphabet without swap_B and swap_C alone
selects the class of std₃ (the primary new test below). The selector is the whole package; no part is credited alone.
- H-LOC is a claim about the unit-cost primitive metric. The selection is known to depend on the metric at n = 2
  (D2 below), so no claim is made for any other cost assignment.
- A success would establish only that this package selects the real-stabilizer class within that family; not that
  locality alone selects QM (the 256 swap-local triples at n = 2 are not one class, `review/extra.out` [exact]), and
  no OI implementation of the lifts or of locality, nothing for G2, and no full equivalence of OI with QM.

## Statement

Organized by the owner's declarations (`../../NOTES.md`, last section); the correspondence form is item 5 here.

1. **Dynamics and resource model.** [hyp]
   - *Systems.* n card systems (n = 2, and n = 3 for the new test), each a visible card q_j and a hidden card p_j.
     Card operations: swap_j (q_j ↔ p_j); couple_jk (q_k ^= q_j, p_j ^= p_k); flip q_j, flip p_j; read_j. Card side as
     in `g1lib.CardTheory` and `review/eng.py` (`Cards`) [exact, review F12].
   - *Records and lift set.* E as in the Claim [G1-REPORT §1(a)–(b): exact at n = 1, arg at n = 2]. The recordable
     class is unique at every n given the classification sequence (for ℤ₂, q is fixed by q(X_j) = q(Z_j) = 0; for ℤ₄,
     q̄ = 0) [arg, review N13]; K-E3 checks the n = 3 instance. Lifts: every automorphism of E covering the card map,
     Ad(P·U) (trivial on C) and, for ℤ₄, the C-inverting Ad(P·U)∘κ, κ complex conjugation. Not taken from QM [review
     F12, exact for n = 2; F8].
   - *Locality (B1), defined on the full lift.* For a set τ of systems, R_τ = ⟨C, d(X_k), d(Z_k) : k ∈ τ⟩ ⊂ E is the
     record algebra of τ, composite records included (for ℤ₄, i·d(X_k)d(Z_k)); C lies in every R_τ, and R_∅ = C. R_τ
     is the full preimage of V_τ [exact, `review/lifts_b1.out`]. A lift φ of an operation on σ is *local* iff φ is the
     identity on R_σ̄, σ̄ the untouched systems. At n = 2 this restricts the swaps only; at n = 3 it also restricts each
     coupling to its two systems.
     - ℤ₂: Aut(C) is trivial; Ad(P·U) is local iff P is the identity outside σ. Local lifts: 4 per swap, 16 per coupling.
     - ℤ₄: Ad(P·U) is local iff P is the identity outside σ (same counts). Ad(P·U)∘κ inverts C and sends each spectator
       record i·d(X_k)d(Z_k) to its value-1 partner, so it fails B1 whatever P is.
     - *Rule for κ.* Every C-inverting lift moves i, and for a spectator k it fixes d(X_k), d(Z_k) only if it sends
       i·d(X_k)d(Z_k) to its value-1 partner, so it fails B1 for every operation with a spectator. For an operation with
       no spectator (the n = 2 coupling) the exclusion is the stipulation R_∅ = C. At n = 3 every declared operation has
       a spectator. The exclusion rests on the composite record i·d(X_k)d(Z_k), equivalently on C ⊂ R_τ: under the
       C-free record algebra ⟨d(X_k), d(Z_k)⟩, κ-type lifts with local P pass (4 per swap, 16 per coupling, ℤ₄;
       `review/lifts_b1.out` [exact]). The rule rests on the single centre shared by all systems (the central-product
       form of E), which is part of the package [assumption-watch].
     - *B2, reported only.* B2 is indistinguishability under the declared measurement menu (owner requirement 4). Let
       𝓡_n be the set of record groups S reachable at n, over every word of every declared alphabet at n, under every
       B1-local tuple. A lift φ of an operation passes B2 iff some B1-local lift φ′ of the same card map satisfies
       φ(g) = φ′(g) for every g in every S ∈ 𝓡_n. Agreement on every S ∈ 𝓡_n implies equal joint record
       distributions on every word over the declared alphabets [arg: φ and φ′ then send each reachable S to the same
       group, and the read rule depends only on S]. κ-type lifts with local P should pass B2 and fail B1: κ fixes the
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
5. **Correspondence, stated in advance, no free length.** [hyp] *Longest agreement*: let ℓ_A(t) be the minimum cost of
   a word over alphabet A on which lift tuple t and the card theory give different joint record distributions (∞ if
   none). In the unit-cost metric every primitive costs 1, so ℓ_A is the shortest such length. The admitted tuples
   maximize ℓ_A.
   - *Why this form.* It has no parameter: it selects the lifts whose first departure from the card theory is latest.
     A fixed window L ∈ {5, 6} is rejected because L was chosen after the counts were seen [COORDINATOR-NOTE item 4].
   - *Why not P4₁ (at most one coupling).* P4₁ also has no free length, but it is already known to fail without
     swap_B even with local lifts: 32 pass, 16 ≡ QM and 16 with W6 = W7 = 0 [`coordinator/p41_local.out`, exact].
   - *What length means: scoped to the declared primitive alphabet.* One unit is one card primitive (one swap of one
     system, one coupling of one pair, one flip, one read). It is not tied to physical resources: no OI result assigns
     a cost to an operation, so "one use of a declared coupling" would assert an underived resource model. Naming a
     compound as one step changes the metric, and at n = 2 it changes the selection (D2); H-LOC is therefore scoped to
     the unit-cost metric.
   - *Disclosure.* This choice is informed by known results on the two-system alphabets. Those results therefore
     carry no evidential weight for H-LOC; the weight rests on the primary new test below.

## Fixed in advance

**Classes and survival.** Two tuples are in the same class over an alphabet A iff they agree on every word over A
(exact pair-BFS); "class" without qualification means over the largest declared alphabet at that n. For each declared
alphabet A, Surv(A) is the set of tuples maximizing ℓ_A (ℓ_A depends only on the lifts of operations in A). A tuple
*survives* iff it lies in every Surv(A) of the intersection at its n. The K-G1 alphabet is **required** in that
intersection: without locality it selects a cards-equivalent class at n = 2 (ℓ = ∞) [`review/alph.out`,
`review/ident.out`, exact], so it is the sensitivity control that shows locality doing work.

**≡ standard QM.** At n = 2: exact pair-BFS equivalence with std = (H_A, H_B, CNOT_AB) over the full n = 2 alphabet. At
n = 3: exact pair-BFS equivalence, on every word of every length over the full n = 3 alphabet, of the class
representative with std₃ = (H_A, H_B, H_C, CNOT_AB, CNOT_BC) in the extension engine, cross-checked against an
independent exact stabilizer simulator; the forced class must consist of exactly the 8 Z-frame conjugates
Ad(W) std₃ Ad(W)⁻¹, W ∈ ⟨Z_A, Z_B, Z_C⟩ (K-QM3). A class ≡ QM on some alphabets only, or up to a relabelling, is not
≡ QM.

**Declared alphabets.** n = 2: the five rows of the table below. n = 3:
- F₃, full: {swap_A, swap_B, swap_C, couple_AB, couple_BC, the six flips, read_A, read_B, read_C};
- NF₃, without flips;
- NSC₃, without swap_C;
- NBC₃, without swap_B and swap_C: {swap_A, couple_AB, couple_BC, the six flips, read_A, read_B, read_C} (the primary
  new test);
- KG₃, K-G1: {swap_A, couple_AB, read_B}, system C idle.

**Reporting:** per C, each Surv(A) (tuples, class labels, ℓ_max), then the intersection, then the verdict generated
from the printed intersection and naming the package (B1 locality, longest agreement, the extension family, lift set,
read rule, unit-cost metric and the declared alphabets).

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
| K-G1 {sA, c, rB} | QM class, ℓ = 7 | cards-equivalent class, ℓ = ∞ | `review/kg1_local.out`, `review/alph.out` [exact] |

The local K-G1 row: over the 64 local (sA, c) pairs, ℓ = 7 is the maximum, reached by exactly the 4 QM pairs; the next
value is ℓ = 6, reached by 4 pairs with c ∈ {Z_B·CNOT, Z_A Z_B·CNOT} [exact, `review/kg1_local.out`]. The margin is
narrow, 7 against 6, and K-KG1 recomputes it in the run. The ℤ₄ entries follow from the ℤ₂ engine by the real-subgroup
argument [arg]; K-PRES computes them in a ℤ₄ engine.

Hence locality is load-bearing within the package. Admitting the κ-type lifts (which fail B1) would multiply every
count by 2³ = 8 at n = 2 (2,048 tuples) and by 2⁵ = 32 at n = 3 (524,288 tuples) and change no survivor class [review
F8, Q4, arg].

**Restriction bound, stated in advance** [exact for the lift algebra, `review/restrict.out`; arg for the bound].
- Under B1, every local n = 3 lift restricts to an n = 2 lift on AB and on BC, and the AB and BC sub-alphabets of F₃
  are copies of the n = 2 full alphabet with the third system idle. Hence ℓ_{F₃}(t) ≤ min(ℓ₂(t|AB), ℓ₂(t|BC)) for
  every tuple t, and the analogous bound holds for each n = 3 alphabet with its AB and BC sub-alphabets.
- Of the 16384 local tuples, exactly 8 have both restrictions in the n = 2 QM class, and these are exactly the
  Z-frame conjugates Ad(W) std₃ Ad(W)⁻¹, W ∈ ⟨Z_A, Z_B, Z_C⟩ [exact, `review/restrict.out`]. Every other local tuple
  restricts to a non-QM n = 2 triple, and every non-QM local n = 2 triple has ℓ ≤ 5 on the full and no-flips alphabets
  [`review/extra.out`, exact]. So every other tuple has ℓ ≤ 5 on F₃ and NF₃.
- NSC₃: its AB part is the n = 2 full alphabet and its BC part a copy of the n = 2 without-swap_B alphabet, on which
  every local triple not ≡ QM over that alphabet has ℓ ≤ 5 [`review/extra.out`, exact]. So on NSC₃ every local tuple
  not ≡ std₃ over NSC₃ has ℓ ≤ 5.
- **Consequence.** On F₃, NF₃ and NSC₃ the n = 3 outcome turns only on whether three-qubit QM first departs from the
  cards at length ≥ 6. That is a fact about QM and the cards, not about the selector, so these lines are CONFIRMING:
  they can refute H-LOC (if ℓ for the QM class is ≤ 5), but a pass on them is not new evidence.
- KG₃ reproduces the n = 2 K-G1 local selection, since local swap_A and couple_AB lifts at n = 3 are determined by
  their AB restrictions; its outcome is known (`review/kg1_local.out`), and the line is CONFIRMING.
- **NBC₃ is the only declared alphabet where the selector has new content.** Its BC words {couple_BC, flips, reads}
  cannot see the Z-type coupling twists: by P2, 4 coupling lifts are ≡ cards there [`controls.out`, exact]. So the
  B1-local lifts CNOT_BC·Z_C and CNOT_BC·Z_B Z_C, which lie outside the QM class, are separated from it on NBC₃ only by
  three-system words, which exist (swap_A and couple_AB carry X_A into B, and couple_BC carries it into C) [arg, review
  F2]. This is also where locality of the couplings does its first real work.

**Compound letters.** For every declared coupling, sc_jk denotes swap_j then couple_jk: sc_AB at n = 2; sc_AB and sc_BC
at n = 3. Each is represented by the composite of the tuple's two lifts (Statement item 2), so no new lift is chosen.
sc_jk is added to every alphabet that contains both its constituents, and nowhere else. The family is symmetric: no
declared coupling is compounded while another is left uncompounded.

**Description controls.**
- *D1, correctness control: same cost, new notation* (n = 2 and n = 3, every alphabet containing a compound's
  constituents). Add every sc_jk at cost 2, the cost of its expansion. Every protocol then expands to one of equal
  behaviour and equal cost, so every tuple's ℓ and every Surv(A) must be unchanged. Any change is an implementation or
  accounting error: the run is void (rule below), and the change is never evidence about H-LOC.
- *D2, metric report: sc_jk at cost 1.* Reported, never decisive.
  - *n = 2, disclosed prior* [arg from `review/extra.out`, `coordinator/survivors.out`, `coordinator/corr3.out`,
    `review/nearmiss.out`; no re-costed ℓ was computed]. Under sc_AB at cost 1 the QM class has ℓ = 4: W6 = (sc)³ r_B
    costs 4, and a word whose expansion has base length m ≥ 7 holds at most ⌊(m − 1)/2⌋ sc letters, so it costs at
    least 4. The four local near-miss triples (0,0,8), (0,3,0), (12,0,8) and (12,3,0) (indexed as in `review/eng.py`,
    P = PAULI[4a + b]) have base ℓ = 5 and first fail on `sA sB c sA rA`; `sB sA c sA rA` gives the identical
    distribution [exact, `review/nearmiss.out`] and contains an adjacent sA, c pair, so it costs 4, and no word of
    cost ≤ 3 distinguishes them. So Surv(full) under this metric holds at least the QM class and the near-miss class:
    the metric dependence is already shown at n = 2. Re-costing every alphabet containing sA and c would make the
    near-miss class tie QM on full and no-flips and coincide with it on every sB-free alphabet, so the intersection
    could never be exactly the QM class: an invariance claim is refuted at n = 2, and H-LOC makes none.
  - *n = 3, robustness report.* With every sc_jk at cost 1 in every alphabet containing its constituents, ℓ is
    computed as exact minimum cost; each re-costed Surv(A) and the re-costed intersection are printed per C beside the
    unit-cost ones. The report does not refute or support H-LOC.
  - The former re-costing (b), the p-flips replaced by their expansions, is dropped: it is the unit-cost alphabet "full
    without p-flips", bounded by ℓ_full ≤ ℓ ≤ ℓ_noflips for every tuple, and asymmetric between p-flips and q-flips. It
    is not a metric test.

**Independent consequences beyond W6/W7.**
- *Primary new test: NBC₃ at n = 3.* [hyp] Under B1 each swap has 4 lifts and each coupling 16, so 4³ · 16² = 16384
  local tuples for each C; ℓ_{NBC₃} depends only on the lifts of swap_A, couple_AB and couple_BC (1024 distinct
  restrictions). Prediction, for each C:
  - (i) ℓ_{NBC₃}(t) ≤ ℓ_{NBC₃}(std₃) for every local tuple t;
  - (ii) equality holds only on the NBC₃-class of std₃: Surv(NBC₃) is exactly the set of local tuples ≡ std₃ over
    NBC₃;
  - in particular, the twist tuples t_Z and t_ZZ (std₃ with couple_BC lifted as CNOT_BC·Z_C, resp. CNOT_BC·Z_B Z_C)
    have ℓ_{NBC₃} < ℓ_{NBC₃}(std₃), and every word over NBC₃ that separates them from std₃ contains swap_A and
    couple_AB [arg, P2].

  The value of ℓ_{NBC₃}(std₃) is not predicted and not computed.
- *Decision rule for NBC₃* (per C, generated from the printed Surv(NBC₃) and its class labels):
  - **NBC₃ selects std₃**: Surv(NBC₃) is exactly the NBC₃-class of std₃. The prediction holds.
  - **NBC₃ tie**: Surv(NBC₃) contains the NBC₃-class of std₃ and at least one other NBC₃-class. Prediction (ii) fails,
    and H-LOC is refuted, even if the intersection still forces the QM class through F₃.
  - **NBC₃ excludes std₃**: the NBC₃-class of std₃ is not in Surv(NBC₃). Prediction (i) fails, and H-LOC is refuted;
    the intersection then cannot contain the QM class.
- *CONFIRMING lines.* F₃, NF₃, NSC₃ and KG₃ at n = 3 (restriction bound above), and the forced 8-tuple class when
  ℓ for the QM class on F₃ is ≥ 6.
- *§A.29 note.* Whether the NBC₃ prediction counts as an independent prediction in the sense of §A.29 is for the owner
  to judge before freeze. If it does not, a three-system alphabet that the restriction bound cannot decide is added by
  a stated rule, before freeze.
- *Postdiction (weak).* The card identity word (swap_A, couple)⁴ flips q_B's record (cards 0, QM 1) [`predictions.out`,
  `d_witness.out`, exact]; implied by the full-table equivalence with QM, so not independent of the controls.

**Decision rule** (outcomes printed only over green checkpoints; verdict text generated from the measurements and
naming the package).
- *Forces*: the intersection is exactly one class. A separate line reports whether that class ≡ standard QM (K-QM3)
  and gives W6 = W7 = 1; H-LOC predicts both. *Permits*: more than one class. *Fails*: the intersection is empty. The
  three outcomes partition the possible intersections, which are unions of classes.
- n = 2: forces, QM class [known, controls]. n = 3: to be measured, for ℤ₂ and ℤ₄; the two are equal by the
  real-subgroup argument, so they are not independent tests, and a disagreement is an engine error that voids the run
  (K-Z24), never a refutation "for either C".
- H-LOC is refuted for G1 if, at n = 3, the outcome is anything other than *forces* with exactly the 8 Z-frame
  conjugates of std₃ (an empty intersection, an intersection of more than one class, or one class other than the 8
  conjugates), or if the NBC₃ decision rule returns "tie" or "excludes std₃". D2 does not decide H-LOC.
- *Order of checks.* K-PRES, K-W, K-KG1, K-E3, K-ENG3, K-B1, K-B2, K-κ, K-ONE and K-RES run and print before any
  n = 3 Surv is computed; a red one stops the run before selection. K-D1, K-Z24 and K-EXACT print before the verdict;
  K-QM3, K-REP, K-ATTR and K-D2 generate and check the verdict lines.
- *Void runs.* A red checkpoint voids the run, which then bears on nothing. A void run is retained with all its
  outputs. A rerun is admissible only for an implementation defect named with a failing mutant, through an
  append-only amendment that changes no frozen element; the void run's n = 3 outputs are published beside the rerun's,
  and any difference between their verdicts is reported. No void may be declared after the outcome is visible except
  by such an amendment.

**Invariant → checkpoint** (§A.41). Every control carries a mutant or sensitivity test that must turn it red.

| invariant asserted | checkpoint | mutant or sensitivity test |
|---|---|---|
| preserved results reproduce (P1–P3, card theory, engine controls, K-STAB-GAP), the ℤ₄ n = 2 rows in a ℤ₄ engine | K-PRES | an expected value altered (the full-alphabet QM ℓ = 7 set to 6) must turn K-PRES red |
| K-G1 witnesses untuned: cards 0, QM 1 | K-W | cards ≠ QM on W6, W7 (built-in sensitivity) |
| item 1: K-G1 in every intersection; its local row (QM, ℓ = 7; next ℓ = 6, 4 pairs) and non-local row (cards-equivalent, ℓ = ∞) recomputed exactly | K-KG1 | the non-local K-G1 row (built-in sensitivity) |
| E at n = 3 built exactly for each C, with commutator (\|C\|/2)·ω and the recordable class; every declared map lifts | K-E3 | the abelian extension (commutator 0) must be rejected |
| the n = 3 engine: the trivial extension ≡ a direct three-card simulation on every word; std₃ ≡ an independent exact three-qubit stabilizer simulator on every word over F₃ | K-ENG3 | dropping the sign update of one swap lift in the extension engine must make std₃ ≠ the simulator |
| "≡ standard QM" at n = 3 as defined above; the forced class is exactly the 8 Z-frame conjugates | K-QM3 | the twist tuple t_Z offered as class representative must be reported not ≡ QM; a class of 7 conjugates must fail "exactly 8" |
| restriction: ℓ_A(t) ≤ the minimum of the n = 2 values on its AB and BC sub-alphabets, for every tuple and alphabet; the 8-tuple identity of `review/restrict.out` | K-RES | a non-local couple_AB lift (with a Z_C factor) must be refused by the restriction map |
| ℤ₂ and ℤ₄ engines give equal ℓ_A(t) for every trivial-on-C tuple and every alphabet | K-Z24 | a ℤ₄ engine whose read rule drops the i-phase of one record must disagree with the ℤ₂ engine |
| item 2: one lift per operation, fixed across words; each automaton built from a single lift table per operation | K-ONE | an automaton that alternates two lifts of swap_A by occurrence parity must be detected |
| item 2: verdict names the whole package; the n = 2 without-locality rows printed beside it | K-ATTR | a verdict line omitting "B1 locality" must turn K-ATTR red |
| item 3, D1: ℓ and every Surv(A) unchanged with every sc_jk at cost 2; otherwise void | K-D1 | an sc built from a lift other than the tuple's own must change some ℓ; sc_AB at cost 1 must give ℓ_QM = 4 at n = 2 |
| D2: the re-costed Surv(A) and intersection printed per C beside the unit-cost ones; never used in the verdict | K-D2 | altering a re-costed Surv must leave the verdict unchanged, and altering a unit-cost Surv must change it |
| item 4, B1: the candidate lifts of each operation, for each C, enumerated by brute force over generator images (every assignment of X_k, Z_k and, for ℤ₄, i to their fibres, kept iff it is a bijective homomorphism), independently of the Ad(P·U) formula, and compared with {Ad(P·U)} ∪ {Ad(P·U)∘κ} as sets; locality checked element-wise on R_σ̄. Expected: n = 2, 16 lifts trivial on C per operation (and 16 C-inverting for ℤ₄), B1-local 4 per swap and 16 per coupling, 256 tuples; n = 3, 64 per operation (and 64 C-inverting for ℤ₄), B1-local 4 per swap and 16 per coupling, 0 C-inverting, 16384 tuples; the engine tuple set equals their product [`review/lifts_b1.out`, exact] | K-B1 | under the C-free record algebra ⟨d(X_k), d(Z_k)⟩, κ-type lifts with local P must pass (4 per swap, 16 per coupling, ℤ₄); a P with spectator support must be rejected |
| item 4, B2: lifts passing B2 and failing B1 printed per C; never used for selection | K-B2 | a selection run fed the B2 set in place of the B1 set must be refused |
| item 4, κ: every record group reachable over every declared alphabet, for every local tuple, lies in the real subgroup; κ commutes with the flips and the read update; so each κ-type lift with local P runs the same automaton as its trivial-on-C partner at n = 3 (F8; cross-referenced with K-B2) | K-κ | a ℤ₄ record group containing i·X_A Z_A, on which a κ-type lift and its partner differ |
| item 5: every Surv(A) and the intersection printed per C; verdict regenerates from them | K-REP | altering one printed Surv must change the regenerated verdict |
| exact arithmetic; two complete runs byte-identical | K-EXACT | a probability converted to floating point in one run must make the two runs differ |

**Runtime and placement (§A.40).** At n = 2 the review engine computes first disagreement for all 256 local triples
over the full alphabet in about 0.7 s; std against the cards has 24 card states, 24 record states and 96 pair nodes
(about 12 ms) [measured on the committed engine; no n = 3 quantity computed]. At n = 3 the real-stabilizer record
states grow to 2³·2·3·5 = 240, the full alphabet from 9 to 14 letters, and the tuple count to 16384 per C. Distinct
restrictions per C are 16384 on F₃ and NF₃, 4096 on NSC₃, 1024 on NBC₃ and 64 on KG₃. Across three metrics (unit
cost, D1, D2), two C and two complete runs (K-EXACT), the run evaluates about 4.6·10⁵ pair automata. Assuming the n = 3
pair automaton is 20 to 600 times the n = 2 one, and a per-node cost about 3 times higher, the estimate is roughly
20 to 3,000 CPU hours; early exit at the first distinguishing word makes the lower end likelier for most tuples. The
run belongs in CI, sharded by C, alphabet and swap_A lift, and its dispatch needs owner approval. The cylinder
reduction (ℓ_A computed once per distinct restriction to A's operations) is exact by definition and is frozen as part
of the engine, with K-RES and K-ONE as its controls; no other symmetry reduction is used unless frozen with its own
control. Before freeze the estimate should be firmed by a pilot that computes no selection quantity, for example the
sizes of the card-only and std₃-only reachable sets at n = 3, subject to owner approval.

**Hard-to-vary statement.** Frozen together, with no fallback: the extension family, lift set, B1 definition and κ
rule, longest-agreement form, unit-cost metric, declared alphabets (K-G1 and NBC₃ included), the compound family sc_jk,
class and survival definitions, the definition of ≡ QM, D1, the D2 report form, the NBC₃ prediction and its decision
rule, the overall decision rule, the order of checks and the void rule. After a failure none is adjusted: no P4₁ or
length window, no exemption of couplings from locality, no B2 in place of B1, no dropped alphabet, no added operation,
no change of cost. An outcome that any such adjustment would rescue refutes H-LOC as stated.

## What H-LOC needs from OI and does not yet have

- *A quadratic phase-cell update.* At q = 2 a swap lift is never affine in any section; the minimum degree is 2 (real
  section: g_swap = x z, g_couple = 0) [G1-REPORT §2(I), exact for n ≤ 2; review F10]. Main.md's update is linear over
  F₂ (Main.md:290) and Lemma 2(iii) acts "with no phase" (Main.md:300) [corpus], so it does not supply it [open]. A ℤ₄
  cell (composite q, "not covered", Main.md:320) still needs nonlinear dynamics [G1-REPORT §2, exact for n ≤ 2].
- *Or the q = 3 route.* At odd prime q every symplectic map lifts with zero phase update [G1-REPORT §2, exact for
  q = 3, n = 1; Main.md:320, corpus]; it needs a q = 3 card theory and composition witness, absent here [open].
- *A physical reading of locality.* That a lift is the identity on every untouched system's record algebra, and that
  a centre-inverting map is never local, is natural for a local substratum update, but no OI result derives it; the
  κ exclusion also rests on the single shared centre [open; assumption-watch].

## Review REVIEW-HLOC-1860b961: where each item is handled

- F1 / Q2: Claim (metric scope), Statement item 5, D2 (n = 2 disclosed prior; invariance withdrawn; n = 3 report),
  decision rule (refutation wording). Re-costing (b) dropped (N2).
- F2: restriction bound, CONFIRMING lines, NBC₃ as the primary new test with its prediction and decision rule, the
  8-tuple class in the Claim, the §A.29 note.
- F3: compound letters sc_jk.
- F4, F7, Q4: the checkpoint table (K-E3, K-ENG3, K-QM3, K-RES, K-Z24, K-ONE added; mutant column; K-B1 brute force;
  K-κ scope).
- F5: definition of ≡ standard QM.
- F6: order of checks and void runs.
- N1: rule for κ. N5: B2. N9: runtime and placement. N11: the ×8 and ×32 factors. N12: ℤ₂ and ℤ₄ not independent.
  N13: recordable class at every n. N14: K-G1 local row [exact], `review/kg1_local.out`. Q3: KG₃ marked CONFIRMING.
  N6, N7, N8: the ℤ₄ tag in the two-system section, survival wording, item 5 wording.
- Not taken up: N3 (a generating rule for the n = 3 alphabet list) and N4 (beyond the naming list now in Reporting);
  both remain for the fresh review before F.

Supporting review scripts, re-run with outputs: `review/lifts_b1.py`, `review/restrict.py`, `review/kg1_local.py`,
`review/nearmiss.py` (with `review/eng.py`). None computes an n = 3 word, an n = 3 distribution or a re-costed metric.

## Closing

The open question is whether this reviewed, fixed package makes the n = 3 prediction. No adjustment after the run
recovers it, and the frozen rule is never revised to fit the outcome.
