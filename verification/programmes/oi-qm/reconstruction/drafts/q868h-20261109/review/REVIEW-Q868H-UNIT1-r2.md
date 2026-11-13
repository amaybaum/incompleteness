# Review of Q-868-H unit 1, revision r2 (heralds on native two-wing U′ preparations)

**Model-written independent review (Claude Code subagent, 2026-11-13). Not human verification; a model review is not
verification under §A.46 item 7.** It authorizes nothing. No push, comment, edit or dispatch was made. The reviewer is
not an author of r1, r2, the r1 review or ASSESS-868.

- **Head reviewed:** `research/q868h-868-20261113` at `82f592db3a0a36f118bf693805be5d1322e32b1e`, fetched by name and
  checked out detached in a worktree. At this head the branch carries no `assess-868-r3a/` directory, so ASSESS-868 r3a
  was read from `820519cf011c09b37690213a758106ed3aa15cc2:handoff-20261109/868-assess/ASSESS-868.md`.
- **Hashes verified before reading** (sha256):
  - `Q868H-UNIT1.md` (r2) `1e128f28…79e6`;
  - `DISPOSITIONS-r2.md` `2916fa33…caf4`;
  - `r1/Q868H-UNIT1.md` `428cc283…1d49`;
  - `review/REVIEW-Q868H-UNIT1.md` `bd82f3fc…b520`;
  - ASSESS-868 r3a `d97c4b6b…8e1b` and REVIEW-868-r3 `2a5014a5…fd1d`, both read at `820519cf`.
  All match the values recorded in r2 and `OBJECTS.md`.
- **Sources read at `fd539e15`** (`git show`; reachable from `main`):
  - QP `DESIGN.md` `11d89c04…32b9`: nodes 5–10 and the ledger (:440-456, :525-620, :724-768, :776-790);
  - AP1 `dd13bf29…ac0c`: :414-444 and :672-684;
  - Main `6144cd4a…6366`: §3.3 (:360-416).
  The existence of the M1D, M2D, MI1 and PROOF-RECOVERY paths at `fd539e15` was checked.
- **Authorization records** were read with `gh api`: #868 c.6742050189, #1210 c.6739250392, #1211 c.6739843458 and
  #1169 c.6852816462.
- **No probe was run**, neither the unit's nor the r1 reviewer's. The probe sources were read, and they encode no OI
  rule, U′ encoding, coupling, cell swap or preparation. Every native-side fact below was re-derived by hand from QP's
  stated formulas.
- **One text scan** was run: the SC-42 added-text regexes, applied to the unit's files. It is a string match, not a
  computation on any mechanism.

***

## Verdict: ACCEPT WITH CHANGES

All of the r1 review's findings (B1–B2, N1–N8) are resolved in r2, and every disposition was checked against the
sources. The three outcomes are reported and proved separately. The headline **(V) PASS, (C) PASS conditional,
QC FAIL** stands on hand derivations that I re-did. Five required changes remain, each a local text change with no
verdict change and no new premise:
- one misstatement of what the QC verdict rests on (RC1);
- two conditions missing from a headline (RC2 for (C), RC3 for QC);
- one negative claim stated beyond its proof (RC4);
- one authorization statement broader than its records (RC5).

## Required changes (exact old → new; r2 line numbers)

**RC1. What QC FAIL rests on (§0, :68-70).** The verdict does not rest on QC-2 alone, and the old sentence contradicts
the sentence after it.
- Under the stated access, which reaches both statuses of `pp`, two tables already fail QC:
  - E2 (`pp` undetermined; type 2, −1/4);
  - E4 without `τ_Y` (`pp` determined; SWAP/2, −1/2).
  Either is enough by the §6.1 map, so "a failure scoped to one status of `pp` … does not carry the verdict on its
  own" is false for the stated class.
- What QC-2 adds is robustness: no restriction of the preparations by the status of `pp` restores QC.
- QC-4 (joint reads; every native state) is a second item that holds for every status of `pp`, so "rests on QC-2" is
  also not exclusive.

Old:
> A failure scoped to one status of `pp` therefore does not
> carry the verdict on its own. The verdict rests on QC-2, which holds for every status of `pp` at the coupling. Under
> the stated access E2 (QC-1) and E4 without `τ_Y` (SWAP/2) are also native non-quantum tables.

New:
> A failure scoped to one status of `pp` therefore does not by itself exclude a
> restriction of the preparations to the other status. Under the stated access, which reaches both, E2 (QC-1, `pp`
> undetermined) and E4 without `τ_Y` (SWAP/2, `pp` determined) are each native non-quantum tables. QC-2 (product tests)
> and QC-4 (joint reads) hold for every status of `pp` at the coupling, so no restriction of the preparations by the
> status of `pp` restores QC.

