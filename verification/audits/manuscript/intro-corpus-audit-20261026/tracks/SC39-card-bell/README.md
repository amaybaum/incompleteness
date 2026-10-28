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
  - a deal arranged with knowledge of the settings (X2);
  - runs without an outcome discarded (X3).
- **Correction (exact text now at ch01:286 = FULL:630).** "One boundary must be stated as plainly as the successes: a card mechanism played under the restrictions below is a local classical toy. It reproduces single-system interference, indivisibility, and division events — the mechanism of this chapter — but it violates no Bell inequality when any chance a shuffle or move uses is private to one player and drawn independently of the settings, once the deal is down every operation, including each shuffle the rules prescribe, each move and each setting choice, reads and writes one player's own cards only, and which operation the rules apply to a player's cards depends on those cards alone, each outcome is read from that player's own cards as a $\pm1$ result in every run, no run is set aside, and the settings are chosen independently of the deal: such a game is a local hidden-variable model (Main §3.3). The Bell-type correlations of §1.7 belong to the full construction, …"
- **History on this branch.** 0c2356f3 restricted only the players' moves (X1′ open). ced30f6c restricted every
  operation but read "acts on" as write-only (L1 open) and fixed no schedule (L2 open), and it required
  determinism, which is narrower than needed. This commit closes L1 and L2 and replaces determinism with the
  private-chance clause (R1 below).
- **Condition map.**

  | Book condition | Main §3.3 hypothesis |
  |---|---|
  | any chance an operation uses is private to one player and drawn independently of the settings | (i), after the reduction below: private chance is dealt in advance as extra hidden cards in that player's region, which enlarges the deal Ω and leaves the dynamics deterministic |
  | once the deal is down, every operation reads and writes one player's own cards only | (ii) for the setting choices; for every later update, no step reads or writes across the hands, so the coupling graph after the deal has no edge between the hands and each readout stays outside the other wing's cone, as (iii) requires |
  | which operation is applied to a player's cards depends on those cards alone | the schedule is part of the dynamics: with this clause the composed post-deal map is fixed by each player's own cards (including the setting card), so (ii)–(iii) hold for the whole sequence and not only per operation |
  | outcome read from own cards, $\pm1$, every run, no run set aside | (iii) and the every-run clause |
  | settings independent of the deal | (iv) |

- **Consistency with SC-33 (#968).** #968's ch03:180 states the ceiling as: setting interventions that "each
  read and write only their own wing"; "the Bell-relevant graph does not connect the wings before readout"; a
  $\pm1$ outcome in every run; a pre-setting ensemble independent of the settings. The card text now uses the
  same "reads and writes" wording. Its every-operation and schedule clauses are the card-table form of the graph
  not connecting the wings before readout. The deal, enlarged by any private chance, is the pre-setting
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
  - "… states its boundary as plainly as its successes: a card game in which, once the deal is down, every operation, including each shuffle the rules prescribe, each move and each setting choice, reads and writes one player's own cards only, and which operation is applied to a player's cards depends on those cards alone, with any chance an operation uses private to one player and drawn independently of the settings, each outcome read from that player's own cards as a $\pm1$ result in every run, no run set aside, and the settings chosen independently of the deal, violates no Bell inequality."
  - "Such a card game is local through and through — each player's hidden cards are their own, and the deal
    does not know the settings — and …"
  - "What the world adds, and no such table can, is …"

  The private-chance clause is stated here as well. The condition does not rest on the phrase "a deterministic
  shuffle" in the chapter's description of the game.
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
3. **The product is fixed by own cards.** Under the schedule clause, which operation is applied to a player's
   cards depends on those cards alone. So F_A is fixed by A's own cards, its dealt cards and setting card, and
   G_B by B's own cards, step by step.
4. **Private chance reduces to the deterministic case.** Chance an operation uses that is private to one player
   and independent of the settings can be dealt in advance as extra hidden cards in that player's region. This
   enlarges Ω, leaves the dynamics deterministic, and keeps p(Ω | a, b) = p(Ω). This is Main §3.3 (i).
5. **Responses are local.** A's outcome, read from R_A as ±1 in every run with no run set aside, is
   q_a(Ω_A), and B's is r_b(Ω_B).
6. **The ceiling applies.** The hypotheses (i)–(iv) of Main §3.3 hold, so |CHSH| ≤ 2. Equivalently, CHSH is
   linear in p(Ω), and every vertex q_a(Ω_A) r_b(Ω_B) has |CHSH| ≤ 2 (K1).

### (2) Exact finite checks (`card_bell_check.py`, output in `card_bell_check.out`, 18 checks pass)

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

  E1′ records that the length-≤2 sequences reach all 65,536 product maps. That reach count is a bounded run;
  the argument in (1) does not need it.
- **ADM, the admissibility checker for the per-operation condition.** A whole-deck map is admitted iff, for one
  player's region R, it writes only R (every card outside R unchanged) and reads only R (the new cards in R are
  a function of R alone). It checks reading as well as writing, so it matches the text's "reads and writes".
  - ADM1 rejects the X1′ shuffle; ADM2 admits a shuffle within one hand (control).
  - L1a rejects L1, which writes only B's cards but reads A's.
  - The schedule clause is not a per-operation property, and ADM alone does not check it. E3 does.
