# Node 9, Option B, card line: exploratory design evidence

**Status.** This is pre-preregistration design evidence for draft PR #885 (`research/missing-component-20261020`, node 9).
It renders no M0–M5 verdict and is not a preregistered run. Every statement is scoped to the card constructions and
bounds defined below. Nothing here is a claim about OI in general, and the card theory is not equated with QM.

**Inputs.** `incompleteness` at `402dd98e`, read through a detached worktree (removed afterwards). `amaybaum/card-table`
at `17115cc`, read only and treated as data. Arithmetic is exact throughout (`fractions.Fraction`; F₂ for K-AFFINE).
Scripts, outputs and `SHA256SUMS` are in this directory. `run_all.sh` regenerates every output, and two consecutive
runs were compared byte for byte (see §f).

**Provenance of this revision.** Corrected in place after the independent review of this directory at `a9af8ef0`
(`REVIEW-CARDS-a9af8ef0.md`, disposition ACCEPT WITH CORRECTIONS). The reviewer's scripts, which import nothing from
`cardtheory.py` or `exactlp.py`, are in `review/` with re-run outputs; the items corrected are listed in §Corrections.

***

## (a) The card model as extracted, with code/book discrepancies

### Book §1.11 (`book/ch01-observation.md:263–297`; mirror `FULL.md:607–641`, identical apart from one trailing blank line)

- **Deck and deal.** The book speaks of a dealt deck. The minimal game has one hole card (red/black, "the coin"), held by
  the player, and one burn card face down ("the memory register").
- **The three modifications.**
  1. The shuffle between streets is a deterministic reversible permutation.
  2. Burn cards are face down, never shown, and correlated with the live cards by the shuffle (C1–C3).
  3. "Revealing a card is an intervention … a revealed card is burned and replaced under a fixed rule."
- **The swap core.** The hole card and the burn card trade places. The book's table:
  - one shuffle: ½;
  - two shuffles: 1;
  - chained through the middle: ½;
  - peek with forced re-burn: ½.
  The book says it has "sixteen cases in the longest protocol".
- **Extension (not implemented in the engine).** A linear shuffle on ranks mod q, and unistochasticity.
- **Boundary.** "No arrangement of cards on a table violates a Bell inequality". `ch03` / `FULL.md:1062` says "each
  player's hidden cards are their own".
- **Cat.** The sealed hour is the two-swap protocol, and opening the box is the peek with its forced re-burn.

### Engine (`src/engine.js`)

- **Swap core.**
  - State (v, h): v is "your card" (visible), h is the hidden card. The only move is the swap.
  - `enumerate` and `dealHand` draw v₀ and h₀ as **independent fair bits**, so there is no deck and no depletion.
  - Peek: after swap 1 the engine records `seen = v` and then **replaces h**, the hidden card that holds v₀, with a fresh
    fair bit. That gives 8 enumerated cases.
- **Cat.** With probability p the environment peeks; `catOdds = 1 − p/2`.
- **Line game.**
  - Euchre deck, 24 cards; m = ±1…6, red negative.
  - Two hidden cards are dealt without replacement. Each acts twice, so d = 2a + 2b.
  - With peek, each card acts once, is burned, and is replaced from the remaining deck: d = a + a′ + b + b′, four
    distinct cards.
  - The marker (screen) is visible and is read at the end.
  - The burn pile is not a position; burned cards just leave the game.
- **What the player can do.** Choose the protocol (peek toggle, isolation dial) and watch the outcome.
- **Records.** The trace (deal, shuffle 1, the peeked value, shuffle 2, showdown) and the marker bin.
- **Slit tables.** These are chosen, not derived (the engine says so). Out of scope here.

### Facts checked

`extract_check.out` is an independent Python enumeration; `node_check.out` imports `engine.js` directly. I did not run
`npm test` (no `node_modules`), but the engine's load-time tests pass: SELF_TEST, CAT_TEST and LINE_TEST
(24 nodes, 11 heights).

| fact | result |
|---|---|
| one / two / chained / engine-peek match | ½ / 1 / ½ / ½, reproduced |
| two-card swap lesson (K-SWAP2) | P1 = (av uniform, a1 = R) and P2 = (av uniform, a1 = B) have the same current visible distribution. One swap separates them perfectly: P(av = R) = 1 vs 0. W rank with read only is 2/4; with read and swap it is 4/4 |
| intervention table (return probability) | none 1, look at visible 1, copy visible 1, replace hidden memory ½, engine peek ½. This reproduces "1, 1, 1, ½, ½" if those are the owner's five rows; the owner's list itself is not in the repo, so that mapping is my reading |
| extra row | burning and replacing the **revealed (visible)** card gives return probability **1** |
| d_blind = 2a + 2b | even in all 552 ordered deals; odd mass 0 |
| peeked odd-position total | 126720 / 255024 = **80/161**, reproduced |
| full blind and peek distributions | equal engine.test.js `EXPECTED_BLIND` / `EXPECTED_PEEK` bin for bin |