**RC2. (C) uses (iv) and does not list it (§0 :55-56; §5.2 :319).**
- K1 takes the unknowns as uniform within a branch, and a branch is conditioned on settings (§1). That requires the
  configuration law to be independent of the settings: Main §3.3 (iv), which r2 carries for (V).
- Without (iv), (C) fails. On E4 (`XX` and `ZZ` determined), let A's choice of read be X exactly when
  `f_z^A(s) = 0`. Conditioning on that setting and on the X record determines both `f_x^B` and `f_z^B`, so B is at
  `(±1, 0, ±1)`.

Changes:
- §0 :55-56. Old: `Under P1, P2, N2, A4 at \`q = 2\`,` / `E-iso, WL and H-PREP,`. New: `Under P1, P2, N2, A4 at \`q = 2\`,` /
  `E-iso, WL, H-PREP and (iv) via P3,`.
- §5.2 :319. Old: `E-iso, WL, H-PREP; NNB for the Y read`. New: `E-iso, WL, H-PREP, (iv) via P3; NNB for the Y read`.

QC FAIL needs no such addition. It is existential, and the protocols with independent settings stay in any enlarged
class.

**RC3. QC FAIL is conditional on NNB (§0 :65; §11 owner question 3, :657).**
- Every QC item needs NNB, either to build (`H`, `S`) or to read Y.
- Tier N is a non-selective pass (§6.5).
- §0's K2 sentence and §6.4 carry "linear N with NNB", but the QC headline and the result proposed for recording in
  #868 do not.

Changes:
- §0 :65. Old: `**Quantum compatibility (QC): FAIL** [A + X].` New: `**Quantum compatibility (QC): FAIL** (with NNB
  carried) [A + X].`
- §11 :657. Old: `and QC fails for U′ composites (including under premise I).` New: `and QC fails for U′ composites with
  NNB carried (including under premise I).`

**RC4. "No native witness" is proved at class level only (§0 :90-91; §7 :520-521).**
- The proof given in §7 is class-level: each class considered contains SWAP/2, so no class has QC.
- §0 places the sentence right after "at property level", where it reads as a property-level claim. At property level
  it is false for the countercontrol classes, by a hand construction from AP1 C9 and E7. With P1 removed, a wing's
  carrier is made sharp (AP1:682), which gives Bloch `(±1, 0, ±1)` because `p` stays uniform. Randomized mixing with
  `Λ_0` at dyadic weight 5/8 gives `(5/8, 0, 5/8)`:
  - its L1 norm is 5/4 > 1, so it is outside the octahedron;
  - its squared norm is 25/32 < 1, so it is inside the ball.
  A product with any A preparation has a PSD table, so QC holds. B is at that point under every A herald, so (C)
  fails.
- The SA-1(c)-removed class gives the same construction from a sharp ready cell.

Changes:
- §0 :90-91. Old: `It is a non-native logical witness, not an input; no native witness exists among the classes
  considered` / `(§7).` New: `It is a non-native logical witness, not an input. No native class-level witness exists
  among the classes considered, since each contains SWAP/2 (§7).`
- §7 :520-521. Old: `No native witness exists` / `among the classes considered here.` New: `No native class-level
  witness exists` / `among the classes considered here.`

Adding the native property-level witness is optional (O5) and would need its own review.

**RC5. The generic-check permission is not recorded for this unit (header :17-18).**
- #868 c.6742050189 reads "No computation", with no carve-out.
- The cited rulings name other units. #1210 c.6739250392 says "within Phase 1". #1211 c.6739843458 says "Applied as on
  #1210" for unit 1. Both were posted before the Q-868-H question was put, and that question was worded without the
  carve-out.
- The r1 and r2 probes were run under the unit's reading. That reading may well be intended, but the text presents it
  as granted.