- **P1, private chance.** Independent private coins (biases 1/2 and 1/3) over all local table pairs give
  max |CHSH| = 2.
- **Must-fire countercontrols, each CHSH = 4:** X1, X1′, L1, L2, P2, X2, X3. Each of the locality (X1, X1′,
  L1), schedule (L2), private-chance (P2), setting-independence (X2) and every-run (X3) conditions is
  therefore needed. Determinism of the dealt-in-advance dynamics is Main's (i).

### (3) Related machine check in the repository

Main's ceiling pointwise bound over the sixteen deterministic response tables is checked exhaustively in
`equivalence_recovery_probes.py` (check 11).

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| ch01:286 = FULL:630 | a card mechanism is a local classical toy | a card mechanism played under the restrictions below is a local classical toy | review O4 |
| ch01:286 = FULL:630 | no arrangement of cards on a table violates a Bell inequality | violates no Bell inequality when any chance a shuffle or move uses is private to one player and independent of the settings, once the deal is down every operation (rule-prescribed shuffles included) reads and writes one player's own cards only, and which operation the rules apply to a player's cards depends on those cards alone, own-card $\pm1$ outcome every run, no run set aside, settings independent of the deal; a local hidden-variable model (Main §3.3) | R-32; Main:356, :360; reviews B1 (rounds 2, 3), R1 |
| ch03:188 = FULL:1064 | no arrangement of cards on a table violates a Bell inequality | a card game in which, once the deal is down, every operation … reads and writes one player's own cards only, and which operation is applied to a player's cards depends on those cards alone, with any chance an operation uses private to one player and independent of the settings, … $\pm1$ result in every run, no run set aside, and settings chosen independently of the deal, violates no Bell inequality | R-32; reviews B1 (rounds 2, 3), R1 |
| ch03:188 = FULL:1064 | A card game is local … hidden cards are their own | Such a card game … hidden cards are their own, and the deal does not know the settings | VERIFY item 5 |
| ch03:188 = FULL:1064 | and no table can | and no such table can | R-32 |

The book is regenerated: `book/The-Incompleteness-of-Observation-FULL.{tex,pdf}`, 558 pages (base 558), with
a median of 2977 characters per page.

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
    - every operation, rule-prescribed shuffles included;
    - schedule;
    - private chance;
    - every run, with no run set aside.

## Open, for #970

The book does not say what a card table outside the conditions can do. Main:356 says so for the global
construction. Whether the book should also say it is an editorial choice, and it is left open.
