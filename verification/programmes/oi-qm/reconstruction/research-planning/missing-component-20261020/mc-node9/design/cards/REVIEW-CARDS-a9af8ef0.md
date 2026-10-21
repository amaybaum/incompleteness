> **Redaction note (committed copy).** Local filesystem paths in the reviewer's original have been replaced by placeholders: the reviewer's worktree by `<reviewer worktree>`, the reviewer's session scratchpad by `<reviewer scratchpad>`, the card-table checkout by `<card-table checkout>` and the node 8 worktree by `<node 8 worktree>`. Nothing else is changed. The scripts the review cites as `indep/` are committed, with re-run outputs, in `review/` beside this file.

# Review: node 9 Option B card-structure design evidence at `a9af8ef0`

**Reviewer.** Independent and skeptical (§A.31). This was a read-only review in a fresh detached worktree
`<reviewer worktree>` at `a9af8ef053a94fe89a42fd5776135622209733a0`, removed afterwards. `amaybaum/card-table` at `17115cc`
was read only and treated as data. All arithmetic is exact (`fractions.Fraction`).

**Scope.** `mc-node9/design/cards/`: CARDS-REPORT.md, the scripts and outputs, `run_all.sh` and `SHA256SUMS`. I read them
against PREREG §1, NOTES (after "Owner inputs after revision 3"), book §1.11 (`book/ch01-observation.md:263–297`), and the
card-table README, `src/engine.js` and `src/engine.test.js`.

Paths below are relative to `mc-node9/design/cards/` unless stated otherwise.

## Disposition: ACCEPT WITH CORRECTIONS

**What replicates.** The computations replicate exactly, both by replay and by an independent reimplementation that
imports nothing from `cardtheory.py` or `exactlp.py`:
- the extraction numbers;
- the 87-realization M1 sweep;
- the exchangeability invariant;
- the 155 extreme states;
- the 3/4 witness and its protocol;
- 67/67 and 27/27;
- NDP, VIS and CSWAP.

**What needs correcting.** The verdict lines stand for Π_B at the stated bounds. Three findings are blocking. Each is a
statement that is stronger than, or contradicted by, the evidence in the same directory:
- the "any size" positive-dependence claim, together with H-5;
- the deal 1 / deal 2 identifications in the Pur-U section;
- a "must fail" control that already fails at the report's own bounds.

All three can be fixed in the text, and replacement wording is given below. None needs a new computation. Several
non-blocking findings correct how the book is read, the scope wording and the proposed classifications. The most
consequential non-blocking point is N7: every Π_B state space is a simplex. M1 is therefore passed here by a classical
theory that has no preparable product states. That should shape both the classification and the preregistration.

***

## Blocking findings

### B1. "No purification at any size" relies on an unproved characterization that also needs deck knowledge, and H-5 says the opposite

**Evidence.**
- CARDS-REPORT.md:217–218 says: "has no purification at any size, because marginals of E(M) satisfy P(RR) = r(r−1)/(n(n−1)) <
  (r/n)². This is [W], checked exactly for n ≤ 12."
- The inequality is pure algebra and holds at every size. r(r−1)/(n(n−1)) < r²/n² ⇔ (r−1)n < r(n−1) ⇔ r < n. So "checked
  for n ≤ 12" understates it.
- The step that is actually load-bearing is different: every pure state of a filled AB is a *single* E(M).
  - Mixtures of E(M) can be positively dependent; for example ½RR + ½BB is a mixture of E(RR) and E(BB).
  - In the report this step is evidenced only within the bounds: "every extreme AB state equals the E(M) formula (155
    checked)", CARDS-REPORT.md:140 and controls.out.
- **That step also needs deck knowledge.** CARDS-REPORT.md:269–270 (H-5) claims deck knowledge "does not affect the
  purity mechanism". This is false.
  - Counterexample, computed exactly by the reviewer (`indep/h5.py`): take a deck composition that is RRRR or BBBB with
    probability ½ each. The record does not fix it.
  - The closure is the same menu. Prep(AB) = {½RRRR + ½BBBB}, which is extreme, so pure.
  - Its A-marginal ½RR + ½BB is mixed, because RR and BB are preparable by peeking a deck card first.
  - So a positively dependent state *is* purified once the composition is not known.
