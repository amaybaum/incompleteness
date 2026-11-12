# Independent re-check of OA-2 r2 (`OA-2-REPORT-r2.md`)

**Reviewer standing.** Read-only and paper-only: no computation, script, commit, push or GitHub
write. Sources were read with `git show`.

- **Main moved again.** It is now `615cc119`. `git diff ec257bee 615cc119` leaves `papers/Main.md`,
  `verification/lean-mathlib/` and every record r2 cites unchanged. It adds TUNE-1 drafts under
  `reconstruction/drafts/tune-1-20261111/` (#1237); see N7.
- **Citation forms.** `r2:n` is a line of `OA-2-REPORT-r2.md`. `Rev:` refers to `REVIEW-OA-2.md`.
  Reviewer derivations are marked [RW].

## Verdict: **ACCEPT WITH NITS**

- **F1–F9 and the item 8/9 notes are applied.** Every verdict-level change is applied correctly and
  propagated: §0, the N-sections, the verdicts, §4, §5, §6 and §9.
- **Verdicts.** No verdict needs to move.
- **Nits.** The nits below are required before r2 is treated as final. Each is local and none changes
  a verdict. N1 is a §A.34 directional issue in a displayed "iff", and I supply the missing
  direction.

***

## Pressure tests requested

### 1. Proposition B, three parts, each direction separately (§A.34)

**(i) Preparation noncontextuality from `R` injective on `W` (r2:228–229): correct.**

**(ii) (⇐) (r2:242): correct.**
- If `ρ` is injective, two available effects that agree on `W` have a difference in
  `span(effects)` that vanishes on `W`.
- That difference therefore vanishes on `U`, and the response functions are equal on `U`.

**(ii) (⇒) (r2:243–247): the stated proof is not valid. The direction is true, and its general
proof is short [RW].**
- **What r2 says.** It says the direction "is shown by the counterexample below, not in general",
  and the Limits repeat this (r2:820–821).
- **Why that cannot stand.** A counterexample cannot establish a universal direction. The sentence
  "forces the model to assign one response to two ontically different functions" conflates two
  different properties:
  - *the configuration model* being measurement-noncontextual, which is what (ii) states;
  - *the fragment* admitting some noncontextual model, which is not what (ii) states.
- **Proof of (⇒) for the configuration model [RW].**
  1. Suppose `ρ` is not injective. Then some `Σ c_i e_i` is zero on `W` and nonzero on `U`.
  2. Split the coefficients by sign and rescale so that each side has total weight at most 1. Pad
     each side with the null effect.
  3. This gives two convex mixtures of available effects. They are operationally equivalent,
     because they are equal on `W`, but they have different ontic response functions on `U`.
  4. So the configuration model is measurement-contextual.
  5. This needs only convex mixing with the null effect, which is standard.
- **What does not follow.** Non-injective `ρ` does **not** imply that the fragment fails to be
  simplex-embeddable. Another model may exist. This is why the counterexample is needed separately,
  for the G3 claim.
- **Required.** Replace the (⇒) proof with the argument above, or display (ii) one way ("if").
  Correct the Limits line r2:820–821.

**(iii) (r2:234–236): acceptable as a sufficient condition.** It nearly restates the definition. It
is "when", not "iff", so §A.34 is satisfied.

**(iv) (r2:237–238): correct.**

**Counterexample (r2:249–268): correct, and it matches my derivation.** One check: `w₁₀` and `w₁₁`
(r2:258) are right on all four vertices.

**Corollary B′ (r2:270–281): correct.**
- It now has the two-route form, credited to MECH-2:842 and MECH-2:521–529.
- It is labelled CONFIRMING.
- Whether the dual route survives closure is correctly left open.

**N2: transformation noncontextuality in Theorem E(b).**
- **The issue.** Theorem E(b) step 5 (r2:462–464) claims measurement **and transformation**
  noncontextuality "by Proposition B(ii)–(iii)". The model there has `Λ` = the values of `Z₀`, not
  the configuration model. B(iii)'s condition, that each procedure act on `Λ` as a stochastic map
  fixed by its operational action, is not checked in that model.
- **Why that matters little here.** G3 as defined (r2:139) is decided by the prepare–measure
  fragment (Schmid et al.), so transformation noncontextuality is not needed for "fails G3".
- **Required.** Drop "and transformation-" from step 5, or check B(iii) in the `Z₀` model. Say
  explicitly that G3 here is the prepare–measure criterion.

### 2. Class-N injectivity (r2:552–568)

- **Effect side [RW]: correct.**
  - The span of native `Z`/`X` effects is `{f(z) + g(x)}`.
  - Suppose it vanishes on the `z`-pair and `x`-pair laws. Then `f ≡ −mean(g)` and `g ≡ −mean(f)`.
    Both are constant, and their sum is zero, so `f(z) + g(x) ≡ 0` on `F_q²`.
  - So `ρ` is injective for every `q`, and (⇐) gives measurement noncontextuality.
- **Preparation side.** At general `q`, `R` is also injective on `W`. Both `W` and the effect span
  have dimension `2q − 1`, and an injective `ρ` between equal dimensions is onto `W*`.
- **N6 (nit).** The text says "`U = F₂²`" and checks "(1, ⟨Z⟩, ⟨X⟩) on the four points", which is
  the `q = 2` case, while the effect check is stated "for every `q`". Either restrict to `q = 2` or
  add the one-line general-`q` preparation argument above.
- **Scope.** The conclusion is stated only for the prepare–measure fragment, which is correct. It is
  conditional on Lemma Q(iii), the type grading and H-LIFT [R]. "Native `Z`/`X` reads only" must be
  read as closed under `e ∘ π` (Lemma 1). The grading is what excludes a `(z + x)` read from that
  closure. That reading is consistent with MECH-2:530–534.

### 3. (H4) nested records and AW-OA2-4

- **(H4) (r2:433).** Correctly stated, typed as a hypothesis, and tied to open retention
  (obsmu:917).
- **(H3) (r2:432).** It now excludes only supplied control. Durations are native, which removes r1's
  conflict with Lemma 1 and Theorem C.
- **Theorem E(b) step 1 (r2:456–457).** It uses (H4) correctly.
- **Pressure test 2 (r2:528–531).** Correctly rewritten.
- **AW-OA2-4 (r2:485–498, r2:757–760).** It states the gap without overclaiming either way, and adds
  the right cross-propagation note: any 5d claim that assumes "one joint record" without retention is
  exposed. **Accepted.**

### 4. C-PM′ and the gadget horizon counts (r2:95–106, r2:336–389)

**Bath count `M_b > K`: correct [RW].**
- A cell that a gadget sends to position `M_b` returns to position 1 only after `M_b − 1` further
  shifts.
- At most `K − 1` gadgets follow, each shifting at most once.
- After PREP(ℓ), the coin is at `M_b`, so the next MEAS uses a fresh bit. This repairs r1's gap.

**Ready count `M_r > 4K`: sufficient [RW].**
- After a PREP, its four used cells sit at positions `M_r − 3 … M_r`.
- The cell at `M_r − 3` reaches the working window, positions 1–4, after `M_r − 7` shifts.
- At most `K − 2` intermediate PREPs come before any later PREP starts, so the shifts number at
  most `4(K − 2)`.
- `4(K − 2) ≤ M_r − 8` holds exactly when `M_r ≥ 4K`. The fresh-supply requirement also gives
  `M_r ≥ 4K`.
- **N3a (nit).** The justification "an information-bearing cell returns to position 1 only after
  `M_r` shifts" (r2:343–344, 357–358) is inaccurate. Cells taken from positions 2–4 pass through
  position 1 inside `ROT_r⁴`, and they re-enter the window after `M_r − 7` to `M_r − 4` further
  shifts. State the window argument above instead. The bound itself stands.
- **N3b (nit).** The record cells need at least `K` blanks. State it alongside `M_b` and `M_r`.

**C-PM′ is not fully physical as built (N3c, nit).** PREP moves the `p` and `ℓ` cells out of reach.
Two kinds of held cell are left behind.

1. **Gadget-selector cells.** These are the setting cells that make `Φ` run PREP(ℓ) rather than
   PREP(p_x, p_y), and they stay held.
   - Claim 1 is unaffected: A and B use the same selector.
   - Claim 2 step 3 compares PREP(A) with a coin mixture of PREP(0,0) and PREP(1,1). These use
     different selectors, so reading the selector cell distinguishes them.
2. **The explicit mixture's coin.** Its location is unspecified. If the coin is any held cell other
   than the `p` cells themselves, it remains readable.

So "𝔊_K uses C-PM′, so it needs no convention" (r2:105) overstates. **Required:** either
- add the selector and coin cells to the swapped-out set and recount `M_r`, or
- state that Claim 2 step 3 uses C-PM (the convention) for selector and coin cells.

Either way the 𝔊_K verdict ("YES per bounded horizon, non-discriminating") is unchanged.

**Claim 2 credit.** The credit to AP1 Lemma 4′ (AP1:698–712) is accurate.
- Lemma 4′ bounds the average signed `P + V` by 1 under an *equality of laws*.
- 𝔊_K's sharp point preparations reach 2 under a certified operational equivalence.
- AP1:714–729 is the matching scope caveat.

### 5. Conditional native-affine NO and Corollary E1

**Verdict N2.4 (r2:473–483), §0.6 (r2:63–65), §4 row (r2:659) and §5 (r2:725–726): correctly
conditional.**
- They carry (H1), H-AR, (H3), (H4), (SP) and (xiv).
- The phrase "narrowed, not closed" is used consistently.
- **N7a (nit).** §0.6 lists "four conditions" and leaves (H3), no supplied control, implicit. Name it.

**Corollary E1 (r2:500–512) is vacuous as worded (N4).**
- **The issue.** Under (H1) and (H3) there is no non-translational setting dependence: Theorem E(a)
  rules it out. So "under (H1), …, (H3) … a G3 escape needs a non-translational setting
  dependence" is vacuous as stated.
- **The intended content [RW]** is the contrapositive of (b). Keep H-AR, (H4), (SP) and (xiv). Then
  a G3 escape requires leaving "settings act on the joint record by translation", that is, leaving
  (H1)∧(H3) through MP-1 or supplied P3/E-iso.
- **A useful generalization [RW].** (b)'s model uses only `Z = Z₀(ω) + h(c)` with `Z₀`
  setting-independent. So the contrapositive holds for any rule in which settings translate the
  joint record, affine or not.
- **Required.** Restate E1 in that form.
- **The three exits listed are correct:** non-additive observers, non-nested reads, and non-spanning
  preparations.
- **Optional addition.** Failure of (xiv) yields preparation correlation, not control (D7).

**Relation to OA-1:515.** The necessity-versus-insufficiency reconciliation (r2:505–508) is
accurate.

### 6. The next-step-2 spec and its controls (r2:688–704)

The spec is much improved: μ, horizon, the label convention, two record variants, a positive
control, and the void-if-(SP)-fails rule for `N₁`. N5 lists what is still needed before it can be a
preregistration. It needs separate owner authorization in any case.

- **(a) Per-object partitions.** "`V` = setting and record cells; the carrier and conveyors in `H`"
  describes 𝔊_K. `N₁` and `G_SM` (`L = 5`) have no designed setting or record cells. State which
  ring sites are `V`, which are settings, which are ready cells, and how a herald is recorded, for
  each object. "Gadget budget" has no meaning for `N₁` or `G_SM`; use a tick horizon there.
- **(b) Non-vacuity of the negative control.**
  - The concern: under μ-G, `N₁`'s fragment could be trivially embeddable, for example if equal-time
    blindness (OA-1 D2) collapses `E` to a point or a segment. A vacuous control is invalid under
    the Code Review Rules.
  - The fix: preregister a non-triviality check, for example at least two operationally distinct
    reachable classes and at least two non-equivalent reads, before the control can count as green.
- **(c) Controls for variant (ii).**
  - The gap: "held = present `V`" has only the prediction-free `N₁` measurement. A non-embeddable
    result there would bear on AW-OA2-4 with no control that validates the variant-(ii) pipeline.
  - The fix: run 𝔊_K in both variants as the positive control. Add a variant-(ii) negative control
    whose classicality is proved independently, for example a single cell with complete reads and
    `W = ℝ^U`.
- **(d) Decision rule.** State in advance what a non-embeddable `G_SM` result would and would not
  establish. It would bear on G3 at the stated horizon and convention only. It would not bear on
  non-import (d)4 or on unbounded horizons (AW-OA2-2).

The exact-rational LP requirement is correctly kept.

***

## Other checks (F-by-F)

- **F1.** Applied, apart from N1 and N2.
- **F2.** Applied (§3 above).
- **F3.** Applied. The §3.3 measure table is accurate, and the (xiv) rows match OA-1 §2A.
- **F4.** Applied, apart from N3.
- **F5.** Applied: ELABORATING, credits, and a tally of 0 NEW.
- **F6.** Applied, apart from N4.
- **F7.** Applied. §1.5's quotations of Main:260 and :650 check out.
- **F8.** Applied. The patched step 3 is correct:
  - `π_E(conv E) = conv E`, so `π_E(K) = K` by continuity;
  - `K` is a convex body in `aff(E)`, so `|det| = 1`.
  The AP1 §5.3 credit and the Main:558 relation are correct.
- **F9.** Applied. The wording on lumpability, on heralds as a countable infinite-order family, on
  H-LIFT in E(c), on CentralObservation as context, on "complements", and on the bounded-horizon
  scope is all correct.
- **Item 8.** Next step 1 now has (a) the gbit shape, (b) the dual shape and (c) the affine attempt
  without (H4). **Correct.**
- **Item 9.** The overreach is removed.

**Nits on citations and scope (N7).**
- **(b) Line range.** r2:439 cites "MECH-1:404–422" for Lemma A. Lemma A is MECH-1:404–418. My r1
  review had the same slip, since corrected. The status table (r2:715) is right.
- **(c) TUNE-1 is now on `main`.** It is at `reconstruction/drafts/tune-1-20261111/` (#1237,
  `c03a576`). Lemma A-T gives coset-uniform record laws and the coset dichotomy
  (`TUNE-1-STEP2-SESSION3.md`:56–98). Credit it beside obsmu Proposition C as research-draft prior
  art for Theorem E's coset structure, and update "Not read: TUNE-1" (r2:808). No verdict depends
  on it.
- **(d) Snapshot line.** Update r2:20 to `615cc119`; nothing it cites changed.

## Required nits (summary)

1. **N1.** Give Proposition B(ii)'s (⇒) the convex-split proof, or display it one way only. Fix the
   Limits line.
2. **N2.** Drop transformation noncontextuality from E(b) step 5, or verify B(iii) in the `Z₀`
   model. Say that G3 here is prepare–measure.
3. **N3.**
   - Swap the selector and coin cells out of reach and recount, or invoke C-PM for them in Claim 2
     step 3.
   - Fix the "returns to position 1" justification; the `M_r > 4K` bound itself holds.
   - State at least `K` blanks.
4. **N4.** Restate Corollary E1 as the contrapositive of (b): settings that translate the joint
   record.
5. **N5.** In next step 2: per-object partitions and a tick horizon; a non-vacuity check for `N₁`;
   controls for variant (ii); a preregistered bearing of a `G_SM` result.
6. **N6.** Make the class-N preparation-side argument general in `q`, or restrict it to `q = 2`.
7. **N7.** Name (H3) in §0.6. Change MECH-1:404–422 to :404–418. Credit TUNE-1 Lemma A-T, now on
   `main`. Update the snapshot.

## What OA-2 r2 establishes, and at which layer

Everything below is paper level. The items are hand derivations, [W] and [RW], unreviewed beyond
this check. None is kernel-checked and none is adopted.

**General results**
- On fixed-lift (or lumpable) record laws, operations are stochastic, and the reversible ones are
  permutations.
- On the operational class E3, induced operations are well defined.
- At fixed finite `S`, reversible trace-preserving emergent operations form a finite group, for every
  rule, measure and interface.
- G3 needs either preparation or effect equivalences coarser than ontic equality. This is the
  M-INACC rationale made frame-free, and it can be met with `R` injective.
- A designed reversible classical computer realizes an exact, preparation-contextual gbit at every
  bounded horizon. So G0–G3 do not discriminate classical from quantum dynamics at bounded horizon.

**Gauge-derived affine class**
- Settings translate records, which restates MECH-1 Lemma A.
- At `q = 2` with parity outcomes and (xiv), CHSH ≤ 2.
- The emergent theory is simplex-embeddable under H-AR, nested records, spanning and (xiv).
  Otherwise the question is narrowed, not closed (AW-OA2-1, AW-OA2-4, dual route).

**Open**
- Admissible non-affine rules such as `G_SM`.

**No manuscript claim is affected, and nothing is NEW.**
