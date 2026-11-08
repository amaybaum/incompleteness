# M-INACC-1 amendment A2: application of the A1 confirmation

**Standing.** WIP / UNVERIFIED. Amendment to `../DESIGN.md`
(`75c0befcb324466cb4bf0e90c7ef3cbe429b58ad`) and to `A1-prereg-review.md`
(`bcf2aba49d5f991b404c24dedbce6910470fda27`, the parent of this amendment's
commit). Writer: Claude Code session, 2026-11-08.

It applies the findings G1–G8 of the reviewer's confirmation of A1 (verdict:
accept with changes; blocking finding G1).

- **Timing.** Written before any derivation. No `RESULT.md` exists when it is
  committed, and it states no result.
- **Precedence.** `DESIGN.md` and A1 are not edited. Where A2 differs from
  them, A2 governs.
- **Scope.** `G_σ` is unchanged. Nothing is adopted.
- **Review.** The reviewer confirms A2 at its exact SHA, as A1.8 requires in
  the form amended by A2.5.

Repository links to the analysis sources are pinned to `main@f88c1842`
(`f88c184220453badfc9279ab9a86b6785e4db5ff`). Owner records are linked by
comment id.

## 0. Amendment table

| ID | Finding | Rule amended | Effect on outcomes |
| --- | --- | --- | --- |
| A2.1 | G1, PROT-R excluded from the decision (blocking) | A1.1; `DESIGN.md` §4.1, §4.2; A1.4; A1.7; A1.21 | PROT-R becomes part of PROT, of (A) and of clause (b). Exposure type (B-R) and partial outcome (C-R) are added. C-LIN checks PROT-R in the linear limits |
| A2.2 | G2, `Π_B` multiplier convention and A1.5 registrability rule | `DESIGN.md` §3.2; A1.5; A1.9; §4.2 (B) | Both rules are kept, with an independent justification and the alternatives stated. Every (B) record for `Π_B` reports gated-edge isolation |
| A2.3 | G3, transported record slots | A1.5 | A record slot written by coupling stays registrable after free ticks |
| A2.4 | G4, the first missing premise `P` | A1.4 | `P` is restricted in content and ordered by step; every candidate is reported |
| A2.5 | G5, amendment anchor | A1.8 | "Reviewed" is anchored to #1198 before the first `RESULT.md` push. A post-result amendment that affects the decision voids the verdicts it affects |
| A2.6 | G6, tier mapping | A1.21 | Positive requires a certified witness. (C-B) maps to Undecided. The extra Negative category is deleted. No combined tier. The owner record is cited and quoted in full |
| A2.7 | G7, C-P1 variant (i) | A1.16 | Both slots are registered at one moment between ticks |
| A2.8 | G8, nits | A1.1, A1.3, A1.6 | Equal duration in USE-ctx; monotonicity of sub-labels; link to AP1:338 |

## 1. Amended rules

### A2.1 (G1): PROT-R enters the decision

- **PROT-R(Π).** For every protocol of `Π`, every tick `t`, every linear
  functional `f` on the cells active at `t` with `Q*(f) = 1`, and every later
  tick `t′ ≥ t`: the value `f(t)` is neither determined nor biased given the
  observer's knowledge `K` at `t′`.
  - `K` at `t′` includes every record up to `t′`.
  - At `t′` the value `f(t)` is in general a nonlinear function of the
    configuration of active and archived cells. Determination and bias are
    judged on its conditional law in each record branch of positive
    probability.
- **PROT(Π)** is the conjunction PROT-D(Π) ∧ PROT-B(Π) ∧ PROT-R(Π). PROT-R at
  `t′ = t` is PROT-D together with PROT-B.
- **(A)** requires PROT(Π). Clause (b) of M-INACC is evaluated as PROT(Π).
  A1.1's sentence that PROT-R is reported but is not part of the (A) decision
  is replaced by this rule.
