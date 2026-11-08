# ARP-1, M-ARC: does protection survive an in-world archive? Native round ARP-1-MARC — PREREGISTRATION (draft r7)

**Status: WIP / UNVERIFIED preregistration, drafting, not a candidate `F`.** Model-written. r3 was independently
reviewed (REVISE) and r4 (ACCEPT WITH CHANGES); r5 applied the r4 review; r5 was checked (ACCEPT WITH
CHANGES), and r6 applied that check's R5-B1 to R5-B3 and N1–N3, with R6-B1 in r6a. r7 applies the static review of the
implementation (REVIEW-MARC-IMPL: I-B1, I-B2 and the §5 text edits); a diff check of the edited lines remains. This file is the control plane of a native round under `AGENTS.md` §A.39, to be drafted on its own guiding
pull request from `D`. Scientific execution is under the owner's programme authorization (#1169 comment 6723277401).
The owner designates `F` and `E` and approves each dispatch, under the designation boundaries of #1169 comment
6723329527 (*Authority*). An instruction to proceed is neither a designation nor a dispatch approval. Nothing is
executed before `F`. Every `PENDING` field is filled before `F` is requested, and control P refuses a `PENDING` field
under `--freeze`. A `PENDING` field is the bare word `PENDING` outside an inline code span; fenced code blocks
count as outside, and the word inside backticks is rule prose, not a field. The last pre-`F` commit replaces this
status paragraph with the candidate form.

```v3-round
round ARP-1-MARC
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/
record AM verification/receipts/ARP-1-MARC.json
execution M .github/workflows/verify.yml
```

**Frozen expectation for the two blocks.** Recorded here, outside the blocks:
- the round declaration's three lines are `round ARP-1-MARC`, `kind non-sealing` and
  `record-directory verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/`;
- the governed-paths digest, computed as `S7` defines it, is
  `4ddc9a8af70564d7b73a65b3f431a0b4fbdf1c1518327f6e4d8ea6dff2702563`.

Precondition 6, and control T at S1 and `E`, re-derive both from the blocks at `F` with `tools/v3_verifier.py`'s
`control_plane` and `governed_digest`. A mismatch fails.

The record directory holds:
- this preregistration, at `verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/preregistration.md`,
  and amendments under `amendments/` (before `F` only);
- `marc_check.py`, the checker, and `controls.py`, each at the blob pinned below;
- structured evidence under `evidence/`;
- the result note `result.md`.

The one execution path is `.github/workflows/verify.yml`, which receives the frozen splice (*The workflow edit*).
None of these changes under any outcome: a manuscript, a built artifact, `verification/ROADMAP.md`, a kernel module,
the source records listed under *Inputs*, another round's record. They lie outside every entry above, so a change to
any of them is unauthorized under `S7`. No Lean module is involved.

## Authority (quoted with author and time)

- **Programme authorization, #1169 comment 6723277401** (posted by the coordinating session as amaybaum,
  2026-11-08T15:21:11Z, recording the owner's chat authorization of about 15:20Z). The passages this round is bound
  by, verbatim:

  > 1. **M-ARC** — Test replacing the supplied, isolated archive with an archive that remains in the world. Preserve
  > the specified exact F₂ span-membership test on 7- and 9-cell rings, its four outcome labels (exposure, survival,
  > size-dependent, void), and the requirement for green controls at both sizes.

  > - Obtain independent review and resolve all blocking findings before freezing.
  > - Establish and record the exact freeze point F before scientific execution.
  > - Execute only the frozen, authorized scope, using the required CI and verification procedures.
  > - Preserve negative, inconclusive and vacuous results without reinterpretation or post-hoc changes to
  >   acceptance criteria.
  > - Stop and report any failed gate, unresolved blocker or material deviation rather than bypassing it.

  > The C2 re-review and consolidated classification-audit findings must be incorporated before M-ARC's freeze. If
  > they require material changes, revise and independently review the affected preregistration first.

  > The priority is genuine assumption removal, not obtaining a positive result by introducing equivalent
  > assumptions under different names.

  > Do not interpret authorization as approval to merge PRs, promote scientific claims or change the underlying
  > physical assumptions without their separate required gates.

- **Designation boundaries, #1169 comment 6723329527** (posted 2026-11-08T15:25:55Z, quoting the owner verbatim):

  > Approve option (a): retain owner designation of each freeze point F and execution head E.

  > Before each freeze, present the reviewed candidate F, exact commit, independent-review verdict, controls and
  > outstanding blockers for my designation. Before each execution, present the exact execution head E and proposed
  > dispatch for my approval.

  > No automatic freezes or dispatches. The halt-only rule remains mandatory, and any failed gate stops progression.

  Applied here: `F` and `E` are each designated by the owner, and each designation is quoted in the record with its
  author and time (§A.42 item 7). Each dispatch (`F`, S1, `E`, and any host-VOID retake) needs its own owner approval,
  under *Approval entries*. **S1 is where the decisive computation runs.** The S1 dispatch is presented to the owner
  as the execution dispatch under the second quoted passage; `E`'s run is the replay attestation of that computation,
  not a second computation. No local run of the decisive mode is made at any stage.

- **Owner direction on assumption-dependence analysis, #1169 comment 6723491138** (posted as amaybaum, author
  association OWNER, 2026-11-08T15:40:41Z, recording the owner's chat direction verbatim). Implemented by
  *Assumption-dependence analysis*. Bound passages, verbatim from that comment:

  > The preregistered outcomes should remain unchanged. Any broader conclusion should be separately qualified, and new
  > variants should be tested in new rounds rather than retroactively modifying the original experiment.

  > Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still produce valid
  > probabilities, observable quantum predictions and consistent behavior across repeated experiments.

  > We should not weaken the empirical standards for equivalence. We should instead challenge whether our chosen
  > mathematical framework for testing equivalence is unnecessarily restrictive.

