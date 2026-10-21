# Node 9, Option B, card line: exploratory design evidence

**Status.** This is pre-preregistration design evidence for draft PR #885 (`research/missing-component-20261020`, node 9).
It renders no M0–M5 verdict and is not a preregistered run. Every statement is scoped to the card constructions and
bounds defined below. Nothing here is a claim about OI in general, and the card theory is not equated with QM.

**Inputs.** `incompleteness` at `402dd98e`, read through a detached worktree (removed afterwards). `amaybaum/card-table`
at `17115cc`, read only and treated as data. Arithmetic is exact throughout (`fractions.Fraction`; F₂ for K-AFFINE).
Scripts, outputs and `SHA256SUMS` are in this directory. `run_all.sh` regenerates every output, and two consecutive
runs were compared byte for byte (see §f).

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
3. **Which card rule 3 burns.** The book says the *revealed* card is burned and replaced. The engine reveals v and
   replaces h, the memory card. Under the literal book rule the return probability is 1 and there is no division event.
   The ½ comes from the declared coupling of "look at v" with "replace h", which is the NOTES remark that "the burn rule
   couples the two by declaration".
4. **Dealing versus independent bits.** The book says cards are dealt; the engine uses independent fair bits, i.e. an
   infinite deck. From a real two-colour deck with depletion:
   - the one-shuffle match is (N/2 − 1)/(N − 1): 0, 1/3, 2/5 and 11/23 for N = 2, 4, 6, 24;
   - the engine-peek match with replacement from the remaining deck is 11/23 at N = 24.

   The table's ½ entries hold only without depletion.
5. **Peek does not fill every node.** README: "flip peek ON … the forbidden positions fill in". Only 22 of the 24 odd
   nodes fill; ±23 stay unreachable with peek, because four distinct cards sum to at most 22 in absolute value.
6. **The marker is non-destructive.** In the line game the marker records a function of hidden cards (2a + 2b) without
   burning them, so rule 3 covers peeks only. This matters in (b) and (e): the MARK perturbation.
7. **Depletion crosses players.** "Each player's hidden cards are their own" does not hold for depletion from a shared
   deck, which correlates different players' hidden cards. That is exactly the source of the M1 pass below. This is not
   a Bell claim.
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

**Derived, not chosen.**
- *Exchangeability invariant* [W, checked]: given the record, every preparation is a mixture of exchangeable deals E(M)
  (uniform over arrangements of a multiset M) over the in-play positions. The non-exchangeable node count is 0 in all
  87 BASE realizations, and every extreme AB state equals the E(M) formula (155 checked).
- *Content-dependent reversible dynamics are invisible.* K-MAXREV: 36 bijections, 900 (state, bijection) pairs, none
  moved. CSWAP gives outputs identical to BASE in 40/40 realizations. So R-MENU maximality holds on the reversible part.
  Everything the principle restricts concerns information flow.

### Menu choices (each is a choice, not a consequence)

- **MC-1** One shared deck per realization. *This conflicts with PREREG §1.1's independently supplied ancillas.*
- **MC-2** Every read is destructive, and revealed cards never return. This universalises rule 3. The book's own visible
  hole card and the line-game marker violate it, and reinsertion of a revealed card is equivalent to NDP.
- **MC-3** No visible in-play card can enter a hidden slot (VIS versus VISNOSWAP).
- **MC-4** No clean ancillas and no second deck (an R-MENU (v) postulate).
- **MC-5** Cards are recorded by colour only.
- **MC-6** `peekdeck` is allowed. This is permissive and harmless under the invariant.
- **MC-7** A peek leaves its slot empty and replacement is a separate deal. The book forces the replacement; this is a
  superset of that.
- **MC-8** A discard is a marginalisation.
- **MC-9** A system is its named hidden slots, and AB must be filled.
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
  preparable (K-HERALD analogue: only a non-destructive read leaves a definite card in play).
- The witness is the owner's deal 1 under the labelling of B's arrangements.