Old:
> "No computation" means no computation on an OI mechanism; exact checks of paper claims on generic mathematical
> objects are allowed if labelled (#1210 c.6739250392; #1211 c.6739843458).

New:
> The authorization says "No computation". This unit applies the owner's generic-check rulings recorded for #1210
> Phase 1 (c.6739250392) and #1211 unit 1 (c.6739843458): exact, labelled checks of paper claims on generic
> mathematical objects, and no computation on an OI mechanism. Those rulings name other units; their application to
> Q-868-H is not separately recorded (owner question 4).

Add owner question 4 to §11:
> 4. **Generic checks.** Do the #1210/#1211 generic-check rulings extend to Q-868-H? The probes of §10 were run under
> that reading.

No verdict changes if the answer is no. Each X-labelled fact the verdicts use has a hand argument in the text, except
the spectra of the named tables, which are elementary in the Bell basis.

***

## 1. The r1 review's findings in r2

| finding | r2 location | resolved? | check |
| --- | --- | --- | --- |
| B1 QC-1 universal; S3 | Lemma P (§2.3); §6.2 QC-1; §0 QC; S3 closed (§0, §11); R-wide marks dropped; owner question 2 | **yes** | Re-derived by hand, below. "R-wide" survives only at :179 (the definition) and :653 (owner question 2). "entangled-type", "S3 (partial)" and "R-wide for E4" have zero hits |
| B2 QC ⇏ (C) level mix | §7 row and note; §0 | **yes**, with RC4 | The witness `\|0⟩ ⊗ (cos π/8 \|0⟩ + sin π/8 \|1⟩)` gives B `(sin π/4, 0, cos π/4)` under every A outcome. QC holds at the state and at the herald, and the point is outside the octahedron, so the levels are consistent. The E4 substitution for the N2-removed class is correct: `⟨XX + YY + ZZ⟩ = 2⟨SWAP⟩ − 1 ≤ 1`, and the determined entries do not depend on N2 |
| N1 "unconditionally" | §7 :513 | yes | |
| N2 (iv), not AP1 C1 | §0, §2.4, §6.0, §11 Q3, §10 | yes | Main:406-407 quoted correctly; AP1:674 is C1 for one wing. RC2 extends the same premise to (C) |
| N3 C6 conditions; non-selective | §6.0, §9 | yes | Hand argument checked. With distinct settings, the four CHSH correlators form a 4-cycle of anticommuting pairs, so a stabilizer state has at most two of them at ±1. With equal settings on a wing, CHSH is twice one correlator. `XX + XZ + ZX − ZZ` has top eigenvalue 2√2 |
| N4 QP hash | §10 | yes | `11d89c04…32b9` recomputed |
| N5 joint reads in the map | §6.1 | yes | |
| N6 encoded vs native local tests | §6.3, §0 J2, §8 J2, §4 remark | yes | The raw-read distinction is correct. The remaining question is stated as not shown |
| N7 `hH2` witness | §8 K2, §0 | yes | `cnot(SWAP/2) = (I + XI + IZ − XZ)/4` (XX → XI, ZZ → IZ, YY → −XZ). On `(−x) ⊗ (−z)` it gives ¼(1 − 1 − 1 − 1) = −½ |
| N8 entry-dependent parity | §6.2, §0 J7, §8 J7, §9 | yes | All four `pp`-carrying pullbacks were re-derived (below). The conflict pairs have `Q* = 1`, also with `pp` added, because `pp` is singular and radical |

No disposition refuses a finding. The two extensions beyond the review's wording are correct: the E4 substitution
under B2, and the check over all 60 stabilizer states under N3.

### Hand derivations re-done (native side, from QP :443-451, :562-615, :748-751)

- **Lemma P.**
  - Step 1 is the map `(z_A, x_A, z_B, x_B) ↦ (z_A + z_B, x_A, z_B, x_B + x_A)`. It is symplectic: the cross terms
    `z_B x′_A` and `x_A z′_B` each appear twice. From `z₁^A = 0` and `x₁^B = 0` known, it determines
    `z₁^A + z₁^B = 0` and `x₁^A + x₁^B = 0`.
  - Step 2: `W = C12 ∘ C21 ∘ C12`, with C12 as at QP:562-563 and W as at QP:612. The z-chain and the x-chain both
    swap the cells, as r2 writes them.
  - Step 3: `pp = 0` is determined, along with `z₂^A + z₂^B` and `x₂^A + x₂^B`. Each has `Q* = 0`, and their pairing
    is `ω = 1 + 1 = 0`, so (K2) and (K3) are respected. No NNB, translation or parity–parity coupling is used.
- **Pullbacks of the graded coupling.** The reading in §2.1 is control A: `x_A += x_B`, `z_B += z_A`. It reproduces
  QP's two stated images. Using `f_y = f_x + f_z + p`:
  - `YY ↦ f_x^A + f_z^B + pp`;
  - `XZ ↦ XX + ZZ = YY + pp`;
  - `XY ↦ YZ + pp`;
  - `YZ ↦ XY + pp`.
- **E3.** Lemma P (`pp = 0`), then `H_A` (`pp = 1`), then CNOT gives `⟨XX⟩ = ⟨ZZ⟩ = 1` and `⟨YY⟩ = −1`: the Φ⁺ table.
- **E4.** After the second carrier coupling, `YY = XX + ZZ + pp = pp`, so the table is SWAP/2 at `pp = 0` and the Φ⁺
  table after `τ_Y`.
- **QC-2.** `S` preserves `f_z` and flips `p`, and `H` flips `p` again. So the two paths give `(−1)^{π+1}` and
  `(−1)^π`, while the comparator gives −1 for both. For mixtures, the paths give `⟨YY⟩ = u` and `−u`, and the Bell-basis
  minimum eigenvalue is `−(1 + u)/4`, so at least one path is below 0.
- **QC-4.** Both line sums equal `Σ f^A + Σ f^B = p_A + p_B`. QM gives row product +I and column product −I.
- **Type 2.** Two commuting determined correlators fix a Bell-basis vector, so the third correlator is ±1 for any
  quantum state. The minimum eigenvalue is −1/4.
- **QC-3.** The transpose acts as `σ_y ↦ −σ_y`, which is the Y-row flip on A.

## 2. The three outcomes, each at its stated scope

- **(V) PASS** holds at its stated scope: native Pauli product tests and every remote herald, with NNB carried and
  premises SA-1(a), P3 with (iv), E-iso and WL.
  - Each wing's record is a function of its own slots (and meter unknowns) under setting-independent sampling, so
    every table is a mixture of products of cube vertices.
  - Lemma P's cross-wing parity correlation does not change this: the model stays local in `s`.
  - The §A.31 skepticism note is apt. (V) is cheap, and it is non-selective at stabilizer scope.
- **(C) PASS conditional** holds once RC2 adds (iv).
  - The remote herald identity uses (K2) and (K3) on `D ∩ B` and is unaffected by Lemma P. A raw read of `z₂^A` after
    Lemma P reveals `z₂^B`, but `p_B` stays undetermined.
  - The countercontrols break (C) as stated.
- **QC FAIL** holds with NNB carried (RC3), and it is over-determined (RC1). E2, SWAP/2, QC-2, QC-3 and QC-4 are
  independent native failures.
  - QC-2 and QC-4 are the items that hold for every status of `pp`.
  - QC-2 also survives premise I. With `π = 0` from Lemma P, or `π` undetermined, it needs no lone translation.
- **"Φ⁺ natively reachable on some branches"** is correctly scoped, as written, to the *Φ⁺ product-test table* ("The
  Φ⁺ table", §0 :66-68; "the natively reachable Φ⁺ table", QC-3). E4 with `τ_Y` builds it without NNB. E3 needs NNB
  for `H`. Reading Y needs NNB in both cases.
  - The same preparation is not Φ⁺-compatible beyond product tests. Under joint reads it has a row sum of
    `pp = 1` with certainty, where QM gives 0 (QC-4). `τ_Y` takes it to SWAP/2 (QC-3).
  - The text never says "Φ⁺ state". O2 suggests making the limit explicit.
- **Separation of the outcomes.** No outcome is inferred from another. The six directions in §7 each carry a witness
  at one level. (V) ⇏ (C) is shown at class level, by the P1-removed class. QC ⇏ (C) is shown at property level, with
  RC4 scoping the native-witness sentence. Every other direction is shown at state level, by E2.

## 3. Claim/evidence boundary

- **Witness → theorem, finite → universal.** The universal claims (Proposition K, Lemma T, the remote herald identity,
  (V), (C)) are proved for every finite protocol of the class. The witnesses are used only for failures and
  non-implications. The negative claims are scoped (§6.4). Exception: the "no native witness" sentence, RC4.
- **Conditional → unconditional.** Two conditions are missing: (iv) for (C) (RC2) and NNB for QC (RC3). Every other
  condition is carried.
- **No quantum states as inputs.** Comparator states enter only in column (iii), and the property-level witness is
  labelled as non-native and not an input. The probes compute only comparator-side and table facts.
- **No new assumptions or construction changes.**
  - Lemma P composes operations QP and r1 already list. ASSESS §7's setting covers it only together with r2's
    within-wing composition after the cross-wing coupling. That is the owner's "repetition and composition" scope, and
    r1 already read §2.3 the same way.
  - Making (iv) explicit names a posit already in Main; it adds no assumption.
- **Computation.** RC5.

## 4. §A.42 item 8: references to content not on `main`

| reference | claim it supports | class |
| --- | --- | --- |
| ASSESS-868 r3a (`reassess/868/ASSESS-868.md`; blob `7196beeb` at `820519cf`) | Q-868-H's definition and the (V)/(C) decision rule (§5.1 "fixed before this work"); Lemma H; w3; the cube-cone duality and (C) ⇒ (V) ("ASSESS r3 W1, W2"); the J-labels; the §4.3 zero completion | **support off `main`: gap.** Open until ASSESS r3a (and the probe or review items behind W1/W2) lands. `OBJECTS.md` records it |
| REVIEW-868-r3 (`2a5014a5`) | the acceptance status of the inputs | provenance (r2 uses no proof content from it beyond what ASSESS carries) |
| "#1210 M3", "ASSESS §6" and SHARED §9 ([D] drafts) | §8 last bullet: the SA-1(c) "QM-only" column-(ii) framing | **support off `main`: gap** for the framing. r2's own content, that (C) uses SA-1(c) and (V) does not, rests on AP1 at `fd539e15` |
| #868 c.6742050189 | the unit's authority and scope | authority record, quoted verbatim (checked). Author `amaybaum`; time 14:07:16Z, given in `OBJECTS.md` |
| #1210 c.6739250392, #1211 c.6739843458 | permission for generic checks | authority records for other units (RC5) |
| #914 row O-K2(P), #1169, #1147, #867 | accountable homes and resources | provenance |
| `fd539e15` sources (QP, AP1, M1D, M2D, MI1, Main, PROOF-RECOVERY, MR-1, COMP-1, PC-1, kernel files) | everything cited as QP, AP1, Main and so on | support on `main` (ancestry of `origin/main` checked) |
| branch `ccr-9c2ecca4-vkb666` at `820519cf` | provenance of the preserved bytes | provenance |
| `src/` extracts (DISPOSITIONS) | none beyond the `fd539e15` files | provenance |
| `probes/*`, `review/rv_*` (this branch) | the X-labelled facts | support on the PR branch; they land with the record or the claims are relabelled |

Item 8 blocks landing until the two gaps close. It does not block review of a WIP draft.

## 5. Register and SC-42 readiness

- **Register.** This is a research record, not `papers/`. It has no reader instruction, no self-narration of the
  manuscript and no revision-history voice in its claims. The header's "revision r2", the §10 run history and
  DISPOSITIONS are record metadata or change notes.
- **SC-42 added-text regexes** (`check_sc42.py` §[5], applied to every file in the directory):
  - history, register, secret and local-path hits: **zero**;
  - caps hits: identifiers and status tokens only (CNOT, SWAP, CHSH, ASSESS, DESIGN, RESULT, PROOF, COMP, REVIEW,
    REVISE, ACCEPT, ELABORATING), plus **`GENERIC`** in line 1 of the docstrings of both writer probes, which is caps
    emphasis.
  The probes are byte-preserved, so editing them would break preservation (see O6). The text added by RC1–RC5 carries
  no caps outside identifiers and no history or register phrase.

## Optional suggestions

- **O1** (§0 QC-2, :77). "eigenvalue −1/2 or −1/4" holds per branch. For a coarse-grained mixture, the worse path has
  `−(1 + |u|)/4 ∈ [−1/2, −1/4]`. Add "per branch; at most −1/4 for mixtures".
- **O2** (§0 :66-68). After "the Φ⁺ table is natively reachable", add: "as a product-test table only: under joint reads
  the same preparation has row sum `pp = 1` (QC-4), and `τ_Y` takes it to SWAP/2 (QC-3)."
- **O3.** "(iv) … supplied here through P3's external controller" could be read as P3 entailing (iv). AP1:421's P3 only
  loads coefficients from a classical controller. Suggested: "carried as a posit; the settings enter through P3's
  external controller".
- **O4** (§10 :603). "a second run is byte-identical" for the r2 probe has no preserved output: `OBJECTS.md` lists runs
  1–3, and run 3 is `.out`. Either preserve that output or drop the clause.
- **O5.** The native property-level witness of QC ⇏ (C) in RC4 (a sharp carrier from AP1 C9 or SA-1(c) removal, mixed
  with `Λ_0` at 5/8) could be added to §7 as a native witness in the countercontrol classes. It is a new hand
  construction and would need review.
- **O6.** If SC-42 is run at landing, record `GENERIC` in the two preserved probe docstrings as an accepted
  substitution, as #1265 did for comparable preserved bytes, rather than edit preserved files.
- **O7** (§6.0). State explicitly that heralds by non-Pauli native reads on A (raw parity-cell, ancilla, multi-record)
  are also mixtures of cube-vertex heralds. The r1 review confirmed this, and r2 derives (V) only from product tests.
