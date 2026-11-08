# M-INACC-1 amendment A1: application of the preregistration review

**Standing.** WIP / UNVERIFIED. Amendment to `../DESIGN.md` at checkpoint 1
(`75c0befcb324466cb4bf0e90c7ef3cbe429b58ad`, the parent of this amendment's
commit). Writer: Claude
Code session, 2026-11-08. It applies the findings F1–F20 of the independent
review of that commit (verdict: accept with changes; blocking finding F1).

- **Timing.** Written before any derivation. No `RESULT.md` exists when this
  amendment is committed, and no result is stated in it.
- **Effect.** It changes the preregistration. It does not change `G_σ` (§2 of
  `DESIGN.md`). `DESIGN.md` itself is not edited. Where this amendment and
  `DESIGN.md` differ, this amendment governs.
- **Review.** The reviewer confirms this amendment at its exact SHA before
  checkpoint 2 begins.
- **Scope.** Paper-only. Nothing is adopted and no premise is proposed for
  adoption.

Repository links to the analysis sources stay pinned to `main@f88c1842`
(`f88c184220453badfc9279ab9a86b6785e4db5ff`). Abbreviations are as in `DESIGN.md`.

## 0. Amendment table

| ID | Finding | Section of `DESIGN.md` amended | Effect on outcomes |
| --- | --- | --- | --- |
| A1.1 | F1, USE-dyn vacuous (blocking) | §4.2 (A)(a), D-Q | Clause (a) is decided by USE-ctx alone. If USE-ctx is undecided, the outcome is (A′) |
| A1.2 | F2, (A) is weaker than M2D's derivation criterion | §4.2 (A) | (A) does not establish M-INACC in M2D's sense. A line is added for M2D's second rule-out route |
| A1.3 | F3, combinations and attribution | §4.2 Combinations, D-ATTR | Pairs are stated on {A∪A′, B, C}. Attribution to `Π_B`'s resources only under (B, A∪A′); undecided under (B, C) |
| A1.4 | F4, partial outcomes and (C) | §4.2 (C), §4.3 node 1 | Step (s5) is added. (C) splits into (C-D) and (C-B). The first missing premise is defined as a named statement `P` |
| A1.5 | F5, access and membership | §1.2, §3.1–§3.3, §3.6 | Registration and translation are restricted to `R`. The meter identification is stated. E-iso leaves gates outside `R` live |
| A1.6 | F6, archive-swap as gate control | §3.2, §3.7, D-ATTR | Archive-swap and refill are recorded as a supplied gate write and attributed |
| A1.7 | F7, CC-OFF and C-LIN | §2.5, §5 | CC-OFF on proofs becomes a consistency rule. C-LIN verifies Lemma Q(iii) under this unit's conventions. Vacancy rule in the linear limits |
| A1.8 | F8, freeze anchor | §2.1, §2.4 (a2)(a3), §5 C-IMPORT(iii), §7 | The anchor is the first `RESULT.md` commit. An ancestry checkpoint is added for amendments |
| A1.9 | F9, R-G disclosure | §4.3 disclosure | Disclosure completed. No rule change |
| A1.10 | F10, alternatives and reading | §2.1, §2.4 | `A + Aᵀ` is added to the alternatives. The union reading and the reason for `L ≥ 5` are stated |
| A1.11 | F11, measure dependence | §4.1, §6 | PROT-B and every (A) verdict carry N2 and H-PS. PROT-D is a support statement |
| A1.12 | F12, authorization provenance | Standing | Link to the owner comment |
| A1.13 | F13, self-check bound | §4.4, §7 | Each self-check is one stated instance, size-bounded and listed |
| A1.14 | F14, Main anchor | §5 C-NS, §9 | Main:366 becomes Main:364 |
| A1.15 | F15, consequences of C-NS and SC-1 | §5 | A C-NS violation voids the composition verdicts. A positive SC-1 finding is a C-IMPORT failure |
| A1.16 | F16, P1 and P2 controls | §5 C-P1, C-P2 | The exposed functional is named. An (A) proof cites where it uses P1 and P2 |
| A1.17 | F17, C-LIN countercontrol | §5 C-LIN | The audit applied to `G_SM` must fail |
| A1.18 | F18, D-Q and USE-ctx | §4.2 D-Q | R1 enters CC-NC only |
| A1.19 | F19, scope of (m3) | §2.3 | (m3) covers edge reciprocity at fixed `u`, not the gate dependence |
| A1.20 | F20, smaller points | §3.1, §3.4, §4.4, §6, §9 | Heralds, ring size, sources, B-B standard |
| A1.21 | Owner reporting layer | New §4.5 | A mapping onto tiers. The decision rule is unchanged |
| A1.22 | SM:112 defect | §2.4 observation | Routed out of this unit |

