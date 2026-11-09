# Review: ARP-3 (Q-C2-2) preregistration r14, an independent review

**Standing.** WIP / UNVERIFIED review note. Model-written. Read-only.
- **Authorization.** #1169 c.6740747027 (amaybaum, 2026-11-09): "Fix B1–B6 and the nits, reusing Q-C2-1's repaired
  wording, then run a further independent review. Paper-only. No F, design run, gate tests or Environment changes.
  Q-C2-2 stays behind Q-C2-1."
- **What was not done.**
  - No repository, git or GitHub write, and no host call.
  - No LP was run on any object. No script self-test was run.
  - No computation was made on F1, `G_SM` or any OI construction.
- **Probes.** The probes in `review/probes-r14/` are rank and size counts and text checks on generic synthetic objects
  (§6).

## Objects (hashes verified)

| object | sha256 |
| --- | --- |
| `preregistration.draft.md` r14 | `9e3ef0c9ddea2876d86bb097e68dc5939487a5a7625333a26167469044c641ba` ✓ |
| `r13/preregistration.draft.md` | `15d90b24496a733d87079256f4a3efb06f426bfaba775aa77e7bc2adda2f4dd2` ✓ |
| `ACCESS.md` r14 / `r13/ACCESS.md` | `e45339ba…e157` ✓ / `9d0305e7…4e71` ✓ |
| `DISPOSITIONS-r14.md` | `8fa42913…4edd` ✓ |
| `IMPL-DELTA-r14.md` | `c2d7286b…02ee2` ✓ |
| `review/REVIEW-QC22-r13-full.md` | `6d1a8f8a…6768` ✓ |
| `r14work/make_r14.py` | `063f83e30df9486dd6202cff1a61f4d3631f0c3923ed2980392d60cf3b20ee22` |
| Q-C2-1 `preregistration.draft.md` r14 | `ae6f0e26…77fd` ✓ (read only) |
| repository | `origin/main` `fd539e15` |

**Reproduction.**
- `python3 -I r14work/make_r14.py r13/preregistration.draft.md <out>` applies 92 edits.
- Its output is byte-identical to r14 (`9e3ef0c9…`) and to `r14work/r14.out.md`.

**V3 blocks.** The `v3-round` and `v3-governed-paths` blocks are byte-identical in r13 and r14 (`p01`). The
governed-paths digest is therefore unchanged.

## Verdict: **REVISE**

- **The six r13 blockers are fixed.** Each fix compares the right object (§1).
  - B4 and B5 hold under every E-READ, E-BIND and E-ID option, apart from one sentence that is false under E-ID (iv)
    (N1).
- **The nits are applied.** N11 and N24 are applied in part.
- **The r14 edits introduce three defects that block `F`.** Each is cheap to fix.
  - **Rb1.** A new size claim in the N5 disposition is false for fixture GX+R-Y, built as F1's completions are built.
    Under r14's listed-count rule, GX+R-Y is `out_of_scope`, so the design run cannot be green.
  - **Rb2.** The new header labels a group of references as provenance. §A.42 item 8 forbids a group label, and the
    label's claim is false for the H3 family of fixtures.
  - **Rb3.** Three owner-reserved choices are made, or left open, with no `PENDING` that blocks `F`. One of them is
    an owner ruling in Q-C2-1.
- **Unchanged.** The mathematics (steps 1–6, C-SYM, Lemma NC-F, `ACCESS.md` §6.4) is correct on paper (§3). Nothing
  in the decision rule, the tokens or the frozen texts changed in a way that prints a verdict over a red control.

## Blockers introduced by r14

**Rb1. GX+R-Y breaks the N5 claim, and C-SYM's brute force is uncapped (N5, N10).**
- **What r14 says** (lines 444–453): every frozen fragment is within the caps as listed, "at most 16 preparations
  (F1+R-S, SF-3)", so "No frozen fragment is therefore `out_of_scope` under one reading and not under the other".
