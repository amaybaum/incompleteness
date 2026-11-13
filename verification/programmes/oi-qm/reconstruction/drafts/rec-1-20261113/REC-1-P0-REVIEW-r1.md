# Independent review of REC-1 P0 (record `REC-1-P0.md`, writer's outcome PASS)

**Reviewer.** Fresh, non-author. Read-only, hand reasoning only. No computation on any OI rule, no
commit, push or post. Sources fetched by name and read with `git show`, not taken from `src/`.

**Verdict: REVISE.** The PASS does not stand. The overall P0 outcome under r7's rule is
**Unresolved (O-U)** for OBL-SP's class. There is a **scoped classical sub-result** for an exactly
stated subclass (LF, §4). The ordering-rule hand-off to AW-OA2-1 does not fire.

Coordinator's disposition table: row (b) applies to the LF subclass, which gets a scoped classical
result while the original OBL-SP stays open. Row (d), O-U, applies to the rest of the class.
- Row (a) fails: the proof does not cover the class (§3).
- Row (c) fails: no counterexample satisfying every r7 hypothesis is exhibited, because the one
  exhibited below fails the rule class R-lin with (xiii).

***

## 0. Pins and verbatim check

- `origin/research/rec-1-1169-20261113` = `9f7d2612f39960a41188eae8f3753d9def8019e8`. `REC-1-r7.md`
  blob `f1ffac0e` (454 lines).
- At `c3b5f37a`: OA3 `0a36fd05`, OA2 `8f8ddf73`, OA1 `5a16b213` and S3 `a9cbc675` all match the
  record's pins. The writer's `src/` copies are byte-identical to `git show` output.
- **Verbatim.** The record's quotations of P0 (r7:317–338), P4 (r7:349–357) and the ordering rule
  (r7:303–311) were diffed against r7 and match exactly. They are quoted in §1, before any
  derivation. The classifier in §2.2 adds nothing to P0's pass conditions, so the rule is applied
  unchanged. Every line citation spot-checked is correct: r7:251–264, :287–290, :328–332,
  :362–366; OA3:101–102, :120–123, :410–416, :474–475; OA2:105–106, :114–115, :502, :525–534;
  OA1:131; S3:50–54, :69–70, :196–207.

## 1. Ruling on the N3 reading (question 1, scope)

**(a) What the class clause fixes.** The clause is "records as in (H4) or in the (V-ii-H) effect
class (OA3:460–476), heralds typed as held at use with records formed inside `S`". Read with the
definitions it cites, it does entail full retention for every instance that meets it, and the
retention is accessibility at the required time, not just "recorded somewhere in `S`":
- (H4) is OA2:502: "the held record at the latest read determines every earlier available read".
- (V-ii-H) is OA3:120–123: heralded composites are available, with no qualifier. Single-tick
  heralds are always admitted procedures. Under the typing, the composite `[Z_{τ₁}=r]·1` is
  available only if `{Z_{τ₁}=r}` is a function of the present `V(τ)` (OA1:131; "held" = a function
  of present `V`, OA3:100). OA3:474–475 states this consequence ("retention-type").

So the writer's R4 and N3 are a literal reading of the clause, not a strengthening of r7's wording.

**(b) r7 is internally inconsistent on this point, and the record must say so.** Three passages
place heralds that cannot be composed inside OBL-SP's own content:
- r7:287–290 lists them in "OBL-SP's open content".
- r7:299–300 calls the herald-retention residual "a subset of OBL-SP's own preparations".
- r7:320–321, P0 itself: "such as heralds that cannot be composed under the fixed typing".

Under the clause, that set is empty by definition. N7 resolves the conflict silently, in the
direction that favours the writer's outcome ("outside the class, not an out-of-form preparation of
it"). Under §A.29 and §A.31, and under the owner's mixed-case safeguard, an executor may not settle
a preregistration ambiguity this way. The record must:
- name the conflict;
- report what each reading gives;
- leave the reading to the owner.

**(c) The reading is not decisive, for two reasons.**
- **The preparation side needs no retention [reviewer, W].** Every admitted preparation herald
  ends at the common use time `t_p` (§2.1). So every admitted herald event is a function of
  `V(t_p)`, and heralding on `V(t_p)` itself (a present read, so always held) is the finest
  admitted herald. Admitted heralds are closed under conjunction at `t_p`. C1 and C2 therefore hold
  with `L* = K ∩ ker G_{V(t_p)}` for every H-AR observer, retaining or not.
  - The composability in N3 is therefore not where the class boundary works. The diagnosis in
    N8.1 and AW-P0-1 ("composability is supplied by the record hypothesis") misplaces the
    boundary.
- **The decisive step is N5 (C3), and it fails under the narrow reading too (§3).**

