# Independent non-author review of the SB-L3 narrow extract

**Verdict: ACCEPT WITH CHANGES.** No blocking finding. Seven should-fix findings (R1–R7) and seven
nits (R8–R14). The quotation is byte-exact and every pin is correct. The Theorem N′ composition
[+3] is valid and adds no new step, but its list of hypotheses is incomplete (R2). One negative
support claim is false: a kernel theorem on `main` already proves the directed cone induction (R1).
Apply R1–R7 before the ChatGPT exact-head review.

## Object and authority

- **Head checked.** `eac7692c77196b070758d70368bf3272bd5f2af9` on
  `records/bell-landing-plan-868-20261114`. This is the single commit after `3859c3ef`; it adds
  only `verification/programmes/oi-qm/reconstruction/bell-landing-20261114/SB-L3.md` (blob
  `fdc73e5bf2c16a9185d215ae961054c203e9e29b`, SHA-256
  `0f70f19d6a29edd7d674df45f9eb05ee899ca032de68d615d19c73e435813e13`, 185 lines). "X:n" below is
  line n of that file.
- **Authority.** Owner decision #868 comment 6874036684 (`amaybaum`, 2026-11-14), read first-hand:
  OQ-3, "SB L3 is carried as a narrow extract. The N′ composition is marked as an addition". Next
  step 2 is drafting the extract, "followed by an independent non-author review of it and then a
  ChatGPT exact-head review". This file is that non-author review.
- **Reviewer.** I wrote neither the extract nor the Bell landing plan.
- **Method.** Hand reasoning only. Sources were read with `git show` at their pins, and reviews and
  comments through the host API. I ran no computation on any OI rule, no probe, and no Lean build.
  The only commands run were `git show`, `cmp`, `sha256sum`, `wc` and `git rev-parse` on file
  bytes. Nothing was written to the repository, and no worktree was created.