- **What the probe finds** (`p03`). Build each fixture's completions as F1's are built, one per preparation, with R-Y
  adding `μ_p(η) ⊗ U_{Y±}`. Then GX+R-Y lists **18** preparations, with `d = 10`. That is over the cap of 16 as r14
  enforces it.
- **Why the two readings differ.** Four of the 18 are mixtures of other listed laws: the X sector's laws with
  η-marginal `(¾, ¼)` or `(¼, ¾)`. So GX+R-Y has at most 14 extreme rays, and it is within the cap as r14 defines it.
  This is exactly the divergence r14 says cannot happen.
- **Consequence.**
  - Under r14's rule (cap defined on extreme rays, checked on listed rows), GX+R-Y is `out_of_scope`.
  - Fixture mode then exits 3, and the design run and 6′ cannot be green. Precondition 6's "A frozen fixture the
    design run cannot decide" applies: the fixtures are revised before `F`.
- **The construction is not frozen.** The text fixes completions only for F1 ("for each branch `p` of input `Z+`")
  and for H3 ("in block B"). For GX it fixes no completion construction, so the claim cannot be checked from the text.
- **C-SYM (N10).** r14 runs C-SYM on every fixture and every completion (lines 380, 475, 570), and exempts the
  exchanged form from the caps.
  - The effect-side brute force over `(d − 1)`-subsets of the reduced effects is then `C(25, 9) = 2,042,975` for
    GX+R-Y. It is `C(25, 8) = 1,081,575` if R-Y is added on X's sector only.
  - The verifier repeats that enumeration. The fixtures run in A3, A5 and B4.
  - Against the cap `C(n, d − 1) ≤ 10^5`, which was set to bound exactly this work, this is a likely job timeout.
- **Fix, any one of these.**
  - Freeze the fixtures' completion construction, for example R-Y as `δ_η ⊗ U_{Y±}` for each `η` the fixture
    charges. GX+R-Y then has 14 rows and the same cone, so the frozen verdicts are unchanged.
  - Count distinct extreme rays with a certified removal, as Q-C2-1 does (B-RAY, M-RAY).
  - Check the cap on listed rows with duplicates and convex mixtures of other rows removed.

  Then correct the sentence at line 450. Also bound C-SYM: run it on the base fixtures only, as r13's "on the
  fixtures" read, or cap `C(E, d − 1)` and report "not run" above the cap.

**Rb2. The provenance header breaks §A.42 item 8 (N24, partial).**
- **The label.** Lines 54–59 apply one label to `ACCESS.md`, `AUDIT-C2.md`, the gate draft, `PLAN.md`, `review/`,
  `controls/` and every review tag: "drafting provenance … no claim, control or verdict here rests on them."
- **What item 8 says.** It requires a finding per reference and says "Provenance only" is "never a label applied to a
  group of them".
- **The label's claim is false for these references.**
  - **H3's definition.** The control H3 (line 549) is defined only as "`ACCESS.md` §6.4". G, X, Q and GX are defined
    through "the rectangle", which is block B's four laws, and those laws appear only in `ACCESS.md` §6.4. These are
    frozen controls with frozen expectations. "Every definition used here is restated below" (line 52) is false for
    them.
  - **Line 131.** "F0 already shows experience without certification inside a classically imitable fragment
    (`ACCESS.md` F-9)" is a factual claim. EXP is not measured on F0 in-run.
  - **The ledger's sources.** The ADA ledger is printed in `result.md`. Its sources cite `ACCESS.md` §2, §3, §6.1,
    F-3 and O-9, and `AUDIT-C2` §0. E-CTX is an empirical claim sourced to `ACCESS.md` O-9, "not read first-hand".