**(d) Under the broader reading, does the sketch in N8.2 succeed?** Not as an in-class
counterexample under either reading: its rule is not R-lin with (xiii), as the writer says. But it
needs no broader reading. A variant that keeps the conveyor inside `V` meets (H4) literally (§3).

## 2. Witness components re-derived (question 2)

- **N1 (law form).** Correct. Affine reads (R1); conditioning a coset-uniform law on an affine
  event gives a coset-uniform law (R2). Mixtures and coins are fine.
- **N2.** Correct and important: C1 is vacuous, since `S = {0}` always works. Nothing in the pass
  leans on C1 alone.
- **N3.** Correct as a literal reading (§1a). Composability is supplied by the hypothesis, not
  derived from φ or `D_0`. The record says so in N3, N8.1 and §7, and it is carried into the
  conclusion. As noted in §1c, it is also not needed.
- **N4 (C2).** Correct. Fibres of `G_{J*}` on `r_p + K` have positive probability, and heralding
  on them reaches every `S*`-coset.
- **N5 (C3). Not established; the step is false in the generality in which it is argued.** The
  bullet "By the record hypothesis … the measurement-stage reads are jointly held at the latest
  read, in cells the effects may read" is asserted without proof. The record hypothesis gives joint
  holding in `V(T)`. It does not give joint holding in cells that hold no preparation-stage record.
  Yet N5's own first bullet makes all such cells labels, excluded from the common effect set by
  C-PM. When the retention of measurement-stage values runs through herald-record cells, the
  coset indicator is not a C-PM effect. §3 gives an explicit instance.
  - N8.3's claim that "the verdict does not depend on how label cells are delimited" fails for
    the same reason. With `Z_e` the label-free part of `V(T)`, single-tick reads at earlier
    measurement ticks are available effects but are not functions of `Z_e`.
- **N6 (C4 and the model).** Given C3, this is correct:
  - preparation noncontextuality from C3;
  - measurement noncontextuality from the reachable vertices `u_{t+S*}` (C2), which is a sound
    use of C2;
  - the equivalence tests follow.

  Without C3, the model still reproduces the statistics and is still measurement-noncontextual,
  but preparation noncontextuality fails. That is exactly the gbit failure.

## 3. The decisive countercontrol (§A.21, §A.31) [reviewer, W, hand]

This is a ring-conveyor version of the writer's own N8.2, keeping the record inside `V`. It works
over `ℤ/q`; `q = 2` suffices.

**Cells.**
- A 3-cycle `(s0, s1, s2)` with `s_i(t+1) = s_{i−1}(t)`, which is N4.2's shift.
- A ring `r_0 … r_L` with `r_j(t+1) = r_{j−1}(t)` for `j ≥ 1` and `r_0(t+1) = r_L(t) + s0(t)`.

This is a block-triangular additive bijection, so (H1) holds.

**Observer and law.**
- `V = {s0, r_0, …, r_N}` with `N ≥ 6`; the remaining ring cells, the feeder, are in `H`. This is
  H-AR.
- Designated cells: `s0(0) = 0`, all `r_0 … r_N` at 0, and the three feeder cells that enter
  `r_0` at ticks 1, 2 and 3 at 0.
- Uniform cells: `s2 = x`, `s1 = y`, and every other feeder cell. Call `u` and `u′` the ones that
  enter at ticks 4 and 5.

This law is in `D_0`.

**Records.**
- `s0(t)` runs `0, x, y, 0, x, y` for `t = 0 … 5`.
- `r_0(t)` runs `0, 0, x, y, u, u′+x`.
- Take `t_p = 3` and `T = 5`. At tick 5, `r_1 = u`, `r_2 = y` and `r_3 = x`.

**The hypotheses hold.**
- *Typing.* The herald on `(V(1), V(2)) = (x, y)` is held at `t_p` in `r_1(3) = x` and
  `r_0(3) = y`, records formed inside `S`. The four point preparations `[ab]` are admitted.
- *(H4).* `V(5)` determines every `V(τ)` with `τ ≤ 5`. The values of `s0` lie in `{0, x, y}`, and
  the earlier ring contents are back-shifts of the ring with known front entries `0, 0, x, y, u`.
- *C-PM.* The labels are the cells that hold the herald records `x` and `y`.
- *H-xiv.* There is no setting.
- *(H3).* There is no supplied control.
- *Horizon.* It is finite.

**The fragment is preparation-contextual.**
- Label-free effects:
  - at tick 4 they read `(x, u)`;
  - at tick 5 they read `(y, u′+x, u)`;
  - the only tick-4 event that is still label-free-held at tick 5 is a function of `u`.
- Under these effects `½([00]+[11]) ∼ ½([01]+[10])`, because `u` and `u′` are uniform and
  independent and `u′` is in `H` until tick 5.
