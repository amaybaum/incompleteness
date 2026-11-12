# Focused recheck of OA-3 r2 (`OA-3-REPORT-r2.md`)

**Reviewer standing.** This is the same independent reviewer as `REVIEW-OA-3.md` (cited as `Rv3`).
The review was read-only and paper-only: no computation, no commit or push, and no GitHub write.
`r2:n` means line `n` of `OA-3-REPORT-r2.md`. Every other abbreviation is as in r2:30–39.

**Snapshot spot-check.** `origin/main` is `911a5cb6`. `git diff 615cc119 911a5cb6` under `papers/`
and `verification/programmes/oi-qm/` touches only the following:

- `papers/Main.md`, at the six one-line hunks 36, 60, 90, 151, 700 and 724.
- `papers/SM.md`, at hunks 196 and 605.

Nothing under `verification/programmes/oi-qm/` changed. A word-level diff of Main:724 shows that
item (xiv) ("measurement independence …; (xiv) enters only the Bell analysis of §3.3") is
byte-identical at both commits. Main:58 and SM:100–169 are unchanged. r2:19–26 is accurate.

## Verdict: **ACCEPT WITH CHANGES**

- **F1–F7.** All are applied as required, and each was checked at its cited lines (§1 below).
- **D1.** The writer's disagreement is correct, and I concede it. My F4.3 step was incomplete, and
  (PT) is a correct sufficient condition for it (§2 below).
- **Required edits.** There are two small ones: a probability formula in Theorem S step 1, and a
  missing handoff-window condition in Amendment 2. Three minor wording points are optional.

***

## 1. F1–F7: applied

Each item was verified against the change map (r2:740–768).