- Deck knowledge therefore carries three things:
  - the pure-state characterization;
  - Pur-U's triviality;
  - the "any size" obstruction.

**Fix.** Either state the claim within the bounds, or add the following proof, which I checked. It holds for Π_B with a
known deck composition, at any size.

> *Lemma (Π_B, known composition).*
> - (i) Given the record, the colour distribution on the in-play positions is a mixture Σ λ_M E(M).
>   - The initial deck is E(M₀).
>   - Content-independent relocations push E(M) forward to E(M).
>   - Every bijection of the arrangements of a fixed multiset, content-dependent or not, fixes the uniform distribution on
>     them.
>   - A destructive reveal at p with outcome c conditions E(M) to E(M − c).
>   - A discard at p marginalizes E(M) to a mixture of E(M − c).
>   - A coarse herald mixes branches.
> - (ii) Every preparable state of a filled system S is a mixture of preparable E_S(M), with branch-probability weights.
>   - Replace each discard in the protocol by a reveal whose record is never used. Then reveal every in-play card outside
>     S.
>   - Feed-forward depends only on records, so the original state is the branch-weighted mixture of the refined
>     branches.
>   - Because the composition is known, each refined branch is E_S(M_b) with M_b fixed by the record.
> - (iii) E_S(M) with distinct M have disjoint supports. So the pure states of S are exactly the preparable E_S(M), and
>   conv(Prep(S)) is a simplex.
> - (iv) Hence:
>   - two-slot marginals of pure states satisfy P(RR) < P(R)² unless monochrome;
>   - single-slot marginals of a pure state on n slots lie in (1/n)ℤ;
>   - distinct pure states of a fixed filled AB have distinct A-marginals.
> - (ii) fails when the record does not fix the composition (counterexample above).

**Replacement for H-5 (CARDS-REPORT.md:269–270).** "H-5 Deck knowledge. With a known composition, the record fixes the
in-play multiset, and pure states are exactly the preparable E(M) (lemma above). With a composition unknown to the record,
pure states need not be single E(M): with RRRR or BBBB at ½ each, ½RRRR + ½BBBB is pure and purifies the positively
dependent ½RR + ½BB. Deck knowledge is therefore load-bearing for the pure-state characterization, for Pur-U's triviality
and for the positive-dependence obstruction."

**Replacement for CARDS-REPORT.md:217–218.** "...has no purification at any size *for a known deck composition*. Pure
states are single E(M) (lemma), and the two-slot marginal of E(M) satisfies P(RR) = r(r−1)/(n(n−1)) < (r/n)² for 0 < r < n
(algebra, all n; brute-forced for n ≤ 7)."

### B2. The deal 1 / deal 2 identifications are wrong for the M1 split, and CARDS-REPORT.md:231 is false for |A| = 2

**Evidence.**
- **The split differs from the encoding.** CARDS-REPORT.md:190 says: "The witness is the owner's deal 1 under the
  labelling of B's arrangements."
  - The M1 witness is E(RRRB) on A = {a1, a2} and B = {b1, b2} (CARDS-REPORT.md:169).
  - The card encoding of deal 1 in controls.py:97–100 uses a different split: A = one slot, B = three slots.
  - In the 2 + 2 split, B = (b1, b2) takes the values RB, BR, RR, RR. That is not injective, so this is not deal 1.
- **The witness is pure while B predicts A at 3/4.** The reviewer computed this exactly (`indep/deal2.py`):
  - in the M1 witness, B predicts a1 with success **3/4**;
  - B predicts A = (a1, a2) with success **3/4**;
  - only A's colour count is predicted with certainty;
  - the joint of (a1; b1 b2) is {(R;RB), (R;BR), (R;RR), (B;RR)} at ¼ each, which is the owner's deal 2 statistics.
- **So line 231 is contradicted by the report's own witness.** CARDS-REPORT.md:231 says: "B always determines A's colour
  count, so deal 2 type states (B predicts A with success 3/4) cannot be pure." The M1 witness is pure, and B predicts A
  in it with success 3/4.
