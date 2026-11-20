# Independent non-author review: Bell debugging ladder r1 (#868)

Reviewer: fresh session, not an author of the ladder, BS, SB, QH or RC. Read-only. Hand reasoning only, plus hand
checks of the ladder's toy maps and three toy maps of the reviewer's own. No script, no computation on any OI rule,
no commit, push or post. Objects were fetched by name only (no `--depth`, `gc` or `prune`).

Record reviewed: `BELL-LADDER.md` (284 lines) and `NOTES.md` (77 lines) in this directory.
Authority: #868 c.6854708572 (`amaybaum`, 2026-11-13T13:44:26Z), read at the host. Its text matches the record's
quotations.

## Verdict: ACCEPT WITH CHANGES

**Ruling on Proposition AL: correct as a conditional proposition. Its relation to E2 is misstated, its
"identifies with certainty" clause is too strong, and one load-bearing hypothesis is implicit.**

- I re-derived steps 1–5 by hand and found no error.
- I found no hidden use of (Sep), (GI) or measurement independence.
- The coset hypothesis (AL2), together with complete-history (NS) on *fixed* regions, does the work that MI does in
  Theorem N′.
- Required changes C1–C4 below fix the relation to E2, narrow the dichotomy clause and make the implicit hypothesis
  explicit. None of them weakens the main implication: (AL1)–(AL4) + (NS) ⇒ the record law is Bell-local.

The ladder's other content is mostly correct and well sourced. The required changes there are:

- one wrong toy claim (check 4);
- one wrong reading in the control table;
- an unqualified access claim in §0;
- a use of the owner's term "escape demonstrated" that does not match the authorization's definition;
- a PPS scope overreach;
- a wrong line citation;
- item 8 classifications for RC and QH.

***

## 1. Proposition AL [A], step by step

**Step 1.** Each `x_t` is `φ^{t−t_s}(x_{t_s})`, which is affine. Restriction to a *fixed* region is a projection,
which is a homomorphism. So `(h_A, h_B) = L x_{t_s} + ℓ` with `L` a homomorphism.

- Correct. OA1 D5 (OA1:176–195 @ `c3b5f37a`, blob `5a16b213`) supports it, but the step is elementary.
- The step needs `R_A^t` and `R_B^t` to be independent of the state and of the settings; see C3.
- Bijectivity is indeed not used, provided the histories start at `t_s`. If earlier ticks are included they are
  affine in `x_{t_s}` because OI's `φ` is bijective (ledger (iii)), or one can move the reference slice back.

**Step 2.** Given `(x, y)`, `x_{t_s}` is uniform on `C_{xy} = C ∩ P^{-1}(x, y)`. This set is a coset of
`K = H ∩ ker P̄`.

- `e_x` exists because `(x, y_0)` is admissible, and `f_y` exists because `(x_0, y)` is admissible.
- Then `c_0 + e_x + f_y ∈ C` has `P = (x, y)`, so `C_{xy} = c_0 + e_x + f_y + K`. Correct.
- The step tacitly takes `e_{x_0} = 0` and `f_{y_0} = 0`, which step 4's `β_A(y_0) = 0` needs. State this.
- Corollary (not stated, but true): for a coset law, `(x, y_0)` and `(x_0, y)` admissible imply `(x, y)`
  admissible. Every coset setting support is therefore closed under products.

**Step 3.** This is Lemma 0 of T1 (T1:50–54): the pushforward of a uniform coset law by an affine map is uniform on
the image coset. Correct.

**Step 4.** Two uniform laws on cosets of one subgroup are equal iff the cosets are equal. (NS) at a single `x`
already gives `β_A(y) ∈ π_A M`. Correct.

**Step 5.** `α(x) − n_x = (α_A(x) − π_A n_x, 0)` and `β(y) − m_y = (0, β_B(y) − π_B m_y)`. With `λ` uniform on
`M`, the model `F_A(λ, x)`, `F_B(λ, y)` reproduces the conditional joint law of the full histories for every
admissible pair, and `λ`'s law does not depend on the settings. Correct.