- **The Bayes observation of A1.1** concerns the statistical reading of clause
  (a), which is not used: clause (a) is decided by USE-ctx. PROT-R and USE-ctx
  do not conflict by definition.
- **Exposure type (B-R).** A protocol of `Π` is exhibited in which, at some
  `t′ > t`, `f(t)` is determined or biased given `K` at `t′`, for a
  `Q* = 1` functional `f` on the cells active at `t`.
  - The record writes out the exact conditional law of `f(t)` in the exposing
    branch, as A1.20 requires for (B-B).
  - CC-OFF applies: run with every gate held constant (`N_1` and `N_0`), the
    same protocol gives no (B-D), (B-B) or (B-R) exposure.
  - D-ATTR applies as for (B-D) and (B-B).
- **Partial outcome (C-R).** PROT-D and PROT-B are proved and PROT-R is open.
  The full set of partial outcomes, in increasing order of what is proved, is:
  - (C-D): PROT-D open;
  - (C-B): PROT-D proved, PROT-B open;
  - (C-R): PROT-D and PROT-B proved, PROT-R open.

  Each partial result proved is reported with its hypotheses.
- **C-LIN.** C-LIN verifies PROT-R in `N_1` and `N_0`, under this unit's
  conventions (A1.7). The expected route is `Q*`-preserving transport together
  with `Q* ≡ 0` on the span of transported known slots and registered records,
  terminal and active cells together. The route is verified in the record, not
  assumed. If PROT-R fails in a linear limit, that limit is reported and C-LIN
  is red for every verdict that relies on PROT-R.
- **Tiers.** The tier table of A2.6 includes PROT-R.

### A2.2 (G2): the `Π_B` multiplier convention and the registrability rule

**Disclosure.** Both rules were written after the mentally worked example of
A1.9: the multiplier convention in `DESIGN.md` §3.2, and the registrability
rule in A1.5. Both are kept. Their justification below is independent of that
example and of any outcome.

**Multiplier convention (`DESIGN.md` §3.2), justification.**

- QA's P3 loads coefficients on the individual couplings of the native rule:
  - "loaded per tick and per edge"
    ([QA:131](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L131));
  - "arbitrary per-tick, per-edge coefficients"
    ([QA:242](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L242));
  - "P3's arming of the individual couplings"
    ([QA:838](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L838)).

  In `G_σ` the individual couplings are the nearest-neighbour edges and the
  gated edges, so each is armed separately.
- P3 does not alter the structure of the rule it arms. In QA it cannot add a
  center term `k_ii` (QA:129–131). Under `G_σ` it likewise cannot remove the
  state dependence of a gated coupling: the multiplier scales the native
  coefficient `1 + u_{i+1}` and does not replace it.
- With all multipliers 1 the native rule is recovered, so `Π_A ⊂ Π_B` holds.

**Alternatives, with the reason each is rejected.**

| Alternative | Reason for rejection |
| --- | --- |
| Replacement: the loaded coefficient replaces the native one on a gated edge (a literal reading of AP1 SA-1(a′)) | It removes the gate on every armed gated edge and makes those couplings ungated next-nearest couplings. That is QA's separate conditional premise NNB ([QA:805](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L805)), not P3. It reduces armed `Π_B` to a linear class that Lemma Q(iii) already covers, so `Π_B` would not test `G_σ`. It breaks `Π_A ⊂ Π_B`, because `1 + u_{i+1}` cannot be loaded classically |
| Gated edges not armable: P3 arms nearest-neighbour edges only | Exempting one coupling family from P3 has no source in QA or AP1, which arm individual couplings. Its only effect relevant here is on gate-mediated reads, so it would be a restriction motivated by protection (CC-RECON) |

**Reporting requirement.** Every (B) record for `Π_B` states, for each tick of
the exposing protocol, whether a gated edge is armed while the
nearest-neighbour edges incident to its endpoints or its gate are disarmed.
This makes the role of the convention visible in the verdict.