- **Deal 2's statistics are preparable.** CARDS-REPORT.md:232 says: "Deal 2 is not exchangeable, so Π_B excludes it."
  That depends on the encoding.
  - With A = 1 slot and B = 2 slots, deal 2's statistics are preparable in Π_B: ¼E(RRR) + ¾E(RRB), the 3-slot marginal
    of E(RRRB).
  - They are mixed (not extreme) at decks 3R1B, 3R2B, 3R3B and 4R2B (`indep/deal2.py`).
  - With B = 3 slots, none of the 3360 injective encodings is exchangeable (reviewer check). The report checks one of
    them.

**Replacement (CARDS-REPORT.md:190).** "Under the 1 + 3 split (A = a1, B = a2 b1 b2), E(RRRB) is the card encoding of the
owner's deal 1 (controls.py:98). Under the M1 split (A = a1 a2, B = b1 b2), B predicts A, and a1, with success 3/4. Only A's
colour count is determined by B."

**Replacement (CARDS-REPORT.md:231–232).** "Pure states are single E(M), so B determines A's colour count. For |A| = 1 this
means B determines A, and a deal-2-type state (B predicts A with success 3/4) cannot be pure. Deal 2's statistics are
nevertheless preparable on a 1 + 2 composite as the mixed state ¼E(RRR) + ¾E(RRB), and no exchangeable encoding of deal 2 on
a 1 + 3 composite exists. So Π_B admits deal 1 as pure and deal 2 only as mixed. For |A| = 2, a pure state can have B
predicting A with success 3/4 (the M1 witness)."

### B3. Proposed "must" columns are already red at the report's own bounds

**Evidence.**
- CARDS-REPORT.md:306 says: "K-NDP, K-VIS (= K-CLASSICAL), K-MARK, K-SPECT and K-SEPDECK-ample: M1 must fail."
- CARDS-REPORT.md:203 says MARK leaves "½ witnesses … in 7/87" realizations. `run_m1.MARK.out` agrees: "with M1
  witness=7".
- So a preregistered "M1 must fail" for K-MARK would be red at n ≤ 5.
- K-SEPDECK-ample's decks ((4,0)+(0,4) and the others, totals 8–10) lie outside the n ≤ 6 bound (§f, CARDS-REPORT.md:281–282).

**Replacement.** "K-NDP, K-VIS (= K-CLASSICAL) and K-SPECT: M1 must fail. K-MARK: no 3/4 witness, and M1 must fail at
n = 6. K-SEPDECK-ample at its stated decks (totals 8–10): M1 must fail. K-SEPDECK-scarce: reported, with no must."

***

## Non-blocking findings

### N1. Discrepancy 3 depends on the reading

- CARDS-REPORT.md:76–79 says: "Under the literal book rule the return probability is 1".
- The book does not say which card the middle-street peek reveals.
  - Rule 3 (ch01:269): "a revealed card is burned and replaced under a fixed rule".
  - The table row (ch01:278): "two shuffles with a peek (and forced re-burn) in the middle | 1/2".
  - ch01:280: "peeking at the middle street, which forces the re-burn".
  - ch01:290: "Opening the box is the peek with its forced re-burn".
- "Re-burn" reads naturally as replacing the burn card, which is what the engine does (engine.js:31:
  `if (peek) { const seen = v; h = rng() < 0.5 ? 0 : 1; …}`).
- Rule 3 applied literally to a revealed *burn* card also gives ½ (11/23 from a depleted 24-card deck; `indep/book.py`).
- **Replacement.** "The book does not fix which card the middle-street peek reveals. If it reveals the visible card and
  rule 3 burns and replaces *that* card, the return probability is 1. If it reveals the burn card and rule 3 replaces
  it, or (as in the engine) the visible card is read and the burn card is replaced ('forced re-burn', ch01:278, 280), the
  return probability is ½."

### N2. Discrepancy 4 and (g)6 overreach

- The book's minimal game is "the coin-and-die model of §1.5 dealt onto a table" (ch01:271), i.e. independent fair bits.
- The engine's swap core and its cat protocol (engine.js:8–36, 67–71) never use the Euchre deck. Only the line game does
  (engine.js:110–141).
