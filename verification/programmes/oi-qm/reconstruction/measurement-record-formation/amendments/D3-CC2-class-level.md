# MR-1 stage 1 — amendment D3: CC2 at class level, no instance

**Status: append-only amendment, subject to independent review.**

- **What it changes.** This amendment changes requirements of the frozen preregistration
  `../preregistration.md` at `1a236f332e8ea12b7fdb125bf8c5098ccd71d36c`. In particular it changes
  the frozen requirement that a CC2 instance be fixed at stage 1. Every change is listed in §D3.2
  against the exact frozen text.
- **What it leaves untouched.** The frozen file itself is unchanged and is not reinterpreted. Where
  this amendment and the frozen text differ, this amendment states the difference. Nothing else in
  the frozen text is changed.
- **What it does not do.** It freezes no `K★`, starts no screen, considers no candidate and runs no
  computation. No computation evaluating any physical, candidate, control or algebraic quantity was
  run for it.

***

## D3.1 Decision and source

**Source.** Owner decision, PR #1023 comment 6554185786 (owner `amaybaum`, 2026-11-01T06:00:19Z).
The decision was given in the coordinating session's chat on 2026-11-01, replying to comment
6553721062, and is recorded there "verbatim in substance".

It chooses option D3 of `MR-star.md` §K★.8, as noted in §K★.11 RC-7. It follows the blocked `K★`
record in `MR-star.md` (§K★, with the review corrections of §K★.11).

**The decision, quoted from the comment:**

> The review found a genuine obstacle. OI fixes the underlying dynamics but does not determine a
> unique classical measurement apparatus. Choosing a convenient apparatus just to make the quantum
> comparison succeed would introduce an unjustified assumption. Under D3:
> - the entire admissible classical comparison class is kept;
> - no single model is chosen arbitrarily;
> - there is **no claim** that OI has ruled out classical explanations;
> - the `CONTEXTUAL` result category is retained, with `CC2-unseparated`;
> - the stronger `NONCLASSICAL` category (2.4) is **unavailable under the amended protocol**.
>
> The owner's framing: "This is a narrowing of what we can claim, not evidence against OI." D3 is to
> be documented in an **append-only, independently reviewed amendment** that states explicitly that
> it changes the previously frozen instance requirement. There is to be no silent reinterpretation
> of the preregistration, and `1a236f33` stays unchanged.

The next step it authorizes: this amendment and the errata provenance; then independent review and
green CI; then revisiting the `K★` freeze decision. Not authorized: stage 2, candidate screening,
Lean or Python computation, manuscript changes, merge.

## D3.2 Frozen text changed or set aside

Line numbers refer to `../preregistration.md` at `1a236f33`. Each item quotes the frozen text, then
states its standing under D3.

**C-1. The CC2-instance rule (§5.8, L561–564).**

> The CC2 instance is fixed by a constraint that OI holds at `D`, cited under Q1's rule (§4.4),
> frozen with `K★` and before the candidate screen; at `D` only K1 qualifies. Under K1 the
> Kochen–Specker-type deterministic class contains `𝔐★`-type models (A1), so a 2.4 token is relative
> to the frozen CC2 instance only, and the class-level ceiling is 2.5 with `CC2-unseparated`.

- **Set aside:** the first sentence, the obligation to fix a CC2 instance. No instance is fixed at
  stage 1 or later.
- **Moot:** the clause "a 2.4 token is relative to the frozen CC2 instance only", since 2.4 is
  unavailable (C-4).
- **Retained and now operative:** the clause "Under K1 the Kochen–Specker-type deterministic class
  contains `𝔐★`-type models (A1)", and the class-level ceiling, 2.5 with `CC2-unseparated`. That
  ceiling becomes the rule for every law.

**C-2. The CC2 row (§5.8 table, L569).**

> | CC2 | disturbance and contextuality: a Kochen–Specker-type deterministic model with disturbing
> readout, extended by a disturbing marker | may return W1 (U2) | a test named at stage 1 among T3,
> T5 and T6 (T6 under K2 is not available to OI, Main:414); if none separates it, the law can be at
> most `CONTEXTUAL` (§6), which is not a control failure |