| Item | Where | Check |
|---|---|---|
| F1.1 | r2:49–51, :169–171, :202–208, :598, :625 | M2:857–859 is cited and quoted correctly. N1.2 is classified ELABORATING ✓ |
| F1.2 | r2:174–181 | Redone [RW], with the four cells −1, 1, 2, 3 refilled per the schedule. Tick 1 gives `r_1 = x`, `u_0(1) = y ⊕ c`. Tick 2 gives `r_2 = y ⊕ c`, `u_0(2) = x ⊕ c`, `v_0(2) = y ⊕ c`. Cell 0 is sharp at `(r_1 ⊕ c, r_2)` ✓ |
| F1, `L ≥ 4` | r2:166–168 | ✓ |
| F2 | r2:53–56, :187–198, :508 | "Exists only under P2" and "not a property of the rule" are removed. The open part is stated. N1.3 is CONFIRMING of OA2:632–633 ✓ |
| F3.1 | r2:137–140, :249–254, :630–632 | Extreme-argument permutivity and block width `l + r` are correct (the inputs are `x_{j−l+1}…x_{j+r}` together with `x_j`'s history) ✓ |
| F3.2 | r2:57–61, :258–265, :615–618 | Hedlund under [L]. obsmu Proposition C is noted. NEW is at corpus level ✓ |
| F3.3 | r2:633–635 | The M-INACC sentence is scoped. Growing carriers (OA1:573–574) are untouched ✓ |
| F4.1 | r2:62–67, :283–284, :703–709 | "MP-0b or (V-ii-H)" is now in the statement. Proof step 2 is adapted correctly to (V-ii-H), since the singleton indicators span `ℝ^U` ✓ |
| F4.2 | r2:322–327 | B(i) and B(ii) (⇐), as OA2:519–525. The non-use of B(iv) is stated ✓ |
| F4.3 | r2:280–354, :724–736 | Applied with (PT). See §2 |
| F4.4 | r2:369–371, :623–624 | ELABORATING. The scope text is kept ✓ |
| F5 cones | r2:458–465 | "Cones coincide; sets differ" ✓ |
| F5.1 | r2:375–390, :476–477, :619–622 | The defect is located at OA2:548–551, with Rv2:115–122 and Rv2b:105–107. Rv2:134–137 is credited ✓ |
| F5.2 | r2:112–115, :391–397, :410–411, :424–425, :455–456, :472, :637–643, :715–716 | Herald typing is carried as an open premise everywhere it bears ✓ |
| F5.3, F5.4 | r2:68–76, :429–430, :473–474, :513 | ✓ |
| F6.1, F6.2 | r2:77–80, :549–563 | The open regime is stated as a union. "Decisive for that instance" ✓ |
| F6.3 | r2:565–572 | Amendment 1 now requires fixing the herald typing ✓ |
| F6.4 | r2:573–585 | Record variant, guard, `Z_4` degeneracy and independence are all present ✓. One condition is missing; see edit E2 |
| F7 | r2:9, :615–626, :647–695 | Tally 2 NEW. Comment id cited. §A.19 basis extended, and the sources only the reviewer checked are attributed to the reviewer ✓ |

## 2. D1 and (PT), redone by hand

**Is my F4.3 step missing something? Yes.** Rv3 said that heralding on the full history gives `δ_ω`
for every `ω` in the support of the law *at `T₁`*. That covers only handoff supports of preparations
whose stage is at least `2(L−3)`.

The gap comes from how `U` is defined:

- `U` is the union of the supports of **all** reachable laws (OA2:131–132).
- The fragment contains preparations that hand off early, followed by measurements that start
  immediately.
- Such a pair is not, in general, equal to "longer preparation, then a shorter measurement". A
  measurement that reads `V` just after an early handoff has no counterpart after the padded one. So
  padding with waiting does not remove these preparations.
- Under a non-invariant initial law, for example MP-0a known-0 cells, the early-handoff support
  `F^t(supp ν)` need not lie in `⋃_{t′ ≥ 2(L−3)} F^{t′}(supp ν)`.

So `W = ℝ^U` does not follow from my argument.

The failure mode the writer gives is also right. With complete effects, `ρ` is injective iff
`W = ℝ^U`. If `W ⊊ ℝ^U`, Proposition B(ii) (⇒) makes the configuration model
measurement-contextual. A fragment with complete reads and non-spanning laws can then genuinely be
non-embeddable: OA-2's own N2.1 counterexample (OA2:280–299) is of exactly this kind. Leaving that
case undecided (r2:348–352) is therefore correct, not merely cautious.

**Is (PT) correct and sufficient? Yes.**

*Sufficiency.* Suppose `ω ∈ U` lies in the handoff support of a preparation `π` of stage
`t_h ≥ 2(L−3)`.

1. Compose `π` with a herald on the held history over `[0, t_h]`, including `V(0)`.
2. By Lemma OBS(i) and bijectivity, the history determines `ω(t_h)` pointwise.
3. `π`'s own heralds are functions of that trajectory, so they are passed with certainty by `ω`.
4. The composite therefore prepares `δ_ω` with positive probability, and `W ⊇ span{δ_ω : ω ∈ U} = ℝ^U`.

Steps 2 and 3 of the proof then go through as in r1.

*(PT-a).* If every preparation has stage at least `2(L−3)`, every reachable law is such a handoff law
or a mixture of them, so (PT) holds trivially. This works under any initial law ✓.

*(PT-b).* Suppose each initial law has `F`-invariant support. Then a short preparation's support lies
in `F^t(supp ν) = supp ν`. The bare preparation "wait `t′ ≥ 2(L−3)`" has handoff support
`F^{t′}(supp ν) = supp ν`, which covers it.

- **μ-G.** Support `S` ✓. A setting chosen by heralding `V(0)` is a herald inside the preparation,
  not a new initial law, so it is covered.
- **μ-O.** Support is the orbit ✓.
- **Horizon.** The long preparation plus its measurement stage needs `2(L−3) + 2(L−2) = 4L − 10` ✓.

*Necessity.* (PT) is sufficient for this proof route, not necessary for `W = ℝ^U`. Non-point laws
could still span. r2 states this correctly (r2:351–352).

**Herald typing (r2:112–115).** OA1:127 types the event of N1-K as "still held at use time". OA1:131
types the records of N4 as held in `V` at the end. OA2:800–801 says only "conditioning on the value
of a stated `V` cell at a stated tick". Recording the typing as open is correct. "Ensemble
conditioning" is the writer's gloss, not OA-2's wording; see m1.

**Amendment 1.** The added requirement to fix the herald typing is sound and correctly framed as a
proposal that needs owner authorization.

**Amendment 2's MP-0a admissibility under (PT).** This is correct via (PT-a), but see E2.

## 3. Required edits

**E1 (Theorem S step 1, r2:307–309).** The formula `ν(F^{−t_h} ω) · P(π's herald)` is wrong.
Given that `ω` is in the support, `π`'s heralds are passed with certainty. The probabilities are:

- **Subnormalized:** the probability of the composite herald is `ν(F^{−t_h} ω)`, times any external
  C-PM coin weight.
- **Renormalized after `π`:** `ν(F^{−t_h} ω) / P(π's herald)`.

Replace the formula with either form. Positivity, which is all the proof uses, is unaffected.

**E2 (Amendment 2, r2:573–580).** Theorem S needs a measurement stage of at least `2(L−2)` after
**every** handoff (r2:286). With horizon 6 on `Z_4`, that means every handoff `t_h ≤ 6 − 4 = 2`. The
amendment does not state this. Its MP-0a example, "every preparation of stage at least
`2(L−3) = 2`", would then allow stage-3 or stage-4 preparations whose measurement stage is too short.

Add: "every preparation hands off at `t_h ≤ T − 2(L−2)` (here `t_h ≤ 2`); under MP-0a with (PT-a)
every preparation therefore has stage exactly 2".

## 4. Minor (optional)

- **m1 (r2:114, :396).** Write "OA-2 conditions on the value of a stated `V` cell at a stated tick
  (OA2:800–801) and does not say whether the event must be held at use time". Mark "ensemble
  conditioning" as the reading that results, not as OA-2's typing.
- **m2 (r2:63–65, :707–708).** Phrase (PT-b) as "initial laws with `F`-invariant support (e.g. μ-G,
  μ-O)". "μ-G or μ-O … any other initial law" undersells (PT-b) and over-assigns to (PT-a). §0 item 4
  also omits μ-O.