## 1. Amended rules, by finding

### A1.1 (F1): clause (a) is decided by USE-ctx alone

Replaces the clause-(a) bullet of `DESIGN.md` §4.2 (A).

- **USE-dyn is vacuous.** For every nonzero `f` with a coefficient-1 slot `s`
  on a cell of `R`, take `w = e_s`. The continuation "register `s`" separates
  `λ` from `λ + w`. USE-dyn is therefore reported, for context only, and
  decides nothing.
- **Incompatibility under the statistical reading.** This is a definitional
  observation, not a result.
  - Read clause (a) statistically: for some continuation protocol, a record
    `r` has `P(r | K, f = 0) ≠ P(r | K, f = 1)` in a positive-probability
    branch.
  - Read clause (b)'s "changes its conditional law" as: the law of `f`'s value
    at the tick of evaluation, given `K` and the records of any continuation,
    equals its law given `K`.
  - By Bayes, the first gives a record value on which `f`'s conditional law
    differs from its law given `K`, which contradicts the second.
  - So the two clauses cannot both hold under these readings, and clause (a)
    is decided by USE-ctx.
- **PROT-R (reported).** The retrodictive property in that reading of (b) is
  recorded as PROT-R. For every protocol, tick `t` and `Q* = 1` functional `f`
  on the active cells at `t`, `f`'s value at `t` is neither determined nor
  biased given the joint record at any later time. PROT-R is reported, together
  with its status in the linear limits under C-LIN. It is not part of the (A)
  decision.

**USE-ctx, definition.**

- **Operations compared.** Two protocols `T` and `T′` of the class `Π` acting
  on the same region `R`. Each is a complete instrument: every record it
  produces, and its outgoing configuration.
- **Realization.** For each protocol, the stochastic kernel from the
  configuration of the dependency cone (including archived cells) at the start
  of the protocol to the pair (joint record, final configuration). Its
  randomness is the fresh unknowns of the cells it supplies, under N2 and H-PS.
- **Indistinguishable over `Π`.** `T` and `T′` are indistinguishable over `Π`
  if, for every preparation protocol `P` of `Π` and every continuation
  protocol `C` of `Π`, the joint law of all records of `P; T; C` equals that
  of `P; T′; C`. This is the observer's full accessible theory: every cell of
  `R`, retained cells and records included. It is not an encoded subtheory.
- **Action on `f`.** Here `f` is a `Q* = 1` linear functional on cells of `R`
  that remain active through `T` and `T′`. The action of `T` on `f` at a
  configuration `λ` is the probability `a_T(λ) = P_T(f(λ′) ≠ f(λ))` under the
  realization.
- **Pass.** Some pair `T`, `T′` is indistinguishable over `Π`, and
  `a_T(λ) ≠ a_{T′}(λ)` at some `λ` in the support of a preparation reachable in
  `Π`. Both the indistinguishability and the difference are proved in the
  record.
- **Fail.** For every pair indistinguishable over `Π`, `a_T = a_{T′}` on the
  support of every reachable preparation. This is proved in the record.
- **Undecided.** Neither is proved. The outcome is then (A′), with clause (a)
  "not decided".

Clause (a) is evaluated separately for each class (A1.3).

### A1.2 (F2): what (A) does not establish

Added to `DESIGN.md` §4.2 (A). An (A) verdict, with or without clause (a),
does not establish M-INACC in M2D's sense, for two reasons.

- M2D's derivation criterion also requires that the graph "keep FB's
  reflections out by a sourced structure"
  ([M2D:862](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L862)).
  That clause is outside this unit and stays open.