### Discrepancies

1. **README deck size.** The README layout says "the 52-card line game". The engine, the tests and the README intro all
   use the Euchre 24-card deck.
2. **Case count.** The book says "sixteen cases in the longest protocol". The engine's peek enumeration has 8 equally
   likely cases (v₀, h₀, fresh card); the peeked value is determined, so it adds none.
3. **Which card the middle-street peek reveals.** The book does not fix it. Rule 3 (ch01:269) says "a revealed card is
   burned and replaced under a fixed rule"; the table row and the cat passage speak of a peek "(and forced re-burn)"
   (ch01:278, 280, 290). If the peek reveals the visible card and rule 3 burns and replaces *that* card, the return
   probability is 1. If it reveals the burn card and rule 3 replaces it, or (as in the engine, engine.js:31) the visible
   card is read and the burn card is replaced ("forced re-burn"), the return probability is ½ (`review/book.out`). The
   engine's reading couples "look at v" with "replace h", which is the NOTES remark that "the burn rule couples the two by
   declaration".
4. **Dealing versus independent bits.** The book says cards are dealt; the engine uses independent fair bits, i.e. an
   infinite deck. From a real two-colour deck with depletion:
   - the one-shuffle match is (N/2 − 1)/(N − 1): 0, 1/3, 2/5 and 11/23 for N = 2, 4, 6, 24;
   - the engine-peek match with replacement from the remaining deck is 11/23 at N = 24.

   This concerns the swap core dealt from a finite deck. The book's minimal game is "the coin-and-die model of §1.5
   dealt onto a table" (ch01:271), i.e. independent fair bits, and the engine's swap core and cat protocol
   (engine.js:8–36, 67–71) never use the Euchre deck; only the line game does (engine.js:110–141). The ½ entries are the
   no-depletion case.
5. **Peek does not fill every node.** README: "flip peek ON … the forbidden positions fill in". Only 22 of the 24 odd
   nodes fill; ±23 stay unreachable with peek, because four distinct cards sum to at most 22 in absolute value.