- Every output that is a function of `h_A`, `h_B` is then Bell-local. This includes thresholded or non-affine
  extractors, heralds read inside the history and a fixed ⊥-rule.

### Counterexample hunt (§A.31, maximum skepticism)

| Attempt | Outcome |
|---|---|
| Coset law that correlates setting cells with hidden cells (MI fails), e.g. `λ = x + y` | Not a counterexample. If the correlated cell lies in a wing's fixed region or reaches it, that wing's complete history reveals the remote setting and (NS) fails; if it never reaches a region, it is irrelevant. AL is right that no MI hypothesis is needed, but only because (NS) is imposed on complete histories of fixed regions. |
| Non-affine local extractors | Covered: step 5 gives a hidden-variable model for the full histories. |
| Heralding without postselection | Covered when the herald is in the history and failures are mapped by a fixed rule. Conditioning on a post-setting event is excluded, as the record states. |
| Multi-valued settings, mixed finite abelian groups | Covered. |
| Non-abelian groups | Outside (AL1). Ledger (xiii) puts values in a finite abelian group (Main:724), so nothing in (vii)/(xiii) is lost. |
| Mixtures of coset laws | If each component satisfies (AL3) on a common menu, the conditional weight of component `k` given a menu pair is `∝ w_k/|P(C_k)|`, which does not depend on the pair. So "setting-independent mixture" holds automatically and the scope remark is correct. |
| **Setting-selected (lossy) read inside a fixed region** | **Load-bearing witness** (reviewer's toy, hand-checked; it uses the ladder's own carrier and `μ_0`). Use the linear update `λ_B0 ⊕= λ_A0`, `λ_B1 ⊕= λ_A0 ⊕ g_A`, an involution and inside (vii), with `μ_0` (coset-uniform, so MI* holds). After the tick, `λ_B = (ρ, ρ ⊕ x)`. Let A output `λ_A0 = ρ` and B output `λ_B[y] = ρ ⊕ xy`. This is the PR box, and the selected history `(y, λ_B[y])` is no-signalling. B's fixed-region history contains `(ρ, ρ ⊕ x)`, however, so complete-history (NS) fails, as AL requires. So with (vii), a coset law, cell-valued settings and MI all kept, the PR box is reachable exactly when no-signalling is imposed on less than the complete fixed-region history. This does not refute AL. It shows that "complete" and "fixed region" in (AL4) are hypotheses the record must state, and that the closing escape list holds only relative to that admissibility criterion (C3, C4). |

**Dichotomy clause.** Failure of (NS) gives, at some own setting `x`, two remote settings `y` and `y′` whose
A-history laws have disjoint supports (total variation 1). That is correct, but it is not "identifies the remote
setting":

- With more than two settings per side, A identifies `y` only modulo the relation `β_A(y) − β_A(y′) ∈ π_A M`.
- The discrimination is conditional on A's own setting, which need not be in `h_A` under (AL3).

See C2.

**Relation to OA2 Corollary E2 (OA2:606–613 @ `c3b5f37a`, blob `8f8ddf73`).** E2 assumes (H1) (an affine
bijection), H-AR, `q = 2`, parity outcomes and (xiv). It covers *every* law that satisfies (xiv), and it needs no
(NS): with additive remote dependence and a biased `Z_0`, an A-parity marginal can depend on `b`. AL needs a
coset-uniform law and (NS). So AL does not contain E2, and "extends E2 … to" is false. The two results trade
hypotheses (C1).

- OA2's `Z_4` example (`g(0) = g(1) = 0`, `g(2) = 1`, `B = ab`) already signals at the output level, so it is
  consistent with AL, as the record says.

**Scope of the conclusions.**

- §0 and §4 confine the class-(vii) conclusion to (vii) + coset laws + cell-valued settings + every-run accounting.
  It is not stated OI-wide.
- "Closes route C for the affine class under (AL2)–(AL4)" follows from AL. The record correctly calls it an
  expectation for the mixed-path unit, not a substitute for that unit.
  - Under §A.29 that expectation must not be entered as an expected outcome in the stage-2 preregistration. The
    preregistration fixes only the decision rule.
