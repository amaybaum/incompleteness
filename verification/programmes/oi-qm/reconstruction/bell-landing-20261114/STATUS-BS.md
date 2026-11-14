# Status note: Bell-scope unit 1, native Bell factorization and its proved class

**Draft for the Bell landing package (`LANDING-PLAN.md` §5).** At landing this note becomes
`verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/STATUS.md`. It gives the
standing of the records in that directory and changes none of them; r2 is the accepted text.

## Accepted record and reviews

- **Record.** At `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918` (PR #1231), a single-parent child of r1 at
  `7abf59d76ba363cbad72c7e0764ce3be2a275d06`, whose parent is `cac5d264`:

  | File | Blob | SHA-256 | Lines |
  |---|---|---|---|
  | `BELL-SCOPE-UNIT1.md` | `5814e479b16929fe8ab045a3f3b8fc4987704633` | `dd7115511e332b1cae20bdda7c3d94ec7f8af20bbd436750d7e6dfccbf078913` | 472 |
  | `DISPOSITIONS-r2.md` | `dd8cbc8c5c29ad28d175cbb67dcf23454fc3915a` | `d3a185181747877f2ef977c2be735b0e8b705164b4bfff7ec8635e4808e08d2f` | 37 |
  | `probes/generic_bell_checks.py` | `e47f3179b0bd4195d67091b1397490433c0316ca` | `83cecb183cf2a625cf5913b6e287350d514297e0cd94fc66ee8f264e7100b6d0` | 172 |
  | `probes/generic_bell_checks.out` | `0798db766ba252dfb01d5622c43adfc8e9edbc6c` | `61deeddd35bedf5ad63b2e133c7067addf30e118f27103208f0965f2ed13e491` | 18 |

  "BS:n" is line n of `BELL-SCOPE-UNIT1.md`. The probe's SHA-256 equals the value at BS:300. The r1
  text is in the history of `7abf59d7`, which stays an ancestor of `main` when the package lands by
  merge commit.
- **Review trail (PR #1231).**
  - ChatGPT review 5857227567 (posted under `amaybaum`, 2026-11-11T10:22:16Z) at `7abf59d7`: REVISE,
    five required fixes (CF and MI direction; the O2 window; NBA's antecedent; tightness scope; the
    rationality aside). Dispositions: `DISPOSITIONS-r2.md`, all applied, none refused.
  - ChatGPT review 5857981727 (posted under `amaybaum`, 2026-11-11T11:24:59Z) at `e1534b08`: "ACCEPT
    WITH NONBLOCKING NITS (paper-only, restricted result)", "ACCEPT for the corrected paper unit at
    its **restricted, conditional** scope; preserve OI-wide verdict **INDETERMINATE** and escape
    **NOT ESTABLISHED**."
- **Nature of the reviews.** Both are model reviews posted under the owner's account; neither is a
  human review, a GitHub approval or an owner decision, and neither is verification (§A.46 item 7).
  No review by a separate non-author reviewer other than ChatGPT is recorded. Theorem N′ and the
  six-site toy member (§4.1) entered in r2 and were read only by the focused re-review.
- **Authority.**
  - Contract: #868 comment 6791565399 (`amaybaum`, 2026-11-11T08:56:50Z), paths A obstruction, B
    escape, C indeterminate; "No OI-mechanism computation, Lean run, new physical premise,
    experiment/design/freeze/dispatch, PR merge or claim promotion is authorized by this note."
  - Writer assignment: #868 comment 6791606126 (`amaybaum`, 2026-11-11T08:59:01Z): "Confirm: Claude
    writes (Recommended)", with the option text "No OI-mechanism computation, no new premise, no
    runs."
  - Landing plan: #868 comment 6873193841 (`amaybaum`, 2026-11-14T06:34:07Z).

  Emphasis is removed from the quotations, except where the review's own bold is kept above.

## What the record supports, and at what strength

| § | Result | Strength in the record |
|---|---|---|
| 3.2 | Theorem N: under (D), (F), (Gen), (Rec), (Sep), (GI), every-run outputs with a fixed local failure rule and (MI) for Ω, one setting-independent λ = Ω factorizes the complete local histories for the whole finite menu; CHSH ≤ 2 | [A] on Main's cone lemma [P]; G1 [X] |
| 3.2 | Theorem N′: the same without (GI), with λ* = (Ω, ρ_A, ρ_B) and the stronger (MI*) | [A] |
| 3.3 | Lemma G: under (M) and (CF), (MI) holds for Ω; one direction only, with the counterexample `r = w` for the converse | [A]; G6a–c [X] |
| 4.1 | ε ≥ (√2−1)/4 for the mean and worst-setting TV to the Tsirelson box, for any MI Bell-local family; optimal over Bell-local tables; attained by an abstract six-site member of 𝒞_sep | bound [A]; optimality [A] with G3 [X]; attainment [A] with G7 [X] |
| 4.2 | full-history contraction: TV on full histories ≥ TV on extracted outputs | [A]; G5 [X] |
| 4.3 | MI-relaxed corollary of Main's bound | [A] on Main:416–423 [P] |
| 0, 3.4 | verdicts: (C) indeterminate for OI itself; (A) obstruction restricted to 𝒞_sep; (B) not established; NBA stated as the missing lemma | classification [A]; NBA open |
| 5 | consequences for #1216 Levels A and B and #1169 | [A], conditional on 𝒞_sep membership or on prepared-pair-source §5 [W] |
| 6 | six candidate principles scored under §A.29 | none adopted |
| 7 | findings F1 and F2 on the corpus | reported, not corrected; see "Source drift" |

**Claim supported by this record:** "For the closed native screened class 𝒞_sep (one fixed
deterministic map on a finite site-factorized space, disjoint generator regions inside the system,
complete local record windows outside the other wing's generator cone in the actual coupling graph
for the whole window, generator isolation, every-run outputs with a fixed local failure rule, no
postselection, and measurement independence for the non-generator variable Ω), one
setting-independent pre-setting variable factorizes the complete local histories for the whole
finite menu, so CHSH ≤ 2; without generator isolation the same holds under measurement independence
for λ* = (Ω, ρ_A, ρ_B); for any measurement-independent Bell-local family the mean and worst-setting
joint-output total-variation error to the Tsirelson box is at least (√2−1)/4, also on full
histories, and the constant is optimal over Bell-local tables and attained by an abstract member of
the class; for OI itself the verdict is indeterminate, the native Bell-availability lemma is open,
and no native escape is established (paper arguments [A] on Main's cone lemma [P], with exact
generic checks [X]; model-reviewed, not independently verified; not adopted; no manuscript claim
affected)."

## Hypotheses

- **Posits of the framework:** (D) one deterministic map; (F) `S = ∏_{i∈V} S_i`, `V` and each `S_i`
  finite (ledger (ii), (viii), Main:724).
- **Protocol properties, posited per protocol (BS:156):** (Gen), (Rec), (Sep) with the symmetrized
  `G_φ` distance (BS:150), (GI), the ⊥-rule; a finite menu with every pair jointly admissible;
  every-run outputs; no postselection.
- **Measure hypotheses:** (MI) for Ω (Theorem N), posited, and on `main` ledger item (xiv),
  Main:724; (MI*) for λ* (Theorem N′), a distinct and stronger hypothesis (owner decision Q2, #1273
  c.6860580909); (M) and (CF) for Lemma G, (M) posited, (CF) open and unsourced.
- **§4:** Bell locality with MI for the bound; one product extractor on both laws, with the target's
  pushforward equal to the Tsirelson box, for the contraction; response-completeness of Ω for §4.3.

## Limitations

- An interface-scoped result, not a no-go for OI: no native protocol is shown to belong to 𝒞_sep
  (BS:45–46, :281–282).
- (Sep) uses the symmetrized distance; it is sufficient, not necessary, for parameter independence
  (review 5857981727; SB L3, landed with this package).
- Attainment of (√2−1)/4 by a member whose map is the native substratum rule is open (BS:339–341).
- The bound does not cover coincidence-only statistics, setting-dependent postselection or wings
  inside each other's `G_φ`-cone (BS:368–369).
- [L] items rest on recall; no primary literature was read first-hand (BS:467).
- The probe encodes no OI rule; its checks support the arguments and do not replace them
  (BS:309–311).

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #868. Model acceptance is evidence of review, not independent mathematical
verification (#1169 comment 6865680499). This plan authorizes no work. Each gap below remains open
until the evidence or decision named for it is recorded on `main`.

Here "independently verified" means verified from `main` to the standard for its kind, for example
kernel-checked or independently verified mathematically (§A.46 item 1); "partially verified" means
reviewed by at least one separate AI-agent reviewer, or resting in part on kernel-checked statements,
without independent mathematical verification of the result; "exploratory" means a result not
reviewed by anyone but its writer, or a proposal that claims no result; "known-invalid" means refuted
on `main` by a counterexample or disproof.

- **Independently verified:** none of the record's own results. Main's cone lemma (Main:362) and
  exogenous theorem (Main:364–389) are manuscript statements on `main`, cited, not re-proved.
- **Known-invalid:** none in r2. In r1 (history of `7abf59d7`), §3.5 item 3 stated MI "equivalent" to
  CF; review 5857227567 gives the counterexample `r = w`, and r2 states one direction (BS:215–219).
  r1's O2 sentence ("inside the graph cone except along the body diagonals") overstated; r2 states the
  window (BS:254–260). The r1 statements are not results of the record.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Theorem N | partially verified; conditional on the hypotheses above | [A] on Main:362 [P]; two ChatGPT reviews | independent mathematical verification | an independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| Theorem N′ | partially verified; conditional, with (MI*) | [A]; one ChatGPT focused review | as for Theorem N | as for Theorem N |
| Lemma G (one direction) | partially verified; conditional on (M), (CF) | [A]; G6a–c [X] | as for Theorem N | as for Theorem N; (CF) stays open |
| §4.1 bound | partially verified | [A], elementary; G2–G4 [X] | as for Theorem N | as for Theorem N |
| §4.1 optimality and attainment in 𝒞_sep | partially verified; abstract class only | [A]; G3, G7 [X] | as for Theorem N; replay of G3 and G7 from `main` | as for Theorem N; a recorded replay |
| §4.2 contraction; §4.3 corollary | partially verified | [A]; G5 [X]; Main:416–423 [P] | as for Theorem N | as for Theorem N |
| Probe checks G1–G7 | exact generic computations, output recorded, no replay from `main` recorded | `generic_bell_checks.out`, 17 PASS lines | a replay from `main` matching the recorded output | a recorded replay (`python3 -I -B`, byte comparison to `.out`); needs its own authorization |
| Verdicts (C), (A) restricted, (B) not established; NBA | classification; NBA open | [A] | NBA itself | a sourced native account of O1–O3 (BS:246–265); remains open under #868 |
| §5 consequences for #1216, #1169 | partially verified; conditional | [A] on 𝒞_sep membership and [W] | as for Theorem N | as for Theorem N; membership stays a named condition |
| §6 candidate principles | exploratory; none adopted | scoring only | — | an owner decision under §A.29, if any is proposed |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

## Dependencies

BS's own §A.42 item 8 table (BS:419–441) classifies its references. At the package landing:

| Reference | Classification |
| --- | --- |
| `papers/Main.md`, `papers/Substratum.md`, `papers/SM.md`, `book/ch18-beyond.md` at `cac5d264` | Support on `main`; `cac5d264` is an ancestor of `main`. See source drift. |
| `composition-source-map.md` at `017ae88e` | Support on `main`, difference stated in BS:430. |
| `prepared-pair-source.md`, `two-system-interface.md`, `NO-SIGNALLING.md`, h-bell preregistration at `cac5d264` | Support on `main`, unchanged from `cac5d264` to `c3b5f37a`. |
| `probes/generic_bell_checks.py` | Support on `main`: it lands in this directory (BS:439). |
| #1210 QX-6 r7c at `4c7f3f86`; session copies of ASSESS-868 r3a, Q868H r2a, LIT-SURVEY | Provenance (BS:435–438). ASSESS-868 r3a is byte-preserved on #1269's branch, off `main`; the classification is unchanged. |
| r1 at `7abf59d7`; r2 at `e1534b08` | On `main` once the package lands by merge commit. |
| Reviews 5857227567, 5857981727; #868, #1169, #914, #866, #1216 comments | Governance and review provenance. |
| #1283 at `f57e576a` (draft §A.46 item 8) | Provenance until adopted (see Landing). |

## Source drift from `cac5d264` to `main` (`c3b5f37a`)

- **Line numbers.** `papers/Main.md` lost two lines at Main:4–5 and changed no other line count, so
  every BS citation `Main:n` with n ≥ 6 is `Main:(n−2)` at `c3b5f37a`: the cone lemma Main:364 is
  Main:362, the theorem Main:366–393 is Main:364–391, Main:406–407 is Main:404–405, Main:416 is
  Main:414, Main:418–425 is Main:416–423, and the ledger Main:726 is Main:724.
- **Content.** Of the cited lines, the cone lemma, the Corollary and the ledger changed (PR #1233):
  - Main:362 defines `G_φ^K` and states that under a linear update (ledger (vii)) the graph is the
    same on every state class, so a state-dependent graph needs an update outside (vii). The
    one-step dependency definition, "symmetrized for the spatial graph", is unchanged.
  - Main:414 states the window `Δt/√3 < d ≤ Δt/‖n̂‖₁` for wings spacelike with respect to *c*
    (BS's O2) and places the adopted preparation-indexed branch outside (vii) (BS's O1).
  - Main:724 scopes ledger (x) to `G_φ^ref`, the reference vacuum/uniform state class, and lists
    measurement independence as ledger item (xiv). BS's finding F1 (unscoped (x)) and the ledger
    half of F2 (MI not itemized) no longer describe `main`. Main:652 cites ledger (v) for hidden-sector
    mixing and states that it is not the Bell-violation mechanism.
  - BS's O1 and O3 therefore read on `main`: under (vii) no preparation-indexed long edge exists;
    MI is the posited ledger item (xiv). O2 and NBA stay open. No result of BS changes.
- `papers/SM.md`:104 changed wording (it now states that `G_φ` collects the dependences at all
  states); SM:108–110, which BS cites for the reference-class restriction, are unchanged.
  `papers/Substratum.md`:131–133 and `book/ch18-beyond.md`:104 are unchanged.

## Superseded lines in the accepted text

- Lines 3–5, "pending re-review", and lines 471–472, "r2 has not been re-reviewed": r2 was
  re-reviewed at `e1534b08` (review 5857981727, quoted above).
- Lines 49–54 (O1), 62–66 (O3) and 451–459 (F1, F2): the corpus lines they describe changed as stated
  under "Source drift".
- Lines 436–437 describe ASSESS-868 r3a and Q868H r2a as session files. ASSESS-868 r3a and Q868H r3 are
  now committed on #1269's branch, off `main`; both remain provenance.

## Landing

- **Together.** This record lands in one merge with the SB L3 carried record and the Bell ladder
  r3, which cite it (`LANDING-PLAN.md` §5).
- **Mode.** Merge commit of `e1534b08`, so that `7abf59d7` and `e1534b08`, which the reviews name,
  remain ancestors of `main`.
- **Basis.** The proposed basis is §A.46 item 8 as drafted in #1283 at `f57e576a`, which is not
  adopted. Until it is adopted, reading R-b is in force and this record meets none of §A.46 item 2's
  current conditions on its own; the basis is open until #1283 is adopted. Record-specific check of
  the draft's conditions:
  - substantive, nonredundant result: met (Theorem N/N′; §4's mean-TV and full-history forms and the
    attainment; `main` carries only the exogenous theorem, Main:364–391);
  - scope and limits documented: met (BS §0, §1, §4.4, §8; this note);
  - independent non-author review and ChatGPT exact-head review: the ChatGPT exact-head review is
    5857981727 at `e1534b08`; no separate non-author review is recorded (owner question OQ-2 of
    `NOTES-PLAN.md`); the package's checks and its ChatGPT exact-head review are pending;
  - accountable Issue, verification status, remediation plan: #868, this note;
  - explicit rationale: the Bell ladder r3 rests on Theorem N/N′ and §4 for stages 5 and 6 and for its
    controlling condition, and #1274's gap E2 is Theorem N; owner merge decision: not recorded.

  The record is preserved, not established (§A.46 item 1). Its removal is not automatic and is
  governed by §A.46 item 6.
- **Owner record.** #868 comment 6873193841: option (1), "land the supporting evidence first", with
  the package "BS Theorem N and N′ (#1231), SB L3 (#1232) and the ladder r3 (#1273). Each component
  has its own record-by-record STATUS notes." No merge decision is recorded.
