# SC-39: the card-game Bell sentence

Base: `main` at `0d917665`. Finding: R-32 (Introduction L188/L255; consolidated audit A-B3, VERIFY item 5) and
its corpus side, which no PR carried. Line numbers are those of the base.

## The governing result

The governing result is Main §3.3, Theorem (Bell ceiling for a screened local completion), Main:360–375.
Its hypotheses are:

- (i) deterministic dynamics;
- (ii) a one-step setting operation on disjoint regions, each intervention reading and writing only its own
  region;
- (iii) ±1 readouts outside the other wing's graph cone;
- (iv) one setting-independent pre-setting ensemble, p(Ω | a, b) = p(Ω);
- a ±1 outcome recorded in every run.

Under these hypotheses |S_CHSH| ≤ 2. Without the locality hypotheses, Main:356 states that globally coupled,
setting-dependent hidden dynamics realize PR-box behaviour. The book's card sentences stated the ceiling for
every arrangement of cards.

## Per claim

### C-1. ch01:286 and FULL:630

- **Original.** "It reproduces single-system interference, indivisibility, and division events — the mechanism
  of this chapter — but no arrangement of cards on a table violates a Bell inequality, and the Bell-type
  correlations of §1.7 belong to the full construction, …" The sentence opens "a card mechanism is a local
  classical toy", also unconditionally.
- **Defect.** Unrestricted. A card table can break each hypothesis of the ceiling, and each break below
  reaches CHSH = 4 (exact):
  - a move after the settings that acts on both hands (X1);
  - a rule-prescribed whole-deck shuffle after the settings that carries A's setting card into B's hand, while
    every player move stays on the player's own cards (X1′);
  - a rule-prescribed shuffle that writes only B's cards but reads A's setting card (L1, the reading
    loophole);
  - a rule that chooses, depending on b, between two operations on A's cards each of which is own-card (L2,
    the schedule loophole);
  - a coin shared by both players and correlated with the settings (P2);
  - two coins, each uniform for every setting pair and each used by one player only, but jointly correlated
    with the settings (C1);
  - A's coin, uniform for every setting pair, jointly encoding ab with A's dealt card (C2);
  - readouts that read only the player's own cards, with the readout function selected by b (C3);
  - a deal arranged with knowledge of the settings (X2);
  - runs without an outcome discarded (X3).
- **Correction (exact text now at ch01:286 = FULL:630).** "One boundary must be stated as plainly as the successes: a card mechanism played under the restrictions below is a local classical toy. It reproduces single-system interference, indivisibility, and division events — the mechanism of this chapter — but it violates no Bell inequality when, once the deal is down, every operation — each shuffle the rules prescribe, each move and each setting choice — reads and writes one player's own cards only; which operation is applied to a player's cards, and how that player's $\pm1$ outcome is read from them, depends only on those cards, that player's own setting and on chance that, taken together with the deal, is independent of the settings; an outcome is recorded in every run and no run is set aside; and the settings are chosen independently of the deal: such a game is a local hidden-variable model (Main §3.3). The Bell-type correlations of §1.7 belong to the full construction, …"
- **History on this branch.**
  - 0c2356f3 restricted only the players' moves, leaving X1′ open.
  - ced30f6c restricted every operation, but read "acts on" as write-only (L1) and fixed no schedule (L2). It
    also required determinism, which is narrower than needed.
  - f0e8e761 closed L1 and L2 and replaced determinism with a private-chance clause. That clause did not give
    the joint independence of (deal, chance) from the settings (C1, C2). It was also narrower than needed: a
    shared setting-independent coin is admissible (C4). It clashed with "depends on those cards alone", which
    forbade chance-driven choices of operation. It left the readout rule unrestricted (C3), and ch01's "which
    operation the rules apply" omitted player-chosen moves.
  - b468ca6e put operation choice and readout under one clause: own cards plus chance drawn, together with
    the deal, independently of the settings. ch01 uses ch03's passive "is applied".
  - This commit makes three wording edits (review round 5, all optional, each making the stated condition
    exact):
    - "chance that, taken together with the deal, is independent of the settings" removes a temporal reading;
    - "that player's own setting" is admitted explicitly, since the setting choice depends on it before it is
      written;
    - the ch03 gloss states the joint condition: "the deal, taken together with any chance the game uses, does
      not know the settings".

    The own-setting admission opens no loophole. Main §3.3 already allows q_a and r_b to depend on the own
    setting. E3/O3b accept an own-setting schedule and reject a b-selected one, O3a gives max |CHSH| = 2 over
    every own-setting-selected readout rule, and C3 (readout selected by b) still fires.