- Two requirements remain:
  - the escape lists must carry the complete-history criterion (C4);
  - the "For OI itself" heading reads wider than the conditional it introduces (C4).

**Priority and classification.** I searched main @ `c3b5f37a` for a two-wing coset or no-signalling Bell result:

- T1 Lemma A-T is single-wing and assumes the rest of the law is independent of `c`.
- OA1 D5 is map-level.
- obsmu Proposition C is single-wing (ANALYSIS.md:546ff.).
- Neither BS nor SB contains such a result.

ELABORATING for AL and NEW for the route-C consequence are supported.

***

## 2. Stages 0–7

### Citations

All of the following were verified at `c3b5f37a`:

- Main.md: blob `0db17597`. Lines :14–18, :97, :360, :362, :364–389, :392–410, :412, :414, :416–423, :427,
  :480–482, :516–518, :546–552, :562 and :724 say what the record says.
- `Equivalence.lean`: blob `9513665b`. `Qfb_imp_S` :245, `D_imp_Qfb` :294, `S_imp_D` :422 and
  `finite_horizon_equivalence` :462 are at the cited lines; :150–156 is the doc comment on the correlated initial
  law; :466–468 assembles the converses as composites.
- PPS :134–145.
- Substratum :131–133.

Off main, the following were verified at their heads:

- BS @ `e1534b08` (blob `5814e479`): (Gen)/(Rec)/(Sep)/(GI)/(MI) :140–157, Theorem N :159–178, N′ :185–196,
  Lemma G :198–228, NBA :232–244, composition :292–294, ε bound :317–330, contraction :345–355.
- SB @ `86a413c8` (blob `9ff0f077`): L4 :155, L3 :167–171, routes :177–181, N3/N4 :189–190, resolution :220.
- QH @ `ffc9cda4` (blob `ebf5215b`): :68–97 and :213–214.
- RC r7 @ `9f7d2612` (blob `f1ffac0e`).

### Classifications

| Stage | Reviewer finding |
|---|---|
| 0 | The content is correct. §A.34 is met: S⇒D, D⇒Q_fb and Q_fb⇒S are three separately witnessed kernel directions, and each converse is a composite (Lean :466–468). Optionally name the composites. The reading of the S⇒D construction as measurement-dependent is correct (the hidden register holds the whole trajectory, :364–372). |
| 1–2 | `φ_×, μ_0` gives `a = ρ`, `b = ρ ⊕ xy` and CHSH 4. Both complete single-run histories are no-signalling. The deterministic pad and pad reuse signal as stated. Correct. |
| 3–4 | `φ_0, μ_MD` is correct: (Sep) and (GI) hold, the box is PR and both histories are no-signalling. By hand, `I_ont = H(Ω) − 1 ≈ 2.41 − 1 = 1.41` bits, consistent with "far above 0.0309". |
| 5 | The hypotheses match BS Theorem N/N′, with one omission: **(Gen) requires disjoint generator regions** (BS:142) (C11). Main:364–389 is the exogenous form with different hypotheses (ii)/(iii). Citing it as a "Source" is fine; it is not the same hypothesis list. No hypothesis is extra; "finite menu" follows from (F). |
| 6 | The AL extension is correct as scoped (§1). **PPS:136 assumes each law is "common across setting interventions", which is MI.** It therefore supports the stage-3-relaxed branch only, not "stage 3 or 5 relaxed" (C9). |
| 7 | UNDETERMINED is correct. The SWAP/2 table is Bell-local over Pauli-axis product tests (a shared uniform triple; each wing outputs the bit for its axis), but QH:68–97 does not say so. That is a reviewer or writer [A] fact, and the native reachability is a QH [D] fact (C13). |

**Owner's classification term (C5).** The authorization defines "escape demonstrated" as "a *native* construction
with complete records and no-signalling checked". Stages 0–4 use the label for designed maps that are not native
(`φ_×` and `φ_0` are non-affine and outside (vii)). The preamble discloses this, but it redefines the owner's term,
so a reader of the table alone would take the stages as native escapes.

