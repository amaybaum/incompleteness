# BQP-P6 plan: (ix), (xi) or PG on the prepared class

**Status: WIP / UNVERIFIED. Committed before any analysis node is written.**

- **Authority.** Owner decision #1169 c.7078857457, BQP row (#1487): a paper-only research unit
  building on BQP-P5 at `ab67a0fc`. Paper arguments, source analysis, literature and mathematical
  counterexamples only. No computation, no Lean, no change to a physical rule, no premise adopted,
  no manuscript edit (`papers/`, `book/`), no merge. C-1 and C-2 remain unauthorized.
- **Stacking.** The branch `research/bqp-p6-20261122` starts at `ab67a0fc`, the head of BQP-P5,
  which is not moved. Accountable Issue: #1487.
- **Inputs.** BQP-P5 (`verification/audits/complexity/bqp-p5-20261122/NOTE.md` at `ab67a0fc`):
  Lemma Γ, Proposition AG, E1, Proposition FS, the MISSING item (S-𝒞) and the three corpus
  readings (R1)–(R3). Its reviews on #1546, c.7076936181 and c.7076963950; the second records that
  Main:736 with Main:424 directly supports (S-𝒞) as MISSING. Rounds #1488, #1498, #1514 and #1527
  as BQP-P5 cites them. `papers/Main.md`, `papers/Substratum.md` and `papers/SM.md` at
  `ab67a0fc`, read only. The literature result LIT1 (Bancal, Pironio, Acín, Liang, Scarani and
  Gisin, Nature Physics 8, 867 (2012), arXiv:1110.3795).
- **A1 ledger check.** `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was
  read at `origin/research/a1exit-deletion-20261121` = `b1b0522d`. Its paths lie under `papers/`,
  `book/`, `AGENTS.md`, `verification/README.md`, `verification/coverage`, `verification/lean`,
  `verification/lean-mathlib`, `verification/lean-manuscript-census.json` and
  `verification/programmes`. It names no path under `verification/audits/`. Every path this round
  writes is in `verification/audits/complexity/bqp-p6-20261122/`, so none is ledgered.

## 1. Preregistered question

On OI's prepared class (the Bell route: option (a), Main:418; H-Bell, Substratum:131–133), does
one of the following hold?

- **(ix)** a uniform bound K on the reading sets N_i, taken as the union over all configurations;
- **(xi)** commutation with lattice translations up to a site-local gauge;
- or, in place of both, **(PG)** polynomial growth of the fixed reading graph Γ.

- **Q1.** Does the native update and preparation structure fix the scope of (ix) and (xi) on the
  prepared class, or is there a prepared-class rule that these posits need not constrain?
- **Q2.** Which of the corpus readings (R1), (R2), (R3) of BQP-P5 §4 survives, by an argument
  from the corpus's own text and definitions?
- **Q3.** If (ix) and (xi), or PG, can fail on the prepared class, which failure leaves room for
  H5 failure, on which site set, and does E1-type dependency growth (|D| ≥ 2^T) arise there?
- **Q4.** Does LIT1 bear on whether (S-𝒞) is compatible with H-Bell (i)–(ii)?

Computational universality, efficient classical simulation and native BQP are kept apart
throughout. Failure of H5 is none of the three. No imported quantum operation counts as native.

## 2. Explicit assumptions

(N) is native: the native update map, the preparation structure as stretches of runs of that map
interleaved with configuration writes, and Main's definitions of the coupling graph and its cone.
(I) is imported: a ledger posit or an added hypothesis, as in BQP-P5.

| Id | Assumption | Label |
|---|---|---|
| A-U | One fixed update map Φ of the configuration; a preparation is runs of Φ interleaved with configuration writes (Main:368, Main:420, SM:104) | (N) |
| A-G | G_φ is one graph collecting the one-step dependences at all states, G_φ = G_φ^S (Main:368, SM:104) | (N), stated in Main |
| A-13 | Ledger item (xiii): second-order form, each F_i reading finitely many sites (Main:736) | (I), posit |
| A-9 | Ledger item (ix), A3: one degree bound across the family (Main:736, Substratum:96) | (I), posit |
| A-11 | Ledger item (xi) first clause, A4: commutation with lattice translations up to gauge, the gauge as Substratum:98 states it | (I), posit |
| A-BQ | BQ1's H1–H4 at the scopes of #1527 §1.1; BQ1 and BQ1-D (#1498) | (I) |
| A-T | Polynomial T (AW-2) | (I) |
| A-14 | Ledger item (xiv), measurement independence, for Q4 only | (I), posit |
| A-P5 | BQP-P5's Lemma Γ, Proposition AG, E1 and Proposition FS, as reviewed at c.7076936181 and c.7076963950 | reviewed derivations, carrying their own labels |

No other premise is used. Any further one that appears is named where it enters and listed in the
record's Assumed section.

## 3. Productivity test (§A.31, fixed now)

The round is **productive** iff it yields at least one of:

- **(P1)** an argument from A-U and A-G alone that fixes, or shows unfixable, the scope of (ix)
  and (xi) on the prepared class;
- **(P2)** a resolution of at least one of (R1)–(R3) by an argument from the corpus's text or
  logic, stronger than restating the readings;
- **(P3)** a classification of the failures of (S-𝒞) and PG, each with its site set and its
  dependency growth, proved or exhibited;
- **(P4)** a hidden assumption in Proposition AG, Proposition FS or (S-𝒞), such as the gauge class
  or the site set;
- **(P5)** a precise statement of LIT1's hypotheses and of whether OI's construction meets them.

A restatement of BQP-P5's §4 is CONFIRMING and does not count. **INCONCLUSIVE is an allowed
outcome**, provided either the readings are resolved with the conditional result stated, or the
corpus is shown not to decide the question.

## 4. Outcomes and decision rule

| Finding | Outcome |
|---|---|
| (ix) and (xi) with a site-local gauge, or PG, follow for every Bell-route rule from (N) assumptions alone | HOLDS, with the derivation |
| A rule meeting every posit the corpus states for the Bell route has an explicit prepared configuration on which (ix) and (xi), and PG, fail | FAILS, with the configuration and the exact class |
| Neither | INCONCLUSIVE, with the readings resolved and the conditional result stated, or with the corpus shown not to decide |

A result that needs an (I) posit for (ix), (xi) or PG is a conditional result and does not make
the outcome HOLDS. A negative result names the exact class it excludes.

## 5. Stop conditions

- Q1–Q4 are answered under §4.
- Or a branch needs a computation, a Lean proof, a choice of physical rule or the adoption of a
  premise. The round then stops at that branch and names the gap.
- Or three consecutive depth-first nodes give no NEW result (§A.31 fixed point).

There is no successor round.

## 6. Goal link (§A.47)

- **Serves:** #1487, whether OI's native dynamics hosts BQP efficiently. That bears on whether OI's
  quantum statistics are derived or only represented (§A.29).
- **Decides:** whether BQP-P5's conditional OBSTRUCTION (I) applies to OI's Bell route as the
  corpus states it, and, if not, which failure of (ix), (xi) or PG leaves room for H5 failure.