- **Replacement (CARDS-REPORT.md:319–320).** "If the swap core is dealt from a finite two-colour deck of N cards, the ½
  entries become (N/2 − 1)/(N − 1) (11/23 at N = 24); the book's coin-and-die game and the engine's fair bits are the
  no-depletion case."

### N3. Discrepancy 7 is not a discrepancy

- ch03:188 (FULL:1062) reads: "A card game is local through and through — each player's hidden cards are their own".
- That is a statement about locality. Depletion from a shared deck is a common-cause correlation, and it is local.
- **Replacement (CARDS-REPORT.md:90–92).** "Depletion from a shared deck correlates different players' hidden cards (a
  common-cause correlation). This is consistent with ch03:188's locality statement and is noted because it is the source
  of the M1 pass; it is not a Bell claim."

### N4. Discrepancy 6 and the MARK row

- The engine reads the marker only at the end: engine.js:115–116, "behind the dealer's screen; screen = final marker
  position".
- MARK (reading it mid-protocol) is the reviewer's perturbation, not engine behaviour.
- **Fix.** Add "The engine reads the marker only at showdown; MARK is a constructed perturbation" to CARDS-REPORT.md:88–89
  and :203.

### N5. A false parenthetical at CARDS-REPORT.md:189

- The text reads: "only a non-destructive read leaves a definite card in play".
- Counting does this too. After revealing the deck down to the last card, that card is definite. Definite single-slot
  states and monochrome deals are preparable; among the unpurified states of the Pur-E realizations, 64 are such definite pure A-states
  (`indep/purclass.py`).
- **Replacement.** "no non-monochrome definite deal of AB is preparable".

### N6. Pur-E omits its most basic obstruction, and `run_pur.py` mislabels it

- A non-monochrome pure two-slot A-state, E(RB), has no purification at **any** purifier size ≥ 1. Writing p for the
  E(M) marginal, p(RR) = p(BB) = 0 forces n ≤ 2.
- This happens 26 times across the 67 realizations (`indep/purclass.py`).
- cardtheory.py:402–416 (`why`) files these under "no E(M) on k slots has this marginal (purifier too small)".
- This obstruction is H-1 (no product states) appearing inside M2: the purification of a pure state would be a product.
- **Fix.** Add an obstruction (0), "non-monochrome pure A-states have no purification at any size", before the three
  listed at CARDS-REPORT.md:214–221, and correct the classifier label.

### N7. Every Π_B state space is a simplex, so M1 is passed by a classical theory

- All 297 preparable AB states in the 87 BASE realizations are the unique colour-count mixture of preparable E(M)
  vertices (`indep/simplex.py`). The lemma in B1 proves this in general for a known composition.
- No non-monochrome preparable AB state is a product.
- So the M1 witness is a vertex of a classical simplex whose A-marginal is not a vertex. M1 passes because the composite
  has no preparable product states. Nothing nonclassical is involved.
- **Fix.** State this in (c) and (e). Add to (g)4: "A Π_B-type M1 PASS is a PASS of a simplicial theory without product
  states; M1 as worded (PREREG §3) does not separate this from a quantum-like composite."

### N8. The proposed classifications (CARDS-REPORT.md:311–314)

- **M1 mechanism, ELABORATING: supported.**
- **H-1/H-2, "NEW candidate": not supported as stated.**
  - H-1 is the failure of the composition-lemma premise. That is the same fact as the M1 mechanism, so it is
    ELABORATING.
  - H-2 (a system is pure only when it holds every in-play card) is the closed-system, fixed-total structure of finite
    exchangeability.
  - The literature has not been checked (§A.31 step 4). Likely sources, all [Q] and unread:
    - the finite de Finetti representation (Diaconis–Freedman 1980);
    - negative dependence in sampling without replacement (Joag-Dev–Proschan 1983).
  - H-2 also touches the corpus's "inert spectators" condition (GR.md:216, item (iii)). That connection should be stated
    as a shared ingredient, not as an identification.