***

## 3. Controls

| Row | Finding |
|---|---|
| Coupling, general (`φ_0′ → φ_×`) | CHSH 2 → 4 with NS kept. Correct, and one change. |
| Coupling, (vii) (`ψ_0 → ψ_×`) | CHSH 2 → 2. Correct (`E = 1, 1, −1, −1`). The relabelling in check 5 is garbled: write `λ′ = ρ ⊕ x`, `a = λ′ ⊕ x`, `b = λ′` (C12). |
| Generator residue | Correct: (GI) fails, MI* holds and N′ applies (symmetrized (Sep) holds for `φ_0′`; see below). |
| `R_A ∋ g_B` | Correct; it changes access and extractor together, which the access change permits. Signalling. |
| **`R_A ∋ r_B`** | **The reading is wrong.** `r_B` is written through `λ_B[g_B]`, so `G_φ` has the edge `g_B → r_B` and (Sep) fails in both forms at the one-tick window. "No change" holds because the dependence is null on the support of `μ_0` (`λ_B = 0`). It is not the SB L3 common-cause case (C7). |
| Initial law (`μ_0 → μ_MD`) | CHSH 0 → 4. Correct. It lies outside the authorized control design ("holding the initial law … fixed") and is labelled as a third lever; keep the label. |

**Check 4.** The claim that `φ_0′` "breaks symmetrized (Sep)" is false at the stated one-tick window:

- In the symmetrized graph, `d(g_A, R_B) = 3` (`g_A–r_A–λ_A0–r_B`) and `d(g_B, R_A) = 2` (`g_B–r_B–λ_A0`), both
  above 1.
- `λ_A0` is a common cause under either form (C6).

**Observer-access claim.** §3 correctly limits it to the toy. §0:66 states it without that limit (C8).

***

## 4. Open premises and status of inputs

**§5 table and owner questions.** They are correctly stated and adopt nothing.

**Stale pins.** BS and SB both descend from `cac5d264` and cite Main there.

- At main, F1 is resolved: (x) is scoped to `G_φ^ref` (Main:724).
- F2 is resolved: ledger (v) no longer cites §3.3 for setting decorrelation, and (xiv) is itemized.
- SB L4 is covered by Main:362 for the linear update of (vii). L4 itself is broader (any abelian groups, no
  finiteness), so "superseded" is right for this ladder's use only.
- Line shifts: Main:364 → :362 and Main:726 → :724. Correct.

**Informational.**

- `research/rec-1-1169-20261113` has moved to `7f465d56` (P0 files added). REC-1-r7's blob is unchanged, but NOTES'
  "match the PR heads" is now stale.
- Review 5858000929 on #1232 is REVISE at `b94b283a`. The item 8 row groups it under "ACCEPT WITH NITS, `86a413c8`"
  (C14).

***

## 5. §A.42 item 8 and register

- **QH.** The stage-7 sentence uses QH's native-reachability content, so for that sentence the reference is support
  off main, not provenance (C13). Stage 4 is provenance. Correct.
- **RC.** (AL2)'s "`D_0` of RC §4" and stage 4's "RC row C4" use RC content. Both facts are on main: MP-0a at
  OA1:556–558 (the `D_0` form), μ-G at OA1:103–105, and settings as configuration content at OA1:111–112 and
  Main:42. Cite those, and RC becomes provenance (C13).
- **SB.** §4 consequence (iii) still cites SB L4 beside Main:362. Cite Main:362 alone.
- **Register.** This is a verification record, so §A.32/§A.33 do not bind. No self-narration or assert-then-qualify
  was found. The status labels are fine.

***

## 6. Required changes (exact old → new, against `BELL-LADDER.md` as it stands)

Old strings are quoted with the file's line wraps collapsed to single spaces. Each was checked to occur exactly once
in the file under that normalization. C11 keeps its blockquote marker, shown explicitly.