- **Retained:** column 2, as the definition of the CC2 *class*. It is unrestricted: every model the
  description admits stays in it, and no member is excluded or preferred. Also retained are the
  reference behaviour "may return W1 (U2)" and the clause "the law can be at most `CONTEXTUAL` (§6),
  which is not a control failure", which now holds for every law.
- **Set aside:** "a test named at stage 1 among T3, T5 and T6". With no instance there is nothing to
  run the test on, and no separating test is named.

**C-3. Control and outcome separation for CC2 (§5.8, L551–557), and the stage-2 controls (§7.1,
L675–676).**

> Controls first (PC-Q, CC1–CC8, mutations, a decision-function self-test with at least one
> synthetic results file per row), then the candidate.

- **Set aside for CC2 only:** CC2 is not executed at stage 2.
- **Its result fields:** its control-separation and outcome-separation fields are the constant "not
  separated (class level, D3)". They are fixed now and are not read from any run.
- **Why no control failure follows:** L553–554 already record CC2's non-separation as admissible
  ("except where the table records non-separation as admissible (CC2, CC8)"). That clause and §6
  0(i) are unchanged.
- **Unchanged:** every other countercontrol runs as frozen.

**C-4. Token 2.4 (§6, L620) and the nonclassical criterion (§5.7, L529–533).**

> | 2.4 | `NONCLASSICAL/W1[+W2]` | W1 decided positive; every countercontrol CC1–CC7 outcome-separated
> from `𝔐★`'s law by its named test (§5.8); T8 removes the witness when the responsible element is
> deleted | …

> A law is reported as nonclassical (token 2.4) only when W1 holds and every countercontrol CC1–CC7
> is separated **from `𝔐★`'s own law** by its named test (§5.8, outcome separation). "Nonclassical" is
> relative to the CC1–CC7 instances frozen at stage 1, not to every classical model.

- **Changed:** token 2.4 is unavailable under the amended protocol.
- **Mechanism:** C-3 fixes CC2's outcome-separation field to "not separated", so the 2.4 criterion
  "every countercontrol CC1–CC7 outcome-separated" is never met. A law with W1 decided positive and
  T8 passing then meets row 2.5 ("some countercontrol among CC1–CC7 not outcome-separated") and
  carries `CC2-unseparated`.
- **Unchanged:** the row texts of 2.4 and 2.5 and the first-match order. The criterion is not
  weakened. The CC2 class is not replaced by a weaker instance, and no route to 2.4 remains.