- **What may qualify as a NEW candidate** is the methodological marker of N7: M1 is passed by a classical (simplicial)
  theory with no preparable products, unless PREREG adds a product-preparability or spectator-stability clause. This
  needs pressure-testing before it is credited. The owner decides.
- **Pur-U, "CONFIRMING/trivial".** It is *vacuous* (0 pairs tested in 67 realizations; `run_pur.out`, "total Pur-U pairs
  tested: 0"). Record it only. The detector countercontrol (K-UNIQ card) is green and not vacuous.

### N9. Mixed units at CARDS-REPORT.md:205–207

- "MARK goes from 9 to 10" counts witness *states*: BASE 73 → 73, MARK 9 → 10 (`run_m1.*.json`, `run_budget_strict.out`).
- The table above it counts *realizations*: BASE 55, MARK 7.
- **Replacement.** "Under the generated-weight budget reading, witness-state counts are BASE 73 → 73, MARK 9 → 10, and
  NDP, VIS, SPECT 0 → 0."

### N10. SEPDECK scope in (g)1 and H-4

- CARDS-REPORT.md:299–300 says: "With independent supply (a second ample deck or clean known cards), the card route's M1
  pass disappears at these bounds."
- The ample decks are beyond the bound (totals 8–10).
- Independent but scarce decks keep witnesses (`run_sepdeck_large.out`, A2B2):
  - (2,2)+(2,2): 10;
  - (2,1)+(2,1): 12;
  - (3,1)+(3,1): 7;
  - (2,2)+(3,1): 5.
- Independence alone does not remove M1; a supply of definite cards does. CARDS-REPORT.md:204 already says this.
- **Replacement.** "With a second deck that can supply enough definite cards of each colour (tested: (4,0)+(0,4),
  (3,1)+(1,3), (3,2)+(2,3), (4,1)+(1,4); totals 8–10, beyond the n ≤ 6 bound), no M1 witness was found; scarce independent
  decks leave witnesses."

### N11. The n = 7, 8 row (CARDS-REPORT.md:198)

- "18/18" is 6 selected decks × 3 splits (`run_extra.py`). State that.
- The reviewer's full sweep strengthens it (`indep/big.out`):
  - all 68 realizations at n = 7, 8 (every composition, splits 11/12/21/22);
  - all 52 two-colour realizations have witnesses, 9 of them at 3/4;
  - 0 non-exchangeable nodes;
  - every extreme state is an E(M).

### N12. PREREG §1.1 conflicts beyond the independent ancillas

MC-1 flags the conflict with independent ancillas. Π_B also departs from three other parts of §1.1:
- the default non-disturbing readout and the "disturbance-free visible copy" grant (MC-2, admissible only as an R-MENU (v)
  postulate);
- the system boundary "visible cells V_S together with the hidden cells" (MC-9: Π_B systems have no visible cells);
- fresh bath cells "used at most once" (the shared deck is a depleting, correlated bath).

**Fix.** State all three under MC-1, MC-2 and MC-9.

### N13. Menu bookkeeping

- `move` and `swap` within one system only (cardtheory.py:70–77) is an unflagged choice, but it is immaterial.
  - The reviewer's superset menu adds cross-system moves and swaps, a second deck shuffle and two content-controlled
    swaps.
  - It gives identical BASE counts: 87, 55, 0 non-exchangeable, 155 extreme, and the same P-values and 3/4 locations.
- "Content-independent pattern changes" is load-bearing and belongs to the principle, not to what is derived. A
  content-controlled move into an empty slot is a non-destructive read through the occupancy pattern.
- **Fix.** Say this beside CARDS-REPORT.md:141–143. The claim that content-dependent *bijections* are invisible is correct
  in general (lemma (i)).

### N14. Wording

- CARDS-REPORT.md:267: "This confirms the C-i/emb lesson" → "This is consistent with the C-i/emb lesson".
- CARDS-REPORT.md:316: "not met by card rules at these bounds" → "not met by Π_B with MC-1–MC-4 at these bounds".
- CARDS-REPORT.md:197: VISNOSWAP is identical to BASE on every M1 field. Its non-exchangeable node counts differ, because
  the visible slots hold read cards. Write "M1 outputs identical to BASE".