- **Condition map.**

  | Book condition | Main §3.3 hypothesis |
  |---|---|
  | once the deal is down, every operation reads and writes one player's own cards only | (ii) for the setting choices; for every later update, no step reads or writes across the hands, so the coupling graph after the deal has no edge between the hands and each readout stays outside the other wing's cone, as (iii) requires |
  | which operation is applied to a player's cards, and how the player's outcome is read from them, depends only on those cards, that player's own setting and on chance that, taken together with the deal, is independent of the settings | (i) and (iv) on the enlarged pre-setting variable Ω′ = (deal, all chance): the chance is fixed in advance as part of Ω′, so the dynamics given Ω′ is deterministic, and p(Ω′ \| a, b) = p(Ω′) |
  | a $\pm1$ outcome recorded in every run, no run set aside | the every-run clause |
  | settings independent of the deal | (iv) |

- **Consistency with SC-33 (#968).** #968's ch03:180 states the ceiling as: setting interventions that "each
  read and write only their own wing"; "the Bell-relevant graph does not connect the wings before readout"; a
  $\pm1$ outcome in every run; a pre-setting ensemble independent of the settings. The card text now uses the
  same "reads and writes" wording. Its every-operation and schedule clauses are the card-table form of the graph
  not connecting the wings before readout. The deal, enlarged by all chance (Ω′), is the pre-setting
  ensemble. $\pm1$ follows #968's notation.
- **Downstream.**
  - ch01:294 ("The boundary drawn above remains load-bearing … it is Bell's two boxes … where the cards must be
    surrendered to the full construction") refers back to this boundary. It is unchanged and is now read with
    the conditions.
  - The pointer to Chapter 3 §§3.7–3.7.1 is unchanged.

### C-2. ch03:188 and FULL:1064

- **Original.**
  - "… and states its boundary as plainly as its successes: no arrangement of cards on a table violates a Bell
    inequality."
  - "A card game is local through and through — each player's hidden cards are their own — and …"
  - "What the world adds, and no table can, is …"
- **Defect.**
  - The first sentence is the same unrestricted claim.
  - The second gives locality but not setting independence (VERIFY item 5).
  - "no table can" is unrestricted for the same reason.
- **Correction (exact text now at ch03:188 = FULL:1064).**
  - "… states its boundary as plainly as its successes: a card game in which, once the deal is down, every operation, including each shuffle the rules prescribe, each move and each setting choice, reads and writes one player's own cards only, and which operation is applied to a player's cards, and how that player's outcome is read from them, depends only on those cards, that player's own setting and on chance that, taken together with the deal, is independent of the settings, with each outcome a $\pm1$ result in every run, no run set aside, and the settings chosen independently of the deal, violates no Bell inequality."
  - "Such a card game is local through and through — each player's hidden cards are their own, and the deal,
    taken together with any chance the game uses, does not know the settings — and …"
  - "What the world adds, and no such table can, is …"

  The paragraph's description of the §1.11 game ("a deterministic shuffle that writes visible history into the
  burn pile and reads it back") describes that game, which is deterministic. The boundary sentence covers more,
  namely games with setting-independent chance. The two agree, and the description is unchanged.
- **Downstream.** The wager that follows (ontic parameter dependence through the shared boundary structure) is
  unchanged. The restriction leaves the framework's adopted branch as Main §3.3 states it: measurement
  independence retained, ontic parameter independence given up. The restricted table is exactly the class the
  ceiling covers.

## Evidence, by class

### (1) Paper argument: the general claim, for any deck and any finite sequence

Let A's region R_A and B's region R_B partition the cards after the deal. Any shared or undealt cards are
untouched after the deal, as the condition requires.

1. **Each admitted operation is a product.** It is f_A × id or id × g_B: it reads and writes one region only,
   with the identity on the rest.
2. **Every sequence is a product.** (f×g)∘(f′×g′) = (f∘f′)×(g∘g′), so by induction every finite sequence of
   admitted operations composes to a product F_A × G_B.
3. **The product is fixed by own cards, own setting and dealt chance.** An operation chosen from R_A's cards
   (which carry A's setting once written), A's own setting and the dealt chance, applied to R_A, is a map R_A → R_A once the chance is fixed. It is therefore admitted, and step 2
   applies. So F_A is fixed by A's own cards (dealt cards and setting card) and the chance, and likewise G_B.
4. **Chance is part of the pre-setting variable.** Let Ω′ = (deal, all chance), whether one player's or shared.
   The text requires the chance, taken together with the deal, to be independent of the settings, so
   p(Ω′ | a, b) = p(Ω′) jointly. Given Ω′ the dynamics is deterministic. This is Main §3.3 (i) and (iv) on Ω′.
   Marginal independence of each coin is not enough (C1, C2).
5. **Responses are local.** The readout rule is fixed by the player's own cards, own setting and the dealt
   chance (C3 shows that it must be). A's outcome, read from R_A as ±1 in every run with no run set aside, is therefore q_a(Ω′), a
   function of A's part of the deal, the chance and a, and B's is r_b(Ω′).
6. **The ceiling applies.** The hypotheses (i)–(iv) of Main §3.3 hold on Ω′, so |CHSH| ≤ 2. Equivalently,
   CHSH is linear in p(Ω′), and every vertex q_a(Ω′) r_b(Ω′) has |CHSH| ≤ 2 (K1).

### (2) Exact finite checks (`card_bell_check.py`, output in `card_bell_check.out`, 25 checks pass)

These are instances and controls, not the proof.

- **K1, K2.** Every pair of local deterministic response tables (4 × 4 = 16 pairs) has |CHSH| ≤ 2, and a
  shared-deal local game attains 2.
- **E0–E3: an exhaustive finite instance of steps 1–5 on a four-card deck.** Each player holds a hand card and
  a setting card. The enumeration covers:
  - every deal and the setting writes;
  - every sequence of length ≤ 2 of admitted operations, interleaved between the players, from all 256 + 256
    own-region maps and the 24 whole-deck permutations (the checker admits exactly 3, E0);
  - every ±1 readout.

  The checks:
  - E1: each player's final cards depend only on its own hand and setting;
  - E2: |CHSH| ≤ 2 for every induced pair and deal;
  - E3: the product test is applied to setting-indexed schedules M_{a,b}. It rejects the L2 schedule and
    accepts a schedule chosen from A's own setting card.
  - O3a, O3b: every readout rule selected by the player's own setting gives max |CHSH| = 2, and E3 still
    separates own-setting from other-setting schedules.
  - PIN: the exact book sentences are pinned. The ch01 and ch03 card sentences and the ch03 gloss must each
    appear in their chapter and exactly once in FULL.

  E1′ records that the length-≤2 sequences reach all 65,536 product maps. That reach count is a bounded run;
  the argument in (1) does not need it.
- **ADM, the admissibility checker for the per-operation condition.** A whole-deck map is admitted iff, for one
  player's region R, it writes only R (every card outside R unchanged) and reads only R (the new cards in R are
  a function of R alone). It checks reading as well as writing, so it matches the text's "reads and writes".
  - ADM1 rejects the X1′ shuffle; ADM2 admits a shuffle within one hand (control).
  - L1a rejects L1, which writes only B's cards but reads A's.
  - The schedule clause is not a per-operation property, and ADM alone does not check it. E3 does.
- **Admit-controls for chance.** P1 (independent one-player coins, biases 1/2 and 1/3) and C4 (a coin shared
  by both players, jointly independent of the settings, biases 1/2 and 1/3) give max |CHSH| = 2 over all
  coin-indexed local tables. Chance need not be private.
- **Must-fire countercontrols, each CHSH = 4:** X1, X1′, L1, L2, C3, P2, C1, C2, X2, X3. Each condition is
  therefore needed:
  - locality (X1, X1′, L1);
  - the choice of operation (L2) and of readout (C3) by own cards and setting-independent chance;
  - setting-independence of chance (P2, C1, C2);
  - setting-independence of the deal (X2);
  - the every-run condition (X3).

  Determinism given Ω′ is Main's (i).

### (3) Related machine check in the repository

Main's ceiling pointwise bound over the sixteen deterministic response tables is checked exhaustively in
`equivalence_recovery_probes.py` (check 11).

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| ch01:286 = FULL:630 | a card mechanism is a local classical toy | a card mechanism played under the restrictions below is a local classical toy | review O4 |
| ch01:286 = FULL:630 | no arrangement of cards on a table violates a Bell inequality | violates no Bell inequality when, once the deal is down, every operation (rule-prescribed shuffles included) reads and writes one player's own cards only; which operation is applied to a player's cards, and how the $\pm1$ outcome is read from them, depends only on those cards, that player's own setting and on chance that, taken together with the deal, is independent of the settings; an outcome in every run, no run set aside; settings independent of the deal; a local hidden-variable model (Main §3.3) | R-32; Main:356, :360; reviews rounds 2–5 |
| ch03:188 = FULL:1064 | no arrangement of cards on a table violates a Bell inequality | a card game in which, once the deal is down, every operation … reads and writes one player's own cards only, and which operation is applied to a player's cards, and how that player's outcome is read from them, depends only on those cards, that player's own setting and on chance that, taken together with the deal, is independent of the settings, with each outcome a $\pm1$ result in every run, no run set aside, and settings chosen independently of the deal, violates no Bell inequality | R-32; reviews rounds 2–5 |
| ch03:188 = FULL:1064 | A card game is local … hidden cards are their own | Such a card game … hidden cards are their own, and the deal, taken together with any chance the game uses, does not know the settings | VERIFY item 5; reviews rounds 4–5 |
| ch03:188 = FULL:1064 | and no table can | and no such table can | R-32 |

The book is regenerated: `book/The-Incompleteness-of-Observation-FULL.{tex,pdf}`, 559 pages (base 558; the longer
boundary sentences add one page), with a median of 2969 characters per page.

## Re-grep

Searched: book chapters, FULL, Explainer, papers.

- **Removed.** "no arrangement of cards" 0 (was 4: ch01:286, ch03:188, FULL:630, FULL:1064); "no table can" 0
  (was 2).
- **Card/Bell sentences remaining.** Every one is now scoped: ch01:286, ch01:294 (back-reference), ch03:188,
  and their FULL mirrors. The Explainer and the papers carry no card-Bell sentence.
- **Other classical/local Bell statements** (Main:22, :82, :410, :558, :766; Methodology:385–393;
  Structure:1141, :1149; Substratum:417, :431; Explainer:58, :300, :338, :563, :1017; book README:15, :50;
  appendix C:32–34). Each already names measurement independence and the cone or locality condition. None is
  unrestricted, and none is edited here. Several are #963's or #968's.

## Claims made conditional or removed

The unrestricted "no arrangement of cards on a table violates a Bell inequality" is removed in both
chapters and in FULL. The book now states the boundary under its conditions. No claim is strengthened.

## Lean

No Lean change is involved, and nothing here requires a formal change.

## Cross-unit dependencies

- **#968 (SC-33, `corpus/sc33-bell-main-book`).**
  - It edits ch01:16, :169, :171, :183; ch03:40, :162, :164, :180, :182; and FULL:277, :291, :360, :513, :515,
    :527, :831, :916, :1038, :1040, :1056, :1058, ….
  - None of these is a line edited here.
  - A trial merge of the two branches on the `.md` sources is clean (see the report).
  - The generated FULL `.tex`/`.pdf` will conflict as binary or generated files and need a rebuild after
    either lands.
- **#963 (SC-17).** It edits ch03:186 and FULL:1062, two lines above this unit's ch03:188 and FULL:1064, with
  an unchanged line between. The trial merge is clean.
- **SC-38 (this agent's other unit).** It edits ch01:135, :273 and FULL:479, :617 in the same chapter. The lines
  are separate.
- **Shared sentences relied on elsewhere.**
  - The book §1.11 card boundary is cited by the Introduction's L188/L255 (R-32, r32).
  - ch03:188's "local through and through" sentence.
  - **For r32.** The Introduction's current L188 ("no card arrangement violates a Bell inequality") and FINDINGS
    R-32's proposed text ("whose moves act only on each player's own cards, with settings chosen independently
    of the deal") both have the gaps closed here. r32 must carry five clauses:
    - read and write;
    - every operation, rule-driven shuffles included;
    - operation choice and readout determined by own cards, own setting and chance that, taken together with
      the deal, is independent of the settings;
    - every run, with no run set aside;
    - settings independent of the deal.

## Open, for #970

The book does not say what a card table outside the conditions can do. Main:356 says so for the global
construction. Whether the book should also say it is an editorial choice, and it is left open.