- **Fix.**
  - Restate block A and block B in the H3 row: four point laws on `(z, x)` at `η = 0`; `(¾, ¼, 0, 0)`,
    `(¾, 0, ¼, 0)`, `(0, ¼, 0, ¾)` and `(0, 0, ¼, ¾)` at `η = 1`, in the order `(z, x) = 00, 01, 10, 11`; point
    reads on all 8 configurations.
  - Drop line 131's factual clause, or source it to an in-run measurement.
  - Replace the group label with a per-reference classification: provenance for definitional pointers and review
    tags; for E-CTX, mark it unsupported here, or cite a source on `main`.
  - The partial refusal of N24, not landing `ACCESS.md`, is acceptable once this is done.

**Rb3. Owner-reserved choices are made, or left open, without a `PENDING`.**
- **(a) An expired artifact fails the S1 binding closed** (line 1636; DISPOSITIONS §3 item 9).
  - Q-C2-1 r14 states the same rule as "draft default, pending owner ruling R6, precondition 2" (its lines 1429–1431
    and C.8 item 3).
  - r14 adopts it for QC22 with no owner record and no `PENDING`. It is also absent from the decision sheet.
- **(b) Precondition 4's reading of "independent ACCEPT of r10"** is "the coordinating session's interpretation …
  the owner can correct it". It carries no `PENDING` field.
  - DISPOSITIONS §5 and §6 state that it is `PENDING` under precondition 2. Neither the text of precondition 2 nor
    that of precondition 4 includes it (`p02`: 30 fields, none for it).
- **(c) Frozen identities that depend on E-ID have no field.** Under E-ID (i), the second account's login is frozen
  into the Environment, B3b and the approval entries. Under (iv), the session's identity is likewise needed. Neither
  has a `PENDING` field. IMPL-DELTA B7 says "`PENDING` until E-ID".
- **Fix.**
  - Add (a) to precondition 2 with fail-closed as the draft default, and add it to the decision sheet.
  - Add a `PENDING` owner confirmation to precondition 4.
  - Add an E-ID-dependent `PENDING` for the reviewer login (i) or session identity (iv).

## 1. The r13 blockers: are they fixed?

| r13 finding | fixed? | what each condition compares |
| --- | --- | --- |
| **B1** replay | ✓ | **B6 at `E`:** E's fresh B4 output against the committed `evidence/measurements.json`, as canonical JSON (`sort_keys`, compact separators, `ensure_ascii=False`, UTF-8), with `parameters.dispatch_sha` removed from both. **At S1** the file is absent, so B6 prints `{"replay":"not-applicable"}` and exits 0. **At `E`,** control R requires the file. The wording is identical to Q-C2-1 C.8 item 3 |
| **B2** digests | ✓ (but see N4, N6) | **No-unapproved-F1 rule:** A3b's step conclusion from the jobs API (A3's in-job file against the schema). **6′:** A3b and A7 conclusions and the artifact list in `confirmation-run.json`. **Stress pin:** A7 at 6′ compares the sha256 of 6′'s own `stress.json`, in the job, with the pin in the tree; `check --freeze` compares the sha256 of the `stress.json` it is given with the pin. **S1 binding:** `sha256(zip bytes)` against the artifact `digest` (both are the archive, which is correct per HF-1); the member list against `["measurements.json"]`; the member against the committed file by B6's comparison. **Control N (a):** A11's live read against the `env-pin.json` in the tree, in the job. **GT-6 (a):** the sha256 of the executor's copy of `env.json` against the owner's posted sha256. **C-STATELESS:** the committed `fixtures` section against `confirmation-measurements.json`, an executor copy of 6′'s A3 file. No condition compares a `digest` with a file's sha256 ✓ |
| **B3** `mkdir` | ✓ | `mkdir -p "$RUNNER_TEMP/arp3-qc22" &&` begins A3 and B4. A3b, A5, A7 and A11 follow A3 in job A, and B6 follows B4 |
| **B4** comments | ✓ (see N1, N2) | The template `issues/comments/{DEC}`. `approvals.json` (schema v1) is committed at `E` and verified against the APIs by `check --stage E` and `verdict`. The `E` entry is built by `verdict`. `F`'s designation is read the same way. The edited-comment rule. The APPROVALS self-test |
| **B5** env placement | ✓ under (a), (b) and (c) | **(a)** A11 compares in the job at S1 and `E`, and `verdict` reads the conclusions. **(b)/(c)** `check --stage S1` reads before the S1 dispatch, into `order-s1.json` at `E`; `check --stage E` and `verdict` read again. No read sits in its own stage's tree. Rule (d) makes every record a mode's stdout. `env-S1.json` and `env-E.json` are gone (grep) |
| **B6** GT-2 | ✓ if E-BIND is adopted | `(S1\|E\|GT-2)`. GT-2's comment matches, so B3b is `success`, B3 is `failure` and B4 is `skipped`. GT-2b gives B3b `failure`. Admitting GT-2 at S1 and `E` leaves the stage bound only afterwards, by the entry, as the text states |