**Registrability rule (A1.5), justification.**

- The rule: a slot is registrable if it was written at a tick in which the cell
  had at least one edge with multiplier 1 (with A2.3 for transported slots).
- It is stated on multipliers, which belong to `K`. Whether a registration is
  permitted is therefore decidable by the observer, so membership of a
  protocol in `Π_B` does not depend on unknown values.
- It identifies the meter by the procedure (an armed coupling), as AP1's "the
  slot written by its coupling" does
  ([AP1:292](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L292)).
- AP1 treats a record whose coupling did not act as the observer intended as a
  registration that yields a different instrument, not as an excluded
  operation (its unheralded defect,
  [AP1:617](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L617)).

**Alternatives to the registrability rule.**

| Alternative | Reason for rejection |
| --- | --- |
| Effective coefficient nonzero: the slot was written by an edge whose effective coefficient (multiplier times gate factor) was 1 | Not decidable from `K` when the gate is unknown, so class membership would depend on unknown values |
| Effective coefficient determined by `K`: the slot was written by an edge whose effective coefficient is fixed by `K` and equal to 1 | Decidable from `K`, and closer to a strict reading of "written by its coupling". Rejected because it conditions an access rule on the observer's knowledge of a gate. AP1 has no such condition (AP1:617 above). Its only effect relevant here is to forbid registrations whose record depends on an unknown gate, which is a restriction motivated by protection (CC-RECON) |

Under the kept rule:

- a pure gate cell with no armed edge cannot be registered;
- a cell whose only armed edge is gated by an unknown gate can be registered.

Every (B) record for `Π_B` states which registrations rely on the second
case.

### A2.3 (G3): transported record slots

A1.5's registrability rule is amended. A slot written at a tick in which the
cell had at least one edge with multiplier 1 stays registrable, as its
transported functional, after any number of free ticks of that cell. This is
AP1 SA-1(b)'s "the slot written by its coupling, transported by the cell's free
evolution". In `Π_A` cells take no free ticks, so the amendment bears on
`Π_B` only.

### A2.4 (G4): the first missing premise `P`

A1.4's definition is amended.

- **Content.** `P` is a statement about `G_σ`, the protocol class or the
  supplies. It does not mention determination, bias or knowledge of
  `Q*`-class functionals, and it does not mention PROT-D, PROT-B or PROT-R.
  A statement that fails this requirement is not a candidate.
- **Sufficiency.** `P`, together with the listed hypotheses, yields the open
  property (PROT-D for (C-D), PROT-B for (C-B), PROT-R for (C-R)) by an
  argument written in the record. `P` is not implied by the class definition.
- **Order.** Candidates are ordered by the earliest step among (s1)–(s5) of
  node 1 whose transfer to `G_σ` `P` secures. "First" refers to that order.
- **Reporting.** Every candidate found is reported, in that order, with the
  step it secures. No candidate is selected over another. Each is reported and
  not adopted, with CC-RECON applied when its only motivation is the
  protection or the target.
- **Blocking premises under (B).** The premise named under (B) as blocking an
  exposure obeys the same content and reporting rules.

### A2.5 (G5): the amendment anchor

A1.8 is amended.

- **Reviewed.** An amendment counts as reviewed only if the reviewer's
  confirmation at the amendment's exact SHA is recorded on draft PR #1198
  before the first commit that adds `RESULT.md` is pushed.
- **Post-result amendments.** An amendment written after a result:
  - if it does not affect the decision, it states this;
  - if it affects the decision, it voids every verdict it affects. Those
    verdicts are reported as void, and they can be re-established only by a new
    preregistered unit.
- **§A.41 row added to `DESIGN.md` §7.**
  - *Invariant:* every pre-result amendment is reviewed before the result.
  - *Checkpoint:* for each amendment, the creation time of the reviewer's
    confirmation comment on #1198 precedes the time at which the first
    `RESULT.md` commit appears on #1198's branch, as shown by the PR timeline.
    The coordinator records both times.