- `X = s0(4)` and `Y = s0(5)` are sharp on `[ab]`.
- R7 (OA2 Claim 2) then shows that no preparation-noncontextual model exists. This is a gbit.
- Raw (SP) fails, since `u` and `u′` are never reachable as point laws.

**Applied verbatim, the record's N1–N6 would certify this fragment.**
- `J*` is admitted.
- `S*` is the span of the `u` and `u′` directions.
- C1 and C2 hold.
- N5 asserts that `1[(x,y) = (a,b)]` is available, which is false here.

**Its only failed hypothesis is the rule class:** the rule is not R-lin with (xiii). N1–N6 use
nothing about R-lin beyond affinity (R1). So the argument as written is invalid. For R-lin with
(xiii), whether retention can be carried only through label cells is **unestablished**: it is
neither excluded by any step of the record nor realized here.

The record's statement in N8.2 that the recorder "fails (H4) and fails (V-ii-H)" is wrong for this
version: measurement-stage values remain held through the herald register. The exclusion of
N4.2's shape from the class therefore does not rest on the record hypothesis. It rests on the rule
class alone, which no step of the record uses.

**Cross-propagation (assumption-watch candidate, record-only).** OA-2 Theorem E(b) step 4
(OA2:534) and OA-3 N4.3 step 4 (OA3:468–469) take singleton indicators to be available under C-PM.
That presumes retention free of labels. The instance above has (SP) failing, so it does not refute
E(b). The presumption should still carry a marker.

## 4. The scoped sub-result that does hold [W, P0 plus a reviewer hand check; not established, §A.46 item 7]

**(LF).** The measurement-stage reads (ticks in `(t_p, T]`) are jointly held at `T` by cells of
`V` that hold no preparation-stage record. The common effect record `Z_e` is that label-free part
of `V(T)`.

For every instance of r7's OBL-SP class (literal clause) that also satisfies (LF), C1 to C4 hold
with `S* = H_e(K ∩ ker G_{J*})`. The argument is N1, N4 and N6 with `H` replaced by `H_e`; C3 now
holds because coset indicators are post-processings of `Z_e`. The coset-space model is then a
simplex embedding of the C-PM prepare–measure fragment. The scope is:
- under (H3), the record class, held-at-use typing with records inside `S`, C-PM, H-xiv, `D_0`
  and (LF);
- one direction only;
- transformation noncontextuality not claimed.

(LF) is an added condition, not one of r7's hypotheses, so this result does not close OBL-SP.
Instances I and II each have a single measurement tick and satisfy (LF), so the sub-result is
non-vacuous.

## 5. Controls (question 3)

| Control | Review |
|---|---|
| (i) | Green. Under (SP), `S* = {0}` and the result agrees with E(b). It inherits E(b)'s indicator assumption (§3, cross-propagation). |
| (ii) | Green and non-vacuous. Hand-checked: C1 holds only with `S = {0}`, where C2 fails (no point law is reachable). The non-simplex classification comes from R6, the supplied counterexample, which r7:335–337 permits. |
| (iii) | Green for the cited artefact: plain N4.2 needs `V(1)` and `V(2)` held at `t_h`, which they are not (OA3:410–413), so the typing excludes it. **The mechanism stated for the variant is inaccurate**: the ring-conveyor recorder meets (H4) and is excluded only by the rule class (§3). Neither the typing nor the record hypothesis excludes N4.2's shape once a register made of `D_0` blanks is inside `V`. |
| (iv) | Green. `𝔊_K` fails C3 (OA2:466–467), and R7 shows contextuality. Non-vacuous. |
| (v) | Green. Recomputed by hand: Instance I gives `V(1) = (u+c−p, u+c)` and `Z₀` uniform on `(−p, 0) + Δ`; Instance II gives `V(1) = (w, u, w+c)`. Both meet H-xiv and the nontrivial-fragment condition, Instance II has its record inside `S`, and both have raw (SP) failing (`dim W = q < q²`). Instance II's nontriviality depends on cell-based delimitation, since `x₁(1) = w + c` carries the herald value. Instance I alone suffices. Both have one measurement tick, so neither exercises C3's general step. |
| (vi) | Green. The O-Q multiplexing fragment is correct. For O-SQ: `Tr(Eρ) = 1` puts `ρ` in the eigenvalue-1 eigenspace `P`, and `Tr(Eρ) = 0` puts it in `ker E ⊆ P^⊥`. Compressing by `P` turns the P2 equality `ρ₀₀+ρ₁₁ = ρ₀₁+ρ₁₀` into `ρ₀₀ = ρ₀₁`, against `Y`. Correct and dimension-free. |

All six controls are green. They were not designed to exercise C3 with several measurement ticks,
and the countercontrol in §3 shows that is where the derivation breaks.

## 6. Scope (question 4) and ordering rule (question 5)

