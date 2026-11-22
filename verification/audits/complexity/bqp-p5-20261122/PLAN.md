# BQP-P5 plan: edge generation on the Bell route

**Status: WIP / UNVERIFIED. Committed before any analysis node is written.**

- **Authority.** Owner decision #1169 c.7076731666, item 2 (BQP, #1487): a bounded, paper-only
  investigation. Paper arguments, source analysis, literature review and mathematical
  counterexamples only. No computation, no Lean, no change to a physical rule, no premise adopted,
  no manuscript edit, no merge. C-1 and C-2 remain unauthorized.
- **Stacking.** The branch starts at `d02be567`, the head of #1527 (round 4), which is not moved.
  Accountable Issue: #1487.
- **Nit scope at `d02be567`.** The commit `6d7d2240..d02be567` touches only round 4's `NOTE.md`. It
  adds (M3) and (M4) to the missing premise and to the Missing list, as the delta review
  c.7067413567 asked. The reading below found nothing beyond that scope.
- **A1 ledger check.** `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was
  read at `origin/research/a1exit-deletion-20261121` = `fef0f158`. It names no path under
  `verification/audits/`. Every path this round writes is in
  `verification/audits/complexity/bqp-p5-20261122/`, so none is ledgered.

## 1. Preregistered question

OI's Bell route (option (a), Main:418; H-Bell, Substratum:131–133) uses preparation-indexed
bounded-degree long edges.

- **Q-A.** Can an edge-generation rule be derived from the native update and the preparation
  structure alone?
- **Q-B.** If it can, is L(n) polynomial or superpolynomial in n? L(n) is the number of long edges
  reachable by a poly(n)-step run, ambient edges included.
- **Q-C.** If it cannot, is there a scoped obstruction, and what exactly is missing?

Computational universality, efficient classical simulation and native BQP are kept apart
throughout. Failure of a hypothesis of BQ1 is not evidence of native BQP.

## 2. Explicit assumptions

(N) is native: the native update and Main's definitions of the coupling graph and its cone.
(I) is imported: a posit of the selected lattice model, or an added hypothesis. This follows round
4's convention, in which ledger posits are (I).

| Id | Assumption | Label |
|---|---|---|
| A-U | One fixed update map Φ of the configuration; setting generators and preparation devices are part of the system (Main:410–416, Main:368) | (N) |
| A-G | Main's coupling graph G_φ, the union of the one-step dependences over all states, and its cone lemma (Main:368) | (N), stated in Main |
| A-13 | Ledger item (xiii): second-order form, each F_i reading finitely many sites (Main:736) | (I), posit |
| A-9 | Ledger item (ix): one degree bound for the coupling graph (A3) | (I), posit; its scope on the prepared class is a question of this round |
| A-11 | Ledger item (xi), first clause: the update commutes with lattice translations up to gauge (A4) | (I), posit; scope on the prepared class as for A-9 |
| A-BQ | BQ1's H1–H4 at the scopes of #1527 §1.1; BQ1-D (#1498) | (I) |
| A-T | Polynomial T as the unit of efficiency (AW-2) | (I) |

No other premise is used. Any further one that appears is named where it enters and listed in the
record's Assumed section.

## 3. Productivity test (§A.31, fixed now)

The round is **productive** iff it yields at least one of:

- **(P1)** a derivation of the form or content of the edge-generation rule from A-U and A-G, with
  its exact scope;
- **(P2)** a bound on L(n) or |D|, polynomial or not, under named premises, with a proof;
- **(P3)** a counterexample showing that the corpus's stated constraints do not fix the outcome,
  together with the premise it isolates;
- **(P4)** a hidden assumption or a non-minimal premise in round 4's missing-premise list.

A restatement of round 4's (M1)–(M4) is CONFIRMING and does not count. **INCONCLUSIVE is an allowed
outcome**, provided the missing premise is named exactly.

## 4. Outcomes and decision rule

| Finding | Outcome |
|---|---|
| L(n) = poly(n) follows for OI's Bell route from A-U, A-G and the posits the corpus states for that route | OBSTRUCTION (I), via BQ1-D, with the excluded class stated exactly |
| A rule following from those sources gives superpolynomial reachable long edges | ESCAPE from H5, with the generated edges exhibited. This is not native BQP |
| The sources fix neither | INCONCLUSIVE, with the missing premise named. Scoped obstructions and counterexamples established on the way are reported with their classes |

A scoped OBSTRUCTION for a class of rules is reported as such. It becomes the verdict for OI's Bell
route only if the corpus places that route in the class.

## 5. Stop conditions

- Q-A to Q-C are answered under §4.
- Or a branch needs a computation, a Lean proof or a new physical rule. The round then stops at
  that branch and names the gap.
- Or a nit at `d02be567` is found to lie beyond the accepted scope. The round then stops and
  reports before building on it.
- Or three consecutive depth-first nodes give no NEW result (§A.31 fixed point).

## 6. Goal link (§A.47)

- **Serves:** #1487, whether OI's native dynamics hosts BQP efficiently. That bears on whether OI's
  quantum statistics are derived or only represented (§A.29).
- **Decides:** whether the Bell route's long edges defeat H5 of BQ1, or the corpus leaves this open
  and, if so, which premise would decide it.