**Perturbations.**

| perturbation | M1 within bounds |
|---|---|
| CSWAP (content-dependent reversible joint op) | identical to BASE |
| VISNOSWAP (visible cards that never return to hidden play) | identical to BASE |
| larger decks n = 7, 8 (beyond the bound) | 18/18 realizations have witnesses, including 3/4 |
| NDP (non-destructive peek) | **fails**, 0/87 |
| VIS = K-CLASSICAL (the book's movable visible hole card) | **fails**, 0/87, and 0/6 with the visible slots inside AB |
| SPECT (one unrevealed card left in a third system, pool unrestricted) | **fails**, 0/71 |
| SEPDECK, second deck with ample cards of each colour ((4,0)+(0,4), (3,1)+(1,3), (3,2)+(2,3), (4,1)+(1,4)) | **fails**, 0 witnesses |
| MARK (line-game marker read mid-protocol) | the 3/4 witness is lost; ½ witnesses remain in 7/87 small-deck realizations (n ≤ 5), none at n = 6 |
| SEPDECK with scarce decks | 38/97 witnesses within the bound; they persist at (2,2)+(2,2) for A2B2 and vanish once each deck can supply enough definite cards (`run_sepdeck_large*.out`) |

Under the stricter generated-weight budget reading, the counts are unchanged for NDP, VIS, SPECT and BASE; MARK goes
from 9 to 10.

### Pur-E under Π_B: fails within bounds

Some preparable A-state lacks a purification in 67 of 67 realizations, and in 27 of 27 with a same-type purifier
(A = 1 with B = 1, or A = 2 with B = 2).

The obstructions:
- **Purifier too small.** An E(M) on 1 + m slots has marginals in (1/(m+1))ℤ. So 3/4 on a 1-slot A needs m ≥ 3 (beyond
  the bound), and K-BIAS (3/8, 3/8, 1/8, 1/8) as a 4-rank slot needs m = 7 (`E({0,0,0,1,1,1,2,3})`, checked exactly).
- **Positive dependence, at any size.** A two-slot state with P(RR) ≥ P(R)², not monochrome, has no purification at any
  size, because marginals of E(M) satisfy P(RR) = r(r−1)/(n(n−1)) < (r/n)². This is [W], checked exactly for n ≤ 12.
  An example is ½RR + ½BB, which is preparable by heralding on two same-colour reveals. All six two-slot encodings of the
  K-BIAS numbers are unpurifiable (|M| ≤ 40).
- **Scarcity.** The required E(M) exists in principle but this realization's deck cannot prepare it.

This is the card analogue of the affine-family Pur-E failure. Unequal fibres escape the affine obstruction for the
biased numbers on a 4-rank slot, but only with a large enough purifier, and not at all for positively correlated
two-slot states.

### Pur-U under Π_B: holds within bounds, trivially

- No pair of distinct pure AB states shares an A-marginal (0 pairs in 67 realizations). An E(M) is fixed by its colour
  count, and its A-marginal determines that count.
- B always determines A's colour count, so deal 2 type states (B predicts A with success 3/4) cannot be pure.
- Deal 2 is not exchangeable, so Π_B excludes it.
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
| K-UNIQ | equal marginals 3/4; prediction 1 vs 3/4; 0 of 24 relabellings connect the deals. Card encoding: deal 1 = E(RRRB), deal 2 non-exchangeable, unconnected |
| K-SWAP2 | as in (a) |
| K-CLASSICAL (= VIS) | M1 **fails** in every realization (87 + 6). Extreme states are definite deals, e.g. 14 of 16 at 3R3B. Required to fail: green |
| K-HERALD (card) | destructive peek leaves a1 empty in every branch; NDP leaves a1 equal to the outcome in every branch |
| Formula and engine checks | hypergeometric formula brute-forced (n ≤ 7); E(M) formula equals the closure's extreme states (155); exact-LP self-test; Lemma W ranks; Python and Node agree on the card-table numbers |

***

## (e) Hidden assumptions (assumption-watch candidates)

1. **H-1 Single deck, so no independent preparation.** In Π_B, R⊗B is never preparable, even though R and B each are.
   Adding a second deck with enough cards kills M1. The M1 pass is the failure of node 8's composition-lemma premise
   (not every composite preparation is a mixture of preparable products). It also contradicts PREREG §1.1's
   independently supplied ancillas.
2. **H-2 Global purity.** E(M) on AB is pure only when AB holds *every* in-play card, the deck included, with the rest
   revealed. A discarded card gives a mixture, and so does one unrevealed spectator card anywhere (SPECT, 0/71). Any
   ancilla in play makes AB mixed.
3. **H-3 No non-destructive record.** This covers NDP, reinsertion of a revealed card, the line-game marker and the
   book's movable visible hole card. A free visible record **that can re-enter hidden play** breaks the restriction (VIS),
   while one that never re-enters is harmless (VISNOSWAP). This confirms the C-i/emb lesson on clean visible resources.
4. **H-4 No clean ancillas or known-card supply** (SEPDECK (4,0)+(0,4)).
5. **H-5 Deck knowledge and counting.** Knowing the deck and remembering reveals sets *which* E(M) are reachable (the
   heralds on revealed counts), but does not affect the purity mechanism. This is argued, not computed.
6. **H-6 Colour-only records** (MC-5).
7. **H-7 Scarcity.** Small-deck witnesses outside BASE (MARK, SEPDECK) disappear as the decks grow. BASE witnesses do
   not (n = 7, 8).
8. **H-8 Degenerate uniqueness.** Pur-U holds because there are few pure states, not because the reversible group is
   rich.

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
- **Compute and replay.** Total compute for one `run_all.sh` is about 4 minutes. Replay: two full runs; all 24 outputs agree byte for byte except 10 whose only differences are wall-clock timing fields (`[…s]`, `"secs"`), verified by diff after stripping those fields.

***

## (g) What Option B's preregistration should take from this

1. **Freeze the deck and ancilla question first.** Fix whether PREREG §1.1's independent ancillas hold in Option B. With
   independent supply (a second ample deck or clean known cards), the card route's M1 pass disappears at these bounds.
   Without it, M1 passes only by violating the composition-lemma premise, and purity becomes global (H-2).
2. **Freeze the read rules, as postulates under R-MENU (v).** "Every read destructive; nothing revealed re-enters
   play; visible cards never enter hidden slots." Ops(Π_B) may admit every content-dependent reversible rearrangement;
   that is derived, not a menu choice.
3. **Carry these controls with fixed "must" columns.**
   - K-NDP, K-VIS (= K-CLASSICAL), K-MARK, K-SPECT and K-SEPDECK-ample: M1 must fail.
   - K-VISNOSWAP and K-MAXREV/CSWAP: outputs must be identical to BASE.
   - K-UNIQ's card encoding and K-BIAS (a)/(b).
4. **Productivity baseline.** Add the exchangeability invariant, the positive-dependence obstruction and the
   denominator obstruction to the §6 baseline. Then an M2 FAIL of a Π_B-type model is a restatement, not a gem.
   - Proposed classification of the present results (for the owner to decide):
     - the M1 mechanism: ELABORATING (an instance of the composition-lemma premise failing);
     - the global-purity / no-independent-ancilla marker H-1/H-2: NEW candidate;
     - Pur-U: CONFIRMING/trivial.
5. **Expected outcomes.** If Option B keeps MC-1 to MC-4, expect M1 PASS, Pur-E FAIL, and Pur-U only trivially true.
   Option B's target (operational purification with essential uniqueness) is then not met by card rules at these bounds.
   A Pur-E repair would need positively dependent states to become non-preparable, or purifiable, without
   reintroducing non-destructive records.
6. **Stop treating ½ as a deck fact.** Use the depleted-deck values (11/23 for Euchre) in any card-derived prediction,
   and state which card rule 3 burns (discrepancy 3).