- M2D states M-INACC per encoded system
  ([M2D:832](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L832)).
  This unit decides a configuration-level protection. Whether an encoded system
  carries a protected functional enters only through CC-NC.

**Line RO-2 (reported).** M2D's second rule-out route is that every functional
the dynamics uses becomes determinable through reuse or recombination. It is
reported through the USE-ctx analysis: for each functional found to pass
USE-ctx, the record reports whether it is determined in some
positive-probability branch of some protocol of `Π`.

### A1.3 (F3): combinations and attribution

Replaces "Combinations" in `DESIGN.md` §4.2 and amends D-ATTR.

- **Protection outcomes.** For each class the protection outcome is one of
  A∪A′, B or C (with C-D and C-B, A1.4). `Π_A ⊂ Π_B` gives:
  - B for `Π_A` implies B for `Π_B`;
  - A∪A′ for `Π_B` implies A∪A′ for `Π_A`.

  The admissible pairs `(Π_B, Π_A)` are (A∪A′, A∪A′), (B, A∪A′), (B, B),
  (B, C), (C, A∪A′) and (C, C).
- **Clauses per class.** Clauses (a) and (c), and the A/A′ split, are
  evaluated for each class separately, because USE-ctx quantifies over the
  protocols of the class.
- **Attribution.**
  - Under (B, A∪A′), the exposure in `Π_B` is attributed to the gate of `G_σ`
    together with the minimal subset of `Π_B`'s added resources the exposing
    protocol uses. It is not attributed to those resources alone: CC-OFF
    tests whether they expose with linear steps.
  - Under (B, B), it is attributed to the gate together with the `Π_A`
    resources used, archive-swap included (A1.6).
  - Under (B, C), the attribution is stated as undecided.
- **D-ATTR** names, for every (B) verdict, the minimal set of resources the
  exposing protocol uses, together with the gate: P3, E-iso, vacancies,
  translations, known-1 cells (H-PREP), archive-swap or refill used as a gate
  setting, and feedback.

### A1.4 (F4): step (s5), partial outcomes, and the first missing premise

- **Node 1 gains step (s5).** In each record branch the conditional law of the
  configuration given `K` is uniform on an affine subspace (AP1 Lemma 3 and the
  paragraph after it,
  [AP1:533](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L533)).
  In the linear class PROT-B rests on (s5), and PROT-D rests on (s1)–(s4).
- **(C) splits.**
  - **(C-D).** PROT-D is not decided.
  - **(C-B).** PROT-D is proved and PROT-B is open.

  Any partial result that is proved is reported with every hypothesis it
  uses.
- **First missing premise.** A named statement `P` such that `P`, together with
  the listed hypotheses, yields PROT-D (for C-D) or PROT-B (for C-B) by an
  argument written in the record, where `P` is not implied by the class
  definition.
  - It is distinct from the first step of (s1)–(s5) that fails to transfer,
    which is reported separately. Step (s1) fails for `G_σ` by inspection,
    since each branch is a fixed nonlinear map, and so is not informative on
    its own.
  - `P` is reported and not adopted. CC-RECON applies when its only motivation
    is the protection or the target.
  - The premise named under (B) as blocking an exposure follows the same rule.

### A1.5 (F5): access and class membership

Amends `DESIGN.md` §1.2, §3.1–§3.3 and §3.6.

- **Registration and translation** apply only to cells at sites of `R`,
  including refills of sites of `R`. Hidden cells (sites outside `R`) are
  active but are never registered or translated.
- **Hidden cells.** By H-PS a hidden cell has the same law as a source cell
  placed in `R`. `R` may be any finite set of sites, so placing a site in `R`
  is the only route to registering its cell.
- **Meter identification.** P1 registers the record slot of a meter
  ([AP1:292](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L292)).
  Here the meter is identified with a ring cell, and a slot is registrable only
  if it was written at a tick in which the cell had at least one edge with
  multiplier 1. In `Π_A` every cell meets this at every tick. In `Π_B` the
  condition is stated on multipliers, not on the gated effective coefficient.
- **§3.6 reads:** the observer has no access other than P1 registration of
  cells in `R` and the supplied known values.