- **Sources.**
  - SB r2 at `86a413c8` (S:1–356, with S:153, S:167–171, S:11 and S:313–331).
  - BS r2 at `e1534b08` (BS:90–196 and BS:232–255).
  - `papers/Main.md` at `cac5d264`, `86a413c8` and `c3b5f37a`.
  - `recursive-substates/README.md`:23 on `main`.
  - #1274 at `fef94857` (`DEPENDENCIES.md`:20–28, `NEW-RESULTS.md`:504–509 and :641, `STATUS.md`:160–163).
  - The plan's `LANDING-PLAN.md` §2.4, §2.5, §3.2, §5.2, §5.3 and §6.3, `STATUS-SB-L3.md`,
    `REVIEW-BELL-PLAN-r1.md` S7/S8 and `CONFIRM-BELL-PLAN-r2.md` C3.
  - Reviews 5857227567 and 5857981727 (PR #1231) and 5858000929 and 5859960068 (PR #1232).
  - `verification/lean-mathlib/OIBridge/RegionTower.lean` on `main`. I read its statements; I did
    not build it.

***

## 1. Check results

### 1.1 Byte-exactness and §0 (X:8–34)

- **The quotation is exact.** X:39–43 (between the fences at X:38 and X:44) and the output of
  `git show 86a413c8…:<source> | sed -n 167,171p` are identical under `cmp`: 5 lines, 1,364 bytes,
  SHA-256 `f1450a7a…cb87`. The source contains no `~~~~`, so the fence cannot close early.
- **The source pins are correct.**
  - Source blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`.
  - SHA-256 `662b9cba…48fd`.
  - 356 lines.
  - The parent of `86a413c8` is `b94b283a`, and the parent of that is `cac5d264`. `cac5d264` is on
    `main`.
- **The BS pin is correct.** BS blob `5814e479b16929fe8ab045a3f3b8fc4987704633` at `e1534b08`.
- **The Main pins are correct.**
  - `papers/Main.md` is the same blob (`5b73da57…`) at `cac5d264` and at `86a413c8`.
  - At `c3b5f37a`, line 362 begins with the full text of old line 364 as an exact byte prefix,
    followed by the `G_φ^K` and linear-update sentences.
- **The owner quotations are verbatim.** Both are substrings of comments 6874036684 and 6873193841.

### 1.2 Additions

- **[+1] (X:48–59) is true.**
  - The five sentences of Main:364 at `cac5d264`/`86a413c8` recur byte-identically as the start of
    Main:362 at `c3b5f37a`.
  - L3 uses only `G_φ` (the `K = S` graph) and the cone induction. It uses neither `G_φ^K` nor the
    linear-update clause.
- **[+2] (X:61–80) is true, with a nit on line references (R12).**
  - Directed (Sep) is implied by symmetrized (Sep), because directed distance ≥ symmetrized
    distance. So the extension weakens a hypothesis and strengthens nothing.
  - The third bullet is a needed hypothesis: if `M` lay inside a generator region, its content
    would not be part of Ω.
- **[+3] (X:82–98): re-derived by hand. Valid, and it adds no step. The hypothesis list is
  incomplete (R2).**
  - *Step 1 with directed distance.* Write `N⁻(i)` for the inputs on which output `i` depends for
    some state. Under (F), output `i` is a function of `x|_{N⁻(i)}`; this is Main's first step,
    which uses finite `V` and the full product.
  - Induction on `k` then gives the following. `(φ^k x)_i` is a function of the inputs from which a
    directed walk of length exactly `k` reaches `i`. Every such input has a directed path of length
    ≤ `k` to `i`.
  - Directed (Sep) says no directed path of length ≤ `t − t_s` runs from `G_B` into `R_A^t`. So
    `x_t|_{R_A^t}` does not depend on `x_{t_s}|_{G_B}`, for every `t` in the window, and hence
    neither does `h_A`.
  - That is step 1 as S:169 states it. N′'s proof (BS:190–191) then needs only three things:
    1. `V = W ⊔ G_A ⊔ G_B`, so `h_A` is a function of `(x|_W, x|_{G_A})`.
    2. The injective chart `x|_{G_A} ↦ (a, ρ_A)` (BS:185).
    3. Steps 3–4 with `λ*` in place of Ω.
  - Nothing in 1–3 uses the symmetrized distance. The composition is therefore exactly "S:169's
    step 1, inserted into BS:190–191". `M`'s content belongs to Ω, and hence to `λ*`, by the third
    bullet of [+2].
  - (MI\*) is correctly required for `λ* = (Ω, ρ_A, ρ_B)`, and correctly not replaced by (MI) for
    Ω (BS:193; review 5857981727 item 3).
- **[+4] (X:100–112): the finite-depth restriction is genuine. The D3 citation is correct.** Two
  wordings need fixing (R3, R4).
  - Theorem N/N′ assume (F), which includes finite `S_i`.
  - Step 1 does not need finite `S_i`: the cone step uses finiteness of `V` only (S:143, L1). Step
    3, the mixture over the law of Ω or `λ*`, does need it. For a general infinite tower it has to
    become an integral, with measurable responses.
  - That extension is not automatic. A finite-valued record can depend on infinitely many digits.
    Where only finitely many digits are read, as in B1, a finite reduction suffices instead (R10).
  - `DEPENDENCIES.md`:24 at `fef94857` is row D3: "L2 (S:153) and class (a)3 (S:263), not
    carried … support off `main` (gap)". OQ-4 keeps D3 open under #1169.
  - `NEW-RESULTS.md`:507 at `fef94857` carries N2 "conditional on L3".
- **[+5] (X:114–122) is true, except for the last clause (R5).** Review 5858000929's quoted
  sentence was checked: "The classical common-cause observation is also correct under MI."
- **[+6] (X:124–132) is true, with a nit (R10).** README.md:23 says B1 acts by
  `T_m : b_0 ↦ b_0 ⊕ b_m` with "others fixed", and "Only the specified finite level m is accessed".
  The wording is C3's replacement, verbatim.
- **[+7] (X:134–143) is true, and S5 cannot fail.** At `86a413c8` the S5 block is
  `generic_substate_checks.py`:240–257 (lines 258–259 are blank; seed 20261111 at :16).
  - Each case is `Σ w(m,x,y)/tot · h_A(m,x,a) h_B(m,y,b)`. The weights `w ≥ 0` do not depend on
    `(a,b)`, and `tot` is their sum, or 1 when every weight is 0.
  - This is a sub-convex combination of deterministic local tables. So `|CHSH| ≤ 2 · Σw/tot ≤ 2`
    for every draw, by the pointwise identity at BS:177–178.
  - S5 cannot exercise the directed-cone step. "Provenance, not support" is correct (R11 makes the
    argument explicit).
- **[+8] (X:145–152): the negative claim is false (R1).**

### 1.3 Reference table (X:154–177)

- **Correct rows:** Main:364 → Main:362, and B1 → README.md:23 (both support on `main`); (Sep) at
  BS:150, step 1 at BS:168–170, Ω at BS:144–145, and BS:247–249 ("Either breaks (Sep) at graph
  distance ≤ 2", at :249) (all in the package); and review 5857981727 and §6 (both provenance).
- **The cone lemma row is correct but incomplete.** "Support on `main` (symmetrized form);
  directed reading [A] in this record" understates the directed reading, which has kernel support
  for its induction (R1).
- **The S5 row is acceptable.** "Provenance; not carried" is acceptable because the quoted S5
  sentence's result follows from the hand argument in R11, not from the run.
- **The lead-in (X:173–177) is correct.**
  - #1274 lands ahead of the package (OQ order), so its rows are support on `main` at landing. Its
    line numbers should be re-read at #1274's landed commit.
  - The plan-directory files are provenance. LP §5.3 keeps them off `main`, which bears on R7.

### 1.4 Status (X:179–185)

- **"Partially verified (model-reviewed, not independently verified)" is right for L3** under the
  vocabulary of STATUS-SB-L3:104–109. L3's statement and argument were reviewed in r1 (5858000929;
  S:167–170 are unchanged since r1). It rests on BS Theorem N [A], itself model-reviewed only.
  Nothing is kernel-checked end to end.
- **[+3] was correctly marked unreviewed at this head.**
- **[+3] now counts as reviewed.** This review re-derived it and found it correct, given the full
  hypothesis list of R2. That makes it one non-author model review. It is not independent
  mathematical verification, and the ChatGPT exact-head review is still pending (R6).

### 1.5 Writer-noted spec differences

| Difference | Assessment |
|---|---|
| BS:190–191 instead of LP's "BS:190" | Acceptable, and more accurate: the proof's last sentence and ∎ are on BS:191. |
| §6 read as SB §6 | Correct. S:11 fixes the convention "(review ids in §6)", and S:320 lists 5857981727. Read first-hand, review 5857981727 has numbered items 1–5 and a notes list, but no §6. |
| Destination `bell-landing-20261114/SB-L3.md` instead of LP §5.2's `…/substate-bridge-l3-<date>/SB-L3.md` | Acceptable for the draft, provided the file moves to the planned path in the package. Its sibling-file citations then need the change in R7. |
| `cac5d264` as Main's pin at the source | Correct. S:7 pins `main` = `cac5d264`, and Main's blob is identical at `86a413c8` (wording nit R13). |

### 1.6 Overstatement and native claims

- **No native OI or OI-wide claim is made.**
  - [+5] excludes measurement-dependent laws.
  - X:185 says "Not adopted; no manuscript claim is affected".
  - Nothing promotes Theorem N/N′ beyond 𝒞_sep with its protocol posits.
- **The only stronger-than-source statements are two wordings.**
  - X:110–111 drops a restriction (R4).
  - X:105's "holds" sits next to "however deep" (R3).
- **One statement contradicts L3 (R5).**
- **One statement understates support (R1).**
- **The quotation's "however deep" is acceptable.** It is verbatim source text inside a marked
  quotation, narrowed by [+4]. It is not an assertion in the record's own voice, provided R3 is
  applied.

***

## 2. Findings

**R1 (should-fix; apply before landing). [+8] makes a false negative claim. The directed cone
induction is kernel-checked on `main`.**
- **Where.** X:151–152 says "No kernel statement, exact computation or exhaustive check supports
  the directed-cone step." X:72–74 and X:163 say the directed form is only [A].
- **The kernel theorem.** `verification/lean-mathlib/OIBridge/RegionTower.lean` on `main` (imported
  by `OIBridge.lean`:161; family listed in the census, `lean-manuscript-census.json`:349; no `sorry`
  or `axiom` in the file) defines:
  - `CouplingGraph φ`, with `nbhd : ι → Finset ι` and
    `local_dep : ∀ i, DependsOnlyOn (fun s => φ s i) (nbhd i)` (:254–256). `nbhd i` is the set of
    sites that `i`'s next value depends on: the in-neighbourhood, with no symmetrization.
  - `ball G A (k+1) = (ball G A k).biUnion G.nbhd` (:259–261), which is backward reachability.
- **What it proves.** `iterate_dependsOnlyOn_ball` (:283) and `readout_unaffected_outside_ball`
  (:304) prove that, after `k` steps, an `A`-supported function depends only on `ball G A k`. That
  is exactly the directed induction.
- **What it does not cover.**
  - Instantiating `nbhd` with Main's one-step dependency sets is Main's first step [P] (finite `V`,
    full product).
  - The kernel uses one alphabet `Q` for every site, so `∏ S_i` is embedded coordinatewise.
- **Consequence.** The directed-cone step has [K] support for its induction and [P] for its
  instance. L3's status is unchanged, because it still rests on Theorem N [A]. §A.19 requires a
  corpus-wide search before a negative support claim.
- **Replacement for X:149–152.** "L3 is a paper argument [A] on Main's cone lemma (Main:362, paper
  proof on `main`) and on Bell-scope Theorem N, itself a paper argument on that lemma (BS:159–178).
  The induction in the directed form L3 uses is kernel-checked on `main`:
  `iterate_dependsOnlyOn_ball` and `readout_unaffected_outside_ball`
  (`verification/lean-mathlib/OIBridge/RegionTower.lean`:283, :304) prove, for any update with
  per-site in-neighbourhoods `nbhd`, that an `A`-supported readout after `k` steps depends only on
  the `k`-fold backward neighbourhood of `A`. That `nbhd i` may be taken to be the set of inputs on
  which output `i` depends for some state is Main's first step (Main:362, finite `V`), a paper
  proof. Steps 2–4 of Theorem N and N′, and [+3], a paper composition on S:169 and BS:190–191,
  have no kernel, exact or exhaustive support."
- **Replacement for X:73–74.** "… the directed form follows by the same induction. That induction
  is kernel-checked for per-site in-neighbourhoods (`OIBridge/RegionTower.lean`:283); its instance
  for Main's dependency sets is Main's first step [P]."
- **Replacement for the X:163 class cell.** "support on `main` (symmetrized form, Main:362 [P];
  directed induction, `OIBridge/RegionTower.lean`:283 [K])".
- **Propagate (§A.25)** to `STATUS-SB-L3.md`:86 and :116, whose remediation example "a kernel
  formalization of the directed cone lemma" already exists for the induction, and to
  `LANDING-PLAN.md` §2.4.

**R2 (should-fix). [+3]'s hypothesis list is incomplete, and it describes N′'s proof slightly too
narrowly.**
- **Where.** X:95–97 lists "(D), (F), (Gen), (Rec), directed (Sep) and (MI\*)".
- **Missing hypotheses.**
  - The finite jointly admissible menu (BS:116).
  - Every-run outputs with the ⊥-rule (BS:126, BS:148–149), and no postselection (BS:126,
    :234–235).
  - [+2]'s third bullet, which "`M`'s content … is part of Ω" needs.
- **Missing proof step.** N′'s proof also uses the injective chart (BS:185, :190) in place of
  step 2.
- **Replacement for X:95–98.** "Theorem N′'s proof consists of step 1, the chart identification
  `(x_{t_s}|_W, x_{t_s}|_{G_A}) = (Ω, ρ_A, a)` (BS:185, :190) and steps 3–4. None of these but
  step 1 uses the distance. With step 1 read as in statement 1, the conclusion of Theorem N′ holds
  under (D), (F), (Gen), (Rec), directed (Sep) and (MI\*), with the finite jointly admissible menu,
  every-run outputs with the ⊥-rule and no postselection (BS:116, :126), and the third hypothesis
  of [+2]. `M`'s content at `t_s` is then part of Ω, hence of λ\*, and `M` is a common cause. This
  composes the two statements and adds no step to either."

**R3 (should-fix). [+4] misdescribes SB L2, and its first sentence reads as endorsing "however
deep".**
- **The L2 gloss is wrong.** X:108 glosses S:153 as "Bell ceiling for a measurable hidden carrier".
  S:153's title is "Bell ceiling with site-fibred towers", and its conclusion is stated for "a
  site-fibred tower under a stencil-respecting rule". L3's `M` is a shared factor with edges to both
  wings, so it is not site-fibred (it is route A's N1, S:179). What an infinite-depth `M` needs is
  L2's measurable-λ argument (step 3 as an integral; Bell's theorem for measurable λ [L]) applied to
  a shared factor, together with L1's alphabet-free cone. SB states this extension for site-fibred
  towers only.
- **"Holds" sits next to "however deep".** In X:105, "Consequence (i) of S:171 ("however deep")
  holds under the hypotheses of [+2]" can be read as endorsing the unbounded wording.
- **Replacement for X:105–110.** "Consequence (i) of S:171 is carried for finite depth only. Under
  the hypotheses of [+2], with (MI) for Ω (or (MI\*)) and directed (Sep), a shared static or
  autonomously evolving substate of any finite depth cannot by itself produce a Bell violation.
  "However deep" is not supported here for an infinite tower. L3 inherits (F), finite `V` and
  finite `S_i`. An infinite-depth shared factor needs a measurable-λ form of Theorem N/N′. SB L2
  (S:153) gives that form for site-fibred towers, not for a shared factor. This extract carries
  neither. The corresponding open gap is D3 of #1274
  (`intervene-substate-results-20261113/DEPENDENCIES.md`:24 at `fef94857`), open under #1169."

**R4 (should-fix). [+4]'s last sentence is unrestricted.**
- **Where.** X:110–111: "Parameter independence fails only through a directed path generator →
  factor → record".
- **Why it is too strong.** Read as stated, it is false: routes B and C (S:177–181) break parameter
  independence with no shared factor. S:171 (ii) states the point for a wing–mode–wing path only.
  The sentence came from review r1's S8 replacement, and `STATUS-SB-L3.md`:70–71 repeats it.
- **Replacement (here and in `STATUS-SB-L3.md`:70–71).** "Through a shared factor, parameter
  independence can fail only along a directed path generator → factor → record within the record
  window: requirement N2 of route A, which #1274 carries conditional on L3 (`NEW-RESULTS.md`:507 at
  `fef94857`)."

**R5 (should-fix). [+5]'s last clause contradicts L3.**
- **Where.** X:121–122: "L3 also says nothing about … the window in which (Sep) fails".
- **Why it contradicts L3.** L3's content, consequence (ii), is precisely a case in which (Sep) as
  BS writes it fails (wing–mode–wing at symmetrized distance ≤ 2) while directed (Sep) holds.
- **Replacement.** "… about routes B and C, or about protocols in which directed (Sep) fails,
  including the window of wings spacelike at the wave speed but inside the graph cone (Main:414 at
  `c3b5f37a`)."

**R6 (should-fix). §4's status needs to record this review and give a status per result.**
- **Where.** X:183–185.
- **Replacement.** "**Status:** partially verified (model-reviewed, not independently verified);
  conditional on the hypotheses of [+2]; accountable Issue #1169. L3's statement and argument were
  model-reviewed at the source (review 5858000929 at `b94b283a`; S:167–170 unchanged since). The
  composition [+3] was re-derived in the independent non-author review of this record at
  `eac7692c`. That is a model review, not independent verification. The ChatGPT exact-head review is
  pending. Not adopted; no manuscript claim is affected."
- **Propagate.** Update `STATUS-SB-L3.md`:117 ("exploratory until the package's reviews") to match.

**R7 (should-fix). Attributions name plan-directory files by bare filename.**
- **Where.**
  - `STATUS-SB-L3.md` at X:50, :64, :103, :116, :137, :147 and :156.
  - `LANDING-PLAN.md` at X:84 and :156.
  - `REVIEW-BELL-PLAN-r1.md` at X:103 and :136.
  - `CONFIRM-BELL-PLAN-r2.md` at X:127.
- **Why it matters.** LP §5.3 keeps the plan directory off `main`. STATUS-SB-L3:4–5 renames the
  note to `substate-bridge-l3-<date>/STATUS.md` at landing. As landed, the bare names would not
  resolve, or would resolve to the wrong file.
- **Fix.**
  - Give each plan-file attribution its branch and commit once, in §0. For example: "Plan files
    named below are on `records/bell-landing-plan-868-20261114` at `3859c3ef` (provenance; they do
    not land)."
  - Cite the landed note as "`STATUS.md` beside this record".
  - Add `LANDING-PLAN.md` to the `SB-L3.md` row of LP §6.3:495. That row now says the notes cite
    neither plan file, but `SB-L3.md` does.

**R8 (nit). X:4–6 overstates the labelling.**
- **Where.** "Every line outside the fenced quotation … is labelled **[+n]**".
- **Why.** The title, the intro, the headings, §3 and §4 are additions without a number.
- **Replacement.** "Every line outside the fenced quotation in §1 is an addition made for this
  extract and is not text of the source. Each substantive addition is numbered **[+0]–[+8]** with
  its attribution; §3 and §4 are additions by the extract's writer."

**R9 (nit). The title (X:1) states the slogan unconditionally, and with a different condition.**
- **Where.** "a shared factor that no setting writes is a common cause".
- **Why.** L3's condition is the absence of a directed remote-generator-to-record path within the
  window. A setting may write `M` too late to reach the other wing.
- **Replacement.** "# SB L3: a shared hidden factor with no directed remote-setting-to-record path
  is a common cause (narrow extract)". Use the same title in `STATUS-SB-L3.md`:1.

**R10 (nit). [+6] should say which bit B1 writes, and that B1 has no wings.**
- **Replacement for X:131–132.** "B1 reads `b_0` and `b_m` and writes only `b_0`, for one fixed
  finite `m` (README.md:23); the remainder of its sequence is fixed and unread. B1 is a single-cell
  model with no spatial sites (S:148). For a B1-type bit read by both wings as a shared factor, the
  finite-depth consequence applies through the finite factor `(b_0, b_m)`."

**R11 (nit). [+7]'s "cannot fail" should carry its one-line reason, and the line range can be
tightened.**
- **Replacement for X:139–143.** "… refer to `probes/generic_substate_checks.py`:240–257 at
  `86a413c8`, which this extract does not carry. S5 draws response tables `h_A(m, l_A, a)`,
  `h_B(m, l_B, b)` that already factorize through the shared mode, with nonnegative,
  setting-independent weights. Each case is therefore a convex combination of deterministic local
  tables, so `|CHSH| ≤ 2` by the pointwise identity of BS:177–178 whatever the draw. The check
  cannot fail and does not exercise the directed-cone step that is L3's content. It is provenance,
  not support; the quoted sentence's result holds by this argument."

**R12 (nit). [+2] cites one range for hypotheses that are stated elsewhere.**
- **Where.** X:66–68 cites "BS:159–178" for the finite menu, every-run outputs and no postselection.
- **Fix.** Add "(BS:116, :126, :148–149; NBA's domain BS:232–236)".

**R13 (nit). [+0]'s Main pin wording is loose.**
- **Where.** X:26–28.
- **Replacement.** "**Main.** "Main:n" is line n of `papers/Main.md`. S:7 pins it at `cac5d264`
  (blob `5b73da57…`, identical at `86a413c8`); this extract re-pins it to `main` at
  `c3b5f37a354bb26437e2e0165c576a347a63c153` ([+1])."

**R14 (nit; cross-propagation marker, outside this file).**
- **Where.** BS's claim table classifies C1, the cone lemma, as layer P only (BS:96). R1's kernel
  theorem also covers C1's induction.
- **Fix.** BS lands byte-identical, so record this in `STATUS-BS.md` and leave BS unchanged.

***

## 3. Disposition

- **Accept the extract with R1–R7 applied.** R8–R14 are at the writer's discretion.
- **After R2, [+3] counts as reviewed** by one independent non-author model review. It is not
  independently verified.
- **L3 remains partially verified**, conditional on Theorem N or N′ with directed (Sep), for finite
  depth only.
- **No native OI Bell result, OI-wide no-go or escape is stated, and none should be.**
- **This review authorizes nothing.** It covers no merge, adoption, probe replay or computation.