**C1** (lines 224–226).
- Old: "*Relation to sources.* ELABORATING: it extends OA2 Corollary E2 (OA2:606–613 [W]: affine, `q = 2`, parity
  outcomes, (xiv), CHSH ≤ 2 without spatial separation) to every finite abelian group and every local extractor,
  replacing H-AR and (xiv) by (NS) and (AL2)."
- New: "*Relation to sources.* ELABORATING. It sits alongside OA2 Corollary E2 (OA2:606–613 [W]: affine bijection
  (H1), H-AR, `q = 2`, parity outcomes, (xiv), CHSH ≤ 2 without spatial separation); neither contains the other. AL
  covers every finite abelian group and every local extractor of the complete histories, but needs (NS) and a
  coset-uniform law (AL2). E2 covers every law satisfying (xiv), coset-uniform or not, and needs no (NS), but only
  for `q = 2` parity outcomes under H-AR."

**C2** (lines 202–204).
- Old: "If (NS) fails, some pair of A-history laws are uniform on two distinct cosets of one subgroup, hence
  disjoint: A's complete history identifies the remote setting with certainty (the 0-or-1 dichotomy …"
- New: "If (NS) fails for wing A, there are `x`, `y`, `y′` for which the laws of `h_A` given `(x, y)` and
  `(x, y′)` are uniform on two distinct cosets of `π_A M`, hence disjoint: at that own setting A's complete history
  distinguishes `y` from `y′` with certainty, total variation 1 (the 0-or-1 dichotomy …"

Also make these two substitutions:

- §0:71–72: "a failure of no-signalling is then perfect discrimination of a remote setting" → "a failure of
  no-signalling then makes two remote settings perfectly distinguishable from one wing's complete history at a
  fixed own setting".
- §4 (ii): "or identifies the remote setting with certainty" → "or makes two remote settings perfectly
  distinguishable".

**C3** (line 191).
- Old: "for any regions (overlap and in-cone regions allowed);"
- New: "for any fixed regions `R_A^t`, `R_B^t`, independent of the state and the settings (overlap and in-cone
  regions allowed), complete in the sense of BS (Rec): every record the wing holds or can obtain in the window;"

Add a scope bullet after "**Postselection** …":

> **Histories.** (NS) is imposed on the complete fixed-region histories. If it is imposed only on a
> setting-selected part, the PR box is reachable inside (vii) with `μ_0`: with `λ_B0 ⊕= λ_A0`,
> `λ_B1 ⊕= λ_A0 ⊕ g_A`, `a = λ_A0` and `b = λ_B[y]`, the selected history `(y, λ_B[y])` is no-signalling, while B's
> fixed-region history `(ρ, ρ ⊕ x)` signals.

**C4.**
- §0:75: "**For OI itself.** Under the full ledger" → "**For OI under the ledger (conditional).** Under the full
  ledger".
- §0:76–78: "(… for graph-separated wings also Theorem N′ [D] with (xiv)). A Bell violation then needs one of:" →
  "(… for graph-separated wings also Theorem N [D] with (GI) and (xiv), or Theorem N′ if (xiv) is read as MI\*). A
  Bell violation with complete-history no-signalling over fixed record regions then needs one of:".
- §4 (iii): "A Bell violation under the ledger therefore requires leaving (vii), (AL2), (AL3) or every-run
  accounting." → "A Bell violation with complete-history no-signalling under the ledger therefore requires leaving
  (vii), (AL2), (AL3) or every-run accounting; no-signalling imposed on less than the complete fixed-region history
  is a weaker admissibility criterion (scope limit **Histories**), not an escape in this ladder's sense."

**C5** (owner term).
- Lines 86–88. Old: "\"Escape demonstrated\" means a member of the stage's admissible class with complete local
  records, every-run outputs and complete-history no-signalling checked by hand; it is a designed map (RC level
  Q2-F at most), not the ledger rule, unless stated."
- New: "\"Not forced (designed witness)\" means a member of the stage's admissible class with complete local
  records, every-run outputs and complete-history no-signalling checked by hand. It is a designed map, not the
  ledger rule, so it is not an escape demonstrated in the authorization's sense (a native construction). For
  OI's native rule the stage is undetermined unless stated."
