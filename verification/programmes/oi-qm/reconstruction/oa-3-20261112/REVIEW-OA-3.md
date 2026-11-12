# Independent review of OA-3 (`OA-3-REPORT.md`)

**Reviewer standing.** Independent reviewer. Read-only and paper-only: no computation, no script, no
commit, no push, no GitHub write. Sources were read with `git show` at the report's pins: `main`
`615cc119` and research branch `research/oa1-w1-1-20261112` at `815d6a8e` (`FETCH_HEAD`).
`origin/main` is now `fba459cb`. Under `papers/` and `verification/programmes/oi-qm/`,
`git diff 615cc119 fba459cb` touches only `papers/Main.md` (6 lines replaced) and `papers/SM.md`
(2 lines replaced). Neither touches SM §3.1 (SM:100–169) or any Main line OA-3 relies on, and line
numbers are unchanged. The pin is current for everything cited. No source copy was written.

**Authorization.** As the coordinator relayed it: owner amaybaum, 2026-11-12, #1169
c.6833027576, a paper-only OA-3. I did not re-fetch it. OA-3 stays inside that scope: no
computation, no Lean, no manuscript change, no premise adopted. Its §4 amendments are proposals
for owner authorization only.

**Citation form.** `R:n` = line `n` of `OA-3-REPORT.md`. Every other abbreviation is as R:19–24:
`OA2` = OA-2 r3, `Rv2` = `REVIEW-OA-2.md`, `OA1` = OA-1 r4, `M2` = MECH-2 `DESIGN.md`, and `MA`/`MAR`
= minacc-1 `DESIGN.md`/`RESULT.md`. `[RW]` marks a derivation I redid by hand (unreviewed).

## Verdict: **ACCEPT WITH CHANGES**

The four derivations are correct as mathematics, and I redid each of them by hand: the
gate-cancellation transfer, Lemma OBS, Theorem S's proof step, and the shift counterexample with
the variant-(ii) heralded-composite (V-ii-H) argument. No finding refutes a stated result. Several
findings change scope, framing or classification:

- Theorem S's hypothesis list omits the record convention its effect side needs.
- Its measure restriction is justified by a reason the proof does not use.
- N4 places OA-2's defect in the wrong sentence.
- N4 leaves the typing of heralds open.
- Two statements overreach their proved scope: the class-N "exists only under P2" sentence and the
  M-INACC sentence in AW-OA3-1.
- The NEW tally should be two, not three.

***

## Findings

### F1 (N1.2): the gate-cancellation transfer is correct, and it answers an open item in M2

**Redone [RW].** At `q = 2`, `f_i = u_{i−1} ⊕ OR(u_{i+1}, u_{i+2})` (M2:157–164; SM:112, where
`L(i) = i − 1` is fixed with coefficient 1). Supplies as R:110–111.

| Step | Value |
|---|---|
| Tick 1, reader | `u_1(1) = 0 ⊕ x ⊕ OR(1, u_3) = x ⊕ 1` |
| Tick 1, target | `u_0(1) = y ⊕ 0 ⊕ OR(α, 1) = y ⊕ 1`, `v_0(1) = x` |
| Refill | cells −1, 1, 2 |
| Tick 2, reader | `u_1(2) = 0 ⊕ (y ⊕ 1) ⊕ OR(1, ·) = y` |
| Tick 2, target | `u_0(2) = x ⊕ 0 ⊕ OR(α₂, 1) = x ⊕ 1`, `v_0(2) = y ⊕ 1` |

So cell 0 is sharp at `(r_1, r_2 ⊕ 1)`. The determination is pointwise, so it holds for every
full-support prior, as MAR:254–255. The schedule needs only `L ≥ 4`: at `L = 4`, site 3 is site −1,
and `OR(1, ·)` still absorbs it. The control `R ≡ i+1` gives `u_0(1) = y ⊕ α`, which is masked ✓.
This is the mirror image of MAR:222–256, with the reader moved to the gated (right) side.

**Required.**

1. **M2's open item.** M2:857–859 states for `G_SM`: "Whether the protection fails under P1 and
   P2 is open." `E_A^SM` answers it at [W] level: it fails, under P1, P2 and H-PREP's known-1
   supply. Say so, cite M2:857–859, and classify N1.2 ELABORATING (a direct transfer that settles a
   recorded open item), not CONFIRMING only (R:141, R:447).