**C-5. The decision-function self-test (§7.1, L675–676: "at least one synthetic results file per
row"; §8, L713: "token 2.4 against 2.5 in the self-test").**

- **Changed for row 2.4:** "at least one synthetic results file per row" becomes a test of
  unreachability. A synthetic results file that separates every countercontrol except CC2, with W1
  decided positive and T8 passing, must return 2.5 with `CC2-unseparated` and `CC8-unseparated`.
  The self-test fails if any input returns 2.4.
- **Unchanged:** every other row's self-test requirement.

**C-6. Stage-1 commit order (§7.1, L661–664).**

> committed in this order: first `K★`, including the CC2 instance and the constraint that fixes it,
> before any candidate screen

- **Changed:** "including the CC2 instance and the constraint that fixes it". `K★` contains no CC2
  instance.
- **Unchanged:** `K★` still precedes any candidate screen, and the rest of the order stands.

**C-7. The Kochen–Specker execution blocker and owed read (§7.1, L668–672; §8, L714; §9, L744–748
and L758).**

> no execution step whose decision depends on a claim from Mazurek et al. 2016, from the
> Kochen–Specker instance (CC2), or from the proof of Props. V.1–V.2 … proceeds until that source
> has been read first-hand and the read is recorded in the stage-1 log.

> | S. Kochen, E. P. Specker, *J. Math. Mech.* 17, 59 (1967) | CC2 instance | at stage 1 | not read
> first-hand; owed at stage 1 |

- **Text retained unchanged.**
- **Standing under D3:** no element and no execution step depends on a claim from a Kochen–Specker
  instance, so the blocker binds no step for CC2. The owed read of L758 supports no element and is
  not owed for D3.
- **The gate itself:** it stays recorded as unresolved: LIT-3 NOT-MET, LIT-5 PARTIAL (§D3.5). It is
  not declared met.

## D3.3 Unchanged

The following stand as frozen, including at every line not named in §D3.2:

- **Countercontrols:** CC1 and CC3–CC8, their reference behaviours, separating tests and stage-1
  instance obligations (L559–560 for CC1, CC3, CC4, CC5, CC7).
- **CC8:** the per-law A-realization, with `CC8-unseparated` mandatory on every 2.4 and 2.5 token
  (L533–536, L575).
- **The battery:** T0–T9, the §5.3 equivalence and conventions c1–c4, and the mutation list.
- **Token 2.5:** with `CC2-unseparated` and `CC8-unseparated`.
- **Rows 0, 2.1–2.3, 2.6–2.9, axis 1, axis 3 and the primitive-proposal track.**
- **The duality rules:** the complementarity benchmark as a consistency requirement and not a
  witness, and the predictability–visibility witness only as a certified T7 instance (§3.5,
  AW-MR6).
- **The benchmark rules:** PC-Q, and the `BENCHMARK-MATCH` and `BENCHMARK-MISMATCH` sub-labels.
- **The `K★` timing rule:** `K★` is frozen before any candidate law is derived (L359–360, L435–436,
  L712), with the mutation "`K★` fixed after a candidate law".
- **Row 0:** 0(iii) and 0(vi), with every other clause of row 0.
- **The rest:** the void clause of §7.1, the authority limits of §7.2 and the hard-to-vary
  requirements of §7.3.

## D3.4 Consequence for `K★`

Under D3 the obligation that blocked `K★` (`MR-star.md` §K★, missing element M1 as restated in
§K★.11 RC-1) is removed, because no instance is required. As it would stand:

- **`K★ = {K1}`**: one fixed native `φ`, not a construction made per law, with `π` and `μ` ranging
  over their admissible classes under Q1 (L330–331, L358–359). The membership reading is
  `MR-star.md` §K★.2: K2 is relinquished; K3 and K6 state no bound; K4 and K5 are not held.
- **CC2 at class level**, with no instance. The class is the L569 description, unrestricted. Under K1
  it contains `𝔐★`-type models (L562–563).
- **No CC2 instance and no CC2 separating test.**

**`K★` is not frozen here. Freezing it is a separate owner decision,** to be revisited after
independent review of this amendment and green CI (comment 6554185786).

## D3.5 Dependence on Mermin-only claims

The Mermin 1993 errata stay unread first-hand. See `stage1-log.json` under `lit5_errata`
(`LIT-5-ERRATA`, with correction REV-8), and `KS-substitution.md` §8.

*Result: no step under D3 depends on a Mermin-only claim.* The reasons, item by item:

- **The finite four-dimensional square (M-b), the product rule, and the finite-menu form of M-c.**
  Within MR-1 these were needed only to certify the Kochen–Specker-type character of a CC2 instance
  on a finite menu. That is missing element M4, which by §K★.11 RC-3 held only under the proposed
  reading (c-iv). D3 fixes no instance, so nothing is certified, and none of the three is used.
- **M-a and the all-rays form of M-c.** These are also supported by Bell 1966 (B-b, B-c; LIT-4, which
  is MET). The candidate locations of errata E1 and E3 (arXiv §VII pp. 19–20; §IX–X pp. 23–24) may
  bear on Mermin's p. 18/19 and p. 24 statements. No D3 step rests on Mermin for either; each rests
  on Bell.
- **The CC2 class description.** Reading "Kochen–Specker-type deterministic" as contextual
  deterministic (LIT-5-C3) is also supported by Bell 1966 §V. Its diagnosis is that, beyond two
  dimensions, a deterministic account escapes only through dependence "on the complete disposition
  of the apparatus" (B-b, B-c). D3 uses the class description only as a definition, with no
  certification.
- **The agreement with Corollary U3 (Mermin p. 23).** Mermin-only, but not load-bearing (frozen
  L345).

## D3.6 Framing

D3 narrows what MR-1 can claim. It is not evidence against OI, and it is not evidence for any
classical model. Specifically:

- **No claim that classical explanations are ruled out.** Axis 2's highest positive token is 2.5,
  `CONTEXTUAL`. That token places a law outside the noncontextual class relative to the frozen
  countercontrols, with `CC2-unseparated` and `CC8-unseparated`. It makes no claim that OI, or the
  unit, has ruled out classical explanations.
- **No global no-go.** None is stated or implied. `GAP`, `FAIL` and `CLASSICAL-REPRODUCED` keep
  their frozen scopes (L650–652).

## D3.7 Hard to vary (§A.29)

- **No free element.** D3 introduces no parameter. CC2's separation fields are a constant fixed now
  (C-3), and the class is the frozen L569 description, unrestricted. Nothing in D3 can be adjusted
  to a later outcome.
- **What re-admitting 2.4 would need.** It needs a CC2 instance, so it needs what M1 found missing:
  an OI-held selection principle within the K1 class, or an independently justified instance from
  new first-hand sources. Either one comes through a new append-only, independently reviewed
  amendment, fixed before `K★` is frozen and before any candidate screen.
- **No re-admission after an outcome.** The frozen text freezes the CC2 instance with `K★`
  (L561–562). An instance introduced after any outcome would therefore be a change to `K★` after an
  outcome, which voids the run under 0(iii). Neither D3 nor any successor amendment can re-admit 2.4
  after a stage-2 result.
- **What D3 keeps as controls.** CC1 and CC3–CC8, the battery, rows 0 and 2.5, and the `K★` timing
  rule (§D3.3).

## D3.8 Commands and hygiene runs

- **Read-only commands:**
  - one GitHub connector read of PR #1023 (issue metadata and the comment page that holds
    6554185786);
  - `git rev-parse HEAD` (`41aa6bdd90a676573b6a6a417d3f56908da8361e`);
  - `git show 1a236f33:…/preregistration.md | grep` for the CC2, instance, 2.4 and nonclassical
    lines;
  - display of the errata reader's off-repository outputs: file listing, and `grep` of the Crossref
    records for title, volume, page and dates, and of the APS and link.aps.org responses for their
    page titles.