- In the stage 0–4 rows, replace "ESCAPE DEMONSTRATED" by "NOT FORCED (designed witness)".
- Alternatively, ask the owner to ratify the record's reading of the term.

**C6** (lines 150–151).
- Old: "The edge `λ_A0 → r_B` breaks symmetrized (Sep) but not directed (Sep) (SB L3)."
- New: "The edge `λ_A0 → r_B` leaves both forms of (Sep) intact at the one-tick window (symmetrized
  `d(g_A, R_B) = 3`, `d(g_B, R_A) = 2`); `λ_A0` is a common cause (SB L3)."

**C7** (line 170), Reading column.
- Old: "a common cause (SB L3)"
- New: "(Sep) fails in `G_φ` (edge `g_B → r_B` through `λ_B[g_B]`); the dependence is null on the support of
  `μ_0` (`λ_B = 0`), and `r_B = ρ` is a common cause"

**C8** (line 66).
- Old: "Observer-access changes alone (generator residues, enlarged record regions) produce either no change or
  signalling."
- New: "In the toy of §2, observer-access changes alone (generator residues, enlarged record regions) produce
  either no change or signalling; no general access-only theorem is claimed (§3)."

**C9** (line 98).
- Old: "for the relaxed branch (stage 3 or 5 relaxed): NS for a full-span preparation family"
- New: "for the branch with stage 3 relaxed and each law common across settings (MI kept): NS for a full-span
  preparation family"

**C10.**
- Line 93: "(Main:484's no-uniform-realization applies only to unbounded instrument sets)" → "(Main:486's
  no-uniform-realization applies to the continuum instrument space, not to a finite menu)".
- Line 272: ":480–484" → ":480–486".

**C11** (lines 54–55, inside the blockquote).
- Old: "(Gen) settings are functions of⏎> generator-region content at the setting slice" (⏎ marks the line break).
- New: "(Gen) settings are functions of⏎> the content of disjoint generator regions at the setting slice"

**C12** (line 153).
- Old: "(`λ = ρ`, `b = λ ⊕ x` read as a local response after relabelling; §4)"
- New: "(with `λ′ = ρ ⊕ x`, uniform and independent of the settings: `a = λ′ ⊕ x`, `b = λ′`; §4)"

**C13** (item 8 and sources).
- (AL2), lines 187–188: "it covers the family `D_0` of RC §4 and μ-G" → "it covers the MP-0a family (designated
  cells at known values, uniform elsewhere; OA1:556–558 [W], RC's `D_0`) and μ-G (OA1:103–105 [W])".
- Stage 4: "settings are configuration content (RC row C4)" → "settings are configuration content (Main:42;
  OA1:111–112 [W])".
- Stage 7: "The native encoded U′ composite reaches non-quantum Bell-local tables (SWAP/2; QH:68–97) [D]" →
  "The native encoded U′ composite reaches the non-quantum table SWAP/2 (QH:68–97) [D], which is Bell-local over
  Pauli-axis product tests [A]".
- QH row, last cell: "**provenance** for stage 4, illustration for stage 7" → "**provenance** for stage 4;
  **support off `main`: gap** for the stage-7 illustration, on which no verdict rests".
- §4 (iii): "Main:362 and SB L4 already exclude" → "Main:362 already excludes".

**C14** (line 284).
- Old: "PR #1232 reviews 5858000929, 5859960068 (ACCEPT WITH NITS, `86a413c8`)"
- New: "PR #1232 reviews 5858000929 (REVISE, `b94b283a`), 5859960068 (ACCEPT WITH NITS, `86a413c8`)"

## 7. Nonblocking

- Step 2: state `e_{x_0} = f_{y_0} = 0`.
- Stage 0: name the composite converses (Lean :466–468).
- NOTES' `Z_3` Birkhoff decomposition remark was not reviewed, and nothing in the record rests on it.
- §A.31 fixed point: one more pass is warranted. The lossy-read witness of §1 was a NEW finding in this review, so
  the record has not reached 3–4 passes without NEW.