2. **The `R ≡ i+2` limit (R:122–126).** The claim is right: cell 1 does not enter `f_0`, so there
   is no kick. But under that limit the reader's update is `f_1 = u_0 ⊕ u_3`, so with cell 3
   "arbitrary" (R:111) the register is `x ⊕ u_3`, not `x ⊕ 1`. Exposure needs cell 3 supplied
   known, which is a P2 cell. I redid this: with `u_3 = 0` known, it exposes `(x ⊕ c′, y ⊕ c)` at
   `t = 2`. State the changed supply.

### F2 (N1.3 and R:34): "exists only under P2" overreaches

- **What is right.** OA2:632–633 itself lists the premises of the class-N single-cell result as
  "Lemma Q(iii) under P1–P2". In E3 an H-AR observer's own cells are held, so a held reader's kick
  is a known translation.
- **What is not shown.** That the class-N restriction "exists only under the supplied
  half-known-reader convention" (R:34), and that it is "not a property of the rule" (R:135).
  - In E3 an unknown disturbance can come from hidden cells that neighbour the carrier, under the
    stated μ. OA-3 says so itself (R:349–350).
  - Lemma OBS removes every restriction only for observers holding a block of 2 sites (class N) or
    3 sites (`G_SM`), over long horizons.
  - For a one-cell class-N observer, `(★)` yields only `x_{a−1} + x_{a+1}`, so whether a native
    restriction exists there is not decided.

**Required.** Narrow R:34 and R:133–135 as follows. *Lemma Q's reader-kick mechanism needs readers
with an unknown slot (P2, with P1). A held E3 reader has none. Whether hidden-cell noise yields a
native restriction for observers below Lemma OBS's block size is open (N5).* With that change, N1.3
is CONFIRMING of OA2:632–633.

### F3 (Lemma OBS): the proof is correct, but the generality clause, the NEW label and AW-OA3-1 need repair

**Redone [RW].** SM:112 gives `x_j(t+1) = x_{j−1}(t) + x_{R(j,x(t))}(t) − x_j(t−1)`. `R(j, ·)` and
`x_R` depend only on `x_{j+1}` and `x_{j+2}`, so `(★)` is exact for every `q` and either sign.

- **Induction.** `D_k ⊇ [k−1, T−k]` holds by induction. The step for `D_k` needs `D_{k−1}` at
  `t ± 1` and `D_{k−2}`, `D_{k−3}` at `t`, all of which hold.
- **Pairs.** Site `a−k`'s pair is known on `[k, T−k]`. The common time is `t* = L − 3` when
  `T ≥ 2(L−3)` ✓.
- **Part (ii).** `D_1 = [2, T_M−1]`, so pairs are known on `[k+2, T_M−k]`, and the common time
  exists when `T_M ≥ 2(L−2)` ✓.
- **Hand checks.** `L = 4` and `L = 5` (common time 2 at `T = 4`) ✓.
- **Bijectivity premise.** It matches SM:112: the left neighbour is fixed with coefficient +1, and
  the right side is the only gated term. `G_σ` (MAR:36–40) is permutive in no argument ✓.

**Required.**

1. **Generality (R:182–184) and AW-OA3-1 (R:452–455).** "Bijective in `x_{j−1}` given the
   right-hand arguments" silently assumes that the update depends on the left only through
   `x_{j−1}`. Suppose a rule also reads `x_{j−2}`, as with left reach `l > 1`. Then `(★)` at `j`
   needs `x_{j−2}`, and the leftward induction stalls unless the **extreme** left argument
   `x_{j−l}` is the permutive one. In that case the held block must have width `l + r`, not
   `r + 1`. State the condition as "permutive in its extreme left (or right) argument; held block
   of width `l + r`". This reduces to `r + 1` when `l = 1`.
2. **NEW label (R:442–444).** Under `[L]`, add the standard prior art: for permutive cellular
   automata, a vertical strip of width equal to the radius determines the space-time diagram on
   the permutive side (Hedlund 1969, and the expansive-CA literature). This is the same argument.
   - Within the corpus I found no statement of the lemma. I checked SM:112's visible-sector
     remark, L3b (`preregistration.md`:65–66, :99–109; `result.md`:51–53), obsmu, PI
     (`oi-qm-ext-1/physical-interface.md`), MECH-1 (:877–891, :1023–1028), minacc-1 and the TUNE-1
     drafts.
   - For class N (affine), the conclusion is an instance of obsmu Proposition C's coset structure
     (obsmu:546–578; determination iff the relevant kernel is trivial), though obsmu does not
     compute that kernel for the ring.
   - So NEW stands only as a corpus-level structural finding: an ungated permutive edge is a
     native return path, which the OA-2 design and the M-INACC framing did not register. Label it
     that way.