- **Gate semantics of E-iso.** E-iso sets multipliers to 0 on edges joining
  `R` to its complement. It does not block gates. An armed gated edge
  `{i, i+2}` inside `R` whose gate site `i + 1` lies outside `R` is gated by
  that hidden cell's `u` slot. The observer may choose `R` gate-closed (every
  gate of an armed edge in `R`), but this is not required.

### A1.6 (F6): archive-swap as a supplied gate write

- In `Π_A`, archiving a cell `g` and refilling its site with a P2 cell whose
  known slot is `u` sets the gate of `{g − 1, g + 1}` deterministically at the
  next tick. This is recorded as a supplied gate write.
- `Π_A`'s P1 is implemented by a supplied cell swap, where AP1 enforces
  terminality through P3 and E-iso
  ([AP1:292](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L292),
  SA-1(b) and §3.2 item 2).
- **Ledger row added to §3.7:** "Archive-swap or refill used as a gate setting
  | Both | Supplied (P1 with P2) | Attributed under D-ATTR".

### A1.7 (F7): CC-OFF and C-LIN

- **CC-OFF on proofs.** The clause "any proof of (A) specializes to Lemma
  Q(iii) for `N_1`" is replaced by a consistency rule:
  - where the (A) proof's hypotheses hold in `N_1` or `N_0`, its conclusion
    agrees with QA's Lemma Q(iii);
  - where they do not, the record states which hypothesis fails.

  The requirement on exposing protocols is unchanged: run with every gate held
  constant, an exposing protocol exposes nothing.
- **Vacancies in the linear limits.** The limits override V-0. In `N_1` every
  gate, vacant sites included, is held at 1, so no next-nearest edge is
  present. In `N_0` every gate, vacant sites included, is held at 0, so every
  next-nearest edge between present cells is present.
- **C-LIN under this unit's conventions.** C-LIN verifies Lemma Q(iii) for
  `N_1` and `N_0` with:
  - archive-swap refills;
  - vacancies;
  - direct registration under the meter identification (A1.5);
  - no heralds.

  The expected route is AP1 Lemma 3 extended to fresh cells of disjoint
  support. The verification is part of the record, not assumed.

### A1.8 (F8): the freeze anchor

- **The preregistration** is checkpoint 1 together with every amendment that is
  reviewed and is committed before the first commit that adds `RESULT.md`.
- **Anchor.** (a2), (a3) and C-IMPORT (iii) refer to that first `RESULT.md`
  commit in place of checkpoint 1. The same anchor applies to the sentence of
  `DESIGN.md` §2.1 that fixes `G_σ`, which this amendment does not change.
- **§A.41 row added to §7.**
  - *Invariant:* every amendment precedes the result, or is marked.
  - *Checkpoint:* for each file under `amendments/`, either
    `git merge-base --is-ancestor <amendment commit> <first RESULT.md commit>`
    succeeds, or the amendment states that it was written after a result and
    does not affect the decision.

### A1.9 (F9): the R-G disclosure, completed

Replaces the disclosure in `DESIGN.md` §4.3.

- **Direction.** Before writing `DESIGN.md`, the writer's informal expectation
  pointed toward exposure, outcome (B-D), in `Π_B` through R-G. The reason was
  that a gate cell influences the edge it gates without receiving a kick
  through that edge. For `Π_A` no expectation was formed. A one-line
  consideration noted that a gate cell in `Π_A` also receives nearest-neighbour
  kicks, so the `Π_B` mechanism does not carry over directly.
- **Example.** One example was worked mentally and was not written down or
  checked:
  - three cells: two ready cells joined by a gated edge whose gate is the
    third, with the nearest-neighbour edges disarmed;
  - known slots chosen so that one endpoint's new `u` slot equals the
    complement of the gate value;
  - registration of that endpoint, repeated at the next tick for the gate's
    other slot.

  It is not a result of this unit. It enters checkpoint 2 only as route R-G,
  and is derived and controlled there like any other route.