## 2. The nits, the partial refusals and DISPOSITIONS §3

- **Fixed and checked:** N1 (identical to Q-C2-1 C.8 item 4), N2, N3, N4, N6, N7, N8 (the arithmetic checks), N9,
  N12–N18, N20–N23 and N25.
  - **N9.** `verify.yml` at `fd539e15` has `pull_request:` with no branch filter, so a pull request based on a
    branch held at `D` triggers it. The fix is implementable.
  - **N10.** The formulation is correct (§3), but its scope is part of Rb1.
  - **N5.** Fails as stated (Rb1).
  - **N19.** See §3 and N8 below.
- **N11 partial (the witness principle declined): acceptable.**
  - IMITABLE asserts a constructed, verified model, which is not a failure to construct one.
  - CONTEXTUAL is a verified impossibility within F1's stated equivalences, which is the principle's own exception.
  - The principle does bite on one rendering, which the decline does not address: N9 below.
- **N24 partial (not landing `ACCESS.md`): acceptable as a route.** Its execution is defective (Rb2).
- **DISPOSITIONS §3 (untraced changes).**
  - Items 1, 2, 4, 5, 7, 8, 10 and 12 are correct and needed.
  - Item 3 (the pin under (a), taken from an A11 run after GT-6b) is correct, and consistent with A11 recording only
    on gate-test trees.
  - Item 6, the authorship line, is false under E-ID (iv) (N1).
  - Item 9 is Rb3 (a).
  - Item 11 (Q12) is correct: `PENDING`, and the text holds under each option.
- **Two errors in DISPOSITIONS itself.** r14 has 2058 lines, not 2056. §5 and §6 call precondition 4's reading
  `PENDING`, which it is not (Rb3 (b)).

## 3. Mathematics (on paper)

- **Lemma NC-F (step 2).** As restated, it is correct and one-directional (F10).
- **Completeness (step 4).**
  - The completeness by Farkas' alternative is correct.
  - Infeasibility needs the complete facet list. The feasible branch needs only supporting facets, as stated.