3. **AW-OA3-1's M-INACC sentence (R:454).** "M-INACC therefore needs every return path gateable"
   transfers Lemma OBS outside its class. Lemma OBS holds only under all of the following:
   - a finite ring;
   - an H-AR observer holding the block;
   - MP-0b history or V-ii-H effects;
   - horizons of about `2L` or more.

   M-INACC (M2:832–871) is stated under P1/P2 registration. The open escape on `main` is M-INACC on
   **growing** carriers (OA1:573–574), where Lemma OBS determines only hidden sites at depth up to
   about `T/2` (R:242–245). Restate it as follows. *For observers in Lemma OBS's class, on a finite
   ring at horizons of order `L`, M-INACC needs no permutive extreme edge on either side. Growing
   carriers and short horizons are untouched.*

### F4 (Theorem S): the proof is correct but immediate; fix the hypothesis list, the citation and the measure scope; reclassify

**Redone [RW].**

- **Point preparations.** The herald on `[0, T₁]` with `V(0)` determines `ω(T₁)`, by Lemma OBS(i)
  and bijectivity. Each herald value fixes one `ω`, with probability `|S|^{−1} = q^{−2L}`, which is
  OA1:152–156 with equality.
- **Effects.** The post-handoff `u`-history determines `ω(T₁)` (Lemma OBS(ii)). So every function
  on `S` is an effect, `R` is injective, `W = ℝ^S`, and `E = R(Δ(S))` is a simplex.
- **Horizon.** `2(L−3) + 2(L−2) = 4L − 10` ✓; for class N, `4L − 6` ✓.

**Required.**

1. **Hypothesis list (R:199–201).** Step 2 needs the post-handoff *history* as an effect, which
   holds under MP-0b (OA1:554–555, a granted convention) or (V-ii-H). Under (V-ii-U), the effects
   are single-tick reads of three sites, and Theorem S fails as proved. Put "MP-0b or (V-ii-H)" in
   the theorem statement, not only in §7 (R:509) and N2's verdict (R:194–195). Plain-language item
   4 (R:36) must carry it too, with "finite ring".
2. **The B(iv) citation (R:225).** Proposition B(iv) needs (i)–(iii) (OA2:248–249), and (iii) is
   not shown. Cite the prepare–measure reading instead: B(i) and B(ii) (⇐), as in Theorem E(b)
   step 5 (OA2:519–525).
3. **Measure scope (R:199, R:230–232).** The stated reasons for excluding μ-O, μ-R and MP-0a are
   "full support", "(xiv) may fail" and "not invariant". None of them is used by the proof:
   - Theorem S has no measurement setting cells. Its effects are post-processings of the history,
     so (xiv) never enters.
   - Proposition B(ii) needs only `W = ℝ^U`, with `U` the union of supports (OA2:242–243).
   - Heralding on the full history gives `δ_ω` for every `ω` in the support of the law at `T₁`,
     under any μ, MP-0a laws included and invariance not needed. So `W = ℝ^U` holds.
   - OA2:730 already types Lemma 1 and Proposition B as holding for every law.

   Either state Theorem S for every μ, as a candidate [W] strengthening with this derivation, or
   keep μ-G and delete the incorrect reasons. §A.31's skepticism applies here even though the
   strengthening widens a negative: the author should check this step and not take it from me.
4. **Classification (R:445).** Given Lemma OBS, "point preparations plus complete effects implies
   a simplex" is immediate. The content is Lemma OBS. Reclassify Theorem S from NEW to
   ELABORATING, as a corollary of Lemma OBS with D3 and Proposition B. The scope statements (R:242–
   248, R:518–519: not an impossibility for `G_SM`, `T ≪ L` open) are correct and must be kept.

### F5 (N4): the counterexample is correct; the defect is in OA-2's gap paragraph, not in its effect definition; herald typing is the open premise