6. **The marker is non-destructive.** In the line game the marker records a function of hidden cards (2a + 2b) without
   burning them, so rule 3 covers peeks only. The engine reads the marker only at showdown (engine.js:115–116, "screen =
   final marker position"); MARK in (c), which reads it mid-protocol, is a constructed perturbation, not engine
   behaviour.
7. **Depletion crosses players (a note, not a discrepancy).** Depletion from a shared deck correlates different players'
   hidden cards (a common-cause correlation). This is consistent with ch03:188's locality statement ("each player's
   hidden cards are their own") and is noted because it is the source of the M1 pass below; it is not a Bell claim.
8. **Papers.** `papers/*.md` has no card-game passage. The only mentions are `Explainer.md:45` ("a shuffled deck of
   cards satisfies it") and `Main.md:60`'s two-state swap remark.

***

## (b) The operational theory, defined before testing (`cardtheory.py`)

### Ontic state and initial condition

- **Ontic state.** The colour (or empty) in each named slot, plus each deck as an ordered sequence. Revealed cards are
  records and are out of play.
- **Initial condition.** Each deck is uniform over the orderings of its distinct physical cards (the counting measure,
  as in Main.md:60's default).

### Generators, closed under composition (closure by BFS to a fixed point; heralding with back-action, g6)

- `deal(s, d)`: the top card of deck d goes into empty slot s.
- `move(s, t)` and `swap(s, t)` within one system.
- `cycle(d)`: a deterministic deck shuffle.
- `peek(s)`: reveals the colour; **the card leaves play**.
- `peekdeck(d)`: reveals and removes the top deck card.
- `discard(s)` and `discarddeck(d)`: the card leaves play unrevealed (a marginalisation).
- Feed-forward: by branching on outcomes.
- Mixtures: only through branch probabilities. There are no external coins; every coin is a card.

### Equivalence

Lemma W is computed on AB alone, with the deck discarded. On the filled arrangements, W has full rank in every
realization of every variant (4/4, 8/8 and 16/16), and also with one ancilla slot (8/8). So operational equivalence is
equality of the colour distribution. Because the rank is already full at k = 0, ancillas cannot refine it at k = 1 or 2.

### Composites

Systems share the realization's deck. A system's state is the marginal on its slots, with everything else discarded, and
AB is required to be filled.

### Principle Π_B (stated in advance)

"Information leaves play with the card." A card's colour reaches a record only by revealing that card, which then
leaves play for good, and every card in play comes from the realization's single deck.

**Ops(Π_B).** Every multiset-preserving rearrangement of in-play positions (content-dependent rearrangements included),
content-independent pattern changes (deal, move, discard), and destructive reveal.

The restriction to *content-independent* pattern changes belongs to the principle and is load-bearing: a
content-controlled move into an empty slot is a non-destructive read through the occupancy pattern. The choice of `move`
and `swap` within one system only (`cardtheory.py:70–77`) is immaterial: the reviewer's superset menu (cross-system
moves and swaps, a second deck shuffle, two content-controlled swaps; `review/rep.py`) gives identical BASE counts (87
realizations, 55 with witnesses, 0 non-exchangeable nodes, 155 extreme states, the same P-values and 3/4 locations;
`review/rep.BASE.out`).

**Derived, not chosen.**
- *Exchangeability invariant* [proved for a known deck composition by the lemma below; checked]: given the record, every
  preparation is a mixture of exchangeable deals E(M) (uniform over arrangements of a multiset M) over the in-play
  positions. The non-exchangeable node count is 0 in all 87 BASE realizations, and every extreme AB state equals the
  E(M) formula (155 checked).
- *Content-dependent reversible dynamics are invisible.* K-MAXREV: 36 bijections, 900 (state, bijection) pairs, none
  moved. CSWAP gives outputs identical to BASE in 40/40 realizations. So R-MENU maximality holds on the reversible part.
  Everything the principle restricts concerns information flow.

**Lemma (Π_B, known deck composition; any size).** Proof checked by the reviewer.
- (i) Given the record, the colour distribution on the in-play positions is a mixture Σ λ_M E(M). The initial deck is
  E(M₀). Content-independent relocations push E(M) forward to E(M). Every bijection of the arrangements of a fixed
  multiset, content-dependent or not, fixes the uniform distribution on them. A destructive reveal at p with outcome c
  conditions E(M) to E(M − c). A discard at p marginalizes E(M) to a mixture of E(M − c). A coarse herald mixes
  branches.
- (ii) Every preparable state of a filled system S is a mixture of preparable E_S(M), with branch-probability weights.
  Replace each discard in the protocol by a reveal whose record is never used, then reveal every in-play card outside S.
  Feed-forward depends only on records, so the original state is the branch-weighted mixture of the refined branches.
  Because the composition is known, each refined branch is E_S(M_b) with M_b fixed by the record.
- (iii) E_S(M) with distinct M have disjoint supports. So the pure states of S are exactly the preparable E_S(M), and
  conv(Prep(S)) is a simplex.
- (iv) Hence: two-slot marginals of pure states satisfy P(RR) < P(R)² unless monochrome; single-slot marginals of a pure
  state on n slots lie in (1/n)ℤ; distinct pure states of a fixed filled AB have distinct A-marginals.
- (ii) fails when the record does not fix the composition. With a deck that is RRRR or BBBB with probability ½ each,
  Prep(AB) on 2 + 2 slots is {½RRRR + ½BBBB}, which is therefore pure, and its A-marginal ½RR + ½BB is mixed (RR and BB
  are each preparable by peeking a deck card first). So ½RRRR + ½BBBB is a pure state that purifies the positively
  dependent ½RR + ½BB (`review/h5.py`, `review/h5.out`).

**Simplex structure (checked).** All 297 preparable AB states in the 87 BASE realizations are the unique colour-count
mixture of preparable E(M) vertices, and no non-monochrome preparable AB state is a product (`review/simplex.out`).
Every Π_B state space at these bounds is therefore a simplex, as (iii) proves in general for a known composition.

### Menu choices (each is a choice, not a consequence)

- **MC-1** One shared deck per realization. *This conflicts with PREREG §1.1's independently supplied ancillas*, and with
  §1.1's fresh bath cells "used at most once": the shared deck is a depleting, correlated bath.
- **MC-2** Every read is destructive, and revealed cards never return. This universalises rule 3. The book's own visible
  hole card and the line-game marker violate it, and reinsertion of a revealed card is equivalent to NDP. *This departs
  from PREREG §1.1's default non-disturbing readout and its "disturbance-free visible copy" grant*; in Option B it is
  admissible only as an R-MENU (v) postulate.
- **MC-3** No visible in-play card can enter a hidden slot (VIS versus VISNOSWAP).
- **MC-4** No clean ancillas and no second deck (an R-MENU (v) postulate).
- **MC-5** Cards are recorded by colour only.
- **MC-6** `peekdeck` is allowed. This is permissive and harmless under the invariant.
- **MC-7** A peek leaves its slot empty and replacement is a separate deal. The book forces the replacement; this is a
  superset of that.
- **MC-8** A discard is a marginalisation.
- **MC-9** A system is its named hidden slots, and AB must be filled. *This departs from PREREG §1.1's system boundary,
  "visible cells V_S together with the hidden cells"*: Π_B systems have no visible cells.
- **MC-10** Coarse-grained heralding is allowed (it is used for Pur-E's mixed states).
- **MC-11** Generated weights are branch probabilities only.

***

## (c) Verdict lines

All lines are for the stated construction and bounds only (§f).

### M1 under Π_B: holds within bounds

**Witness.** ψ = E(RRRB) on A = {a1, a2} and B = {b1, b2}:

| arrangement | RRRB | RRBR | RBRR | BRRR |
|---|---|---|---|---|
| probability | ¼ | ¼ | ¼ | ¼ |

- The accessible binary measurement `peek a1` gives P(R) = **3/4**.
- ψ is extreme in conv(Prep(AB)), checked by exact LP, so it is pure on all three readings.
- **At the budget:** ψ is reached at depth 4–6.
- **Across the model:** it remains pure at the closure's fixed point.
- **Convex closure:** it is extreme.
- The A-marginal is mixed with a generated weight: ¾·E(RRB)|_A + ¼·RR, or ½/½ for deck 5R1B.
- Protocol for deck 3R3B: reveal the top 2 deck cards, herald on BB (probability 1/5), deal a1, a2, b1, b2.

**Where it holds.**
- The 3/4 witness is found in 6 realizations: 3R1B, 3R2B, 3R3B, 4R1B, 4R2B and 5R1B. In 5 of them |Prep(AB)| > 1;
  3R1B is the trivial one.
- 55 of 87 realizations have some witness (47 nontrivial), with P(a1 = R) ∈ {1/4, 1/3, 1/2, 2/3, 3/4}.
- ψ is not a product, and no non-monochrome extreme state is a product. Shared depletion therefore gives pure correlated
  states that are not mixtures of preparable products. The definite deals that decompose them ontically are never
  preparable (K-HERALD analogue: no non-monochrome definite deal of AB is preparable; definite single-slot states and
  monochrome deals are, e.g. by revealing the deck down to its last card).
- **The pass is a pass of a simplicial theory.** Every Π_B state space at these bounds is a simplex (lemma (iii) and the
  simplex check in (b)), with no preparable non-monochrome product states. ψ is a vertex of a classical simplex whose
  A-marginal is not a vertex. M1 passes because the composite has no preparable product states; nothing nonclassical is
  involved. "Pure" is honest for Π_B, and it is not evidence of nonclassical structure.
- Under the 1 + 3 split (A = a1, B = a2 b1 b2), E(RRRB) is the card encoding of the owner's deal 1 (controls.py:98).
  Under the M1 split (A = a1 a2, B = b1 b2), B predicts A, and a1, with success 3/4; only A's colour count is determined
  by B. The joint of (a1; b1 b2) is {(R;RB), (R;BR), (R;RR), (B;RR)} at ¼ each, which is the owner's deal 2 statistics
  (`review/deal2.out`).

**Perturbations.**

| perturbation | M1 within bounds |
|---|---|
| CSWAP (content-dependent reversible joint op) | identical to BASE |
| VISNOSWAP (visible cards that never return to hidden play) | M1 outputs identical to BASE (non-exchangeable node counts differ, because the visible slots hold read cards) |
| larger decks n = 7, 8 (beyond the bound) | 18/18 in `run_extra.py`'s selection (6 decks × 3 splits) have witnesses, including 3/4. The reviewer's full sweep (all 68 realizations at n = 7, 8, every composition, splits A1B1, A1B2, A2B1, A2B2): witnesses in all 52 two-colour realizations, 9 of them at 3/4, 0 non-exchangeable nodes, every extreme state an E(M) (`review/big.out`) |
| NDP (non-destructive peek) | **fails**, 0/87 |
| VIS = K-CLASSICAL (the book's movable visible hole card) | **fails**, 0/87, and 0/6 with the visible slots inside AB |
| SPECT (one unrevealed card left in a third system, pool unrestricted) | **fails**, 0/71 |
| SEPDECK, second deck with ample cards of each colour ((4,0)+(0,4), (3,1)+(1,3), (3,2)+(2,3), (4,1)+(1,4); totals 8–10, beyond the n ≤ 6 bound) | **fails**, 0 witnesses |
| MARK (line-game marker read mid-protocol; a constructed perturbation, since the engine reads the marker only at showdown) | the 3/4 witness is lost; ½ witnesses remain in 7/87 small-deck realizations (n ≤ 5), none at n = 6 |
| SEPDECK with scarce decks | 38/97 witnesses within the bound. Independent scarce decks keep witnesses for A2B2 (witness states, `run_sepdeck_large.out`): (2,2)+(2,2) 10, (2,1)+(2,1) 12, (3,1)+(3,1) 7, (2,2)+(3,1) 5. They vanish once each deck can supply enough definite cards (`run_sepdeck_large*.out`) |

Under the stricter generated-weight budget reading, witness-state counts are BASE 73 → 73, MARK 9 → 10, and NDP, VIS,
SPECT 0 → 0 (`run_m1.*.json`, `run_budget_strict.out`). The table above counts realizations (BASE 55, MARK 7).

### Pur-E under Π_B: fails within bounds

Some preparable A-state lacks a purification in 67 of 67 realizations, and in 27 of 27 with a same-type purifier
(A = 1 with B = 1, or A = 2 with B = 2).

The obstructions:
- **(0) Non-monochrome pure A-states, at any size.** A non-monochrome pure two-slot A-state, E(RB), has no purification
  at any purifier size ≥ 1: writing p for the two-slot marginal of an E(M) on n slots, p(RR) = p(BB) = 0 forces n ≤ 2.
  This occurs 26 times across the 67 realizations (`review/purclass.out`). It is H-1 (no product states) appearing
  inside M2: the purification of a pure state would be a product. `run_pur.out` labels it "non-monochrome pure A-state
  E(RB): no purification at any size" and counts it 30 times; the 4 extra are the coarse-herald extra state, which in
  1R3B and 3R1B (A = 2, B = 1 and 2) coincides with a heralded marginal already listed.
- **Purifier too small.** An E(M) on 1 + m slots has marginals in (1/(m+1))ℤ. So 3/4 on a 1-slot A needs m ≥ 3 (beyond
  the bound), and K-BIAS (3/8, 3/8, 1/8, 1/8) as a 4-rank slot needs m = 7 (`E({0,0,0,1,1,1,2,3})`, checked exactly).
- **Positive dependence, at any size, for a known deck composition.** A two-slot state with P(RR) ≥ P(R)², not
  monochrome, has no purification at any size for a known deck composition. Pure states are single E(M) (lemma (iii)),
  and the two-slot marginal of E(M) satisfies P(RR) = r(r−1)/(n(n−1)) < (r/n)² for 0 < r < n (algebra, all n:
  (r−1)n < r(n−1) ⇔ r < n; brute-forced for n ≤ 7). With a composition unknown to the record the obstruction fails
  (lemma, last item). An example is ½RR + ½BB, which is preparable by heralding on two same-colour reveals. All six two-slot encodings of the
  K-BIAS numbers are unpurifiable (|M| ≤ 40).
- **Scarcity.** The required E(M) exists in principle but this realization's deck cannot prepare it.

This is the card analogue of the affine-family Pur-E failure. Unequal fibres escape the affine obstruction for the
biased numbers on a 4-rank slot, but only with a large enough purifier, and not at all for positively correlated
two-slot states.

### Pur-U under Π_B: vacuous within bounds

- No pair of distinct pure AB states shares an A-marginal, so no pair is tested (0 pairs in 67 realizations;
  `run_pur.out`, "total Pur-U pairs tested: 0"). An E(M) is fixed by its colour count, and its A-marginal determines
  that count (P(a1 = R) = r/|AB|); this uses the lemma's pure-state characterization and MC-9 (AB filled).
- Pure states are single E(M), so B determines A's colour count. For |A| = 1 this means B determines A, and a
  deal-2-type state (B predicts A with success 3/4) cannot be pure. Deal 2's statistics are nevertheless preparable on a
  1 + 2 composite as the mixed state ¼E(RRR) + ¾E(RRB), the 3-slot marginal of E(RRRB) (mixed at decks 3R1B, 3R2B, 3R3B
  and 4R2B), and no exchangeable encoding of deal 2 on a 1 + 3 composite exists (0 of 3360 injective encodings;
  `review/deal2.out`). So Π_B admits deal 1 as pure and deal 2 only as mixed. For |A| = 2, a pure state can have B
  predicting A with success 3/4 (the M1 witness).
- The detector reports (deal 1, deal 2) unconnected under S₃, and none of the 24 relabellings connects them
  (countercontrol green).
- No B-local reversible operation acts nontrivially on any preparable state (K-MAXREV). This "uniqueness" therefore
  comes from how few pure states there are, not from a transitive reversible group.

**Pur-E and Pur-U are kept separate.** States with no purification count against Pur-E only.

***

## (d) Controls (`controls.out`: 15/15 green)

| control | result |
|---|---|
| K-AFFINE | F₂^{2(1+m)}, m = 1, 2: 307 and 26387 affine subsets; no marginal equals the biased state, so Pur-E fails; local binary linear measurements give only {0, ½, 1} |
| K-BIAS | (3/8, 3/8, 1/8, 1/8) = ½·unif{00, 01} + ½·unif(all). In cards: (a) and (b) as in Pur-E above |
| K-UNIQ | equal marginals 3/4; prediction 1 vs 3/4; 0 of 24 relabellings connect the deals. Card encoding (1 + 3 split, controls.py:97–100): deal 1 = E(RRRB), deal 2 non-exchangeable, unconnected. No exchangeable 1 + 3 encoding of deal 2 exists (0 of 3360, `review/deal2.out`); on 1 + 2 its statistics are preparable as a mixed state (Pur-U above). The detector countercontrol is green and not vacuous |
| K-SWAP2 | as in (a) |
| K-CLASSICAL (= VIS) | M1 **fails** in every realization (87 + 6). Extreme states are definite deals, e.g. 14 of 16 at 3R3B. Required to fail: green |
| K-HERALD (card) | destructive peek leaves a1 empty in every branch; NDP leaves a1 equal to the outcome in every branch |
| Formula and engine checks | hypergeometric formula brute-forced (n ≤ 7); E(M) formula equals the closure's extreme states (155); exact-LP self-test; Lemma W ranks; Python and Node agree on the card-table numbers |

***

## (e) Hidden assumptions (assumption-watch candidates)

1. **H-1 Single deck, so no independent preparation.** In Π_B, R⊗B is never preparable, even though R and B each are.
   Adding a second deck that can supply enough definite cards kills M1 (scarce independent decks do not; (c)). The M1
   pass is the failure of node 8's composition-lemma premise (not every composite preparation is a mixture of
   preparable products). It also contradicts PREREG §1.1's independently supplied ancillas.
2. **H-2 Global purity.** E(M) on AB is pure only when AB holds *every* in-play card, the deck included, with the rest
   revealed. A discarded card gives a mixture, and so does one unrevealed spectator card anywhere (SPECT, 0/71). Any
   ancilla in play makes AB mixed. This is the closed-system, fixed-total structure of finite exchangeability; the
   literature has not been checked (finite de Finetti, Diaconis–Freedman 1980; negative dependence under sampling
   without replacement, Joag-Dev–Proschan 1983; both [Q], unread). H-2 shares an ingredient with the corpus's "inert
   spectators" condition (GR.md:216, item (iii)); that is a shared ingredient, not an identification.
3. **H-3 No non-destructive record.** This covers NDP, reinsertion of a revealed card, the line-game marker and the
   book's movable visible hole card. A free visible record **that can re-enter hidden play** breaks the restriction (VIS),
   while one that never re-enters is harmless (VISNOSWAP). This is consistent with the C-i/emb lesson on clean visible
   resources.
4. **H-4 No clean ancillas or known-card supply** (SEPDECK (4,0)+(0,4)).
5. **H-5 Deck knowledge.** With a known composition, the record fixes the in-play multiset, and pure states are exactly
   the preparable E(M) (lemma in (b)). With a composition unknown to the record, pure states need not be single E(M):
   with RRRR or BBBB at ½ each, ½RRRR + ½BBBB is pure and purifies the positively dependent ½RR + ½BB (`review/h5.out`).
   Deck knowledge is therefore load-bearing for the pure-state characterization, for Pur-U's triviality and for the
   positive-dependence obstruction.
6. **H-6 Colour-only records** (MC-5).
7. **H-7 Scarcity.** Small-deck witnesses outside BASE (MARK, SEPDECK) disappear as the decks grow. BASE witnesses do
   not (n = 7, 8).
8. **H-8 Degenerate uniqueness.** Pur-U holds because there are few pure states, not because the reversible group is
   rich; at these bounds it is vacuous (0 pairs).
9. **H-9 Simplicial state spaces without product states.** Every Π_B state space is a simplex (lemma (iii); 297/297 at
   these bounds), and no non-monochrome preparable AB state is a product. M1 as worded (PREREG §3) is passed by this
   classical theory; the pass rests on the absence of product preparations (H-1), not on nonclassical structure.

***

## (f) Bounds

- **Decks.** n = 2…6 cards, 1–2 colours, every composition. A single deck, except SEPDECK (two decks, total ≤ 6 within
  the bound; up to 10 beyond it). n = 7, 8 for robustness only. A 4-rank slot and |M| ≤ 40 only in the direct
  K-BIAS checks.
- **Slots.** A and B have 1–2 hidden slots each; VIS adds 1 visible slot per system; B = 3 for Pur-E only, beyond the
  bound.
- **Closure.** Every closure reached a fixed point (completeness certificate), with fixed-point depth ≤ 16, s_max = 3–6·10⁵
  never reached, and nothing PARKED.
- **Equivalence.** Lemma W at k = 0, plus one ancilla slot. The k = 2 result follows from full rank at k = 0.
- **Purity.** Exact LP extremality (convex-closure reading, which implies the other two). The budget reading uses pair
  decompositions over the heralded marginals.
- **Mixtures.** Not enumerated beyond heralded marginals and the named coarse-herald states.
- **Not computed.** Bell, no-signalling, M3 and M5, and the "no counting" variant.
- **Record pinning.** This report and `SHA256SUMS` are not listed in `SHA256SUMS`; the report is pinned by its commit.
  `review/SHA256SUMS` covers the reviewer's scripts and their re-run outputs. Recipe: from `review/`,
  `python3 -I <name>.py > <name>.out` for `h5`, `deal2`, `pur`, `purclass`, `simplex`, `book` and `big`, and
  `python3 -I rep.py > rep.BASE.out`; about 15 s in total, and two runs agree byte for byte.
- **Compute and replay.** Total compute for one `run_all.sh` is about 4 minutes. Replay: two full runs; all 24 outputs agree byte for byte except 10 whose only differences are wall-clock timing fields (`[…s]`, `"secs"`), verified by diff after stripping those fields.

***

## (g) What Option B's preregistration should take from this

1. **Freeze the deck and ancilla question first.** Fix whether PREREG §1.1's independent ancillas hold in Option B. With
   a second deck that can supply enough definite cards of each colour (tested: (4,0)+(0,4), (3,1)+(1,3), (3,2)+(2,3),
   (4,1)+(1,4); totals 8–10, beyond the n ≤ 6 bound), no M1 witness was found; scarce independent decks leave witnesses.
   Without it, M1 passes only by violating the composition-lemma premise, and purity becomes global (H-2).
2. **Freeze the read rules, as postulates under R-MENU (v).** "Every read destructive; nothing revealed re-enters
   play; visible cards never enter hidden slots." Ops(Π_B) may admit every content-dependent reversible rearrangement;
   that is derived, not a menu choice.
3. **Carry these controls with fixed "must" columns.**
   - K-NDP, K-VIS (= K-CLASSICAL) and K-SPECT: M1 must fail. K-MARK: no 3/4 witness, and M1 must fail at n = 6 (½
     witnesses remain in 7/87 realizations at n ≤ 5). K-SEPDECK-ample at its stated decks (totals 8–10, outside the
     n ≤ 6 bound): M1 must fail. K-SEPDECK-scarce: reported, with no must.
   - K-VISNOSWAP and K-MAXREV/CSWAP: outputs must be identical to BASE.
   - K-UNIQ's card encoding and K-BIAS (a)/(b).
4. **Productivity baseline.** Add the exchangeability invariant, the positive-dependence obstruction and the
   denominator obstruction, together with obstruction (0) (non-monochrome pure A-states have no purification), to the
   §6 baseline. Then an M2 FAIL of a Π_B-type model is a restatement, not a gem. A Π_B-type M1 PASS is a PASS of a
   simplicial theory without product states; M1 as worded (PREREG §3) does not separate this from a quantum-like
   composite.
   - Proposed classification of the present results (for the owner to decide):
     - the M1 mechanism: ELABORATING (an instance of the composition-lemma premise failing);
     - H-1: ELABORATING. It is the failure of the composition-lemma premise, the same fact as the M1 mechanism;
     - H-2: not credited before a literature check (finite de Finetti, Diaconis–Freedman; negative dependence under
       sampling without replacement, Joag-Dev–Proschan; [Q]);
     - NEW candidate, a methodology marker (H-9): M1 is passed by a classical simplicial theory with no preparable
       products unless the preregistration adds a product-preparability or spectator-stability clause. It needs
       pressure-testing before it is credited (PREREG §3, M1, carries a draft clause);
     - Pur-U: vacuous (0 pairs tested); record only. The detector countercontrol (K-UNIQ card) is green and not
       vacuous.
5. **Expected outcomes.** If Option B keeps MC-1 to MC-4, expect M1 PASS, Pur-E FAIL, and Pur-U only trivially true.
   Option B's target (operational purification with essential uniqueness) is then not met by Π_B with MC-1–MC-4 at
   these bounds.
   A Pur-E repair would need positively dependent states to become non-preparable, or purifiable, without
   reintroducing non-destructive records.
6. **State the deck model.** If the swap core is dealt from a finite two-colour deck of N cards, the ½ entries become
   (N/2 − 1)/(N − 1) (11/23 at N = 24); the book's coin-and-die game and the engine's fair bits are the no-depletion
   case. State which card the peek reveals and which card rule 3 burns (discrepancy 3).

***

## Corrections

Applied in place after `REVIEW-CARDS-a9af8ef0.md`; the review's finding IDs are kept. Evidence is in `review/` (scripts
re-run; outputs committed) unless stated otherwise.

- **B1.** "No purification at any size" is now scoped to a known deck composition, with the lemma and its proof in (b).
  The inequality P(RR) < P(R)² is algebra at all n, not a check up to n ≤ 12. H-5 is replaced: deck knowledge is
  load-bearing, with the unknown-composition counterexample ½RRRR + ½BBBB (`review/h5.py`, `review/h5.out`).
- **B2.** The deal 1 / deal 2 statements in (c) and Pur-U are corrected: on the 2 + 2 split the M1 witness has B
  predicting a1 and A with success 3/4 (deal 2's statistics); "cannot be pure" holds only for |A| = 1; deal 2's
  statistics are preparable on 1 + 2 only as the mixed ¼E(RRR) + ¾E(RRB); no 1 + 3 encoding of deal 2 out of 3360 is
  exchangeable (`review/deal2.out`).
- **B3.** The (g)3 "must" columns no longer require K-MARK to fail at n ≤ 5 (7/87 ½ witnesses there); K-SEPDECK-ample is
  marked as lying outside the n ≤ 6 bound.
- **N1–N4.** Discrepancy 3 is reading-dependent, and the book's "forced re-burn" (ch01:278, 280, 290) matches the
  engine (`review/book.out`); 11/23 concerns a deck-dealt swap core, not the book's coin-and-die game (ch01:271);
  discrepancy 7 is a note on common-cause correlation, consistent with ch03:188; the marker is read at showdown only,
  and MARK is a constructed perturbation.
- **N5.** The K-HERALD parenthetical in (c) is corrected: counting also leaves definite cards; no non-monochrome
  definite deal of AB is preparable.
- **N6.** Obstruction (0) is added to Pur-E (26 occurrences, `review/purclass.out`). The classifier `why` in
  `cardtheory.py` (`pur_analysis`) now labels E(RB) "non-monochrome pure A-state E(RB): no purification at any size"
  instead of "purifier too small". `run_pur.out` was regenerated; it differs from its previous version only in the
  obstruction-class lines, where these states move from the "purifier too small" label to the new one. A full
  `run_all.sh` replay after the change reproduces every committed output byte for byte, apart from the 10 files whose
  only differences are wall-clock fields.
- **N7.** The simplex structure is stated in (b), (c) and (e) (H-9; `review/simplex.out`).
- **N8.** The proposed classifications in (g)4 are revised: the M1 mechanism and H-1 ELABORATING; H-2 pending a
  literature check; a methodology marker (H-9) as the NEW candidate; Pur-U vacuous, record only.
- **N9.** The budget-reading counts are stated in witness states, separately from the realization counts.
- **N10.** The SEPDECK statements in (c), (g)1 and H-1 distinguish ample decks (beyond the bound) from scarce
  independent decks, which keep witnesses.
- **N11.** The n = 7, 8 row states the 6-deck selection and adds the full sweep (`review/big.out`).
- **N12.** MC-1, MC-2 and MC-9 state their departures from PREREG §1.1.
- **N13.** The load-bearing restriction to content-independent pattern changes and the immateriality of the
  within-system `move`/`swap` choice are stated in (b) (`review/rep.BASE.out`).
- **N14.** Wording in H-3, (g)5 and the VISNOSWAP row.
- **N15.** (f) states that this report is pinned by its commit rather than by `SHA256SUMS`.