- **C-SYM (r14's definition).**
  - The regrouping `κ_λ = Σ_k c_{λk} h_k` holds because `cone{b_e}` is full-dimensional (`B` has full column rank)
    and pointed (`(Σ_p a_p) · b_e > 0` for `b_e ≠ 0`).
  - **Soundness:** `tr W = Σ_{k,p} y_{kp} κ′_k · a_p ≥ 0`.
  - **Model:** `μ_p(k) = (κ′_k · a_p)(h_k · b_u)` and `ξ_e(k) = (h_k · b_e)/(h_k · b_u)` reproduce `a_pᵀ b_e`. They
    normalize, and `ξ ≤ 1` holds by complements. `h_k · b_u > 0` for a nonzero facet normal. ✓
  - **Not stated explicitly:** that the verifier re-enumerates the facets of `cone{b_e}` by its own brute force.
    IMPL-DELTA B10 says so; say it in the C-SYM row.
- **`ACCESS.md` §6.4, the support condition (N19).** It is correct.
  - **Preparations.** The removed point reads give 0, and their complements give 1, on every retained preparation.
    So the retained equivalences are the same in the whole.
  - **Effects.** Each sub-fragment relation, rewritten over the retained point reads, holds in the whole. The whole
    model's removed reads vanish on the retained support, so the rewrite holds pointwise there.
  - Valid for H3, and for GX+R-Y, whose R-Y laws `μ_p(η) ⊗ U` stay within a sector.
- **Counts.** 73 effects for F1; 75 for F1+R-G; 16 for F1+R-S and SF-3; `C(16, 8) = 12,870`; F1+R-G `d ≤ r_S ≤ 6`
  ✓. GX+R-Y is the exception (Rb1).

## 4. Consistency with Q-C2-1 r14's shared wording

- **Identical:** the replay; the S1 binding steps; `h_sha256` with its vectors; `s_entry` and `os`; `SPLICE_*` and
  `run_class_*`; ZIP-1 to ZIP-3; `io`/`zipfile`; the `mkdir` form; the edited-comment rule; the E-entry construction.
- **Divergences.**
  - The expiry ruling, R6 (Rb3 (a)).
  - Q-C2-1 names B5's artifact (`arp2-qc21-measurements`, its row 88). QC22 says "B5's artifact name (frozen in the
    splice)" and states no name (N3).
  - Q-C2-1 keeps "the binding's record at `E`" (derive-run records the binding's inputs in `s1-run/results.json`,
    and `verdict` requires its own read to equal them). QC22 omits it (N6).
  - The caps reading (Rb1).
- **Intended divergences, as DISPOSITIONS states:** the ratification at `E` and the absence of an Environment in
  Q-C2-1; the test-level VOID; the raised caps; ST-BP.
- **The no-unapproved-F1 rule's treatment of a red A3 is shared** (N10).

## 5. §A.41, §A.42, §A.44 and the register

- **§A.41.** Every new mechanism has a checkpoint. Gaps:
  - S1-BIND is not named in any invariant row.
  - The rows' "M-GUARD (BYP-1 to BYP-18)" is stale: it now runs to BYP-26 plus ZIP-1 to ZIP-3.
  - The binding of the 6′ records is self-referential (N4).
- **§A.42 item 8.** Rb2.
  - **Residual for the owner, not introduced by r14.** Under E-READ (b)/(c), control N at `E` and `verdict`'s
    capture records are, by design, provenance posted on the PR (lines 1202–1203, 1445–1446). The validity of a
    non-VOID token therefore rests partly on records off `main`. That is acceptable only as a stated exception, or
    with the re-establishment route of §A.42 item 7, which does not re-run these checks.
- **§A.44.** No condition reads log text. "Not-applicable" is described, never parsed, and B6's conclusion carries
  it.
- **Register.**
  - **S4.** The frozen texts (lines 745–803, 861–869, 903–906) contain no S4 phrase (`p05`, empty). The owner's
    standard and the ladder rows are verbatim; checked against the recorded c.6723491138 text.
  - **Caps.** The added identifiers (ZIP-1, S1-BIND, GT-8, HEX40) are acronyms or code names.

## Nits (fix in the same revision)

- **N1.** Under E-ID (iv) the session's credential is not `amaybaum`'s, so two sentences are false.
  - "Host records cannot tell the owner's comment from one posted with the session's credential" (line 1498, new in
    r14) and 2b (b)'s "the host cannot tell the poster from the session".
  - **Fix:** scope both to (i)–(iii).
- **N2. Retakes, and the E entry's measurements.**
  - `verdict` now requires "every approval entry holds". But a host-VOID run's entry cannot meet the review and
    binding conditions (no approved review, or B3 not `success`), so any retake after a host VOID ends VOID.
  - `verdict` builds only one `E` entry, so an `E` retake leaves the void `E` deployment unmapped.
  - The `E` entry's "the measurements' `parameters.dispatch_sha`" needs E's artifact, which nothing reads; B3 already
    implies it.
  - **Fix:** scope the binding to the attesting run; build one entry per E-stage comment id; drop the `E`
    measurements clause, or read E's archive by the S1-binding route.
- **N3. Artifact names.**
  - `upload-artifact@v4` defaults to `name: artifact` and refuses a duplicate name within a run, so A4, A6, B5 and
    A11 need distinct names.
  - The S1 binding and 6′'s check ("no `measurements.json` artifact") read names.
  - **Fix:** state them, as Q-C2-1 does.
- **N4. The 6′ records are not re-derived from the host.**
  - `check --freeze` verifies `design-run.json` and `confirmation-run.json` only against pins taken from the same
    files. It re-reads the gate-test runs (line 2039) but not these two.
  - The binding that replaces r13's digest link (A3b and A7 at 6′) thus rests on a supplied copy.
  - **Fix:** re-derive the needed subset (conclusions, `head_sha`, `pull_requests`) by the pinned run ids.
    `confirmation-measurements.json` is likewise an unbound executor copy. That is low-risk, since any pre-S1
    fixture-mode output yields the same section, but say so.
- **N5.** The id of GT-6 (a)'s owner comment, which `check --freeze` reads, is neither a field nor an argument of
  `check --freeze`. Record it in `gate-tests.json` or as a `PENDING` field.
- **N6.** Adopt Q-C2-1's "binding's record at `E`" (inputs in `s1-run/results.json`, and `verdict`'s read equal to
  them), so that S1's binding is recorded on `main` (§A.42 items 7 and 8).