**Redone [RW].**

- **N4.2.** The shift `ω(t+1)_i = ω(t)_{i−1}` on 3 cells, with `V` = cell 0, shows `p, x, y, p, …`
  at `t ≡ 0, 1, 2`. Heralding `V(1) = a` and `V(2) = b` gives the point preparations `[ab]` at
  `t_h = 3`.
  - Under (V-ii-U), `A = ½([00]+[11])` and `B = ½([01]+[10])` agree on every single-tick read.
  - OA2:427–442 applies verbatim, so the fragment is preparation-contextual.
  - The herald `V(t_h+1) = 0` maps `A` and `B` to `[00]` and `[01]`, and the read one tick later
    separates them. So Lemma 1 fails under (V-ii-U) ✓.
- **N4.3.** Under (V-ii-H) with (H1), H-AR, (H3), (xiv) and (SP) for the formal joint record:
  - every heralded composite is a function of `Z₀` after translation by `h(c)`;
  - singleton indicators come from heralds at every tick followed by a final read;
  - the proof of OA2:512–525 then goes through without (H4) ✓.
- **N4.4.** The *cones* coincide with variant (i)'s. The effect *sets* do not: a cross-tick parity
  indicator such as `[00]+[11]` is in the cone but is not one run's outcome without memory. Since
  simplex-embeddability is a condition on the cones and the unit (Schmid et al. 2021, as
  OA2:150), "same verdict" is right. Say "the cones coincide", not "the variants coincide".

**Required.**

1. **Where the defect is (R:252–260, R:446, R:457).** OA-2's own text does **not** exclude heralded
   composites:
   - Proc contains heralds (OA2:96–97);
   - Proc is closed under composition (OA2:98);
   - OA2:522–523 folds every procedure into a measurement "procedure, then read";
   - Lemma 1 (OA2:224–227) uses `e∘π`.

   The statement inconsistent with these is the gap paragraph, "only the marginals are available
   statistics" (OA2:548–551), taken from Rv2:115–122 and accepted in `REVIEW-OA-2-r2.md`:105–107.
   (V-ii-U) is OA-3's literal reading of OA2:107–108 and is legitimate as a contrast class. Reframe
   the finding as follows. *OA-2 r3's gap paragraph, and both reviews, assumed an effect class
   under which OA-2's own Lemma 1 is false (N4.2). Under the class Lemma 1 presupposes, (H4) is
   redundant for E(b) (N4.3).* Credit Rv2:134–137 as the nearest prior art; it flagged a
   closure-versus-timing tension. With that credit, NEW for N4 is justified: no source I searched
   (the OA-1 and OA-2 reports and all five reviews) notes that heralded composites supply the joint
   statistics.
2. **Herald typing (new; affects N4.2, N4.3, Theorem S and AW-OA3-2).** OA-1 types a herald event
   as "still held at use time" (N1-K, OA1:127), and complete records as "every outcome, herald and
   failure … held in `V` at the end" (N4, OA1:131).
   - If E3 heralds carry that typing, then under "held = present `V`" a multi-tick herald needs an
     MP-0b-type retention convention (OA1:554–555). This applies equally to N4.2's *preparations*
     (`V(1)`, `V(2)` are not held at `t_h`) and to N4.3's *effects*.
   - If heralds are ensemble conditionings, as OA-2 uses them, no retention is needed and (V-ii-H)
     is OA-2's own reading.

   State this dependency. Then (a) N4.2's "exit" is the asymmetric class: multi-tick heralds for
   preparations, but not for effects. R:287–290 already gives this diagnosis, so make it the
   formal statement. (b) N4.3 replaces (H4) by the effect class Lemma 1 presupposes. Under
   held-at-use-time typing that class is itself retention-type, so "without (H4)" (R:37, R:300,
   R:393) must not read as "without any retention convention". Extend AW-OA3-2 to name this typing
   question.
3. **"Rule-independent" (R:290, R:327, R:366).** The artefact needs dynamics that cycle distinct
   contents through a one-cell `V`; identity dynamics on a static `V` do not produce it. Say
   "present already for trivial dynamics (a shift)".
4. **Plain-language item 5 (R:37).** Add the conditions (H1), H-AR, (H3), (xiv) and (SP), and the
   affine-class scope.

### F6 (§4): the remaining question and the amendments