- **Conventions.**
  - The `Π_B` multiplier convention (each gated edge armable separately from
    the nearest-neighbour edges, with the gate factor not removable) is the
    convention the example assumed. It was written after the example. It was
    chosen as the per-edge analogue of P3 in QA's N, not to admit R-G. The
    reviewer may judge whether that order matters.
  - Refill in `Π_A` was chosen to make P1 terminality definable on an
    always-on ring.
  - V-0 was chosen as the vacancy-skip reading of SM's ring.
  - Direct registration of ring cells was adopted from M2D's practice.
  - E-iso without gate blocking was not considered when `DESIGN.md` was
    written. It is fixed in A1.5, and gates outside `R` remain live.
  - None of these four was chosen with the example in view.

### A1.10 (F10): the reading of the ring, and `L ≥ 5`

- **Reading.** `E(u)` is the support (union) reading of SM's directed ring: an
  undirected edge is present when at least one directed edge is present.
- **Added to the alternatives table of §2.4:** "`F_2` symmetrization
  `A + Aᵀ` of the directed adjacency | Edge `{i, i+1}` gets weight
  `1 + u_{i+1}`, gated by its own endpoint, so `f_{i+1}` reads `u_{i+1}`.
  This violates SM constraint (ii), as the intersection reading does. Edge
  `{i, i+2}` gets weight `1 + u_{i+1}`".
- **Why `L ≥ 5`.** At `L = 4`, `i + 2 = i − 2`, so `{i, i+2} = {i+2, i+4}` is
  one edge with two gates (`i + 1` and `i − 1`), and its presence is not fixed
  by (1). SM allows `L ≥ 4` for its directed rule. `G_σ` requires `L ≥ 5`.

### A1.11 (F11): dependence on the measure

- PROT-D is a statement about support. Its verdict is the same for every
  full-support product prior on the unknown slots.
- PROT-B and every (A) verdict are stated under N2 and H-PS. Independence from
  the measure is not claimed.
- On the finite ring of A1.20, H-INF-μ is not used.

### A1.12 (F12): provenance of the authorization

