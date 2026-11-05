# Independent exact-head review: O-RET Phase B, Theorem N (landed paper record)

**Reviewed head:** `82e146d887633e56fb75b9de4c84ee4bb918d059` on `land/oret-phaseb-negative-20261105`
(PR #1120). Its history from `main` at `53a3eb3d1485601982b28c11def5e7b2a0db21b9` is:
- `6102cb5ff1abef5acef4da065c50b644d82c1090` (commit `A`, reviewed in full in §1–§7);
- `32fadc60be9e2c9d0204de1fbf7d187e5df7b39c`;
- `82e146d887633e56fb75b9de4c84ee4bb918d059`.

§8 records the delta checks of the last two commits.

**Files reviewed:** `phaseB-negative/THEOREM-N.md` (new, 552 lines at the reviewed head) and the three-line
`Phase B` pointer added to the programme `README.md`.

**Comparison source:** `phase-b-design/DESIGN-PHASE-B.md` (DPB) at `4b4cacc93884039afadd0069373b0ac448761a6b`
on `research/o-ret-phaseb-design-20261105`, sha256
`22cdae48f345760323778e7d080124118c508c5e0600f5008f1c4d43f22cf023`.

**Reviewer:** an independent, model-authored reviewer who wrote neither DPB nor the extract. The review is
read-only: hand mathematics, a line-by-line comparison with the source, and the repository's hygiene
checks. No computation, enumeration or simulation was run. Line numbers of `THEOREM-N.md` below refer to
the reviewed head.

## 1. The [D] items, re-derived from `THEOREM-N.md` alone

Each item was checked by hand under its stated hypotheses.

- **Lemma TV (§3.1).** For `σ, σ′ ∈ P` with `f(σ) = 0` and `f(σ′) = 1`,
  `μ(g ≠ 0 | σ) + μ(g ≠ 1 | σ′) ≥ 1 − δ`, so `ε_max ≥ (1 − δ)/2`. Correct for deterministic and
  randomized decoders.
- **Lemma PAD (§4.1).** Suppose `x_A(t₀)` is uniform and independent of `W`. Then
  `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` is uniform given `W`, so the readout is blind. Correct.
- **Lemma NP (§4.2).** Correct.
  - `G₀` reads neither `y₀` (the rule is centre-free) nor `x₀`. Under a product law its law is therefore
    independent of `σ`.
  - J-i forces the translates of that law by `0` and by `1` to coincide, so the law is uniform over `𝔽₂`.
    This needs both values of `x₀` for some `c`, which is a stated hypothesis.
  - Under `δ₀`, `G₀ = 0`.
- **Proposition AE (§4.3).** Correct.
  - The write structure `(n_x, n + c·b)` holds, and `(n_x, n)` does not depend on `σ`.
  - The join holds: `ℓ* = (H(n_x, q_rest) + q₀b − n, n_x)` gives `f_R(ℓ*; q) = (n_x, n)` and
    `f_R(ℓ*; q + e_{y₀}) = (n_x, n + b)`, so any `G` containing both `q` and `q + e_{y₀}` is inconsistent.
  - The translation holds: `L(Q_{t₀+1} | σ₁) = L(Q_{t₀+1} | σ₀) + e_{y₀}`, because only `y₀(t₀+1)` reads
    `x₀`.
  - The bound holds: `Σ_q p(q)[1_G(q) + 1_G(q + e_{y₀})] ≤ 1`, so `η_{t₀+1} ≥ 1/2`.
  - In case (b), `b ≠ 0`, which puts `y₀` in `Q`.
  - The K1 instance takes `b` as the indicator of the sites of `A` adjacent to site 0.
  - The SMR instance takes `b = e₁`. Its parent list `{1, N−2, N−1}` matches
    `y′_i = y_{i−1} ⊕ (y_{i+1} ∨ y_{i+2}) ⊕ x_i` (SM:112).
- **Proposition LS (§4.4).** Correct.
  - Every sub-case of (i), (ii) and (iii) holds.
  - In (i) and (iii-a), the joint leak `y′₀ ⊕ y′₁ = c ⊕ x₀` makes J-i fail.
  - In (ii), conditioning on `y_{N−1} = 1` gives `δ ≤ 1/2`.
  - In (iii-b), J-ii fails.
  - The three cases exhaust the arcs. `N ≥ 7` keeps sites 1–3 out of `A` in cases (i) and (iii).
- **Observation U (§4.5)**, with its arc lists for `N = 7` and `N = 8`. Correct.
- **The `N = 5` table (§4.6).** Every entry at `r = 0` and `r = 1` was re-derived from the five update
  formulas, together with the list of registers whose `r = 1` law equals `δ₀`. Representative values:
  - `{1,4}`: the conditional laws are `{00: 1/4, 10: 1/4, 11: 1/2}` and `{11: 1/4, 01: 1/4, 00: 1/2}`, so
    `δ = 1/2`, and the bound `1/4` is attained.
  - `{1,3}` and `{2,4}`: `δ = 1/2`.
  - `{2,3,4}`, `{1,2,3}` and `{1,3,4}`: `R` fixes the cell that `y′₀` pairs with `x₀`, so J-ii fails.
  - `{1,2,4}`: `G₀ = 0`, so J-i fails.

  For `{1,3}` and `{2,4}` the stated bound `≥ 1/4` is valid, and it suffices since `ε* < 1/4`. The
  deterministic minimax there is in fact `1/2`.
- **Lemma SS-2 (§4.7).** Correct. `x_i(t₀+1) = y_i(t₀)` is constant, and `G_i` reads only `Q` because the
  rule is centre-free. So `y_i(t₀+2)` is a function of `Q_{t₀+1}`, and J-i makes it independent of `κ`.
  The lemma relies on the current-slice read (H-cur), which it states.
- **The slice-level shape (§4.8).** Correct at `N ≥ 7` and at `N = 6`, where `x₁` pads `y′₁`.
  `y_{N−1}(t₀+2)` is uniform given `σ`.
- **Observation W1 (§4.9).** Under `δ₀` with `x₀ = 0`:
  - `y(t₀+1) = (0, c, 0, 0, c)`, `x(t₀+1) = (c, 0, 0, 0, 0)` and `y(t₀+2) = (c, 0, c, c, 0)`.
  - `Q = {y₀}`, and `y₀(t₀+1) = y₄ + y₁ − x₀ = 0`, so J-1 holds at `t₀+1`.
  - OR decodes `c` at both ticks.
  - The orbit of the zero configuration is `{0}`, so DIL∃ holds on `W₁` and `τ = ∞`.
  - `y₀(t₀+2) = c + c − c = c`, so J-i fails at hold tick `t₀+2`.
  - The draft's locality gate applies because the environment `Λ ∖ {0, …, 4}` is empty.
- **Theorem N and its coverage table (§4.10).** Every tuple of `𝔉` falls under an item:
  - `π₀` is covered by PAD.
  - K1 is covered by AE, for every register and every product law.
  - At `N ∈ {7, 8}`, each SMR arc falls in exactly one of AE (SMR), U and LS.
  - At `N = 5`, SMR is covered by PAD, NP, AE, U and §4.6.

  Every law other than `π₀` is site-level with `A` ready, under any reading of the one-sided laws, since
  `Z ⊇ A`. Each failure is either a J-1 failure at `t₀+1` or an ST violation at `t₀+1` or `t₀+2`. Both
  ticks lie in `W_T` for every `T ≥ 1`, and every bound is `≥ 1/4`. A J-1 failure assigns row 1 before the
  storage step (PREREG §4 step 2), and an ST failure excludes rows 5, 6 and I-10.
- **§6.1.** The scope statement restates exactly the family and classifier of §3.2–§3.3 and claims nothing
  beyond Theorem N. The wider hypotheses of AE and SS-2 are kept out of the negative's scope.
- **§7.1.** Each family is undecided by the six lemmas as stated:
  - O2: AE and U decide every other one-site register under product laws.
  - O3: SS-2 decides width-1 registers with a fixed current slice.
  - O5: it is open only for SMR registers meeting `{N−2, N−1}`, and for `q > 2`.
  - O4: it is undecided beyond W1.
- **§7.2.** The six conditions are exactly the failure of at least one hypothesis of each lemma, with NP's
  exception, including the `q > 2` and preparation clauses. The O1 and O5 derivations are correct. "Whether
  one route is smallest is not established" is supported: D-SML (DEFINITIONS:215–218) compares resources
  rather than ranking by one scalar.

**Without §5 and Corollary AE-D2.** No landed sentence, table row or proof step uses decoder D2, the
free-map class, Proposition IP, the calibration controls or the counting criterion. Theorem N holds for
every fixed decoder and uses no counting rule (§3.3, §4.10). The phrase "whatever `T*`, `w*` or counting
rule is chosen" is generic: `T*` and `w*` are PREREG fields. The derivations stand without the excluded
material.

## 2. Faithfulness to DPB at `4b4cacc9`

I compared the extract's body (§3–§7) line by line with DPB 105–741, less DPB 271–274 and 459–623. Every
difference is one of the listed adaptations:

- **A3.** The E-SDC assessment is cut after the label on DPB 116, and the label is kept. The decoder
  sentence at DPB 127 keeps its first sentence. "D1, D1′, D2" is removed at DPB 433 and 633.
- **A4.** Corollary AE-D2 is absent.
- **A5.** Glosses are added for B-1, G-6 (c), G-9 (a), I-10, B-2 to B-6, the locality gate and G-6 (b).
  Each was checked against the draft at `43370576`:
  - I-10 and B-4: the environment `Λ ∖ (Σ ∪ sites(R) ∪ sites(Q))` is empty.
  - B-2 to B-6: the write gate, the decoder rule, the locality gate, the handling of `T*` and `w*`, and the
    exit-4 guard.
  - G-9 (a): pairing `N = 8` with `N = 6` or `7`.
  - G-6 (b): the restricted-carrier family `x₀ = 0`.
  - G-6 (c): the one-sided ready regions.
- **A6.** W1's status, O4's row and the O4 paragraph are restated. DPB 417–419 are verbatim.
- **A7.** The status lines at DPB 426–427 and 638–639 are replaced. The "not independently reviewed"
  labels are removed, as is "unreviewed," at DPB 642.
- **A10.** DPB 661 is retargeted to the DESIGN-PULSE obligations.
- **A11.** The DPB 679 locator is widened (see §8).

No claim changes outside these adaptations. The header (A1) and the reference table (A9) are new text by
design.

**Section numbers.** The extract keeps DPB's section numbers (§3, §4, §6, §7, §10) rather than renumbering
them. This departs from the proposal's "headings are renumbered" and is accepted. The deviation is stated
in the header (lines 27 and 35). It keeps every internal reference, and every provenance citation of the
#1115 reviews (for example "§4.6", "§4.8"), valid without edits, and it keeps the mechanical comparison
one-to-one. The header explains the gaps in the numbering.

## 3. O4 against owner ruling (a)

The record meets each requirement of ruling (a) (#1115 c.6652197336):

- **Test case, not mechanism.** O4 is a restricted-carrier mathematical test case, not an established
  physical-retention mechanism: §4.9 (the quoted ruling), the §7.1 O4 row and §7.2's O4 paragraph.
- **Explicit preparation.** The restricted preparation is stated as `P = {(0,0), (0,1)}`, "`x₀(t₀) = 0`
  fixed, `c` free", under `δ₀` (§4.9 instance and line 379), and as "`x₀(t₀)` fixed" in the §7.1 row.
- **No physical availability.** It is not physically available without independent sourcing: §4.9, §7.1
  and §7.2.
- **Later-tick failure visible.** "At `T = 2`: `y₀(t₀+2) = c`, J-i fails, row 1" (verbatim from DPB) and
  "The failure is J-i at hold tick `t₀+2`" (§4.9); the same appears in §7.1 and §7.2.
- **`T = 1` outcome not overstated.** The added sentence reads: "The `T = 1` outcome is a one-hold-tick toy
  outcome under an imposed preparation, and is not evidence of retention".
- **Scope of the instance.** "§4 leaves O4 undecided beyond W1" appears in §4.9, §7.1 and §7.2.
- **Motivation kept separate.** O4 lies outside `𝔉` by definition, since `𝔉` requires all four
  preparations. The RET-st and HC-K4 text is labelled [R], motivation only.

The quotation of ruling (a) is verbatim, with its author, channel and posting time (2026-11-05T07:19:55Z).

## 4. Status header

The header states:

- a scoped paper negative for `𝔉`, independently reviewed at exact head in `REVIEW.md` (this directory);
- no manuscript or correctness status change, attributed accurately to the recording comment
  c.6652197336;
- not a universal no-go for OI retention;
- no premise adopted (E-SDC, `ν_r` (H-sel) and H-cur stay labelled and unadopted);
- O4 per ruling (a);
- no Phase B run planned or authorized;
- accountable Issue #1032, with provenance #1115.

The owner quotations from #1032 c.6651202161 (amaybaum, 2026-11-05T06:15:39Z) are verbatim:

- "a negative for this rule, register, preparation and decoder family is not a universal no-go theorem for
  OI retention";
- "**Not authorized:** Phase B freeze, enumeration, execution, any new physical premise, or scientific
  promotion".

## 5. Citations and their §A.42 item 8 classification

Every on-`main` locator was checked at `53a3eb3d`, whose tree is identical to `f5c281ae`. ROUTES was read
at `49f0bd41`, which is reachable from `main`.

| Source | Locator | Content checked |
| --- | --- | --- |
| PREREG | P:57 | the window |
| PREREG | P:79–80 | the metrics |
| PREREG | P:176–185 | Remark C's frozen wording |
| PREREG | P:418–500 | §4, the decision rule |
| PREREG | P:471–473 | row 4 |
| DESIGN-PULSE | D:32–37 | the obligations table, rows O1–O4 |
| DESIGN-PULSE | D:98–99 | DIL∃ generated over all of `config(R)` |
| DESIGN-PULSE | D:151–155 | Observation K (K-1) |
| DESIGN-PULSE | D:407 | row 4 and Remark C |
| DESIGN-PULSE | D:577 | K1 at K-18(b), `|S| = 2¹⁰`, sites 1–4 |
| DEFINITIONS | :69–73 | Remark C |
| DEFINITIONS | :82 | HC-K4 among the rejected cases |
| DEFINITIONS | :159–183 | D-TRN |
| DEFINITIONS | :215–218 | D-SML |
| SM | :106 | the second-order form |
| SM | :112 | the ring rule with `R(i, x)` |
| Main | :726 | the posit ledger, with posits (vii) (linearity of the update, A5) and (x) |
| MR-star | MR:464–465 | `φ(u_prev, u) = (u, A u − u_prev)` |
| MR-star | MR:1342 | "C-3. The R gap, reframed" |
| INTERFACE-CONTRACT | :32–36 | rule h's torus side and update |
| ROUTES at `F` | R:19 | K-18(b), `(d,N,q,a) = (1,5,2,1)` |
| ROUTES at `F` | R:33–34 | RET-st not the adopted definition |
| ROUTES at `F` | R:46–50 | RET-st excludes HC-K4 by full carrier support |
| ROUTES at `F` | R:163–168 | HC-K4 |
| ROUTES at `F` | R:233–240 | route I's classification |
| ROUTES at `F` | R:314–315 | CN and K1's pad |
| ROUTES at `F` | R:421–426 | route III, conditional on E-reg |
| programme `README.md` | :33–38 | the "Paper results" paragraph |

The record's phrase "the native step form of posit (vii)" for Main:726 is supported together with
MR:464–465. The quotations of #1032's requirements 1 and 2 match the issue body verbatim. The relative
paths to `MR-star.md` and `INTERFACE-CONTRACT.md` resolve from `phaseB-negative/`.

The classifications in §10 are correct:

- The owner records (#1032 c.6651202161, #1115 c.6652197336 and the #1032 issue body) are quoted with
  author and time (§A.42 item 7).
- The #1115 review and design comments are model-authored provenance.
- DPB, `43370576` and `5839e064` exist in the repository but are not reachable from `main`, and are offered
  as provenance only (§A.42 item 3).
- The files on `main` are support.
- ROUTES is [R], motivation only.

## 6. README pointer and placement

The pointer reads: "**Phase B.** `phaseB-negative/THEOREM-N.md` records a scoped paper negative (Theorem N)
for the family it names. It is not a universal no-go for OI retention, and no Phase B run is planned."

It is accurate, in the programme's status-note register, and placed before the list of superseded status
lines. The record and this review share a programme subdirectory (§A.36). `phaseB-negative/` did not exist
on `main` and is distinct from the research branch's `phase-b-design/`. No frozen Phase A file and no
`legacy-records.json` entry is changed.

## 7. Checks

Each check was run with `python3 -I` from a detached checkout, at `6102cb5f` and again at the reviewed head
`82e146d8`. Both runs gave the same results.

| Check | Exit | Result |
| --- | --- | --- |
| `legacy_records_check.py <head>` | 0 | 303 records in 75 closed namespaces, all intact |
| `citation_roles_check.py <head>` | 0 | 0 manifests, all hold |
| `duplicate_check.py` | 0 | no paragraph repeated within a file |
| `staleness_check.py` | 0 | 13 matched, 0 unstamped |
| `artifact_placement_check.py` | 0 | no unaccounted root artifact |
| `voice_check.py` | 0 | no manuscript-voice history narration; 40 manuscript files scanned |
| `claims_check.py` | 0 | no withdrawn result asserted unconditionally |

## 8. Delta checks after `6102cb5f`

The review of `6102cb5f` returned ACCEPT WITH CHANGES. One correction was required (C-1) and three were
optional (C-2 to C-4):

- **C-1.** The [R] label cited "programme `README.md:30–35`". The commit's own README pointer moved that
  paragraph to lines 33–38.
- **C-2.** The rule-h locator should include the torus side.
- **C-3.** §10 lacked rows for the named on-`main` definitions and for #1032's requirements.
- **C-4.** The status wording "reviewed … reviewed" repeated itself.

**`6102cb5f` → `32fadc60`** (single parent; `THEOREM-N.md` only, +13/−10). Every hunk maps to C-1 to C-4
or to the new adaptation 11, which records C-2 at DPB 679. Nothing else changed.

- **C-1.** The citation now reads `README.md:33–38`, which at this head is exactly the "Paper results"
  paragraph.
- **C-2.** `INTERFACE-CONTRACT.md:32–36` now carries line 33's torus side, which supports `|S| ≥ 2⁴⁸`.
- **C-3.** The new §10 rows were verified locator by locator as listed in §5. The #1032 row gives the
  issue's author and creation time (2026-11-02T01:50:32Z) and verbatim quotations of requirements 1 and 2.
- **C-4.** The status wording is corrected in the header, §4.10 and §6.1.

Two phrases in the new §10 rows were not supported by their sources:

- "read as last edited 2026-11-05T06:15:39Z". That timestamp is the issue's last-update time, which
  coincides with the posting of c.6651202161, not a verified body-edit time.
- "rule h and its smallest torus". The contract states a torus side, not a smallest torus.

**`32fadc60` → `82e146d8`** (single parent; `THEOREM-N.md` only, +2/−2). Both lines changed are exactly
those two phrases. They now read "read 2026-11-05; issue last updated 2026-11-05T06:15:39Z" and "rule h
and its torus side". Nothing else changed. The checks of §7 pass at this head.

## Verdict

The mathematics of `THEOREM-N.md` is correct and complete under its stated hypotheses, and Theorem N holds
on `𝔉` as scoped. The extract is faithful to DPB at `4b4cacc9` apart from the listed adaptations. O4 is
recorded as owner ruling (a) requires. Every citation resolves on `main` as classified, and every
correction requested in review is applied at the reviewed head.

**VERDICT: ACCEPT, at `82e146d887633e56fb75b9de4c84ee4bb918d059`.**
