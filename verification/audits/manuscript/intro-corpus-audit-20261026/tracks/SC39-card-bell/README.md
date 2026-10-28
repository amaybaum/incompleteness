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
  correlations of §1.7 belong to the full construction, …"
- **Defect.** Unrestricted. A card table can break each hypothesis of the ceiling:
  - a move after the settings that acts on both hands (X1);
  - a deal arranged with knowledge of the settings (X2);
  - runs without an outcome discarded (X3).

  Each of these reaches CHSH = 4.
- **Correction.** "… but it violates no Bell inequality when its shuffles are deterministic, each player's
  moves and setting choices act only on that player's own cards once the deal is down, each outcome is read
  from that player's own cards as a ±1 result in every run, and the settings are chosen independently of the
  deal: such a game is a local hidden-variable model (Main §3.3). The Bell-type correlations of §1.7 belong to
  the full construction, …"
- **Condition map.**

  | Book condition | Main §3.3 hypothesis |
  |---|---|
  | deterministic shuffles | (i) |
  | moves and setting choices on own cards once the deal is down | (ii) and the cone separation of (iii); with no cross-hand move after the deal the two hands' cones never meet |
  | outcome read from own cards, ±1, every run | (iii) and the every-run clause |
  | settings independent of the deal | (iv) |

  The deal is the pre-setting variable Ω. A shuffle before the settings may correlate the hands, which is how
  K2 attains CHSH = 2.
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
- **Correction.**
  - "… states its boundary as plainly as its successes: a card game whose moves and setting choices act only
    on each player's own cards, with each outcome read from that player's own cards as a ±1 result in every
    run and the settings chosen independently of the deal, violates no Bell inequality."
  - "Such a card game is local through and through — each player's hidden cards are their own, and the deal
    does not know the settings — and …"
  - "What the world adds, and no such table can, is …"

  Determinism is carried by "a deterministic shuffle" in the same sentence's description of the game.
- **Downstream.** The wager that follows (ontic parameter dependence through the shared boundary structure) is
  unchanged. The restriction leaves the framework's adopted branch as Main §3.3 states it: measurement
  independence retained, ontic parameter independence given up. The restricted table is exactly the class the
  ceiling covers.

## Evidence

`card_bell_check.py` (run as `python3 -I card_bell_check.py`; output in `card_bell_check.out`) checks the
following in exact Fractions:

- **K1.** Every local deterministic response pair (16 × 16 tables) has |CHSH| ≤ 2, so every deal distribution
  does too. The local models form the convex hull of these vertices.
- **K2.** A shared-deal local game attains 2.
- **Countercontrols.** X1 (a post-setting move on both hands), X2 (a setting-dependent deal) and X3 (runs
  without an outcome discarded) each give CHSH = 4. Each condition in the restated sentence is therefore
  needed.

The ceiling itself is Main's paper theorem, and its pointwise bound is exhaustively checked in
`equivalence_recovery_probes.py` (check 11). This check adds the card-table instances and the
countercontrols. Evidence level: a paper theorem, plus exact finite checks.

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| ch01:286 = FULL:630 | no arrangement of cards on a table violates a Bell inequality | violates no Bell inequality when shuffles are deterministic, own-card moves and settings after the deal, own-card ±1 outcome every run, settings independent of the deal; a local hidden-variable model (Main §3.3) | R-32; Main:356, :360 |
| ch03:188 = FULL:1064 | no arrangement of cards on a table violates a Bell inequality | a card game whose moves and setting choices act only on each player's own cards, … ±1 result in every run and settings chosen independently of the deal, violates no Bell inequality | R-32 |
| ch03:188 = FULL:1064 | A card game is local … hidden cards are their own | Such a card game … hidden cards are their own, and the deal does not know the settings | VERIFY item 5 |
| ch03:188 = FULL:1064 | and no table can | and no such table can | R-32 |

The book is regenerated: `book/The-Incompleteness-of-Observation-FULL.{tex,pdf}`, 558 pages (base 558), with
a median of 2968 characters per page.

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
  - The proposed Introduction text (FINDINGS R-32) uses the same conditions.

## Open, for #970

The book does not say what a card table outside the conditions can do. Main:356 says so for the global
construction. Whether the book should also say it is an editorial choice, and it is left open.
