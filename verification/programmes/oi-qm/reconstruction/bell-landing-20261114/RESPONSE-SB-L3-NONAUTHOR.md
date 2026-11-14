# Response to the non-author review of the SB-L3 extract

- **Review.** `REVIEW-SB-L3-NONAUTHOR.md` at `1bc55b29` on `records/bell-landing-plan-868-20261114`,
  reviewing `SB-L3.md` at `eac7692c`: ACCEPT WITH CHANGES, no blocking finding. "X:n" is line n of
  `SB-L3.md` at `eac7692c`; "X′:n" is line n of the revised working-tree file. Other files are cited
  at their revised lines.
- **Scope.** R1–R14 applied; the review's replacement text is used wherever it gives one. Paper edits
  only; no computation, no Lean build (the module's statements were read on `main`).
- **Quotation.** X′:46–50, between the fences at X′:45 and X′:51, still equal
  `git show 86a413c88cd14d344aa41b6f47885aeb24da6910:<source> | sed -n 167,171p` under `cmp`.

## R1 check before use

`verification/lean-mathlib/OIBridge/RegionTower.lean` at `c3b5f37a` (`main`) was read. It defines
`CouplingGraph φ` with `nbhd : ι → Finset ι` and `local_dep : ∀ i, DependsOnlyOn (fun s => φ s i)
(nbhd i)` (:254–256). `nbhd i` is the set the next value at `i` depends on, with no symmetrization.
`ball G A (k+1) = (ball G A k).biUnion G.nbhd` (:259–261) iterates it backward.
`iterate_dependsOnlyOn_ball` (:283) and `readout_unaffected_outside_ball` (:304) are stated as the
review says. The module contains no `sorry`, and `OIBridge.lean`:161 imports it. The neighbourhoods
are one-directional, so the review's reading holds.

## Dispositions

| Finding | Disposition | Where |
|---|---|---|
| R1 | Applied with the review's replacements. In [+8], one sentence from the review's "What it does not cover" was added: the kernel uses one alphabet `Q`, so `∏ S_i` enters through a coordinatewise embedding. The cone-lemma row's "Resolves to" cell now points to [+2] and [+8] in place of "its directed reading is L3's argument". L3's status is unchanged. | `SB-L3.md` X′:80–84 (was X:72–74), X′:170–182 (was X:145–152), X′:194 (was X:163); `STATUS-SB-L3.md`:93–96 (was :86), :126 (was :116); `LANDING-PLAN.md` §2.4, :157–160. Mirror: `STATUS-SB-L3.md`:83–87 (was :78–80), the same sentence as X:73–74. |
| R2 | Applied with the review's replacement for X:95–98: the chart step (BS:185, :190), the finite menu, every-run outputs with the ⊥-rule, no postselection (BS:116, :126) and [+2]'s third hypothesis. | `SB-L3.md` X′:106–112; attribution X′:94–96 |
| R3 | Applied with the review's replacement for X:105–110. It says plainly that "however deep" is not supported for an infinite tower, and that L2 is stated for site-fibred towers. | `SB-L3.md` X′:120–126. Mirror: `STATUS-SB-L3.md`:72–73, which glossed L2 the same way ("infinite towers need SB L2"). |
| R4 | Applied: "Through a shared factor, … within the record window". | `SB-L3.md` X′:127–129 (was X:110–112); `STATUS-SB-L3.md`:74–76 (was :70–71) |
| R5 | Applied: protocols in which directed (Sep) fails, including the window of Main:414 at `c3b5f37a`. | `SB-L3.md` X′:138–141 (was X:121–122) |
| R6 | Applied with the review's replacement for §4. The N′ row now records one non-author model review: not independent verification, with the ChatGPT exact-head review pending. Mirrors of the same fact: the Reviews paragraph and the claim block, which said the carried text and the N′ addition were not yet reviewed. | `SB-L3.md` X′:216–221 (was X:183–185); `STATUS-SB-L3.md`:127 (was :117), :116's last cell, now :126; mirrors :51–56, :66–68 |
| R7 | Applied. The branch and commit of the plan files are given once, in §0. Sibling-note citations read "`STATUS.md` beside this record", and §0 says it is drafted as `STATUS-SB-L3.md`. The plan's §6.3 row now records that `SB-L3.md` cites `LANDING-PLAN.md`. | `SB-L3.md` X′:11, :30–35, :57–58, :71–72, :94, :117, :133, :158, :170, :186–187, :204–210; `LANDING-PLAN.md`:498 (was :495) |
| R8 | Applied, with the review's replacement. | `SB-L3.md` X′:3–7 |
| R9 | Applied, with the review's title. | `SB-L3.md` X′:1; `STATUS-SB-L3.md`:1 |
| R10 | Applied, with the review's replacement. | `SB-L3.md` X′:149–153 |
| R11 | Applied, with the review's replacement; line range 240–257. | `SB-L3.md` X′:160–166, :198 |
| R12 | Applied. | `SB-L3.md` X′:76 |
| R13 | Applied, with the review's replacement. | `SB-L3.md` X′:27–29 |
| R14 | Applied in `STATUS-BS.md`. BS is not changed. | `STATUS-BS.md`:121–126 |

## Not changed, for the coordinator

- **R10 and R11 mirrors.** `STATUS-SB-L3.md`:139 (B1 dependency row) and `LANDING-PLAN.md`:500 (§6.3
  B1 row) carried C3's "reads and writes only `b_0` and `b_m`"; `STATUS-SB-L3.md`:97 and
  `LANDING-PLAN.md`:153 cited S5 at `generic_substate_checks.py`:241–259. These rows were not named
  for change. The coordinator propagated R10 ("reads `b_0` and `b_m` and writes only `b_0`") and R11
  (:240–257) to all four in the same commit.
- **Item-8 condition in `STATUS-SB-L3.md` "Landing".** It still reads "not met for the carried
  text". That remains true while the ChatGPT exact-head review is pending, so it was not edited.

## Diff summary (working tree against `d712097f`, which adds only `REVIEW-BS-r2-NONAUTHOR.md` after `1bc55b29`)

- `SB-L3.md`: R1–R13; quotation byte-identical.
- `STATUS-SB-L3.md`:
  - the title (R9);
  - the Reviews paragraph and the claim block (R6 mirrors);
  - the consequence paragraph (R3 mirror, R4);
  - the cone-lemma hypothesis and the first limitation (R1);
  - the two status rows (R1, R6).
- `LANDING-PLAN.md`: the S5 bullet in §2.4 (R1); the plan-files row in §6.3 (R7).
- `STATUS-BS.md`: "Independently verified" bullet (R14).
- New: this file.

## ChatGPT exact-head review 5903029353 at `8177c917`

Posted under `amaybaum`, 2026-11-14T08:11:19Z: ACCEPT WITH CHANGES, documentation only. Its two
changes are applied after `8177c917`; `SB-L3.md` is not changed.

| Change | Disposition | Where |
| --- | --- | --- |
| 1. `STATUS-SB-L3.md`: replace the future-tense statements with the pin of the reviewed extract; name the chart-identification step in the N′ composition; keep `M ⊂ W` and the directed no-path condition explicit in the scoped claim; update the review gate | Applied. | `STATUS-SB-L3.md` Source, "What the record supports", Reviews, status table, Landing |
| 2. R10 mirrors: B1 reads `b_0` and `b_m` and writes only `b_0` | Applied. | `STATUS-SB-L3.md` dependency row; `LANDING-PLAN.md` §6.3 B1 row |

The same review records a separate gate for Bell-scope r2: findings 1–3 of
`REVIEW-BS-r2-NONAUTHOR.md` need an owner-selected route (a corrected `STATUS-BS.md` or a
Bell-scope r3). `STATUS-BS.md` is not changed for them here.