- **Owner directions, #1169 comment 6723571280** (posted as amaybaum, author association OWNER,
  2026-11-08T15:47:58Z, recording the owner's chat directions verbatim). Bound passages:

  > Continue the approved sequence unchanged. I would not introduce another round or change M-ARC's acceptance
  > criteria now.

  > One additional principle should guide interpretation: failure to construct a witness is not proof that no witness
  > exists, unless a theorem establishes that impossibility within a clearly stated scope.

  > The third is what ultimately matters. We cannot establish equivalence merely by escaping a no-go theorem.

  The witness principle is applied in ADA Part 2; the third passage refers to the third row of the owner's
  significance ladder in the same comment ("The mechanism reproduces the required quantum predictions, measurements
  and composition | We advance toward operational equivalence"). **The acceptance criteria are those of M-ARC as
  authorized:** the four labels, the parameters, and green controls at both sizes. Revisions r2–r4 add checkpoints, an
  independent recomputation of the exposure count (C-XB) and the ADA; each changes no label or parameter and moves no
  case between EXPOSURE and SURVIVAL; four specified controls carry strengthened, entailed pass conditions (item 10). C-XB's exposure comparison can only void a run whose span-method count
  is not reproduced independently.

- **The specification.** M-ARC as accepted in the EOI classification audit, cluster C3, revision r3 (§2, "Named
  follow-up, M-ARC"), accepted by the independent re-review of r3 with optional points n1–n3, all three applied
  here: n1 names the non-uniform law in C-SUPP; n2 rewords C-NV (no separate meter cells); n3 names variant D in the
  exposure and survival labels. The audit is paper-only, model-written and model-reviewed; nothing in it is adopted
  here. Its content enters this round only through the definitions restated below, each traced to a record on `main`.
- **The consolidated audit package**, accepted by model review (REVIEW-PACKAGE-r2); owner acceptance of the package
  (package §8 item 1) pending (precondition 1).

**References off `main` (§A.42 item 8).**

| reference | used for | classification |
| --- | --- | --- |
| `AUDIT-C3.md` r3 (sha256 `d143754b…5e40e68b`), `REVIEW-C3-r3.md` n1–n3, `PACKAGE.md` r3 (sha256 `33075f9f2e4df52cf87536ebcb8c8c931f89960e3a067af30c182587f3109b74`), all scratchpad | the source of the question's wording | provenance: every definition, parameter and control is restated in this file, which lands on `main`, and traced to records on `main` |
| #1169 comments 6723277401, 6723329527, 6723491138, 6723571280 | authority, designation boundaries, the ADA direction, the witness principle | owner records of decisions; no scientific claim rests on them |
| the dev branch `draft/arp1-marc-dev` and its runs | design evidence (precondition 4); the dev-branch clause of the ordering rule | design evidence: provenance; the scripts land on `main` at S1 at their pinned blobs, and `evidence/design-run.json` lands at S1. The ordering rule's dev-branch clause uses those commits: it is a governance attestation outside any enduring scientific claim, and `order.json` commits each dev run's commit id, tree id and shard-job text sha256, so the classification can be re-read from `main` without the branch; the remaining dependence is on the dev commits themselves for any re-derivation of those digests |
| CI runs of `F`, S1 and `E` | the attestations | provenance under §A.42 item 2; the computation is re-established from `E` on `main` by the recipe `python3 -I -B <rd>/marc_check.py` and the committed `evidence/measurements.json` |

## The objects

- **`D`** = PENDING: the head of `main` from which the round PR begins, as a full 40-hex id.
- **`F`**: the commit carrying this file that the owner designates. `delta(D, F)` is this file and any amendments.
- **S1**: a single-parent child of `F`. It adds `marc_check.py` and `controls.py` at their pinned blobs,
  `evidence/design-run.json`, `evidence/f-run/results.json` and the frozen workflow splice. **S1 is where the decisive
  computation runs:** its owner-approved exact-head dispatch is the execution dispatch and the first computation of
  variant D. Ordinary CI at S1 does not compute it: the check step runs only on `workflow_dispatch` or when committed
  measurements exist, and the order rule requires that check step to be `skipped` in every non-dispatch run at S1.
  After `E`, every run replays the committed measurements. The output of the S1 dispatch is the artifact
  `arp1-marc-measurements`, retrieved through the artifacts API (§A.44).
- **`E`**: a single-parent child of S1 adding `evidence/measurements.json` (the S1 artifact's bytes),
  `evidence/s1-run/results.json`, `evidence/order.json` and `result.md`, and nothing else. Its owner-approved dispatch
  is the replay attestation: the checker runs again and the committed bytes must match. The owner designates `E`.

**Branches (frozen; held byte-identical in every commit of `D..F`).** The writer of record is the coordinating Claude
Code session. The following line stands alone at column 0 in the round PR's first control-plane commit and in every
later commit of `D..F`; P reads each of those commits through git:

arp1-marc branches: round research/arp1-marc-20261108; dev draft/arp1-marc-dev

The dev branch carries the scripts before `F` and the design run (precondition 4), on its own draft PR, under ordinary
`pull_request` CI only, and every one of its runs is `design` or `none` (checked by `controls.py plane` before `F`
and by the order rule at `E`). No execution work happens on it after `F`: S1 is committed on the round branch from the frozen blobs. The dev
branch is not deleted, and its commits are not force-pushed away, before `order.json` is captured.
- **`W`**, **`Λ`**, **`Q`**: the withdrawal commit of a halt, the last reconciliation and the receipt commit
  (§A.39 items 3–4, `S12`).

**Drift, measured.** The audit's snapshot is `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`. No path under the four
source record directories (*Inputs*), `tools/`, `.github/` or `verification/infrastructure/` changed from it to
`2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`, the head of `main` as last read. When `D` is filled in, this sentence is
extended from `2cd49dc0` to `D` (PENDING). Control DS measures it in two parts: from `5ce4f98e` to `D`, no change under
those directories; from `D` to the commit under check, no change under them except `.github/workflows/verify.yml`
(which W checks is `D`'s plus the frozen splice) and except the record directory; and the seven input blobs
unchanged at the commit.

## Inputs (read from `D`; blobs at `2cd49dc0`, re-checked by DS)

`R/` = `verification/programmes/oi-qm/reconstruction/`.

| short | path | blob | used for |
| --- | --- | --- | --- |
| QA | `R/quarter-phase-native-20261107/DESIGN.md` | `fb21999b0d45750a465dda742589f0af11575326` | Lemma Q (QA:460-495); P2 without a law (QA:142-144); support, not measure (QA:499-501) |
| AP1 | `R/apparatus-1-20261107/DESIGN.md` | `51c24aeb7b42a915b8942462435fd9fe129861de` | SA-1(b) terminality (AP1:292-296); SA-1(c) (AP1:297-299); Lemma 3 (AP1:533-561); C9 (AP1:682); budget-relative isolation (AP1:338-343) |
| MI-D | `R/minacc-1-20261108/DESIGN.md` | `737047be04dcf94f1ddcf7eae0abf736e2c0d52e` | definitions (MI-D:124-145); `N_1` (MI-D:282-287); archive (MI-D:351-365); PROT-D (MI-D:429-436) |
| MI-R | `R/minacc-1-20261108/RESULT.md` | `5adf76ebc8afa95cc51f45fb84c909b13876516c` | C-LIN, PROT-D in the linear limits (MI-R:394-428); C-P1, C-P2 (MI-R:373-374) |
| MI-A1 | `R/minacc-1-20261108/amendments/A1-prereg-review.md` | `3031a78d5ffe33c182e7fc70236b5e51566cadbe` | provenance |
| MI-A3 | `R/minacc-1-20261108/amendments/A3-post-result-prot-r.md` | `216e0a216a4d276144156a993ab5189d16a18e54` | information moved to archived cells (MI-A3:21-38); provenance |
| M2D | `R/mechanism-2-20261108/DESIGN.md` | `9352d9da7da6a55a52e6ada235034219638b34d2` | the claim under test, "native instance" (M2D:853-854) |

All seven records are themselves **WIP / UNVERIFIED** and model-reviewed. This round uses from them only
definitions, which it restates, and Lemma Q(iii) in the linear limit as the countercontrol's expectation. It uses no
result of theirs as a premise (§A.46 item 7): CC-ISO re-derives Lemma Q(iii)'s conclusion in this model by
computation, and a failure voids the round.

## The question

**As M-ARC fixes it.** In variant D, is any `Q* = 1` linear functional on the cells of the current `V` determined in
a positive-probability record branch within the horizon `T`? Variant I, the supplied isolated archive (P1), is the
countercontrol.

**The model** (M-ARC, restated on the records' definitions).
- Ring `Z_L`, alphabet `F_2`. Each cell carries `(u_i, v_i)` with `u_i = x_i(t)`, `v_i = x_i(t−1)` (MI-D:124).
- The rule is `N_1`, always on: `u_i' = u_{i−1} + u_{i+1} + v_i`, `v_i' = u_i` (MI-D:282-287; QA:462-464 with
  `k_ij = 1` for nearest neighbours, `k_ii = 0`; the sign of `v` is immaterial at `q = 2`).
- `V` = sites `{0, 1, 2}` (`w = 3`); `H` = sites `{3, …, L − 1}`; `|H| ∈ {4, 6}`, so `L ∈ {7, 9}`; horizon `T = 4`.
- At `t = 0` each site of `V` holds a P2 ready cell: exactly one slot known (value 0, or 1 through H-PREP), the other
  unknown (AP1:297-299; QA:142-144). Which slot is known is a supply choice: all `2³ = 8` **supply patterns** are
  enumerated. Each site of `H` holds a source cell, both slots unknown.
- **Registration** happens between ticks. At each time `t ∈ {0, 1, …, T}` the observer may register one slot (`u` or
  `v`) of one cell of the current `V`; that slot's value at `t` enters the record. Each cell is registered at most
  once. Registration is the only access (MI-D:363). Allowing `t = T` (after the last tick) makes the schedule set a
  superset of "between ticks": every schedule without a registration at `T` is still enumerated. Exposure is an
  existential over cases, so a superset can only add exposing cases and never remove one; a survival over the
  superset implies survival over the subset. Lemma Q(iii) covers every time, so CC-ISO is unaffected. Because an
  EXPOSURE could rest only on schedules outside a strict "between ticks" reading, the measurements carry sub-counts
  (no registration at `t = T`: 361 schedules per pattern; registrations only at `t ∈ {1, …, T − 1}`: 139), which the
  EXPOSURE and SIZE-DEPENDENT texts print; they do not enter the label. No refills, no swaps, no arming, no isolation
  edits, no translations, no vacancies other than variant I's.
- **Variant D (de-isolated).** The registered cell stays at its site and keeps taking the `N_1` step with its
  neighbours. Its site leaves `V` and joins `H`. It is never registered again.
- **Variant I (isolated).** The registered cell is removed from the ring and takes free ticks `(u, v) ↦ (v, u)`
  thereafter, as in MI's archive (MI-D:357-358). Its site is left decoupled: its neighbours' sums omit it, as for a
  vacant site (MI-D:341-345; MI-R:401-403). Its site also leaves `V`.
- **Order at each time `t`:** the registration (if any), then the evaluation on the current `V`, then the tick to
  `t + 1` (for `t < T`).
- **Determined** (MI-D:135-137): constant on the support of the conditional law given the observer's knowledge `K`
  (supplied placement and known values, the schedule, the entire joint record), branch by branch, before any
  averaging.

**Kept, removed and not used.**

| item | status in this round | where it enters |
| --- | --- | --- |
| `N_1` at `q = 2`: symmetric, center-free, linear, nearest-neighbour (A4, A5; QA ledger N1, N1-CI) | kept | every tick, both variants |
| P2: one known slot per ready cell; no supplied cell with both slots known | kept | `I_0` |
| P2's support clause: full joint support of the unknowns | kept; it is what makes determination equal span membership | the span method |
| H-PREP for a known value 1 | kept, inert: values only translate the knowledge set | none of the span computation |
| Supplied registration: one slot of one `V` cell between ticks, at most once per cell, record kept whole | kept | the schedule set |
| Supplied schedule choice, adaptive or not (feedback executor) | kept | covered by enumerating fixed schedules |
| Finite ring; source cells in `H` | kept | the model |
| Refills and archive swaps (MI-A1:203-213) | **not used**, in both variants (M-ARC: "No refills and no swaps") | — |
| P3 arming, E-iso, translations | not used | — |
| N2 and H-PS (product-uniform law) | **not used** for determination; used only in C-SUPP-F, with the named non-uniform law | — |
| **SA-1(b)'s terminality: "A registered cell is not coupled to any cell afterwards" (AP1:295-296); MI's archive "leaves the ring, takes free ticks thereafter, couples to no cell" (MI-D:357-358)** | **removed in variant D; kept in variant I** | the step after a registration |

The one assumption removed is the coupling isolation of the archived cell. What variant D keeps of the archive is
its defining access property, shared with variant I: the registered cell is out of the observer's window and is not
read again. That is the observer's access, not a property of the dynamics.

**Isolation must not return under another name (control C-DEISO, below).** Variant D passes only if all of these are
measured to hold at both sizes:
- (a) its step at every tick of every case is the unmodified `N_1` ring step on all `L` sites: no dropped edge, no
  vacancy, no free tick, no reset, no refill;
- (b) for every case, D's and I's step matrices differ only in rows or columns of archived cells;
- (c) re-coupling is real: in D, some case has a transported registered functional `ρ_t` with `ω(ρ_t, g) = 1` for
  some slot `g` of a current-`V` cell within `T`; in I, no case has one (the commutation AP1 Lemma 3 uses,
  AP1:543-545);
- (d) D and I run over the identical list of cases, and no record is dropped: `R_t` carries every registration made;
- (e) no functional is added to `I_t` after `t = 0`.

The renaming check of the ADA (Part 3) maps each imported item to these clauses. The clauses differ in strength:
(a), with C-XB's independent simulation, is the substantive guard; (b) and (c)'s D-half are measured comparisons;
(c)'s I-half holds by disjoint support, (d)'s rank holds under any invertible transport, and (e) is a counter the code
keeps about itself. These three are construction checks, not independent evidence.

## The exact method

**Representation.** The state at `t` is `x_t ∈ F_2^{2L}`, ordered `(u_0, …, u_{L−1}, v_0, …, v_{L−1})`. A tick is
`x_{t+1} = M_t x_t`. In D, `M_t` is the `N_1` ring matrix `M_L` at every tick. In I, `M_t` is the ring matrix with the
archived cells' edges removed and free ticks on the archived cells. A linear functional is a row vector `g`; a value
known at time `s` is known at `t > s` as `g (M_{t−1} ⋯ M_s)^{−1}`. Each inverse is applied through the explicit
second-order inverse `(a, b) ↦ (b, a + f(b))`, written independently of `M_t` and checked against it (C-STEP).

**Knowledge.** `I_t` = the transported known slots (one per `V` cell, by pattern). `R_t` = the transported registered
slots. `S_t = span(I_t ∪ R_t)`. `W_V(t)` = the functionals supported on the current-`V` cells. Under P2's support
clause the knowledge set in each branch is an affine subspace with direction cut out by `S_t`, so `f` is determined
in a branch exactly when `f ∈ S_t` (AP1:546-547; MI-R:408-411). That is the same in every branch of a fixed schedule;
the known values and record values only translate the knowledge set. No probability enters, and N2 does not enter.

**Adaptive schedules.** An adaptive schedule is, within each record branch, a fixed schedule; determination for a
fixed schedule does not depend on the branch. So enumerating every fixed schedule covers every adaptive one.

**Cases.** A case is a supply pattern and a schedule. Schedules: at each `t ∈ {0, …, 4}`, nothing or one registration
`(site, slot)` of a current-`V` cell, each cell at most once. Their number is `Σ_k C(5, k) · 3!/(3−k)! · 2^k = 751`,
so each variant and size has `8 · 751 = 6008` cases and `5` evaluation times.

**Exposure test (span).** At each case and time, compute a basis of the intersection `S_t ∩ W_V(t)` over `F_2` by
elimination (eliminating the coordinates outside the current `V` first; an intersection, never a projection). `Q*`
vanishes on a subspace exactly when it vanishes on each basis vector and `ω` vanishes on each pair, since
`Q*(f + f') = Q*(f) + Q*(f') + ω(f, f')`. An **exposing case** is one with some `t ≤ T` at which `Q*` does not vanish
on `S_t ∩ W_V(t)`. The **witness** is the first exposing case in the frozen enumeration order (patterns as words over
`u < v` in site order; schedules as the tuple of per-time actions with nothing `<` `(0,u)` `<` `(0,v)` `<` `(1,u)` `<`
…; then `t`), with the least `Q* = 1` element of `S_t ∩ W_V(t)` in this encoding: the current-`V` cells in ascending
site order, each contributing the pair `(u_c, v_c)`, the first cell's `u_c` the least significant bit. The witness
also records whether its schedule registers at `t = T`.

**Brute-force cross-check (C-XB), independent of the span method.** For each case of D and I at both sizes, simulate
`N_1` (or I's archive) directly on bit-sliced Python integers over every assignment of the unknown slots (`2^{2L−3}`
assignments: 2048 at `L = 7`, 32768 at `L = 9`), with known values all 0. Group assignments by record branch. For each
`t` and each of the `4^{|V(t)|}` functionals on the current `V`, determined-by-enumeration in each branch must equal
membership in `S_t`. C-XB then evaluates `Q*` directly, coordinate by coordinate, on every functional it found
determined, and sets its own exposure flag for each case and time; this flag must equal the span method's. The same is
done for variant C9, which has exposures, so the comparison is exercised on positive cases at both sizes. At `L = 7`
the D and I comparison is repeated with known values all 1 (H-PREP). C-XB shares no code with the span method beyond
the case list. Under C-XB the cases checked per variant and size are 6008, the evaluation times per case 5, and the
(functional, branch) checks 808,960.

**Arithmetic.** Integers and bit operations over `F_2`; `fractions.Fraction` for C-SUPP-F's law. No floating point
anywhere. No measure is used for any determination statement.

## The controls

Each control is evaluated at `|H| = 4` and at `|H| = 6`. Its green criterion is frozen. `decide` recomputes every green
flag from the raw counts in `measurements.json`, and the checker's own flags must agree with it.

| code | what it is | green when | how it can fail |
| --- | --- | --- | --- |
| **CC-ISO** (countercontrol) | Variant I over all 6008 cases. Lemma Q(iii) as stated, on the intersection `S_t ∩ W_active(t)` (Lemma 3's object, AP1:547), where `W_active(t)` is the functionals supported on on-ring cells: `Q*` vanishes on it and it is isotropic; hence nothing on the current `V` | `exposing_active = 0`, `exposing_V = 0`, `nonisotropic = 0` | a transport, archive or elimination error that lets isolated registration expose; it shows that "survival" is a reachable reading |
| **C-NV** (non-vacuity; n2's wording) | In D and in I: some `Q* = 0` functional on the current `V` is determined by registration, i.e. lies in `S_t ∩ W_V(t)` and not in `span(I_t) ∩ W_V(t)` | `nv_cases > 0` in D and in I | records that never reach `V` (inert `R_t`), which would make exposure unreachable. Reachable by hand: pattern `vvv`, register `(1, u)` at `t = 1`; then `v_0 + v_2` at `t = 1` |
| **C-SUPP-X** (exact relation, §0.3 type; MI-R:374) | Variant I over all cases with the supplied relation `u_1 + v_0` added to `I_0` (a support restriction) | `exposing_V > 0` | a checker that ignores supplied knowledge. Reachable by hand: pattern `uvv`, register `(0, v)` at `t = 0`; then `u_1 + v_1` |
| **C-SUPP-F** (full-support correlated law, n1) | Variant I, the fixed protocol: pattern `uvv` with known values 0, register `(0, v)` at `t = 0`, evaluate at `t = 0`. The law of `(u_1, v_0)` is §0.3's pair: `P(u_1 = v_0) = 3/4`, that is `P(0,0) = P(1,1) = 3/8`, `P(0,1) = P(1,0) = 1/8`; every other unknown uniform and independent. Exact enumeration in `Fraction` | in branch `v_0 = 0`, `P(u_1 + v_1 = 0) = 3/4`; in branch `v_0 = 1`, `1/4`: biased, not determined; and the span method on the same protocol, without the relation, finds `u_1 + v_1 ∉ S_0` | a law treated as a relation (determination), or a wrong conditional law; the two values are pencil-derived and independent of the checker. The span half ties the control to the decisive pipeline |
| **C9** (P1 removed from I; AP1:682; MI-R:373) | Variant I with P1 dropped: the registered cell is not archived; it stays coupled on the ring and stays in the current `V`. Deviation, stated: AP1's C9 is a two-read form (register a meter, then read its kick slot through a fresh meter). This model has no separate meter cells (n2), so C9 takes MI-R's C-P1 form (i): registration while the cell stays active (MI-R:373) | `exposing_V > 0`; `exposing_at_registration` (cases that expose at `t = 0` at a registration made at `t = 0`, before any tick) is recorded, and L-ACC's ADA status reads it | a determination predicate, or an archive path, that still reports protection once P1 is removed. It tests P1's removal because the one-slot-per-cell isotropy that Lemma 3 needs (AP1:543-545) fails as soon as a registered slot and the cell's known slot stay together on an active cell. It exposes at registration time without a tick, so it tests the predicate, not transport; transport is tested by C-NV, C-XB and C-DEISO (c). Reachable by hand: register the unknown slot of any ready cell |
| **C-DEISO** | (a)–(e) of *The question*; ADA Part 3 | all five hold | isolation reintroduced in D under another name, or D and I differing in more than the archive |
| **C-XB** | the brute-force cross-check, membership and exposure | `mismatches = 0`; `exposure_mismatches = 0`; its own `exposing_V` equal to the span method's for D, I and C9 at each size; every case and time checked | span method and direct simulation disagree on membership (transport direction, archive handling, elimination) or on exposure (a dropped `ω` term, a `v`-index offset), so a false SURVIVAL from a false-negative detector is caught |
| **M-PLANT** (mutation) | D and I with a planted `Q* = 1` known functional `u_1 + v_1` added to `I_0` (C-P2's form, MI-R:374) | the empty schedule exposes at `t = 0` for every supply pattern, in both variants, and `exposing_V > 0` in both | an exposure detector or witness path that cannot report a planted exposure |
| **C-STEP** | every step matrix used: invertible against the independent inverse, symplectic (`MᵀJM = J`), `Q*` and `ω` preserved on every basis pair | `violations = 0` | a wrong rule (for example a center term, which breaks `Q`, QA:518-521) |
| **C-HOR** (size and horizon) | `T ≤ |H|`, and `M_L^t`, `M_L^{−t}` vanish between sites at ring distance `> t` for `t ≤ T` | both hold | wrap-around through `H` back into `V` within `T` |

**Field → predicate (frozen; `decide` recomputes each flag from these raw fields, at each size key).**

| control | raw fields | green when |
| --- | --- | --- |
| CC-ISO | `I.exposing_V`, `I.exposing_active`, `I.nonisotropic` | all 0 |
| C-NV | `D.nv_cases`, `I.nv_cases` | both > 0 |
| C-SUPP-X | `supp_x.exposing_V` | > 0 |
| C-SUPP-F | `supp_f.cond_v0_0`, `supp_f.cond_v0_1`, `supp_f.span_determined` | `"3/4"`, `"1/4"`, `false` |
| C9 | `c9.exposing_V`, `c9.exposing_at_registration` | first > 0 (second is recorded) |
| C-DEISO | `D.step_is_ring_violations`, `d_i_diff_outside_archived`, `D.coupling_cases`, `I.coupling_cases`, `case_list_sha256.D`, `case_list_sha256.I`, `D.records_kept_violations`, `D.min_rank_I`, `D.knowledge_injections` | 0, 0, > 0, 0, equal, equal, 0, 3, 0 |
| C-XB | `xb.checked_cases` (per variant), `xb.checked_times`, `xb.mismatches`, `xb.exposure_mismatches`, `xb.exposing_V` (per variant), the all-1 repeat at `"4"` | 6008 each for D, I and C9; 5 × 6008 each; 0; 0; equal to `D.exposing_V`, `I.exposing_V`, `c9.exposing_V`; its mismatches 0 |
| M-PLANT | `plant.D.empty_t0`, `plant.I.empty_t0`, `plant.D.exposing_V`, `plant.I.exposing_V` | `true`, `true`, > 0, > 0 |
| C-STEP | `step.violations` | 0 |
| C-HOR | `horizon.T_le_H`, `horizon.radius_violations` | `true`, 0 |

**Self-tests** (none enumerates variant D):
- *decision path:* `decide` and the note generator driven through every label, and through VOID for each control
  flipped at each size and for each malformed or missing field;
- *transport:* `M` in place of `M^{−1}` must fail C-XB on the C-NV hand case;
- *detector:* with the `ω`-pair term dropped from the span detector, C-XB must report an `exposure_mismatch` on C9's
  hand case (`v_1` known, `u_1` registered); the pass condition is that mismatch, whatever basis the elimination
  returns;
  a `v`-index offset at `L = 9` must fail C-STEP or C-XB on the C-NV hand case;
- *workflow (B1):* removing the check step's `if:` condition, or the dev splice's `--fixture-output`, fails W or the
  order rule; a non-dispatch run at S1 whose check step is `success` fails the order rule; a dev run whose shard job
  differs from the frozen design job, or whose scripts are not at the pinned blobs, is not `design` and fails;
- *attempts:* a dispatch run with `run_attempt = 2` fails the order rule and `verdict`;
- *host-VOID:* at `E`, a run whose check step started and failed, with the replay step `skipped`, is classified not
  host-VOID; a run whose check step is absent, `skipped` or without `started_at` is host-VOID; a dev run with a script
  pair outside the frozen list of design pairs is `other`;
- *jobs answer:* `verdict` and `derive-run` on a realistic jobs-API answer that lists the synthetic steps ("Set up
  job", "Post …", "Complete job") beside the seven named steps pass, and fail when a named step is missing or not
  `success`;
- *screen:* a paraphrase of either frozen owner quotation is caught by S4, and the exact quotations pass.

## The decision rule (frozen; `controls.py decide`)

Inputs: `evidence/measurements.json`, read as structured data, and the checker's exit status.

1. **VOID** when any of these holds: the checker's exit status is not 0; the file is missing, does not parse, or
   breaks its schema; `complete` is not `true`; any control is red at either size; the checker's flags disagree with
   `decide`'s recomputation.
2. Otherwise, with `X(n)` = "variant D has `exposing_V > 0` at `|H| = n`":
   - **EXPOSURE** (in variant D) when `X(4)` and `X(6)`;
   - **SURVIVAL** (in variant D) when neither;
   - **SIZE-DEPENDENT** when exactly one; it is reported and carries neither reading.

Tokens: `ARP1-MARC-EXPOSURE`, `ARP1-MARC-SURVIVAL`, `ARP1-MARC-SIZE-DEPENDENT`, `ARP1-MARC-VOID`. The label is
computed from the measurements and from nothing else; no measured number is preregistered. VOID is not an outcome
about variant D; it halts the round (*Stop rule*).

**Added VOID routes (listed for the owner at `F`).** Each can turn a run VOID, and so halt the round; none changes a
label or a parameter, and none moves a case between EXPOSURE and SURVIVAL:
1. C-XB, membership and exposure comparison (an independent recomputation not specified by M-ARC);
2. C-DEISO, the renaming check (the owner's instruction against equivalent assumptions under other names);
3. M-PLANT and C-STEP (detector and rule integrity);
4. agreement of the checker's flags with `decide`'s recomputation, and the measurement schema;
5. the replay at `E` (byte equality of the committed measurements with a fresh computation);
6. the governance controls T, G, R, B, W, DS, P and V, the S4 phrase screen on the note included;
7. the ordering and dispatch rules: a non-dispatch run at S1 that computed; a dev-branch run neither `design` nor
   `none`; an unapproved dispatch, on any branch at S1 or `E`; any `run_attempt` greater than 1; and the ordering's
   other clauses: the designation of `F` before the first execution run, the branch names, complete captures;
8. a red job outside the shard at S1 or `E`;
9. the step and job time limits (15 and 30 minutes);
10. strengthened forms of specified controls: CC-ISO's `nonisotropic = 0` (Lemma 3's isotropy beside PROT-D); C-HOR's
    `radius_violations = 0` beside `T ≤ |H|`; C-SUPP-F's exact values `"3/4"` and `"1/4"` and `span_determined =
    false`, where M-ARC says "at most bias"; C-NV's "determined by registration" (not in `span(I_t)`, n2's wording).
    Each follows from the specified condition when the computation is correct (a theorem in variant I, the rule's
    radius, pencil values, n2), so each can only make a broken run VOID;
11. `derive-run`'s artifact checks: the zip's `digest`, `workflow_run.id` and `head_sha`;
12. a host-VOID with no recorded retake decision.

## What each outcome would and would not show (frozen texts of the result note)

`controls.py note` generates `result.md` from `measurements.json` and the derived run results: the round, `D`, `F`,
S1, `E`; the control table (code, size, PASS or FAIL, the raw counts); the token; then exactly one frozen text below,
with only measured integers and the witness interpolated; then the section `ADA` (*Assumption-dependence
analysis*, Part 2). The note passes the phrase screen S4.

**Common clause, in every substantive text:** "This concerns the finite model of this round: the ring `Z_L` with
`L ∈ {7, 9}`, the rule `N_1` at `q = 2`, a three-cell window, horizon `T = 4`, at most one registration per tick and
each cell registered at most once. It is conditional on the supplied registration, on P2 with its support clause, and
on H-PREP for a known value 1. Determination uses no measure; no statement about bias is made. Agreement of the two
ring sizes is not evidence about an infinite chain: at both sizes some sites of `H` are reached within `T` from both
ends of the window, which only `|H| ≥ 2T = 8` would exclude. Nothing here concerns other rules, larger windows or
horizons, an archive held elsewhere, or a physically sourced observer."

- **EXPOSURE.** "In variant D, where the registered cell stays on the ring and its site joins `H`, the span of the
  transported known and registered functionals contains a `Q* = 1` linear functional on the current `V` in {n4} of
  6008 cases at `|H| = 4` and {n6} of 6008 at `|H| = 6`; among cases with no registration at `t = T`, {m4} and {m6};
  among cases registering only at `t ∈ {1, …, T − 1}`, {k4} and {k6}. First witness, at `|H| = 4`: {witness}; it {uses or does not
  use} a registration at `t = T`. Every control is green at both
  sizes; variant I gives no such functional at either size. In this model the de-isolated archive does not protect:
  the protection Lemma Q(iii) gives here needs the archived cell's isolation from the ring, which the fixed partition
  into `V` and `H` does not supply." + common clause.
- **SURVIVAL.** "In variant D, where the registered cell stays on the ring and its site joins `H`, no case up to
  `T = 4` places a `Q* = 1` linear functional on the current `V` in the span of the transported known and registered
  functionals, at `|H| = 4` or at `|H| = 6`. Every control is green at both sizes. In this model, protection of
  `Q* = 1` functionals on the current `V` survives the removal of the archive's coupling isolation. It does not
  derive P1, P2 or the support clause, and it is not a statement beyond the stated horizon and sizes." + common
  clause.
- **SIZE-DEPENDENT.** "The two sizes disagree: variant D has {n4} exposing cases at `|H| = 4` and {n6} at
  `|H| = 6` (with no registration at `t = T`: {m4} and {m6}; registering only at `t ∈ {1, …, T − 1}`: {k4} and
  {k6}). Every control is green at both sizes. The result is reported as size-dependent and carries neither the
  exposure nor the survival reading." + common clause.
- **VOID.** "A required control failed, or the output was incomplete: {codes and sizes}. No reading about variant D
  is made. The measurements are preserved as produced."

**What no outcome shows**, carried as frozen text after the token: it is not a universal statement in either
direction; it does not adopt or promote M2D's reading of Lemma Q as an instance of M-INACC, or Lemma Q's labels; it does not change the
status of P1, P2, H-PREP or any manuscript claim; an exposure is not evidence that a physically sourced observer
could expose, and a survival is not evidence that P1 is dispensable outside this model.

**S4 phrase screen** (case-insensitive; on the note outside the frozen texts, and on the frozen texts themselves in
the self-test). Before screening, the byte-exact frozen owner quotations are removed: the witness principle and the
"Conversely, relaxing an assumption …" standard. Phrases: "native protection", "native instance", "theorem",
"proves", "proved", "never", "permanently", "always protects", "derived from A4", " iff ", "if and only if",
"is equivalent to", "exactly when", "in general", "for every observer", "physically justified", "should not be
read". A hit fails V. The phrases include the over-readings the consolidated audit lists for Lemma Q and M2D
(PACKAGE K-17).

## Assumption-dependence analysis (ADA)

Owner direction of 2026-11-08 (#1169 comment 6723491138, quoted under *Authority*): identifying assumption-induced obstructions is an
explicit objective. The ADA is separate from the verdict. It cannot change the preregistered label, and the
preregistered outcomes are unchanged by it. New variants are named as candidate new rounds and are not run here.

### Part 1. The assumption ledger (frozen at `F`)

Types, as the owner fixed them: **native** OI principles (preserve unless an extension is under test); **empirical**
requirements of QM (their observable consequences must be reproduced); **imported** mathematical or modelling
assumptions (challenge individually; not assumed necessary). Where the type is uncertain, the entry says so, and the
ADA carries both readings rather than the favourable one.

| id | assumption, as this round uses it | type | source |
| --- | --- | --- | --- |
| L-STEP | second-order, linear, symmetric, center-free update (`k_ij = k_ji`, `k_ii = 0`) | native | Substratum:98, :100 (A4, A5); QA:774-775 |
| L-NN | nearest-neighbour coupling | **uncertain**: QA's ledger calls it "Native, selected branch"; SM calls it an assumption beyond bounded coupling degree (A3). Carried both ways | SM:224-226; QA:776 |
| L-Q2 | alphabet `F_2` (`q = 2`) | **uncertain**: the records call it "Native parameter value, chosen per the owner's instruction"; whether the protection depends on it is untested; carried both ways | QA:462-464; MI-D:595 |
| L-RING | one-dimensional ring `Z_L`, odd `L ∈ {7, 9}`, three-cell window, horizon `T = 4`; the archived site adjacent to the window | imported (modelling reduction of the cubic graph; the odd ring is not bipartite globally, only within the no-wrap cones C-HOR measures; at both sizes some `H` sites are reached from both window ends within `T`) | QA:776 (H-FIN); M-ARC parameters |
| L-P2 | ready cells with exactly one known slot; no supplied cell with both slots, or `u + v`, known | imported (supplied posit; motivation programme-internal) | AP1:297-299, :347-349; QA:780 |
| L-SUP | full joint support of the unknowns (P2's support clause) | imported | AP1:297-299, :547; QA:499-501 |
| L-PRIOR | product-uniform law (N2, H-PS) | **uncertain**: the records call N2 a native measure applied through H-PREP; its use on supplied cells goes through an imported hypothesis | QA:777; MI-D:309, :605 |
| L-HPREP | known value 1 through H-PREP | imported (open hypothesis) | QA:782 |
| L-REG | supplied registration: one slot of one window cell between ticks, at most once per cell, the joint record kept whole | imported (SA-1(b), access part) | AP1:292-296; MI-D:351-365 |
| L-SWAP | refills and archive swaps | imported; **not in this model** | MI-D:361-362; MI-A1:203-213 |
| L-ISO | the archived cell's coupling isolation (P1 terminality) | imported; **removed in variant D**, kept in I. Not enforced natively; enforced within a budget below recurrence only by the supplied P3 and E-iso | AP1:295-296, :338-343; QA:781; MI-D:357-358 |
| L-ACC | the archived cell leaves the window and is not read again | imported (access part of P1), kept in both variants | MI-D:357-360; M-ARC |
| L-DET | "determined" as constant on the support given `K`; PROT-D as the absence of a determined `Q* = 1` functional on active cells | imported (definitional) | MI-D:135-137, :429-432 |
| L-PROTB | PROT-B (no bias) | imported (definitional); **not evaluated** here | MI-D:433-436 |
| L-INACC | the identification of protection with inaccessibility in M-INACC's sense. Reading used (AW-C3-4): clause (b) read as non-determination of a `Q* = 1` functional on the current window (PROT-D); clause (b)'s conditional-law reading (bias) and clause (a) are not tested | imported (interpretive); the identification with this functional is model-specific | M2D:832-840; MI-A1:59-70 |
| E-AR | at most two perfectly distinguishable preparations of a qubit carrier: the observable bound behind L-INACC | empirical; **not tested** in this round (NR-7) | AP1:439, :677 |

This round tests no empirical requirement of QM (E-AR is listed, not tested). None of its outputs is an observable
prediction, so no outcome reproduces or contradicts one, and no outcome reaches the third row of the owner's
significance ladder (c.6723571280).

**Which direction is the obstruction.** Primary reading: the target is QM-like inaccessibility, a functional the
dynamics uses and the observer cannot determine (M-INACC, M2D:832-840). Under it the obstruction is **EXPOSURE**:
exposure means that the protection depended on the imported isolation L-ISO. Opposite reading: if the target is taken
instead as an observer able to determine what the dynamics uses, the obstruction is **SURVIVAL**. Part 2 answers the
five questions for whichever substantive label is measured, under the reading in which that label is the obstruction,
and states the other reading beside it. Neither label is pre-judged as favourable. SIZE-DEPENDENT and VOID get no ADA
beyond Part 3 and the record of what was measured.

### Part 2. The post-result ADA (frozen template; section `ADA` of `result.md`, after the verdict)

Generated by `controls.py note` from `measurements.json` and the ledger, with frozen sentences. It cites only the
measured outputs of the frozen controls and variants, and these named results: Lemma Q(i)–(iii) (QA:460-495) and AP1
Lemma 3 (AP1:533-561), both WIP / UNVERIFIED records used as named, not as premises. Every sentence broader than this
model carries the qualifier "outside this round's model, not established".

**Statuses.** For each ledger item the note prints one status. Statuses are of three kinds, kept apart: *measured*
(a comparison this round makes between variants), *fixed by the controls' design* (true in every non-VOID result,
because the control must be green for any label; each shows that some violation of the item exposes, which is
sufficient to expose, not necessity of the item as stated), and *used, not varied*.

| item | status rule | kind |
| --- | --- | --- |
| L-ISO | at `|H| = n`: **removal measured to expose** when D exposes and I does not (CC-ISO green); **removal measured not to expose** when D does not expose | measured |
| L-ACC | **protection-carrying**: violating it (C9) exposes at `t = 0` at a registration made at `t = 0`, before any tick (`c9.exposing_at_registration > 0`), so coupling plays no part; otherwise **not attributed** | fixed by design, read from the recorded count |
| L-P2 | **protection-carrying**: a planted `u + v`-known cell exposes, in both variants (M-PLANT) | fixed by design |
| L-SUP | **protection-carrying in variant I**: a supplied exact relation exposes (C-SUPP-X runs in variant I only) | fixed by design |
| L-PRIOR | **idle for determination**: a full-support correlated law does not determine (C-SUPP-F, variant I, one protocol); it enters no span computation | fixed by design |
| L-HPREP | **idle at `L = 7`**: C-XB's all-1 repeat agrees with the span method (`L = 9` not repeated) | fixed by design |
| L-SWAP, L-PROTB | **absent or not evaluated** | — |
| L-STEP, L-NN, L-Q2, L-REG, L-DET, L-INACC, E-AR | **used, not varied** (E-AR: not used). L-STEP's center-freeness is used by Lemma Q(i) (QA:478-486); its necessity is the records' result (QA:518-521), not measured here | used, not varied |
| L-RING | `|H|` varied (agreement of the two sizes, measured); `w`, `T`, the dimension, the parity of `L` and the archive's adjacency not varied; agreement is not evidence about an infinite chain (`|H| ≥ 2T` would be needed) | partly measured |

**The five questions, for EXPOSURE (the obstruction under the primary reading):**
1. *Essential to the failure:* the exposure followed the removal of L-ISO alone (D against I, measured at both sizes).
   Which kept assumptions the exposure needs is not measured here (NR-1 to NR-4, NR-6). Used and not varied, so
   untested as causes: L-STEP, L-NN, L-Q2, L-REG, L-P2's half-known supply, L-SUP, L-RING with the archive's
   adjacency. The protection-carrying items above are not causes of the exposure: violating any of them makes
   exposure easier.
2. *Their types:* from the ledger: L-ISO is imported. For L-Q2, L-NN and L-PRIOR both readings are printed.
3. *Does removing an imported assumption eliminate the obstruction?* Not decided here. The exposure arose from
   removing L-ISO. Whether removing or changing another imported item (L-REG, L-P2, L-RING) restores protection needs a
   new variant: candidate rounds NR-1 to NR-4.
4. *A counterexample satisfying the same observable requirements without it?* Not decided here: this round measures
   no observable requirement (NR-7).
5. *All OI models, or only this one?* Only this model: `N_1`, `q = 2`, the ring `Z_L` with `L ∈ {7, 9}`, `w = 3`,
   `T = 4`, supplied registration and P2.

**The five questions, for SURVIVAL (the obstruction under the opposite reading):**
1. *Essential to the survival:* L-ISO's removal is measured not to expose. The protection-carrying items, as fixed by
   the controls' design: L-ACC (C9, exposure at registration time), L-P2 (M-PLANT, both variants), L-SUP (C-SUPP-X,
   variant I only). Used and not varied: L-STEP, L-NN, L-Q2, L-REG, L-RING.
2. *Their types:* from the ledger, both readings for L-Q2, L-NN and L-PRIOR.
3. *Does removing an imported assumption eliminate it?* Not decided here; removing L-REG or L-P2, or changing L-RING,
   needs a new variant (NR-2 to NR-4).
4. *A counterexample satisfying the same observable requirements without it?* Not decided here (NR-7).
5. *All OI models, or only this one?* Only this model, as listed for EXPOSURE.

**The witness principle, applied to SURVIVAL.** The note prints, verbatim, the owner's principle: "failure to
construct a witness is not proof that no witness exists, unless a theorem establishes that impossibility within a
clearly stated scope." A SURVIVAL label is finite and conditional. Within the enumerated scope (the 6008 fixed-schedule
cases at each size, `T = 4`, `w = 3`, `|H| ∈ {4, 6}`, the kept assumptions) it is an exhaustive finite computation of
span membership, cross-checked by C-XB's direct simulation under the uniform law with known values 0; it is classified
as that verification layer. Its extension to every full-support law and every adaptive schedule is a paper reduction
(*The exact method*: the knowledge set is affine; an adaptive schedule is fixed within a branch), sound but on paper.
Outside that scope it is not an impossibility of exposure. The only impossibility result
used here is Lemma Q(iii), and its scope is the isolated archive under P1 and P2 (variant I), not variant D.

**For either substantive label**, the note adds the owner's standard verbatim: "Conversely, relaxing an assumption is
not sufficient by itself. The resulting model must still produce valid probabilities, observable quantum predictions
and consistent behavior across repeated experiments." Variant D's probabilities, predictions and repeatability are not
measured here (NR-5, NR-7).

**Candidate new rounds (named, not run):** NR-1 the archive held away from the window (a non-adjacent site of `H`,
or moved), the budget question of AP1:338-343; NR-2 larger `w`, `T`, `|H|`, including `|H| ≥ 2T` (free of two-sided
finite-size effects) and `T > |H|`; NR-3 registration through
a native coupling to a meter cell instead of a supplied slot read (removing L-REG); NR-4 ready cells prepared by the
dynamics instead of supplied (removing L-P2); NR-5 bias (PROT-B) in D under named full-support laws; NR-6 other
alphabets (L-Q2), next-nearest-neighbour center-free couplings (L-NN) and the cubic graph (L-RING), as extensions; NR-7 the observable level: valid probabilities,
quantum predictions and repeatability of variant D's induced statistics, without weakening the empirical standard.

### Part 3. The renaming check (C-DEISO, extended)

Variant D must not carry an imported item under another name. Each row is measured at both sizes and is part of
C-DEISO's green criterion.

| imported item | the form it could take in D | how it is excluded |
| --- | --- | --- |
| L-ISO (coupling isolation) | a dropped or weakened edge, a vacancy, a free tick, delayed coupling | (a) D's step is the unmodified ring matrix at every tick; (b) D and I differ only in archived rows and columns; (c) re-coupling reaches the window in D and in no case of I |
| L-SWAP (refill, swap) | a reset or replacement of the archived cell's state; a fresh known cell | (a); (e) no functional is added to `I_t` after `t = 0` (`knowledge_injections = 0`) |
| P3, E-iso | an edge multiplier | (a) |
| narrower access in D | fewer schedules or windows than I | (d) identical case lists, supply patterns included |
| discarded knowledge | a dropped record, or `I_t` not transported whole | (d) `R_t` carries every registration; `I_t` keeps rank 3 |
| a restricted prior | a support restriction in D's supply | (d) identical supply patterns; C-SUPP-X's relation enters variant I only |
| a narrowed target | fewer functionals evaluated in D than in I | the same evaluation rule (every functional on the current window) in both; L-ACC is shared and its effect is measured by C9 |

L-ACC is the archive's access property. It is kept in both variants, named in the ledger, and its effect is measured
(C9). It is not isolation renamed: it restricts what the observer reads, not what the dynamics couples.

## The checker and `controls.py`

**`marc_check.py`** (record directory; blob PENDING, sha256 PENDING).
- Imports only `fractions`, `itertools`, `json`, `sys`. No `open`, `exec`, `eval`, `__import__`, `importlib` or
  `subprocess`. Reads no file and nothing from the repository.
- `python3 -I -B marc_check.py` writes `measurements.json` to stdout as canonical JSON (`sort_keys`, separators
  `(",", ":")`, a final newline) and exits **0** when the output is complete and every control is green at both
  sizes, **3** when it is complete and some control is red. Any other status, or a crash, is incomplete.
- `--self-test`: the fixtures and mutations named under *Self-tests* (hand cases, C-SUPP-F's law, M-PLANT at
  `t = 0`, C-STEP, C-HOR, the transport, `ω`-drop and `v`-offset mutations); exits 0 when all behave as stated. It does
  not enumerate variant D.
- `--fixture-output`: prints a hand-written synthetic record in the measurement schema; used only by the design run
  (precondition 4). It computes nothing.
- Outside the default mode, a guard refuses the enumeration and any case evaluation of variant D, and of C9 beyond
  `t = 0` (C9's span is D's span).

**Measurement schema** (`arp1-marc-measurements`, version 1): `parameters` (`q`, `w`, `T`, `H`, `L`, `rule`,
registration times, pattern and schedule counts); `complete`; and for each size key `"4"`, `"6"`:
- `D`: `cases`, `exposing_V`, `exposing_V_no_reg_at_T`, `exposing_V_reg_in_1_to_Tm1`, `witness` (or `null`; with
  `uses_t_eq_T`), `nv_cases`, `coupling_cases`, `step_is_ring_violations`, `records_kept_violations`, `min_rank_I`,
  `knowledge_injections`;
- `I`: `cases`, `exposing_V`, `exposing_active`, `nonisotropic`, `nv_cases`, `coupling_cases`;
- `d_i_diff_outside_archived`; `case_list_sha256` (`D`, `I`);
- `supp_x`: `cases`, `exposing_V`; `supp_f`: `law`, `cond_v0_0`, `cond_v0_1` (as `"p/q"`), `span_determined`;
- `c9`: `cases`, `exposing_V`, `exposing_at_registration` (cases that expose at `t = 0` at a registration made at
  `t = 0`, before any tick); `plant`: `D` and `I`, each `empty_t0`, `exposing_V`;
- `xb`: `checked_cases` and `exposing_V` (each per `D`, `I`, `C9`), `checked_times`, `mismatches`,
  `exposure_mismatches`, and at `"4"` the all-1 repeat (`checked_cases`, `mismatches`, `exposure_mismatches`);
- `step`: `violations`; `horizon`: `T_le_H`, `radius_violations`;
- `flags`: the checker's green flags.

No timestamp, duration, host or interpreter field.

**`controls.py`** (record directory; blob PENDING, sha256 PENDING). Imports only `ast`, `hashlib`, `io`, `json`,
`os`, `re`, `subprocess`, `sys`, `tempfile`, `zipfile`. Reads commits with read-only git commands; imports nothing from the
repository; runs precondition 6's command for T as a subprocess. Its only write-mode `open` is in the self-test,
inside a `tempfile` directory. Generated files go to stdout, and the executor commits them. Modes: `check <commit> --freeze F [--stage S1|E|W]`, `decide <file> [--exit-status N]`,
`note <file> [--runs <s1-run>] [--freeze F]` (`--runs` omitted only at a halt before S1, where `--freeze` is given), `replay <file>`, `derive-run --run-api RUN --jobs-api JOBS [--artifacts-api A
--artifact-zip Z] [--void-run S1|E]` (`--void-run` writes the `void-run` record), `order …`, `verdict E --freeze F --run-api RUN --jobs-api JOBS --approvals APPROVALS
--branch-runs RUNS`, `plane <candidate F> --dev-runs DEVRUNS` (the P subset that `F`'s own tree can carry: `PENDING`, the branches line,
the blocks), `--self-test`. Codes:
- **T** (chain): `D..commit` is one chain of single-parent commits through `F`; `delta(D, F)` is the control plane;
  the round lines and digest at `F` equal the frozen expectation; the preregistration at the commit is `F`'s.
- **G** (paths): `delta(F, commit)` is `verify.yml` (`M`) plus record files.
- **R** (record files): at S1 exactly the S1 set; at `E` the S1 set plus the `E` set; at `W` the S1 set, `result.md`
  and the halt evidence; `amendments/` only if present at `F`. `measurements.json` and `result.md` appear together.
  **A halt before S1 exists** (for example when the S1 push precondition fails): the commit in `W`'s place (`S12`, a
  single-parent child of `F` changing only record paths) carries `result.md` and, if captured, `evidence/order.json`,
  and nothing else.
- **B** (blobs and static form): both scripts at their pinned blobs; the AST import allowlists; the forbidden names;
  the write-mode `open` sites; every `subprocess` call in `controls.py` launches only `git` (first argument the literal
  `git`) or the precondition-6 command, whose full argv must equal the frozen command apart from the two commit ids,
  so `controls.py` never launches `marc_check.py`.
- **W** (workflow): `verify.yml` at S1 and `E` is `D`'s with exactly the frozen splice, `if:` conditions included; at
  `W` it is `F`'s.
- **DS** (sources): from `5ce4f98e` to `D`, no change under the four source directories, `tools/`, `.github/` or
  `verification/infrastructure/`; from `D` to the commit, no change under them except `.github/workflows/verify.yml`
  (W) and the record directory; the seven inputs at the blobs above.
- **X** (measurements): schema, `complete`, flags agree with `decide`.
- **V** (note): `result.md` equals `note`'s regeneration byte for byte; S4.
- **P** (pins and evidence): no `PENDING` under `--freeze`; the branches line is present once at column 0 and
  byte-identical in every commit of `D..F`; `evidence/design-run.json` and `evidence/f-run/results.json`
  at their pinned sha256 and of their own schema, the design run's record showing conclusion `success` and every job
  `success`; `evidence/s1-run/results.json` and `evidence/order.json` meet their schemas and rules. At a halt before S1
  exists, P's S1 evidence (`design-run.json`, `f-run/results.json`, `s1-run/results.json`) is exempt, and only
  `evidence/order.json`, if present, is checked.

`replay <file>`: when the checked-out tree has neither `evidence/measurements.json` nor `result.md`, it prints
`replay: no committed measurements` and exits 0; when it has both, it exits 0 exactly when `<file>` equals the
committed measurements byte for byte; otherwise it exits 1.

## The workflow edit (frozen text; control W)

One job, `probes_arp1marc`, inserted directly after the job that is last before the `probes` aggregate at `D`
(anchor: PENDING), and four aggregate edits: `probes_arp1marc` appended to `needs`, `ARP1MARC_RESULT:
${{ needs.probes_arp1marc.result }}` in `env`, `echo "arp1marc=${ARP1MARC_RESULT}"` and
`test "${ARP1MARC_RESULT}" = success`, each after the last round's line at `D` (anchors: PENDING).

```yaml
  probes_arp1marc:
    name: Numerical probes / ARP-1-MARC exact span check
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: ARP-1-MARC exact span check
        if: ${{ github.event_name == 'workflow_dispatch' || hashFiles('verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/evidence/measurements.json') != '' }}
        timeout-minutes: 15
        run: |
          mkdir -p "$RUNNER_TEMP/arp1-marc"
          python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/marc_check.py > "$RUNNER_TEMP/arp1-marc/measurements.json"

      - name: ARP-1-MARC keep the measurements
        if: ${{ always() && github.event_name == 'workflow_dispatch' }}
        uses: actions/upload-artifact@v4
        with:
          name: arp1-marc-measurements
          path: ${{ runner.temp }}/arp1-marc/measurements.json
          if-no-files-found: error
          retention-days: 30

      - name: ARP-1-MARC replay against the committed measurements
        if: ${{ github.event_name == 'workflow_dispatch' || hashFiles('verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/evidence/measurements.json') != '' }}
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/controls.py replay "$RUNNER_TEMP/arp1-marc/measurements.json"

      - name: ARP-1-MARC checker self-test
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/marc_check.py --self-test

      - name: ARP-1-MARC control mutation tests
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/controls.py --self-test
```

No step continues on error, overrides the shell or masks a status with `||`. The job installs no third-party
package. **Runtime.** From the case count (6008 cases per variant and size; six enumerations of span checks per size;
brute force over `2^11` and `2^15` assignments for D and I, plus the all-1 repeat at `L = 7`) and a mock benchmark of
the same operations on random maps of the same sizes (about 0.3 s per 6008-case span enumeration and about 1 s and 3 s
per brute-force enumeration at `L = 7` and `L = 9`), the computation is estimated at about 15 s, under one minute
with a fourfold margin; C-XB's added exposure comparison and its C9 run add a few seconds. **When the computation
runs.** Not on ordinary CI before `E`: the check and replay steps run only on `workflow_dispatch`, or when the
committed measurements exist. So the S1 dispatch is the first computation of variant D, and non-dispatch runs at S1
skip both steps (the order rule checks this through the jobs API). From `E` on, every event replays the committed
measurements, so later builds re-check the claim (§A.42); the pull-request run at `E` before `E`'s dispatch replays
the S1 computation and computes nothing new. The self-test steps run on every event and do not enumerate variant D.
The check step's 15-minute limit and the job's 30-minute limit bound a runaway; reaching either is not host-VOID
(*Stop rule*).

**The design splice** (precondition 4) differs from this text in exactly three places: `marc_check.py` carries
`--fixture-output` on the check step's second line; the check and replay steps carry no `if:`; the upload step's
condition is `${{ always() }}`. So the design run exercises every step and computes nothing.

## Runs, evidence and approvals

**The run at a stage** is the completed `workflow_dispatch` run of `.github/workflows/verify.yml` in
`amaybaum/incompleteness` whose `head_sha` is that stage's full commit, with a positive run id and `run_attempt = 1`
(a re-run attempt of a dispatch run is a checker rerun: unapproved, VOID and a halt), every job
at that commit. A pull-request run, a push run, or a run of another repository or workflow path is not the run.
`controls.py derive-run` turns the runs and jobs API answers (`?per_page=100`, every page) into
`{schema, version, run_id, run_attempt, head_sha, event, workflow_path, conclusion, jobs: [{name, conclusion}],
shard_steps: [{name, conclusion, started}], artifact_sha256}` with no timestamp or duration (`started` is whether the
jobs API gives the step a `started_at`). For `artifact_sha256`, `derive-run` takes the artifacts-list API answer and the
downloaded zip, checks the zip's sha256 against the API's `digest`, and the artifact's `workflow_run.id` and
`head_sha` against the run, then extracts `measurements.json` and hashes it; it never reads a log (§A.44).

| stage | its tree | its run must show | evidence | control |
| --- | --- | --- | --- | --- |
| `F` | `D` plus the control plane | every job `success`; the ARP-1-MARC shard absent | `evidence/f-run/results.json`, added at S1 | P |
| S1 | `F` plus both scripts, the splice, `design-run.json`, `f-run/results.json` | the decisive computation: check step conclusion (its exit status), the artifact, every job. Every non-dispatch run at S1: check and replay steps `skipped` | `evidence/s1-run/results.json` and `evidence/measurements.json` (the artifact's bytes), added at `E` | `check S1 --freeze F --stage S1`, run on the S1 commit before it is pushed and again before the dispatch |
| `E` | S1 plus the `E` set | every job `success`; the replay step `success`, so the committed measurements equal a fresh computation at `E` | `RUN`, `JOBS` for `E`'s run, kept uncommitted with their sha256 in the receipt's attestation | `verdict E --freeze F --run-api RUN --jobs-api JOBS` |

**`verdict`** prints `VERDICT  <token>` from `decide` on the measurements at `E` only when all of these hold:
- every control of `check E` passes;
- `E`'s run is the run at `E`, with every job `success`; the shard job present once; its seven named steps (checkout,
  setup-python, check, upload, replay, checker self-test, mutation tests) present by name, each `success`; and every
  step the jobs API lists for the shard job `success` or, for the upload step only, `skipped` (none here, since `E`'s
  run is a dispatch); synthetic steps the API adds are matched by no name and tolerated if `success`;
- `evidence/s1-run/results.json` is the run at S1 with `run_attempt = 1`, conclusion `success`, the seven named shard
  steps `success` by name, and
  `artifact_sha256` equal to the sha256 of the committed `measurements.json`;
- `result.md`'s token line equals the token;
- **dispatches after `order.json`'s capture** (`APPROVALS`, the captured approval-comment answers for `E`'s dispatch
  and any retake at `E`; `RUNS`, fresh captures, every page, complete against their `total_count`, taken after `E`'s
  run completed, of the round branch's runs and, repository-wide, of `GET …/actions/runs?head_sha=` for S1 and for
  `E`, each run with its `run_attempt`): `E`'s run has a valid approval entry with stage `E`; every
  `workflow_dispatch` run in those captures is matched, by `run_id`, by a valid entry in `order.json` or in
  `APPROVALS`, and has `run_attempt = 1`; every other run there is `pull_request`, and each with `head_sha` S1 has its
  check and replay steps `skipped`.

Otherwise it prints `VERDICT  VOID` with a frozen reason and exits 1. A VOID label from `decide` is printed the same
way, as `VERDICT  VOID` with exit 1, never as a token with exit 0. The verdict's output and the sha256 of
`APPROVALS` and `RUNS` are recorded on the round PR and in the receipt's `E` attestations.

**Approval entries.** Every dispatch needs its own owner approval. Each entry is `{run_id, run_attempt, head_sha, stage,
approval_comment_id, approval_author, approval_author_association, approval_created_at, quoted_words}`; stage is `F`, `F retaken`, `S1`, `E` or
`retake after host VOID`. A retake entry also carries `voided_run_id`, `preservation_comment_id` and
`preservation_created_at`. An entry is valid only when:
- `quoted_words`, the owner's words as the approval comment quotes them, name the dispatched commit by its full 40-hex
  id and name the stage, and the stage matches the commit's role: a stage-`F` (or `F retaken`) entry names `F`, a
  stage-S1 entry names S1, a stage-`E` entry names `E`, and a retake names the voided run's commit;
- the run's `head_sha` equals that id, its `run_attempt` is 1, and `approval_created_at` is earlier than the run's
  `created_at`;
- `approval_author` is `amaybaum` and `approval_author_association` is `OWNER`, as for `designation_f`. The
  coordinating session also posts as `amaybaum`, so the login shows no human authorship; the approval rests on the
  owner's words the comment quotes;
- no `approval_comment_id` occurs twice, so each approval authorizes one run;
- for a retake: the preservation comment names `voided_run_id` and the sha256 of its `void-run` record, and
  `preservation_created_at` < `approval_created_at` < the retake's `created_at`, with the same `head_sha`.

**`evidence/order.json`** (schema `arp1-marc-order`, version 1; host timestamps are its content), produced by
`controls.py order` from captured answers (every page, each capture complete against its `total_count`):
`designation_f: {comment_id, author, author_association, created_at, quoted_words}`; `approved_dispatches` (entries for `F` and S1, and
any retake before `E`); `round_branch_runs: {total_count, runs: [{run_id, run_attempt, head_sha, event,
created_at}]}`; `s1_sha_runs`, the repository-wide `?head_sha=` capture for S1 in the same form;
`dev_branch: {name, pr_number, total_count, runs: [{run_id, run_attempt, head_sha, tree, event, splice,
job_sha256}]}`, where `splice` is read through git at the run's `head_sha`: **`design`** exactly when that commit's
`probes_arp1marc` job is byte-identical to the frozen design job (the frozen job with the three listed substitutions)
and its (`marc_check.py` blob, `controls.py` blob) pair is in the frozen list of design pairs below, **and no other
file under `.github/` (workflows, actions, other jobs) references the record directory**; **`none`** when no file under
`.github/` at that commit references the record directory; **`other`** otherwise; `s1_nondispatch_runs: [{run_id, check_step,
replay_step}]`, from the jobs API; `first_execution_run`; `sources` (sha256 of each captured page and comment answer);
`ordering`. **The ordering holds** exactly when:
`designation_f.quoted_words` name `F` by its full id; `designation_f.created_at` is earlier than the `created_at` of the
first host run whose `head_sha` is S1 or a later execution commit; every `workflow_dispatch` run on the round branch is
an approved entry, matched by `run_id`, with `run_attempt = 1`, and every other run there is `pull_request`; the same
holds for `s1_sha_runs`; every non-dispatch run whose `head_sha` is S1 has its check and replay steps `skipped`; every
dev-branch run is `pull_request` and its `splice` is `design` or `none` (development iterations of the scripts are
tested locally, under the stated limit below), with each run's `head_sha` reachable; both branch names equal the frozen branches line; every capture
is complete. The `E` dispatch, its approval and any later dispatch are checked by `verdict` (above), and the owner's
designation of `E` is quoted in the receipt; no V3 predicate reads attestations (`S5`).

**Design pairs (frozen at `F`).** The (`marc_check.py` blob, `controls.py` blob) pairs that ran under the design job
in dev CI before `F`, each with its `--fixture-output` and `--self-test` paths statically reviewed not to enumerate
variant D; the final pair, pinned under *The checker and `controls.py`*, is one of them. The list: PENDING.

**Stated limit:** local work before the first push is not measurable. Nor is a deliberate computation on another
commit that contains the checker, or from a copy of `marc_check.py` outside the record directory: the captures cover
the S1 and `E` commits and the two branches only. No local run of the decisive mode is part of the procedure, and the
checker's blob is frozen at `F`, so no such work can change what is computed: S1's dispatch computes the frozen code,
and `E` replays it. Nor is a dev commit that edits a file an existing CI job already runs, so as to invoke the checker
without any reference under `.github/`; the dev-branch captures record such runs but their classification cannot see it.

**Disclosure: the implementer's toy run.** During implementation, two harnesses ran the checker's functions on a toy
ring: `harness/toy_smoke.py` (sha256 `ff2e594a…`) and `harness/toy_timing.py` (sha256 `d5cb0c23…`). They ran at
`L = 5`, with C9 substituted for every variant, and refused any evaluation of D, and of I except C-SUPP-F's `t = 0` protocol. Only the schema, flag agreement,
C-XB mismatch counts and C9's label were inspected; no exposure count was printed. The unpatched checker at `L ∈ {7, 9}` (the
decisive mode) was never run. The harnesses are not committed (§A.28); the guard now also refuses C9 beyond `t = 0`.

**S1 push precondition (after `F`; frozen here).** The S1 commit is built locally and `check S1 --freeze F --stage S1`
exits 0 on it before it is pushed, so control R prevents, not only detects, a committed `evidence/measurements.json`
at S1 (which would make its pull-request run compute). If it does not exit 0, S1 is not pushed and the finding is
reported on the round PR.

## Stop rule (halt-only)

The round **halts** under `S12` on any of these, and no checker rerun is pre-registered:
- any control of `check` fails at S1 or `E`;
- **at S1, any decisive-computation result other than exit 0 with complete output**: exit 3 (a control red), any other
  status, a crash, a missing or unparseable artifact, or an artifact that breaks the schema;
- **at `E`, any failed control, crash or incomplete output**: a red job, a replay mismatch, or `verdict` VOID that
  arises from the checker or the controls;
- **at S1, a red job outside the shard** while every shard step succeeded: the round halts. A retake would only
  replay a deterministic computation, and the halt-only rule admits none;
- a **host-VOID**, at S1 or `E`, unless the owner records a separate decision to retake it **after** the evidence is
  preserved. Host-VOID is defined on the jobs API only: the shard job is absent, or its **check** step is absent
  (an empty steps list included), `skipped` (for example because checkout or setup failed) or has no `started_at`; at
  `E`, also the replay step not having run **while the check step succeeded**. If the check step started and did not
  succeed, whether it failed, was cancelled or timed out, the run is never host-VOID, whatever conclusion the host
  reports for it; this takes precedence over every clause above. For a
  host-VOID the evidence is the voided run's `void-run` record
  (`{schema: "arp1-marc-void-run", version: 1, run_id, run_attempt, head_sha, event, status, conclusion,
  jobs: [{name, conclusion}], shard_steps: [{name, conclusion, started}], refusal_code}`) and its sha256, posted on
  the round PR. The retake is then an approval
  entry with stage `retake after host VOID`. Without that decision, the round halts;
- any `run_attempt` greater than 1 of a dispatch run at `F`, S1 or `E` (a re-run, not a new approved dispatch);
- the control plane would need to change (no amendment after `F`; a successor round is drafted instead);
- the computation would need a parameter, variant, control or premise not frozen here.

A substantive token (EXPOSURE, SURVIVAL, SIZE-DEPENDENT) is not a halt. SIZE-DEPENDENT is a complete result.

**At a halt**, `W` restores `verify.yml` to its state at `F` and keeps the record files. It adds, in structured form and
without personal data: the S1 artifact as `evidence/measurements.json` when one exists (preserved as produced, red
flags included); `evidence/s1-run/results.json` or the `void-run` record; `evidence/order.json`; and `result.md`, the
VOID text generated from what was measured. Negative, inconclusive and vacuous results are preserved without
reinterpretation. A halt record on the round PR asks the owner for any further decision; progression to ARP-2 stops
(#1169 c.6723329527: "any failed gate stops progression").

**Pauses.** A §A.26 provenance anomaly in the round's work area stops all measurement and every push until a full
sweep resolves it. It is not by itself a halt.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| the decision rule, controls and texts are fixed before any computation of variant D | `F` designated before the first execution run (P on `order.json`); the checker's blob frozen at `F` (B); self-tests never enumerate D (static review of the pinned blobs before `F`) |
| no automatic computation of variant D: its first computation is the owner-approved S1 dispatch | the check and replay steps' `if:` conditions in the frozen splice (W, with a self-test that removing them fails); every non-dispatch run at S1 has both steps `skipped` (order rule, jobs API; re-checked by `verdict` on a fresh capture); every dev-branch run's commit carries the design splice (order rule, through git); self-tests for each |
| the question is M-ARC's, with exactly one assumption removed | C-DEISO (a)–(e) at both sizes; the *Kept, removed and not used* table frozen at `F` |
| the dev branch and round branch are the frozen ones, and no dispatch runs on the dev branch | the branches line, byte-identical in `D..F` (P); `order.json`'s branch rules |
| SURVIVAL is not reported as an impossibility of exposure | the witness-principle text in ADA Part 2, regenerated by V; S4 |
| the assumption ledger and its types are fixed before any result | the ADA ledger is in the control plane at `F` (`G7`); uncertain types carry both readings |
| the ADA cannot change the label or broaden it unqualified | `decide` reads no ADA field; the ADA is generated from frozen sentences after the token; V regenerates it; S4 and the qualifier rule in its self-test |
| variant D renames no imported assumption | ADA Part 3, through C-DEISO (a)–(e) |
| variant D carries no isolation under another name | C-DEISO (a)–(e) |
| the countercontrol makes survival reachable; the controls make exposure reachable | CC-ISO; C-NV, C-SUPP-X, C9, M-PLANT, each at both sizes |
| determination uses support only, no measure, no floating point | span method and C-XB use no probability; C-SUPP-F alone uses `Fraction`; B's import allowlist (no `float` source module); self-test screens for float literals |
| the span method is right for this construction | C-XB at both sizes over every case and time of D and I; C-STEP; C-HOR |
| no measurements file reaches S1's pull-request run | the S1 push precondition: `check S1` (R) on the S1 commit before its push |
| no dispatch run is re-run | `run_attempt = 1` required in approval entries, `order.json` (round branch, the S1 `?head_sha=` capture) and `verdict`'s fresh captures; the attempt-2 self-test |
| `verdict` reads the shard's steps correctly | the seven named steps matched by name, synthetic steps tolerated; the realistic jobs-answer self-test |
| the exposure count is reproduced independently | C-XB's direct `Q*` evaluation, `exposure_mismatches = 0` and equal `exposing_V` for D, I and C9 at both sizes; the `ω`-drop and `v`-offset self-test mutations |
| both sizes are decided, with no wrap-around within `T` | C-HOR; the decision rule reads both size keys |
| no label over a red or missing control | `decide`'s VOID clause; `verdict`; their self-test VOID cases |
| verdicts read structured data only | checker exit status; the artifact via the artifacts API; job and step conclusions via the jobs API; `replay`'s exit status; no log parsing |
| the committed measurements are the host's computation, replayable at `E` | `artifact_sha256` equal to the committed file's sha256; the replay step at `E` |
| the result note says no more than the measurements | V (regeneration byte for byte); S4; the frozen texts |
| each dispatch is owner-approved; `F` and `E` are owner-designated | approval-entry rules in `order.json` (`F`, S1, retakes before its capture); `verdict`'s dispatch clause on `APPROVALS` and a fresh capture of the round branch's runs (`E`, any later retake, any unapproved dispatch); designation quotes with author and time |
| no checker rerun; host VOIDs retaken only under a later owner decision | *Stop rule* (a check step that started and did not succeed is never host-VOID); approval entries with stage `retake after host VOID`; the host-VOID self-test |
| execution changes only `verify.yml` and the record | `S7` through `--verify-round Q`; G, R, W |
| the inputs are the records as cited, and nothing outside the record and `verify.yml` moves | DS at S1 and `E` (`5ce4f98e..D` unchanged; `D..commit` only `verify.yml` and the record directory; the seven blobs) |
| the ADA attributes causes only from measurements | the status kinds (measured / fixed by design / used, not varied) frozen in ADA Part 2; V regenerates the section |
| no `PENDING` field reaches `F`; no dev run is outside `design` or `none` | `controls.py plane <candidate F>`, run from the dev branch at the pinned blob (precondition 6); P and the order rule at S1 and `E` |
| no manuscript or ROADMAP change | G; `S7` |
| the audit findings are incorporated before `F` | precondition 1, with the package's sha256 |
| the receipt holds; legacy records untouched | `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`; `legacy_records_check.py` at `E` and `Q` |

## Preconditions of `F`

1. **Classification audit incorporated.** Input: the consolidated package `PACKAGE.md` r3, sha256
   `33075f9f2e4df52cf87536ebcb8c8c931f89960e3a067af30c182587f3109b74`, model-reviewed (r2 `ef061202…` ACCEPT in
   REVIEW-PACKAGE-r2; r3 applies its non-blocking items); owner acceptance of the package (package §8 item 1)
   pending, consolidating clusters C1, C2 (with its re-review), C3 and C5. Items bearing on
   this round, with their disposition:

   | package item | bearing | disposition |
   | --- | --- | --- |
   | §6 item 1, M-ARC (question, initial state C3:169-170, variant I C3:175-176, check, controls, rule) | the specification | matches *The question* and *The controls*; the C9 form and the supply-pattern enumeration are disclosed elaborations |
   | §6 item 1, "a preregistration would cite REVIEW-C3-r3" for n1–n3 | provenance | cited under *Authority*; classified in the §A.42 item 8 table |
   | §1 standing: c.6723571280 ("I would not introduce another round or change M-ARC's acceptance criteria now") | the criteria | quoted under *Authority*; no criterion changed |
   | §1 standing: c.6723585151 ("A proof that excludes such memory is valid only within that restricted model; it cannot automatically establish a limitation of OI generally") | scope of negative readings | consistent with ADA question 5 and *What no outcome shows*; no change |
   | c.6723585151 (amaybaum, OWNER, 2026-11-08T15:49:15Z): "Add a hidden-prior sensitivity requirement. When a result changes under correlated hidden distributions, its stated scope must identify that dependence." | scope of the result | no change: determination is support-only; C-SUPP-X (exact relation, exposes) and C-SUPP-F (full-support correlated law, does not determine) exhibit the correlated cases; the common clause carries the support dependence |
   | §9 AW-C3-1 (P2 + step → isotropy; P1 → retention) | what L-ISO carries | the ledger's L-ISO, L-P2 and L-SUP rows |
   | §9 AW-C3-2 (support for determination; product law for non-bias) | the prior | L-SUP and L-PRIOR are separate rows; no bias statement |
   | §9 AW-C3-3 ("never/permanently" fail for archived information) | the target | the target is the current window only; S4 screens both words |
   | §9 AW-C3-4 (state the reading of M-INACC) | L-INACC | the reading is stated in the L-INACC row (added in r4) |
   | §4 K-17 (over-readings QA:46, 51-53, 523-525, 799; M2D:853-854, 947) | the note's wording | S4's phrases cover them; no K row is a site this round edits |
   | §7 gate (EOI classes) | none | the round assigns no EOI class |
   | §8 item 6 (whether ARP-1 is the accountable home of M2D:853-854) | planning | an owner decision outside this round; no change |
   | §10 (audit files off `main`) | §A.42 item 8 | provenance here, because every definition is restated in this file |

   No other K row touches AP1, QA or MI as this round uses them (K-17's AP1:72-75 and 732-733 and MI-R:255 are not used
   here). C1 and C5 findings concern manuscripts and kernel modules this round does not use. **None of these items
   requires a material change** to the question, parameters, controls or decision rule. The ledger addition
   (L-INACC's reading) is in the ADA, which `decide` does not read.
2. **Independent review.** A review of the candidate control plane with no open blocking finding, recorded on the
   round PR with its verdict.
3. **No `PENDING`** remains: `D`; the drift extension; both scripts' blobs and sha256; the design PR number and
   `design-run.json`'s sha256; the workflow anchors at `D`; the list of design pairs. P and `plane` parse the fills with
   fixed patterns, so each is written in exactly this form (40 or 64 lowercase hexadecimal digits, in backticks):
   - `D`: ``- **`D`** = `<40-hex>`: …``;
   - each script: ``(record directory; blob `<40-hex>`, sha256 `<64-hex>`)``;
   - the design run: ``whose sha256 is pinned here: `<64-hex>` ``;
   - the design PR: ``The design PR number: #<digits>``;
   - the design pairs: ``The list: (`<marc_check.py blob>`, `<controls.py blob>`), (…, …).``, each blob 40 hex digits.

   A fill in another form fails P.
4. **Design run.** The dev branch `draft/arp1-marc-dev`, with its own draft PR, carries the predicted S1 tree less
   `evidence/`, with the design splice. Its ordinary `pull_request` CI is green on every job; `derive-run` turns it into
   `evidence/design-run.json`, whose sha256 is pinned here: PENDING. The design PR number: PENDING. It is design
   evidence, not an attestation. `derive-run` is exercised on its artifact (the design splice uploads it).
5. **Self-tests pass** locally and in the design run, at the pinned blobs. Variant D has not been enumerated.
6. **Chain and blocks.** From the repository root, this command exits 0:

   ```sh
   python3 -I -c "import sys; sys.path.insert(0, 'tools'); import v3_verifier as v; r = v.Repo('.'); d, f = sys.argv[1], sys.argv[2]; rd, rid, kind, ent, cp, codes = v.control_plane(r, d, f); t1 = v.check_t1(r, d, f, cp); dig = v.governed_digest(ent) if ent else None; print(rid, kind, rd, dig, codes + t1); sys.exit(0 if not (codes or t1) and (rid, kind, rd) == ('ARP-1-MARC', 'non-sealing', b'verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/') and dig == '4ddc9a8af70564d7b73a65b3f431a0b4fbdf1c1518327f6e4d8ea6dff2702563' else 1)" <D> <candidate F>
   ```

   Then, from the dev branch at the pinned `controls.py` blob, `python3 -I -B <rd>/controls.py plane <candidate F>`
   exits 0: no `PENDING` field, the branches line once at column 0 in every commit of `D..<candidate F>`, the blocks as
   frozen, and every dev-branch run so far classified `design` (its job the frozen design job and its script pair in
   the frozen list of design pairs) or `none`.

7. **`F` dispatch.** With the owner's approval entry (stage `F`), the run at candidate `F` is green on every job.
8. **Designation request.** The reviewed candidate `F`, its exact commit, the independent-review verdict, the controls
   and any outstanding blockers are presented to the owner (#1169 c.6723329527). The presentation states in one line
   that the decisive computation runs at the S1 dispatch and that `E`'s run replays it, and asks the owner to confirm
   that reading of "present the exact execution head E and proposed dispatch" (open owner confirmation). It also
   discloses that pushing `E` starts an ordinary pull-request run that replays the S1 computation automatically before
   `E`'s dispatch; lists owner acceptance of the consolidated package (package §8 item 1) as outstanding; lists the
   *Added VOID routes*; gives the toy-run disclosure; and notes that each `F`, S1 and `E` dispatch also runs the Act-42
   exclusion shards (about six CPU-hours each, on `workflow_dispatch` only), and that under the stop rule any red
   job outside the shard at S1 halts the round. The owner designates `F`.

**If any precondition cannot be met, no `F` is requested**, preparation stops, and the finding is reported to the
owner on the round PR.