**Scope.** §7 of the record states that the result is conditional on:
- H-xiv;
- the herald typing;
- H-AR;
- (H3);
- C-PM;
- `D_0`;
- the record hypothesis.

It is one direction only, which is correct under §A.34. It lists these exclusions:
- non-additive observers (AW-OA2-1);
- laws outside `D_0`, including μ-O and μ-R;
- procedures for which H-xiv fails;
- other typings (C7);
- non-retaining observers (C6);
- non-affine rules (C2);
- unbounded horizons;
- transformation noncontextuality.

Nothing is stated OI-wide. Three statements overclaim given §3 and must go or be narrowed:
- "No content of OBL-SP remains open within its class".
- The §7 restatement of r7:362–366's O-C bearing as holding.
- N6's "re-derives S3:206–207's statement for the C-PM fragment of this class", which must be
  narrowed to (LF).

**Ordering rule.** The record draws the consequence correctly given a PASS, but the PASS fails.
Under r7:309–311 ("If the coset form holds but an operational check fails or is unestablished, the
outcome is O-U (P0), and Q4 is not handed to AW-OA2-1 on that basis"), the hand-off is withdrawn.

## 7. Required changes

1. **§6.** Replace the heading "**PASS.**" and the text from "For every instance of the class …"
   through "… the prepare–measure fragment is simplex-embeddable for every instance of the class."
   with:

   > **Unresolved (O-U), with a scoped pass.** C1 and C2 hold for every instance of the class
   > (N1, N4). C3 is established only under (LF): the measurement-stage reads are jointly held at
   > `T` by cells holding no preparation-stage record. Under (LF), C1–C4 and the simplex embedding
   > hold (N5, N6). Without (LF), C3 is unestablished. An affine instance meeting every hypothesis
   > except R-lin with (xiii) is preparation-contextual (N8.2), and no step uses R-lin beyond
   > affinity. Under r7:335–338 the outcome is O-U. No in-class contextual counterexample is
   > supplied.

   Replace "The mixed case of the safeguard does not arise." with:

   > Mixed case (safeguard): the in-form instances that satisfy (LF) pass. The C3 check is
   > unestablished for the rest. The anticipated non-composable heralds (r7:287–290, :299–300,
   > :320–321) are excluded by the class clause read literally, and that reading conflicts with
   > those passages; the owner fixes the reading.

2. **N5.** Replace "By the record hypothesis (N3), the measurement-stage reads are jointly held at
   the latest read, in cells the effects may read." with:

   > The record hypothesis gives joint holding in `V(T)`, not in cells free of labels. C3 is
   > established under (LF); without it, C3 is unestablished (N8.2).

   Delete "The witness does not depend on how label cells are delimited" in N5. In N8.3, delete
   "so the verdict does not depend on how cells carrying retained herald content are delimited".

3. **N8.2 and control (iii).**
   - Replace the sketch's conclusion "The instance fails (H4) and fails (V-ii-H) under the
     typing, so it is outside the class … rests on the record hypothesis, not on the herald
     typing alone" with the §3 instance and its verdict: (H4) holds, the fragment is a
     preparation-contextual gbit, and it is excluded only by the rule class.
   - In control (iii), replace "The recorder variant (N8.2) re-admits them with records inside
     `S` but fails the record hypothesis" with "The recorder variant (N8.2) re-admits them with
     records inside `S` and meets (H4); it is excluded only by the rule class (not R-lin)".

4. **N3, N8.1, AW-P0-1.**
   - State that composability at the common `t_p` needs no retention (§1c).
   - Restate AW-P0-1 as: "Under C-PM, retention held in herald-label cells does not give
     label-free joint accessibility. For additive bijections, a gbit meets every OBL-SP
     hypothesis except R-lin with (xiii). Applies to AW-OA2-1, to E(b) step 4 and to N4.3 step 4."
   - Delete the clause in AW-P0-1 about relaxation to "composites as far as the typing admits".

5. **N7.** Replace "Within the class, none." with "Within the class read literally, none. r7's
   anticipated residual (r7:287–290, :299–300, :320–321) is empty under that reading, which
   conflicts with those passages (§6)."

6. **§7.**
   - Delete "No content of OBL-SP remains open within its class."
   - Restate the bearing as conditional on (LF).
   - Replace the ordering paragraph with "P0 is O-U; under r7:309–311 Q4 is not handed to
     AW-OA2-1 on that basis. The next decisive step is C3 for R-lin with (xiii): realize or
     exclude retention carried only through label cells."
   - Narrow N6's S3 sentence to (LF).

7. **N8 classification.** Add the §3 finding as NEW (it is against the favourable branch).
   Reclassify N3's composability as POSITIVE: the preparation side needs no retention.

The decision rule and the class are off `main` (r7 at `9f7d2612`). The record flags this correctly
as an item-8 gap (§A.42 item 8); it is unchanged by this review.
