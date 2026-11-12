# Delta review of OA-3 r2 → r3 (exact text at `469ecee9`)

**Reviewer standing.** Focused exact-text delta review under the owner gate of 2026-11-12 (amaybaum):
only the r2→r3 edits E1, E2, m1–m3 and the other r2→r3 differences. Read-only and paper-only: no
computation, no commit or push, no GitHub write.

**Objects.** Commit `469ecee9134c15ad147eb2baa1dc2efe455cdcfd` on `research/oa1-w1-1-20261112`,
directory `verification/programmes/oi-qm/reconstruction/oa-3-20261112/`. `r2:n` / `r3:n` = line `n`
of `OA-3-REPORT-r2.md` / `OA-3-REPORT-r3.md` there; `Rc:n` = line `n` of `RECHECK-OA-3-r2.md` there.
The delta is `diff OA-3-REPORT-r2.md OA-3-REPORT-r3.md` on the committed blobs (16 hunks). The committed
`REVIEW-OA-3.md`, `OA-3-REPORT.md`, `OA-3-REPORT-r2.md` and `RECHECK-OA-3-r2.md` are byte-identical
(`cmp`) to the scratchpad copies r1–r3 previously cited, so `Rv3:n` and `r1:n` resolve unchanged;
spot-checked Rv3:99, :105–111, :159–170. OA2:767–770 and :800–801 read at `815d6a8e`.

## Verdict: **ACCEPT WITH CHANGES**

E2 is implemented faithfully. E1 is implemented except for one factor the recheck stated. m1, m2
and m3 are each applied at one of the sites the recheck named but not at the other, and the m3 edit
changes the quoted wording of the gbit criterion. None of the required edits below changes an
assumption, quantifier, effect class or conclusion; they bring the text into line with the accepted
corrections. The Standing note's "all applied" (r3:5) becomes true once R2–R4 are made. Nothing
overstates review status.

## 1. The accepted corrections

### E1 — Theorem S step 1 herald weight (r2:307–308 → r3:310–313)

- r3:310–312: "subnormalized weight `ν(F^{−t_h} ω) > 0` (after renormalizing on `π`'s herald,
  `ν(F^{−t_h} ω) / P(π's herald) > 0`) … Only positivity is used."
- The wrong product `ν(F^{−t_h} ω) · P(π's herald)` is removed. The renormalized form matches Rc:121.
  "Only positivity is used" matches Rc:123. The step's conclusion (r3:314, `W = ℝ^U`) is unchanged.
- **Gap.** Rc:120 gives the subnormalized form as `ν(F^{−t_h} ω)` "times any external C-PM coin
  weight". r3 omits that factor, so the stated weight is wrong for a coin-mixed `π`, which C-PM
  admits (r3:91, :413). Positivity is unaffected. → **R1**.
- Residual (optional, O5): r3:312 "Under μ-G this is `|S|^{−1} = q^{−2L}` for the unheralded `π`".
  In the subnormalized form the value is `|S|^{−1}` for any coin-free `π` under μ-G, so "for the
  unheralded `π`" is now redundant. It is not wrong.

### E2 — Amendment 2 handoff (r2:580 → r3:585–587, inserted)

- r3:585–587: "**Handoff.** Every handoff is at `t_h ≤ T − 2(L−2)`, which is `t_h ≤ 2` at horizon `6`,
  so every measurement stage is at least `2(L−2)`. Under MP-0a with (PT-a), every preparation then
  has stage exactly `2`."
- Checked: at `L = 4`, `2(L−2) = 4`, so `T = 6` gives `t_h ≤ 2`. (PT-a) needs stage `≥ 2(L−3) = 2`
  (r3:583–584), so the stage is exactly 2. This agrees with Rc:137–138 and with Theorem S's hypothesis
  r3:289. The Initial-law bullet (r3:582–584) is unchanged and is now consistent with it. ✓
- "then" binds to the horizon-6 clause, as "here" does in Rc:137. For `T > 6` the bound is
  `t_h ≤ T − 4`. Faithful.

### m1 — "ensemble conditioning" is the report's reading (Rc:143–145; sites r2:114, :396)