- **m3 (r2:266–269).** Under (V-ii-H), say the *joint statistics* are available, because the joint
  indicators lie in the effect cone. That is what the gbit's restriction concerns at the GPT level
  (N4.4); a single-run joint effect may still be absent.

## 5. Anything new in r2

- **New claims.** The only new mathematical claims are (PT), (PT-a) and (PT-b). They are correct and
  sufficient as shown in §2. They narrow, and do not widen, my F4.3 proposal.
- **Overreach.** None found.
- **Labels.** The [RW] labels are accurate: they mark proof steps I redid in Rv3 (N1.2 including the
  `R ≡ i+2` exposure, Lemma OBS, Theorem S's step under μ-G, N4.2–N4.4). r2 marks its own changes
  unreviewed (r2:534–535, :702). Label changes match Rv3 F7: two NEW, Theorem S and N1.2 ELABORATING,
  N1.3 CONFIRMING.
- **Register.** No register problems.
- **Manuscript and premises.** No manuscript bearing, and no premise adopted.

After E1 and E2, OA-3 establishes the following, at [W] with [RW] proof steps:

- N1.2 settles M2:857–859.
- Lemma OBS holds.
- Theorem S holds under (PT) for any initial law, and hence under μ-G and μ-O at horizon
  `≥ 4L − 10`.
- N4 locates OA-2 r3's AW-OA2-4 gap in an effect class inconsistent with its Lemma 1, with herald
  typing open.