- **N7.** Line 1209, "`controls.py` never reads it directly unless E-READ (c) is adopted", is false under (a): A11
  runs `controls.py env-read`. It predates r14, but sits in the paragraph r14 rewrote.
- **N8 (`ACCESS.md`).**
  - §6.3 still justifies GX+R-Y by "every effect is a sum of point reads", although the r14 header says §6.4's
    condition is "used for both". Cite §6.4.
  - §6.4's "The infeasibilities also rest on the exact LP" is not yet true for GX+R-Y: no exact LP has been run on it
    (`r13-full` §1; 6′ pending).
- **N9 (the witness principle; bears on the N11 decline).** The CONTEXTUAL text renders `cert_X3` as "A native read
  equal to `g`: no". The search covered only F1's 36 reads on `Ω_reach`. Scope it: "An F1 read equal to `g` on
  `Ω_reach`: no".
- **N10 (shared with Q-C2-1; predates r14).**
  - **The trap.** A red A3 in any non-dispatch run on a recorded branch makes A3b `skipped`, which is a violation,
    and the round is VOID. That includes a design-branch iteration whose fixture expectations do not yet match.
  - **Fix:** either state that no red-A3 push is made on a recorded branch after `T0`, or give A3b `if: always()`.
    A3b would then still fail on a missing or non-fixture output.
- **N11.** 6′'s tree differences: the preregistration in 6′'s tree also carries the later steps' fields unfilled
  (`env-pin.json`, `gate-tests.json` and the `F` dispatch), not only "6′'s own".

## 6. Probe files (`review/probes-r14/`; reviewer checks, not evidence)

| file | what |
| --- | --- |
| `r14.rebuilt.md` | `make_r14.py`'s output, `9e3ef0c9…` |
| `p01_v3blocks.py` / `p01.out` | the V3 blocks of r13 and r14 compared: equal |
| `p02_pending.py` / `p02.out` | unbackticked `PENDING`: r13 29, r14 30 |
| `p03_sizes.py` / `p03.out` | fixture families (G, X, Q, H3, GX with completions): listed `n`, `d`, `E`, `C(n, d − 1)`, `C(E, d − 1)`. Ranks only, no LP |
| `p04_edits.py` / `p04.out` | the 92 edits by tag |
| `p05_s4.py` / `p05.out` | the S4 screen of the frozen texts: no hit |