1. **Remaining question (R:396–399).** It is stated as a conjunction: no three-block **and**
   `T < 4L − 10`. The open regime is the complement of Theorem S's class, a **union**: no
   three-block, *or* `T` below the bounds, *or* infinite windows, plus μ if F4.3 is not adopted.
   As written, it omits for example:
   - a three-block with `2(L−2) ≤ T < 4L − 10`, where shape (a) is excluded but (b) is open;
   - a small observer at long `T`.

   Restate it as the union.
2. **"Decisive" (R:401).** The preregistered computation decides only its instance (`Z_5`,
   `V = {0, 1}`, `T ≤ 4`, OA2:797, :832–833). Say "decisive for that instance".
3. **Amendment 1 (R:406–412).** Sound. Correctly framed as needing owner authorization. It
   correctly replaces the "measurement without a prediction" reading. Tie it to F5.2: the
   preregistration must also fix the herald typing.
4. **Amendment 2 (R:413–415).** Sound in purpose. It needs four additions:
   - **Record variant.** State it as (i) MP-0b, or (V-ii-H) if that is implemented, never
     (V-ii-U), under which Theorem S does not apply (F4.1).
   - **Guards.** Carry the non-vacuity guard (OA2:809–811).
   - **Degenerate instance.** Note that at `L = 4` `G_SM`'s edges are reciprocal (M2:191: "At
     `L = 4`, `i + 4 = i`"), so `Z_4` tests the pipeline, not the non-reciprocal regime.
   - **Independence.** The control's "independent proof" is Theorem S at [W]. It counts as an
     independent control only once Theorem S has passed review. This review accepts its proof
     step, subject to F4.

   If F4.3's measure generalization is adopted, MP-0a ready cells as in OA2:797 are also
   admissible.
5. **Amendment 3 (R:416–417).** Sound.

### F7 (labels, markers, minor)

- **NEW tally (R:448).**
  - **Lemma OBS:** NEW, at corpus level, with the [L] caveat (F3.2).
  - **Theorem S:** ELABORATING (F4.4).
  - **N4:** NEW (F5.1).
  - **Tally:** 2 NEW, plus N1.2 ELABORATING (F1.1).
- **AW-OA3-1.** Sound after F3.1 and F3.3.
- **AW-OA3-2.** Sound. Extend it per F5.2.
- **Authorization (R:8–9).** Cite the comment id c.6833027576.
- **Reading inventory (R:490–492).** It says obsmu, MECH-1 and TUNE-1 were not read. F3.2 records
  what this review checked there. Add those sources to the §A.19 basis.
- **Register.** The report keeps to the §A.32/§A.33 register: I found no meta-commentary,
  caps emphasis or revision narration. No manuscript is touched.

***

## What OA-3 establishes, and at which layer

OA-3 establishes, as mathematical derivations on paper ([W], here re-derived by hand by the
reviewer, with no kernel check and no computation), the following:

1. **Gate cancellation.** minacc-1's gate-cancellation exposure transfers to `G_SM` under P1, P2
   and H-PREP. It thereby settles M2's open item: `G_SM` does not keep Lemma Q's protection there.
2. **Lemma OBS.** For SM's ring rule at every `q`, and for class N, the history of a block of
   width (reach + 1), with left reach 1, determines the whole configuration of a finite ring
   within a horizon of order `2L`. The statement is pointwise, so measure-free.
3. **Theorem S.** As a corollary, under MP-0b or heralded composites, with heralds and a horizon
   of at least `4L − 10`, the prepare–measure fragment for such observers is a simplex. Neither
   the gbit nor the dual shape occurs. Proved under μ-G; the proof appears to need only the
   support (F4.3).
4. **N4.** OA-2 r3's AW-OA2-4 gap rests on an effect class that contradicts OA-2's own closure
   Lemma 1. Under the class Lemma 1 presupposes, Theorem E(b) holds without (H4). Under the
   narrower class, a three-cell shift gives an exact, convention-imposed gbit.

These are scoped negatives for `G_SM`, a Layer-0 revision candidate (OA2:660–661). They are not
impossibility results for `G_SM` or for OI. Small observers, short horizons (`T ≪ L`) and
infinite windows stay open. The record-typing of heralds is an open interface premise. Nothing
here moves a manuscript claim, adopts a premise, or bears on correctness (§A.23: a consistency
axis only).