- **Hygiene, run D-1 (on the staged draft):** placement, census and SC-42. The results are in
  `stage1-log.json` under `d3_step`.
- **Hygiene, run D-2 (on the staged final content, before the single commit):** the same three
  tools, then `git diff --cached --stat 1a236f33 -- ../preregistration.md` and the deleted-line
  check. This run is declared here before it is made, and its outcome is stated in the commit
  message.

## D3.9 Review corrections

**Source.** Independent review of `987ecf5e` (verdict: accept with changes), relayed by the
coordinator. The text above is kept as written; this section adds to §D3.2.

**C-8. Outcome (2) and the axis-2 heading (§1, L45–47; §6, L613).**

> **Outcomes, reported on separate axes (§6):** (1) a sourced physical interaction and its records
> (row 20; row 14 through the frozen `(Obs, μ)`); (2) nonclassical coherent recombination,
> distinguishable within the declared controlled operational class; (3) full instrument and composite

> **Axis 2 — nonclassical coherent recombination** (evaluated only after 1.4).

- **Retained as labels only.** The wording of both lines is unchanged and names the axis.
- **Their strongest token under D3:** 2.5, `CONTEXTUAL`, with `CC2-unseparated` and
  `CC8-unseparated`. Token 2.4, `NONCLASSICAL`, is unreachable (C-4).
- **No claim follows from the label.** No result under D3 is reported as nonclassical coherent
  recombination in the sense of token 2.4.

**Hygiene for this section:** runs E-1 and E-2, recorded in `stage1-log.json` under
`d3_review_corrections`.