- r2:114–115 → r3:116–118: "OA-2 conditions on the value of a stated `V` cell at a stated tick
  (OA2:800–801); 'ensemble conditioning' is this report's reading of that wording, not OA-2's term."
  This agrees with OA2:800–801 ("a herald is conditioning on the value of a stated `V` cell at a stated
  tick"). ✓
- **Gap.** The second site Rc:143 names, r2:396 = r3:400–401, is unchanged: "If heralds are ensemble
  conditionings, **as OA-2 uses them (OA2:800–801)**, no retention is needed and (V-ii-H) is
  **OA-2's own reading**." It still attributes the typing to OA-2, which contradicts r3:117–118 ("not
  OA-2's term"; "not fixed by either source"). → **R2**.
- r3:570, :613 and :647 use "ensemble conditioning" as the name of one typing option. That is
  acceptable once §1 defines it; :647's bare "(OA2:800–801)" is optional to tag (O2).

### m2 — (PT-b) phrasing; μ-O in §0 item 4 (Rc:146–148; sites r2:63–65, :707–708)

- §0 item 4, r2:65 → r3:67: "true under initial laws with `F`-invariant support, e.g. μ-G and μ-O,
  whenever the horizon is at least `4L − 10` …". μ-O is added. ✓
- N3 (PT-b), r2:292–294 → r3:295–297: "(PT-b) For preparations of any stage, for initial laws with
  `F`-invariant support (e.g. μ-G, support `S`, and μ-O, support an orbit, OA1:97–98), when a
  preparation of stage at least `2(L−3)` from them fits the horizon, i.e. horizon at least `4L − 10`."
  - *Quantifier check.* r2 read "when each initial law of the fragment has `F`-invariant support". r3
    reads it per law. That is the form Rc:147 asks for. It is also correct per configuration: (PT) is
    a condition on each `ω ∈ U` (r3:290–291), and a short preparation from an invariant-support `ν`
    is covered by the long wait from the same `ν` (Rc:83–85). Laws without invariant support remain
    under (PT-a) or (PT) itself.
  - *Equivalence check.* "i.e. horizon at least `4L − 10`" holds given the standing hypothesis of a
    measurement stage `≥ 2(L−2)`: `2(L−3) + 2(L−2) = 4L − 10` (Rc:91). Not a widening. ✓
- **Gap.** The second site Rc:146 names, r2:707–708 = r3:715–716 (§7 Limits), is unchanged: "(PT):
  under μ-G or μ-O a horizon of at least `4L − 10`; **under any other initial law** every preparation
  of stage at least `2(L−3)`." This is the "μ-G or μ-O … any other initial law" wording Rc:147 says
  undersells (PT-b) and over-assigns to (PT-a). The r3 change map row m2 (r3:787) omits §7. → **R3**.
- r3:545–546 (§4 item 2) lists only μ-G or μ-O for the horizon branch. It says "any initial law",
  not "any other", so it is not wrong; aligning it is optional (O1).

### m3 — joint statistics under V-ii-H (Rc:149–151; site r2:266–269)

- r2:267–269 → r3:270–272: "…(under MP-0b); under V-ii-H the joint statistics are available, since
  the joint indicators lie in the effect cone generated by the heralded composites over that history.
  The gbit's 'joint statistics unavailable under every protocol' fails."
- The first sentence implements Rc:149–150. ✓
- **Defect.** The edit changes the quoted criterion from r2's "joint read unavailable under every
  protocol" to "joint statistics unavailable under every protocol" and still presents it in quotation
  marks as "the gbit's". No source has that wording: the shape's definition in r3:107 keeps "joint
  read unavailable under every protocol", and so does OA2:767–770 ("makes the joint read unavailable
  under every protocol").
  - The substitution is the GPT-level reading Rc:150–151 endorses via N4.4 (r3:462–469), so the N2
    verdict (r3:276–278) is unaffected.
  - But the text now silently redefines the quoted criterion, and it drops Rc:151's caveat that a
    single-run joint effect may still be absent under V-ii-H (cf. r3:465–466). → **R4**.

## 2. Every other r2→r3 difference (16 hunks; nothing else changed)

| # | r2 → r3 | Change | Check |
|---|---|---|---|
| 1 | 1 → 1 | Title "(r2)" → "(r3)" | ✓ |
| 2 | 3–4 → 3–6 | Standing note | Recheck verdict, "E1, E2 required; m1–m3 optional" (Rc:24–25), re-derivation and acceptance of (PT), (PT-a), (PT-b) (Rc §2) and the concession of D1 (Rc:22–23) are accurately reported. "r3's own edits are unreviewed" ✓. "All applied" is not yet true (R1–R4). |
| 3 | 38–39 → 40–41 | `Rv3`, `r1` cite sibling files in this directory | Committed blobs are byte-identical to the scratchpad copies, so line numbers are unchanged ✓ |
| 4 | 65 → 67 | m2, §0 item 4 | ✓ (§1 m2). The line is 165 characters, against about 100 elsewhere; reflow is optional (O4). |
| 5 | 114–115 → 116–118 | m1, §1 | ✓ (§1 m1) |
| 6 | 267–269 → 270–272 | m3 | R4 |
| 7 | 292–294 → 295–297 | m2, (PT-b) | ✓ (§1 m2) |
| 8 | 307–308 → 310–312 | E1 | R1 |
| 9 | 535 → 539 | §4 preamble: "r2's changes rechecked in `RECHECK-OA-3-r2.md`, r3's edits unreviewed" | ✓ |
| 10 | 580 a → 585–587 | E2 | ✓ |
| 11 | 585 → 592–593 | Independence: "the focused recheck accepted the (PT) form; r3 as a whole is unreviewed" | ✓. The control still counts as independent only "once Theorem S has passed review" (r3:591), which r3's unreviewed step-1 edit does not yet meet. Not overstated. |
| 12 | 603 → 611 | Status cell: "(PT) form accepted in the focused recheck" | ✓ (Rc:66, :87–89) |
| 13 | 626 → 634 | Tally: "r2's changes rechecked, r3's edits unreviewed" | ✓ |
| 14 | 682 → 690 | §6 "This directory." lists r1, review, recheck | ✓. 132 characters (O4). |
| 15 | 702 → 710 | §7: "r2's changes, including (PT), passed the focused recheck; r3's edits (E1, E2, m1–m3) are unreviewed" | ✓. Rc passed r2 "with changes" (E1/E2), and r3 records those as its own unreviewed edits. Acceptable. 128 characters (O4). |
| 16 | 768 a → 777–789 | "Change map r3" | Rows E1, E2, m1 and m3 point to the right places. Row m2 omits §7 (R3); row m1 omits N4.1 (R2). Status-phrase hunks 9, 11–13, 15 and citation hunks 3, 14 are not mapped (O3). |

No hunk changes an assumption, quantifier, effect class or conclusion, apart from the m3 quotation
(R4) and the per-law (PT-b) reading (checked correct above). No status is overstated: every
reference to r3 says unreviewed, and every acceptance is attributed to Rc's actual scope.

## 3. Required edits

- **R1 (E1, r3:310).** Replace "has subnormalized weight `ν(F^{−t_h} ω) > 0`" with "has
  subnormalized weight `ν(F^{−t_h} ω)`, times any external C-PM coin weight, `> 0`".
- **R2 (m1, r3:400–401).** Replace "If heralds are ensemble conditionings, as OA-2 uses them
  (OA2:800–801), no retention is needed and (V-ii-H) is OA-2's own reading." with "If heralds are
  ensemble conditionings (this report's reading of OA2:800–801; §1), no retention is needed and
  (V-ii-H) is the class OA-2's Lemma 1 uses (OA2:226)." The replacement wording is supported by
  r3:112–113. Add "N4.1 herald-typing bullet" to change-map row m1 (r3:786).
- **R3 (m2, r3:715–716).** Replace "(PT): under μ-G or μ-O a horizon of at least `4L − 10`; under any
  other initial law every preparation of stage at least `2(L−3)`;" with "(PT): for initial laws with
  `F`-invariant support (e.g. μ-G, μ-O), a horizon of at least `4L − 10`; under any initial law,
  every preparation of stage at least `2(L−3)`;". Add "§7" to change-map row m2 (r3:787).
- **R4 (m3, r3:272).** Replace "The gbit's 'joint statistics unavailable under every protocol'
  fails." with "The gbit's 'joint read unavailable under every protocol' (§1; OA2:767–770) therefore
  fails under MP-0b. Under V-ii-H the gbit's restriction fails at the level of joint statistics,
  which is what it concerns at the GPT level (N4.4); a single-run joint effect may still be absent."

## 4. Optional

- **O1.** r3:545–546 (§4 item 2): use the (PT-b) phrasing, i.e. "for initial laws with `F`-invariant
  support (e.g. μ-G, μ-O)".
- **O2.** r3:647: "as ensemble conditionings (the reading of OA2:800–801, §1)".
- **O3.** Add to the change map r3 a row "Review-status phrases and citation forms | Standing; §0
  citation forms; §4 preamble; §5 row and tally; §6 'This directory'; §7".
- **O4.** Reflow r3:67, :690 and :710 to the file's line width.
- **O5.** r3:312: drop "for the unheralded `π`", or say "for coin-free `π`".
- **Outside the delta (not reviewed under this gate; noted only).** r3:10 "Nothing committed, pushed
  or posted" and r3:14 "Commands used (r1 and r2)" are unchanged from r2. The file is now committed
  at `469ecee9`, by the coordinator rather than the unit author.

***

## Recheck of a55f0588

**Objects.** `git diff 469ecee9 a55f0588` touches only this directory. It adds
`DELTA-REVIEW-OA-3-r3.md`, which is byte-identical to this file as it stood before this section, and
changes `OA-3-REPORT-r3.md` in 10 hunks. `a55:n` = line `n` of `OA-3-REPORT-r3.md` at `a55f0588`.
PR #1265 was read through the REST API: open, draft, head `research/oa1-w1-1-20261112`, base `main`,
not merged.

### Verdict: **ACCEPT WITH CHANGES** (one phrase)

**Required edits (R1–R4)**

- **R1 ✓.** a55:315–316 has the coin factor exactly as required ("subnormalized weight
  `ν(F^{−t_h} ω)`, times any external C-PM coin weight, `> 0`").
  - The renormalized form was reworded to "divided by `P(π's herald)`". With the coin factor that
    gives `ν·c / P(π's herald)`, which is the correct conditional probability.
  - Positivity is unchanged.
- **R2 ✓.** a55:405–406 is exactly as required. Change-map row m1 adds N4.1.
- **R3 ✓.** a55:722–723 is exactly as required. Change-map row m2 adds §7.
- **R4 ✓.** a55:274–277 is exactly as required. The §1 definition (r3:107 at `469ecee9`) is unchanged and now
  agrees with the quotation.

**Optional edits (O1, O2, O3, O5)**

- **O1 ✓.** a55:550–551 uses the (PT-b) wording. The "any initial law" branch is unchanged.
- **O2 ✓.** a55:652–653.
- **O3 ✓.** The new row at a55:797 is accurate.
- **O5: one defect, from combining R1 with O5's "drop" option.** a55:317–318 reads "Under μ-G this
  is `|S|^{−1} = q^{−2L}`". "This" now refers to the weight including the C-PM coin factor, which is
  `c·|S|^{−1}`, not `|S|^{−1}`, when a coin is present.
  - **Required edit (D1):** replace "Under μ-G this is `|S|^{−1} = q^{−2L}`, which is OA-1 D3 with
    equality" with "Under μ-G, `ν(F^{−t_h} ω) = |S|^{−1} = q^{−2L}`, which is OA-1 D3 with
    equality".
  - Nothing else in the step changes.

**Other changed text**

- **Standing (a55:5–8): accurate.** "m1–m3 optional, all applied" is now true. "R1–R4 required,
  O1–O5 optional" and "required edits and optional O1–O3 and O5 are applied here; those edits are
  unreviewed" both match this review and the diff.
- **Scope line (a55:12): accurate.** It is checked against #1265 above. It replaces the stale
  "Nothing committed, pushed or posted".
- **Status phrases: accurate; none says an edit is accepted that this review did not accept.**
  - §4 lead-in (a55:544).
  - Amendment 2 Independence (a55:598). The condition "once Theorem S has passed review" is
    unchanged, and R1/D1 in step 1 keep it unmet.
  - §5 tally (a55:639).
  - §7 (a55:716–717).
- **Change map r3, delta-review edits (a55:799–812): accurate.**
  - "R2 … N4.1 second bullet": the edited text is the second sub-bullet of N4.1's herald-typing
    bullet (a55:400–406). The locator is loose but findable; tightening it is optional.
  - "O2 … §5 AW-OA3-2" is correct: AW-OA3-2 lies under §5 (a55:604–661).

None of these changes alters an assumption, quantifier, effect class or conclusion.

**No other difference.** All 10 hunks are accounted for above.

**Layout (O4 class, optional).** a55:544, :639 and :716 exceed the file's line width. The O2 edit
leaves a short line at a55:653 ("OA2:800–801). Under the").
