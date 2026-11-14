# SB L3: a shared hidden factor with no directed remote-setting-to-record path is a common cause (narrow extract)

This record carries one lemma of SUBSTATE-BRIDGE-1 unit 1 r2, L3 (its §3.2), as a narrow extract:
the five source lines S:167–171, quoted verbatim in §1, and nothing else from that file. Every line
outside the fenced quotation in §1 is an addition made for this extract and is not text of the
source. Each substantive addition is numbered **[+0]–[+8]** with its attribution; §3 and §4 are
additions by the extract's writer.

## 0. Pin block [+0]

*Addition [+0], by the extract's writer, from `STATUS.md` beside this record.*

- **Source file.**
  `verification/programmes/oi-qm/reconstruction/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md`
  at `86a413c88cd14d344aa41b6f47885aeb24da6910` (branch `research/substate-bridge-1-20261111`,
  PR #1232, r2; parent `b94b283a`, r1; base `cac5d264`), blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`,
  SHA-256 `662b9cbaab4237a357174b675c7ee7734c4d4512ef68d530555111230bde48fd`, 356 lines. "S:n" is
  line n of that file.
- **Extract.** S:167–171 (§3.2, L3): 5 lines, 1,364 bytes including the final newline, SHA-256
  `f1450a7a07f3efdbdbc391d4e1c697dd2a046c08ec10a1b0555dd359c8efcb87`. Recipe: `git show
  86a413c88cd14d344aa41b6f47885aeb24da6910:<source file> | sed -n 167,171p`; the lines between the
  fence markers in §1 equal that output byte for byte.
- **Bell-scope.** "BS:n" is line n of
  `verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/BELL-SCOPE-UNIT1.md`
  at `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918` (PR #1231, r2), blob
  `5814e479b16929fe8ab045a3f3b8fc4987704633`, which lands in the same package.
- **Main.** "Main:n" is line n of `papers/Main.md`. S:7 pins it at `cac5d264` (blob `5b73da57…`,
  identical at `86a413c8`); this extract re-pins it to `main` at
  `c3b5f37a354bb26437e2e0165c576a347a63c153` ([+1]).
- **Plan files.** `LANDING-PLAN.md`, `REVIEW-BELL-PLAN-r1.md` and `CONFIRM-BELL-PLAN-r2.md`, named
  below, are in `verification/programmes/oi-qm/reconstruction/bell-landing-20261114/` on
  `records/bell-landing-plan-868-20261114` at `3859c3ef` (provenance; they do not land). "`STATUS.md`
  beside this record" is the status note drafted there as `STATUS-SB-L3.md`. The non-author review
  of this record is `REVIEW-SB-L3-NONAUTHOR.md` on the same branch at `1bc55b29`, reviewing
  `eac7692c`.
- **Owner decision.** #868 comment 6874036684 (`amaybaum`, 2026-11-14), route item OQ-3: "SB L3 is
  carried as a narrow extract. The N′ composition is marked as an addition." The package that
  carries it is option (1) of #868 comment 6873193841: "one combined Bell package: BS Theorem N and
  N′ (#1231), SB L3 (#1232) and the ladder r3 (#1273)".
- **Narrow extract.** No other line of SUBSTATE-BRIDGE-1 is carried: not its L1, L2, L4, routes
  A/B/C, N1–N4, §6 or probe files. The quoted lines keep the source's references; §3 resolves each.

## 1. Quotation: S:167–171, verbatim

~~~~text
### 3.2 L3: a shared factor is harmless unless a setting writes it [A; X S5]

Main's `G_φ` is "symmetrized for the spatial graph" (Main:364), and Bell-scope's (Sep) uses that symmetrized distance. The induction in the cone lemma is directed: output `i` depends on the inputs that have an edge *into* `i`. Let `M` be a hidden factor read by both wings (edges `M → R_A`, `M → R_B`). If there is no directed path from `G_B` to `R_A^t` of length at most `t − t_s`, then step 1 of Theorem N goes through with directed distance, `M`'s content at `t_s` is part of Ω, and the conclusion is unchanged: `M` is a common cause. S5 checks 300 random response tables with a shared mode and correlated priors: `|CHSH| ≤ 2` in each.

Two consequences. (i) A shared, static or autonomously evolving substate — B1's static bit, a conveyor of fresh digits delivered to both wings — cannot produce a Bell violation, however deep. (ii) Bell-scope's statement that a wing–mode–wing path "breaks (Sep) at graph distance ≤ 2" is correct for (Sep) as written, but parameter independence fails only if the path is directed generator → mode → record. (Sep) is sufficient, not sharp; this is a remark for that draft's review, not a correction made here. The independent re-review of Bell-scope r2 records the same point as a nonblocking note (review 5857981727, §6).
~~~~

## 2. Additions

### [+1] Re-pin of Main:364 to Main:362

*Addition, by the extract's writer; source drift measured in `STATUS.md` beside this record
("Source drift").*

S:169 cites Main:364 for the definition of `G_φ`. At `c3b5f37a` (`main`) the same sentence is
Main:362: "define the coupling graph $G_\varphi$ by one-step dependency: $i\sim j$ whenever the $i$th
output component of $\varphi$ depends on the $j$th input component for some state (symmetrized for
the spatial graph)", followed by the cone lemma, "Then, by induction, $(\varphi^k(s))_i$ depends
only on initial components in the graph ball $B_{G_\varphi}(i,k)$." The five sentences of the
paragraph at Main:364 (`86a413c8`) recur unchanged at Main:362 (`c3b5f37a`). Main:362 also defines
`G_φ^K` and states the linear-update clause; L3 uses neither. The quotation is not edited: "Main:364"
in S:169 reads as Main:362 on `main`.

### [+2] Hypotheses

*Addition, by the extract's writer; from BS §3.1–3.2 (BS:139–196) and `STATUS.md` beside this
record ("Hypotheses"); kernel citation and line references from the non-author review (R1, R12).*

- Every hypothesis of Bell-scope Theorem N (BS:159–178): (D), (F), (Gen), (Rec), (GI), every-run
  outputs with a fixed local failure rule, a finite jointly admissible menu, no postselection and
  (MI) for Ω (BS:116, :126, :148–149; NBA's domain BS:232–236); or of Theorem N′ (BS:185–191)
  with (MI\*) for λ\* = (Ω, ρ_A, ρ_B) in place of (GI) and (MI). In either case (Sep) (BS:150) is
  read with the directed distance: for every `t ∈ [t_s, T_A]`, no directed `G_φ` path of length at
  most `t − t_s` runs from `G_B` into `R_A^t`, and symmetrically for B.
- The directed reading of Main's cone lemma: `(φ^k(s))_i` depends only on components with a
  directed path into `i` of length at most `k`. Main:362 states the lemma for the symmetrized graph;
  the directed form follows by the same induction. That induction is kernel-checked for per-site
  in-neighbourhoods (`OIBridge/RegionTower.lean`:283); its instance for Main's dependency sets is
  Main's first step [P].
- The shared factor `M`'s content at `t_s` lies outside the generator regions, so it is part of
  `W = V ∖ (G_A ∪ G_B)` and of Ω = `x_{t_s}|_W` (BS:144–145), and (MI) or (MI\*) applies to it.

(D) and (F) are posits of the framework; (Gen), (Rec), (Sep), (GI) and the failure rule (BS's
⊥-rule) are properties of a protocol (BS:156–157); (MI) is posited (BS:153), and (MI\*) is a posited
hypothesis of Theorem N′ (BS:99, :187).

### [+3] Composition with Theorem N′

*Addition, by the extract's writer, as specified by the Bell landing plan (`LANDING-PLAN.md` §2.5);
its source is BS:190–191 at `e1534b08`; hypothesis list completed per the non-author review (R2).
Not in SUBSTATE-BRIDGE-1.*

The quotation names Theorem N only. Two cited statements compose to cover Theorem N′:

1. S:169: under the directed no-path condition, "step 1 of Theorem N goes through with directed
   distance".
2. BS:190–191, the proof of Theorem N′: "Step 1 does not use (GI) and gives `h_A` as a function of
   `(x_{t_s}|_W, x_{t_s}|_{G_A}) = (Ω, ρ_A, a)`, which is a function of `(λ*, a)`; symmetrically for
   B. Steps 3–4 apply with λ* in place of Ω. ∎"

Theorem N′'s proof consists of step 1, the chart identification
`(x_{t_s}|_W, x_{t_s}|_{G_A}) = (Ω, ρ_A, a)` (BS:185, :190) and steps 3–4. None of these but step 1
uses the distance. With step 1 read as in statement 1, the conclusion of Theorem N′ holds under (D),
(F), (Gen), (Rec), directed (Sep) and (MI\*), with the finite jointly admissible menu, every-run
outputs with the ⊥-rule and no postselection (BS:116, :126), and the third hypothesis of [+2].
`M`'s content at `t_s` is then part of Ω, hence of λ\*, and `M` is a common cause. This composes the
two statements and adds no step to either.

### [+4] Finite depth

*Addition, by the extract's writer; from review r1 of the landing plan, finding S8
(`REVIEW-BELL-PLAN-r1.md`), as adopted in `STATUS.md` beside this record; amended per the
non-author review (R3, R4).*

Consequence (i) of S:171 is carried for finite depth only. Under the hypotheses of [+2], with (MI)
for Ω (or (MI\*)) and directed (Sep), a shared static or autonomously evolving substate of any finite
depth cannot by itself produce a Bell violation. "However deep" is not supported here for an
infinite tower. L3 inherits (F), finite `V` and finite `S_i`. An infinite-depth shared factor needs
a measurable-λ form of Theorem N/N′. SB L2 (S:153) gives that form for site-fibred towers, not for
a shared factor. This extract carries neither. The corresponding open gap is D3 of #1274
(`intervene-substate-results-20261113/DEPENDENCIES.md`:24 at `fef94857`), open under #1169.
Through a shared factor, parameter independence can fail only along a directed path generator →
factor → record within the record window: requirement N2 of route A, which #1274 carries
conditional on L3 (`NEW-RESULTS.md`:507 at `fef94857`).

### [+5] Measurement independence kept

*Addition, by the extract's writer; from `STATUS.md` beside this record ("Hypotheses",
"Limitations") and review 5858000929 ("The classical common-cause observation is also correct under
MI"); last clause per the non-author review (R5).*

L3 and [+3] assume (MI) for Ω or (MI\*) for λ\*. A law in which the settings depend on Ω or λ\* is
outside their hypotheses, and nothing here is stated for it. L3 also says nothing about a factor
that a setting writes (route A with N2), about routes B and C, or about protocols in which directed
(Sep) fails, including the window of wings spacelike at the wave speed but inside the graph cone
(Main:414 at `c3b5f37a`).

### [+6] B1 through its finite factor

*Addition, by the extract's writer; wording from confirmation r2 of the landing plan, finding C3
(`CONFIRM-BELL-PLAN-r2.md`), amended per the non-author review (R10).*

"B1's static bit" (S:171) is Model B1 of the recursive-substates record,
`verification/programmes/substratum/recursive-substates/README.md`:23 on `main`. B1 reads `b_0` and
`b_m` and writes only `b_0`, for one fixed finite `m` (README.md:23); the remainder of its sequence
is fixed and unread. B1 is a single-cell model with no spatial sites (S:148). For a B1-type bit read
by both wings as a shared factor, the finite-depth consequence applies through the finite factor
`(b_0, b_m)`.

### [+7] The check S5

*Addition, by the extract's writer; from review r1 of the landing plan, finding S7, and `STATUS.md`
beside this record ("Limitations"); argument and line range per the non-author review (R11).*

The tag "[X S5]" (S:167) and the sentence "S5 checks 300 random response tables …" (S:169) refer to
`probes/generic_substate_checks.py`:240–257 at `86a413c8`, which this extract does not carry. S5
draws response tables `h_A(m, l_A, a)`, `h_B(m, l_B, b)` that already factorize through the shared
mode, with nonnegative, setting-independent weights. Each case is therefore a convex combination of
deterministic local tables, so `|CHSH| ≤ 2` by the pointwise identity of BS:177–178 whatever the
draw. The check cannot fail and does not exercise the directed-cone step that is L3's content. It
is provenance, not support; the quoted sentence's result holds by this argument.

### [+8] Support layer

*Addition, by the extract's writer; from `STATUS.md` beside this record ("What the record
supports"); kernel support per the non-author review (R1).*

L3 is a paper argument [A] on Main's cone lemma (Main:362, paper proof on `main`) and on Bell-scope
Theorem N, itself a paper argument on that lemma (BS:159–178). The induction in the directed form
L3 uses is kernel-checked on `main`: `iterate_dependsOnlyOn_ball` and
`readout_unaffected_outside_ball` (`verification/lean-mathlib/OIBridge/RegionTower.lean`:283, :304)
prove, for any update with per-site in-neighbourhoods `nbhd`, that an `A`-supported readout after
`k` steps depends only on the `k`-fold backward neighbourhood of `A`. That `nbhd i` may be taken to
be the set of inputs on which output `i` depends for some state is Main's first step (Main:362,
finite `V`), a paper proof. The kernel statement uses one alphabet `Q` for every site, so `∏ S_i`
enters it through a coordinatewise embedding. Steps 2–4 of Theorem N and N′, and [+3], a paper
composition on S:169 and BS:190–191, have no kernel, exact or exhaustive support.

## 3. Reference resolution

*Addition, by the extract's writer. Classes, as in `STATUS.md` beside this record and
`LANDING-PLAN.md` §6.3: **support on `main`**; **in the package** (support on `main` once the Bell
package lands, in the same merge); **provenance** (the extract's claims do not rest on the
referenced content).*

| Reference in S:167–171 | Resolves to | Class |
|---|---|---|
| "Main's `G_φ` is 'symmetrized for the spatial graph' (Main:364)" (S:169) | `papers/Main.md`:362 at `c3b5f37a` ([+1]) | support on `main` |
| "the cone lemma" (S:169) | Main:362, "Then, by induction, …"; directed form ([+2], [+8]) | support on `main` (symmetrized form, Main:362 [P]; directed induction, `OIBridge/RegionTower.lean`:283 [K]) |
| "Bell-scope's (Sep)" (S:169) | BS:150 at `e1534b08` | in the package |
| "step 1 of Theorem N" (S:169) | BS:168–170 (Theorem N, BS:159–178) | in the package |
| "Ω" (S:169) | BS:144–145, `Ω = x_{t_s}\|_W` | in the package |
| "[X S5]" (S:167); "S5 checks 300 random response tables …" (S:169) | `probes/generic_substate_checks.py`:240–257 at `86a413c8` ([+7]) | provenance; not carried |
| "B1's static bit" (S:171) | Model B1, `verification/programmes/substratum/recursive-substates/README.md`:23 ([+6]) | support on `main` |
| "Bell-scope's statement that a wing–mode–wing path 'breaks (Sep) at graph distance ≤ 2'" (S:171) | BS:247–249 | in the package |
| "review 5857981727" (S:171) | ChatGPT re-review of Bell-scope r2 at `e1534b08` | provenance (review) |
| "§6" (S:171) | SUBSTATE-BRIDGE-1 §6, its off-`main` reference table (S:313–331), which lists that review | provenance; not carried |

References in the additions: BS:116, :126, :148–149, :177–178, :185–191 and :232–236 are in the
package; `verification/lean-mathlib/OIBridge/RegionTower.lean`:283, :304 and Main:414 at `c3b5f37a`
are support on `main`; `NEW-RESULTS.md`:507 and `DEPENDENCIES.md`:24 at `fef94857` (#1274) are
support on `main` once #1274 lands ahead of the package, and provenance until then; S:7, S:148 and
S:153 (SB L2) are provenance and are not carried; `STATUS.md` beside this record is in the package;
reviews 5858000929 and 5857981727, the plan files and the non-author review named in [+0] are
provenance; #868 comments 6874036684 and 6873193841 are governance provenance.

## 4. Status

*Addition, by the extract's writer; per the non-author review (R6).*

**Status:** partially verified (model-reviewed, not independently verified); conditional on the
hypotheses of [+2]; accountable Issue #1169. L3's statement and argument were model-reviewed at the
source (review 5858000929 at `b94b283a`; S:167–170 unchanged since). The composition [+3] was
re-derived in the independent non-author review of this record at `eac7692c`. That is a model
review, not independent verification. The ChatGPT exact-head review is pending. Not adopted; no
manuscript claim is affected.