### N15. CARDS-REPORT.md is not in SHA256SUMS

The record is pinned by its commit, so this is acceptable. Say so in §f.

***

## Answers to the review questions

### (a) Extraction

| item | result | evidence |
|---|---|---|
| 52 vs 24 cards | verified | README:49–50 "the 52-card line game"; README:9 and engine.js:111 "the 24 cards 9,10,J,Q,K,A" |
| "sixteen" vs 8 cases | verified | ch01:280 "there are sixteen cases in the longest protocol"; engine.js:10–15 enumerate v0, h0, h2 = 8 |
| which card is burned | correct as one reading, overstated as "the literal book rule" | N1 |
| independent bits vs depletion | verified | engine.js:27 `const v0 = rng() < 0.5 ? 0 : 1, h0 = …`; 11/23 reproduced, and the scope is overstated (N2) |
| 22 of 24, ±23 unreachable | verified | README:13–15 "the forbidden positions fill in"; engine.js:162 already restricts `midFilled` to \|x\| ≤ 22; max \|d\| with peek = 22 |
| marker as a non-destructive read | verified, but end-of-game only | N4 |
| 80/161, 552 even | verified | independent recomputation |

### (b) Π_B

- **Menu choices.** Flagged, with N12 and N13 added.
- **The "derived" exchangeability invariant.** Correct, and provable at every size given a known composition (lemma in
  B1). Replicated: 0 exceptions in 87 realizations with a larger menu.
- **Invisibility of content-dependent bijections.** True in general, by lemma (i). Content-dependent pattern changes are
  excluded by the principle, and that exclusion is load-bearing.

### (c) M1

- **Replicated.** E(RRRB) on 2 + 2 is extreme in conv(Prep(AB)) in all six realizations. This was checked by an exact
  Carathéodory enumeration with exact Gaussian elimination, independent of `exactlp.py`.
- **Structural certificate.** No other preparable AB state is supported inside the 3R1B colour class.
- **A-marginal.** ½RR + ¼RB + ¼BR = ½E(RR) + ½E(RB) (in Prep(A)), and also ¾E(RRB)|_A + ¼RR. Both decompositions are
  mixed.
- **Protocol.** At deck 3R3B, keeping both black has probability (3/6)(2/5) = 1/5, and the remaining 3R1B dealt into four
  slots is E(RRRB).
- **Purity is judged on the closed menu.** The closure reaches a fixed point under every Π_B generator, including
  heralding with back-action, feed-forward, deck reveals and discards. A strictly larger menu gives the same answer.
- **Purity is relative to the principle.**
  - Admitting a non-destructive read (NDP) removes every witness: 73 realizations computed by the reviewer, 0 witnesses;
    3R3B A2B2 was parked at the reviewer's 4·10⁵ cap.
  - Admitting the book's own movable visible hole card (VIS) does the same: 9 realizations computed by the reviewer,
    including 3R1B and 3R2B A2B2, 0 witnesses.
  - Purity is global, not inert under spectators (SPECT).
  - Every state space is a simplex (N7).
- **Verdict.** "Pure" here is honest for Π_B. It is not evidence of nonclassical structure.

### (d) Pur-E

- **Counts.** 67/67 and 27/27 replicated, without the coarse-herald extras.
- **Denominators.** Correct; (1/n)ℤ at all sizes.
- **Positive dependence.**
  - The inequality is proved by algebra.
  - The "any size" claim needs the pure-state lemma and a known composition (B1).
  - In the closure's node set positive dependence occurs only through coarse heralding (MC-10). Node marginals are
    marginals of a single larger E(M), so they are negatively dependent.
- **Scarcity.** Correct.
- **Missing obstruction.** The no-product obstruction is missing (N6).

### (e) Pur-U

- "Determined by its colour count ⇒ no two pure states share an A-marginal" holds (P(a1 = R) = r/|AB|). It needs the
  pure-state lemma and MC-9 (AB filled).
- Pur-U is vacuous (0 pairs).
- The owner's deal 2 is preparable on a 1 + 2 composite as a *mixed* state. It is non-preparable only in the 1 + 3
  encoding (B2).