### A2.6 (G6): the tier mapping

A1.21's tier table and its quotation are replaced.

**Owner record.** The tier instruction is recorded at
[#1169 comment 6719192859](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719192859)
(posted by amaybaum, 2026-11-08T08:19:45Z, as "Owner guidance (chat,
2026-11-08): M-INACC result tiers, recorded by the coordinating session"). The
tier passage, in full:

> For the eventual M-INACC result, I would distinguish three outcomes:
>
> * Positive: The mechanism satisfies P1/P2 and survives the controls. This would provide a candidate for further physical validation.
>
> * Partial: The mechanism succeeds mathematically but requires an additional physical assumption or fails to distinguish itself from a classical imitation.
>
> * Negative: The mechanism cannot satisfy the required conditions within its registered scope.
>
> Even a positive result would not yet establish full OI–QM equivalence. We would still need to demonstrate physical realizability and establish the remaining conditions.

The same record quotes the owner on the classical-imitation control: "Even if
the construction reproduces the target quantum behaviour, we need to establish
that it does something genuinely quantum rather than merely reproducing the
same observable statistics through classical means."

**Mapping.** The tiers are a reporting layer and change no outcome, control or
criterion.

| Tier | Outcome of the decision rule |
| --- | --- |
| **Positive** | (A): PROT(Π) proved (PROT-D, PROT-B and PROT-R), clauses (a)–(c) met, and every control green. In addition, a contextuality witness is exhibited, certified over tomographically complete equivalences, with the blocked spanning reads shown. Without that witness the tier is Partial |
| **Partial** | (A′); or (A) without a certified witness, whether CC-NC is not decided or a classical model is found |
| **Negative** | (B), in any of its types (B-D), (B-B) or (B-R) |
| **Undecided** | (C-D), (C-B) or (C-R). The properties proved are reported as proved, and every candidate `P` (A2.4) is named. This tier is not counted as negative |

A1.21's "or protection otherwise shown to fail" is deleted.

**No combined tier.**

- Each class is reported in its own tier, `Π_A` first: it has fewer supplied
  resources, and so it is the natural class for the question whether OI
  produces the property.
- No tier combining the two classes is reported, and the more favourable
  class is never promoted to a headline.

**What Positive establishes.** As A1.21 states: a candidate for further
physical validation. It does not establish:

- physical realizability;
- the remaining conditions of #1169;
- OI–QM equivalence;
- M-INACC in M2D's full sense.

### A2.7 (G7): C-P1 variant (i)

A1.16's variant (i) is replaced. A registered cell stays on the ring, and both
its slots `u` and `v` are registered at one moment between ticks. Without P1's
archive the cell remains active, and its `u + v` (`Q* = 1`) is determined, as
by QA's two-slice receiver
([QA:512](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L512)).
Variant (ii) and C-P2 are unchanged.

### A2.8 (G8): nits

- **Duration in USE-ctx.** In A1.1, the protocols `T` and `T′` have the same
  tick count, so timing enters `K` identically for both.
- **Monotonicity of sub-labels.** Since `Π_A ⊂ Π_B`, every property proved for
  `Π_B` holds for `Π_A`, and the record carries the proof over. Every exposure
  in `Π_A` is an exposure in `Π_B`. Hence, when `Π_B`'s outcome is not (B):

  | `Π_B` | Possible `Π_A` |
  | --- | --- |
  | (C-D) | A∪A′, (C-D), (C-B) or (C-R) |
  | (C-B) | A∪A′, (C-B) or (C-R) |
  | (C-R) | A∪A′ or (C-R) |
  | A∪A′ | A∪A′ |
- **A1.6 citation.** The sentence that terminality is enforced by P3 and E-iso
  is at
  [AP1:338](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L338)
  (§3.2 item 2), not AP1:292.