The owner authorization quoted in `DESIGN.md` is
[#1169 comment 6718997520](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6718997520)
(amaybaum, 2026-11-08T07:57:54Z, "Owner decisions (chat, 2026-11-08)"). The
review found the quote verbatim. The comment was posted after the checkpoint-1
commit. Before that, the decision was held as an owner chat decision.

### A1.13 (F13): bound on the self-checks

- **Bound.** Each self-check re-evaluates one instance stated in the record:
  a fixed protocol on stated cells with stated settings. It sums only over
  that instance's own unknown supplied bits, at most 16 bits per check. It
  searches no space of protocols, rules or instances.
- **Listing.** `RESULT.md` lists each check's instance, its number of unknown
  bits, its arithmetic, and what it controls.
- **§A.41 row added to §7.**
  - *Invariant:* no simulation, search or enumeration campaign.
  - *Checkpoint:* the self-check list in `RESULT.md`, each entry within the
    bound; the reviewer confirms this.

### A1.14 (F14): Main anchor

The cone theorem is
[Main:364](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/Main.md#L364).
Every citation of Main:366 in `DESIGN.md` (§5 C-NS and §9) reads Main:364.

### A1.15 (F15): consequences of C-NS and SC-1

- A C-NS violation for separated systems contradicts Main's cone theorem. It
  therefore voids every composition verdict (route R-C and Q3).
- A positive SC-1 finding, that is quantum behaviour imported as a premise,
  is a C-IMPORT failure and voids every verdict.
- SC-2 and SC-3 are reported.

### A1.16 (F16): the P1 and P2 controls

- **C-P1, variant (i).** A registered cell stays on the ring. Registering its
  two slots at consecutive ticks while it remains active must determine that
  active cell's `u + v` (`Q* = 1`), as QA's two-slice receiver does
  ([QA:512](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L512)).
- **C-P1, variant (ii).** A registered meter is coupled again (AP1 C9). It
  must determine both slots of the active partner cell, hence that cell's
  `u + v`.
- **C-P2.** A supplied cell with known `u + v` exposes that cell's `u + v`
  while the cell is active.
- **Use in proofs.** C-P1 and C-P2 check the definitions. In addition, an (A)
  proof cites the step at which it uses P1 and the step at which it uses P2. A
  proof that uses neither fails C-P1 or C-P2 by construction.

### A1.17 (F17): countercontrol to C-LIN

Applied to `G_SM`, the node-1 audit must record two failures:

- the failure of Lemma Q(i), by M2D Lemma Qσ(b);
- the failure of step (s3).

If the audit does not register them, it is insensitive, and C-LIN fails.

### A1.18 (F18): D-Q and USE-ctx

D-Q reads: no quantum quantity enters PROT-D, PROT-B, PROT-R or USE-ctx, all
of which are decided at configuration level on the full accessible theory. R1
and the comparator enter CC-NC only.

### A1.19 (F19): the scope of (m3)

(m3) motivates reciprocity of the edges at fixed `u`. The dependence on the
gate is one-way by construction: the gate influences the endpoints of the edge
it gates, and the endpoints do not act on the gate through that edge. (m3)
does not cover this dependence. Its motivation is (m1) and (m2), SM's graph.

### A1.20 (F20): smaller points

- **Heralds.** QA's N admits heralds. A heralded protocol is a mixture over
  herald values with input-independent weights. Each herald branch is a
  protocol with fixed settings, so determination and bias, which are judged
  per branch, lose nothing when heralds are excluded.
- **Ring.** The ring is `Z_L`, finite, with `L ≥ 5`. Statements are made for
  protocols whose cones do not wind (H-NW). This rule replaces the "infinite
  ring" sentence of §3.1, and H-INF-μ is not used.
- **B-B standard.** For B-B, §4.4 requires the conditional law of `f` in the
  exposing branch to be written out exactly, not only its support.
- **Sources added to §9.**
  - #1147: P2 resource accounting (provenance).
  - [#1169 comment 6713653816](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6713653816):
    the conditions profile, for condition (iv) (provenance).
  - [M1D:900](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L900):
    the SC-2 finding, cited for the supplied feedback executor.

## 2. A1.21: the owner's reporting layer

On 2026-11-08 the owner asked, in chat, that results be reported in three
tiers:

> Positive: The mechanism satisfies P1/P2 and survives the controls. …
> Partial: The mechanism succeeds mathematically but requires an additional
> physical assumption or fails to distinguish itself from a classical
> imitation. Negative: The mechanism cannot satisfy the required conditions
> within its registered scope.

and

> Even a positive result would not yet establish full OI–QM equivalence.

The tiers are a mapping onto the outcomes of the decision rule. They change no
outcome, control or criterion. Each class is reported in one tier.

| Tier | Outcome of the decision rule |
| --- | --- |
| **Positive** | (A), with every control of §5 and A1.7–A1.17 green, CC-NC included. A classical imitation counts as excluded only if the record shows the blocked spanning reads and exhibits a contextuality witness certified over tomographically complete equivalences |
| **Partial** | Any of: (A′); (A) with CC-NC not decided, or with a classical model found; (C-B), PROT-D proved and PROT-B open |
| **Negative** | (B), or protection otherwise shown to fail within the registered scope (`G_σ`, the stated class, P1, P2 and the ledger hypotheses) |
| **Undecided** | (C-D). The first missing premise `P` (A1.4) is named. This tier is not counted as negative |

**What Positive establishes.** Only a candidate: within the registered scope,
`G_σ` with P1 and P2 protects `Q* = 1` functionals and meets clauses (a)–(c).
It does not establish:

- physical realizability of `G_σ`, P1, P2, P3 or H-PREP;
- the other completion conditions of #1169;
- OI–QM equivalence;
- M-INACC in M2D's full sense, whose FB-reflection clause stays open (A1.2).

## 3. A1.22: the SM:112 defect, routed out

The review confirms the observation of `DESIGN.md` §2.4. SM:112 prints the
undirected degree as "bounded in [3, 2]", which is not an interval, and no
reading of SM's directed ring gives it. The reviewer's table:

- the support graph has degree 2 or 3 at `L = 4`, and 2, 3 or 4 at `L ≥ 5`;
- the out-degree is exactly 2;
- the in-degree is 1 to 3.

The likely intended bound is `[2, 4]`.

The defect is routed out of this unit to the coordinator, for an accountable
Issue under §A.45 rule 6. This unit makes no manuscript edit, and no verdict
depends on the printed bound.