### (f) Controls

- 15/15 green on replay.
- Replicated independently:
  - NDP: M1 broken;
  - VIS: M1 broken;
  - CSWAP / content-controlled swaps: no change;
  - n = 7, 8: witnesses in every two-colour realization (N11).
- The K-MARK "must" is inconsistent (B3).

### (g) Scope

- No claim about OI in general (CARDS-REPORT.md:5).
- No equation of the cards with QM.
- The conflict with §1.1's ancillas is stated (MC-1, H-1, (g)1); add N12.
- Classifications as in N8.

***

## Independent replications

The reviewer's scripts are in
`<reviewer scratchpad>/revcards/indep/`. They import
nothing from the reviewed code.

**`book.py`**
- One shuffle from a depleted deck: 1/3, 2/5, 11/23 at N = 4, 6, 24.
- Engine-peek: the same values.
- Reveal and burn the visible card: 1.
- Reveal and burn the burn card: the depleted value.
- Line game: 552 blind deals, all even; peek odd mass 80/161; 22 of 24 odd positions filled; max \|d\| = 22.

**`rep.py`** (larger menu; extremality by exact Carathéodory)
- BASE: 87 realizations, 55 with witnesses, 73 witness states, 0 non-exchangeable nodes, 155 extreme states, all E(M).
- P(a1 = R) ∈ {1/4, 1/3, 1/2, 2/3, 3/4}.
- 3/4 at 3R1B, 3R2B, 4R1B, 3R3B, 4R2B, 5R1B (A2B2).
- 3R3B A2B2: \|Prep(AB)\| = 6, \|Prep(A)\| = 11, 3 extreme, 3 witnesses (1/4, 1/2, 3/4). This matches `witnesses.out`.

**`rep.py NDP`**
- 73 realizations completed, 0 witnesses.
- 3R3B A2B2 exceeded the reviewer's cap of 4·10⁵ nodes. The report's own run reached a fixed point there.

**`vis.py`**
- VIS on 9 realizations, including 3R1B and 3R2B A2B2: 0 witnesses.

**`big.py`** (n = 7, 8, all 68 realizations)
- 52 of 52 two-colour realizations have witnesses, 9 of them at 3/4.
- 0 non-exchangeable nodes; all extreme states are E(M).

**`pur.py` and `purclass.py`**
- Pur-E fails in 67/67, and in 27/27 for the same-type split.
- 0 Pur-U pairs.
- 26 non-monochrome pure A-states have no purification at any size.

**`simplex.py`**
- 297/297 preparable AB states are the unique count-mixture of preparable E(M).
- 0 non-monochrome product states.

**`deal2.py`**
- Deal 2's statistics are preparable and mixed on 1 + 2.
- In the M1 witness, B predicts a1 and A with 3/4.
- 0 of 3360 encodings of deal 2 on 1 + 3 are exchangeable.

**`h5.py`**
- The unknown-composition counterexample to H-5.

## Replay

- **SHA256SUMS.** `sha256sum -c` passes on all 33 listed files at `a9af8ef0`. Not listed: `run_all.sh` (as stated),
  `CARDS-REPORT.md` and `SHA256SUMS` itself.
- **Runs.** `CARD_TABLE=<card-table checkout> sh run_all.sh` ran twice, each in its own copy of the directory.
  Both runs exited 0; wall time 4 min 58 s and 4 min 56 s.
- **Comparison.** Of the 24 outputs, 14 are byte-identical to the committed files and to each other. The other 10 differ
  only in wall-clock fields; after stripping `[…s]` and `"secs"` they are identical:
  - `run_extra.out`;
  - `run_m1.{BASE,CSWAP,MARK,NDP,SPECT,VIS,VISNOSWAP}.json`;
  - `run_sepdeck_large.out` and `run_sepdeck_large2.out`.

  This matches CARDS-REPORT.md:293.
- **Node.** `node_check.out` was reproduced from the read-only card-table checkout.

The worktree `<reviewer worktree>` was removed after the review. No git writes were made, and `<node 8 worktree>` was not
touched.
