# C3 for R-lin with (xiii): label-cell-only retention (paper-only check, r3)

**Revision.** r3 applies changes C2–C4 of the focused confirmation of r2 (verdict ACCEPT WITH
CHANGES, `CONFIRM-r2.md`, r2 at `ee4db4f1`), with the dispositions in `RESPONSE-r2.md`; C1 is
applied in the §2 heading note and recorded in `RESPONSE-r2.md`. r2 applies findings 1–11 of the independent review of r1 (verdict REVISE,
`REVIEW-r1.md` at `a03af682`, branch `research/c3-rlin-xiii-1169-20261113`; r1 at `00c84af2`). The
dispositions are in `RESPONSE-r1.md`. The readings R1v and R2(iii) and the reviewer's label sets were
re-derived by hand before use. The class-level verdict (C) is unchanged; its grounds change.

**Standing.** WIP / UNVERIFIED. Hand reasoning only, unreviewed. No computation, no script, no
Lean, no manuscript or record edit, no premise adopted, no rule changed, no status or priority
changed. Under §A.46 item 7 nothing here may serve as a premise of an established claim before
independent review.

**Authority.** Owner decision, #1169 comment 6863414487 (`amaybaum`, 2026-11-13T19:58:05Z),
fetched in this unit:

> **C3 check (SQ3).** A bounded, paper-only check of the actual R-lin update with (xiii). It either
> exhibits retention of a label cell only, with the common effects lost, or proves that cannot
> happen. It runs with these frozen: H-xiv, D₀, H-AR, C-PM, every herald and failure record, and the
> full timing convention. It adds no new physical premise and makes no rule change.

**Origin of the obligation.** ChatGPT exact-head review 5892912758 on #1268 (posted by `amaybaum`,
2026-11-13T14:39:31Z): "C3 is the essential gap. Retention inside `V(T)` does not imply an accessible
*label-free* indicator under C-PM. Consequently C4's preparation-equivalence direction is
unestablished without (LF)." Next obligation named there: "a bounded paper-only C3 check for the
actual R-lin/(xiii) update, either exhibiting label-cell-only retention with lost common effects or
proving it cannot happen."

**Pins.**

| Short | Path | Commit | Blob |
|---|---|---|---|
| Main | `papers/Main.md` | `main` `c3b5f37a` | `0db17597` |
| OA1 | `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` | `c3b5f37a` | `5a16b213` |
| OA2 | `…/oa-2-20261112/OA-2-REPORT-r4.md` | `c3b5f37a` | `8f8ddf73` |
| OA3 | `…/oa-3-20261112/OA-3-REPORT-r4.md` | `c3b5f37a` | `0a36fd05` |
| P | `…/drafts/tune-1-20261111/TUNE-1-STEP2-PROPOSAL.md` | `c3b5f37a` | `84f71030` |
| P0 | `…/drafts/rec-1-20261113/REC-1-P0-r3.md` | `research/rec-1-1169-20261113` `3a3aa146` | `611a4d9a` |
| P0C | `…/drafts/rec-1-20261113/REC-1-P0-CONFIRM-r3.md` | `3a3aa146` | `8b440f2d` |
| P0R | `…/drafts/rec-1-20261113/REC-1-P0-REVIEW-r1.md` | `3a3aa146` | `ec5178ca` |
| P0N | `…/drafts/rec-1-20261113/REC-1-P0-NOTES-r2.md` | `3a3aa146` | `1cd2e3fa` |
| R9 | `…/drafts/rec-1-20261113/REC-1-r9.md` | `3a3aa146` | `945b7982` |
| SY | `…/drafts/synthesis-1169-20261113/SYNTHESIS-r3.md` | `research/synthesis-1169-20261113` `9eeee392` | `e6829509` |
| RV | `…/drafts/c3-rlin-xiii-20261113/REVIEW-r1.md` | `research/c3-rlin-xiii-1169-20261113` `a03af682` | — |

`…` abbreviates `verification/programmes/oi-qm/reconstruction`. The P0, P0C, P0R and P0N blobs are
the same at `2a9f10ba` and `3a3aa146`. R9 differs from `REC-1-r8.md` (`615b7de8`) only in its revision
line, P5 and §6 rows; the passages cited here are unchanged and shifted by +4 lines. P0 through RV are
off `main` (§9).

**Support labels.** [K] kernel-checked; [A] exact algebra, checked by hand here; [P] paper
derivation (this record unless a source is named), unreviewed; [L] literature, context only;
[R] research record on `main`, not independently established; [R-off] research record off `main`.
A *reading* is an interpretation of an undefined interface item; no reading is adopted here.

***

## 1. C3 stated for R-lin with (xiii)

### 1.1 The rule

- Ledger (xiii) (Main:724): each site carries a previous and a current value in a finite abelian
  group, and one step is `(x(t−1), x(t)) ↦ (x(t), F(x(t)) − x(t−1))`; ledger (vii) linearity, (viii)
  site factorization, (x) nearest-neighbour range on the simple-cubic graph, (xi) no explicit copy of
  the site's own value (Main:724). Main:292–294 displays the instance at `q = 2`.
- R-lin: `F` is the nearest-neighbour sum on the simple cubic lattice, at general `q` (P:85–89).
  Per site, `(y_i, x_i) ↦ (x_i, Σ_{j∈N(i)} x_j − y_i)` (OA1:335–336).
- Cells are the slots `y_i`, `x_i`. P0's instances use slot-level observers on rings (P0:392–411);
  Main:292–294 uses site regions (both slots). Both granularities are treated below.
- Carriers treated: finite tori `(ℤ/L)^d` and finite-horizon windows of `ℤ^d` (OA2:92), any `q ≥ 2`,
  with every site having a neighbour whose multiplicity in `N(i)` is not divisible by `q` (true on
  every window and on every torus with a side ≥ 3). This excludes only `F ≡ 0 (mod q)`. Whether the
  class admits rings (`d = 1`), as P0's instances do (P0:392, :402), or only the simple cubic lattice
  (P:85–86; Main:724 (x)) is not fixed by the class statement; owner question 5.

### 1.2 The class (OBL-SP)

R9:259–272: φ in the gauge-derived affine class (ledger (vii); R-lin with (xiii)) on a finite
carrier; initial law in `D_0` (designated cells known, every other cell uniform and independent);
H-AR observers (OA2:182–193); (H3) no supplied control (OA2:501); records as in (H4) (OA2:502) or in
the (V-ii-H) effect class (OA3:120–123); heralds held at use with records formed inside `S`; the
closure-defined prepare–measure fragment under C-PM (OA2:88–125); H-xiv. The literal L reading is
stated at R9:301–307 and rests on the owner decision #1268 c.6860582570 (`amaybaum`,
2026-11-13T17:47:34Z), fetched in this unit: "The **literal L reading** of the preregistered r7
class is kept. That reading is '(H4) or (V-ii-H)' with held-at-use typing." Under it every observer
of the class retains every read of the horizon in `V`. P0 and the review treat the rule class as
R-lin with (xiii), not the whole affine class (P0:350–352; review 5892912758: the ring conveyor "is
outside R-lin with (xiii)"). This record does the same (owner question 4).

Notation (P0 §2.1, P0:115–129): an instance is `(φ, V, D, r, T, t_p)`; `K` is the free subgroup;
records `Z_τ = V(τ)`. **Full retention** (L reading): `V(τ)` is a function of `V(τ′)` on the support
for `τ ≤ τ′ ≤ T`. The check below verifies it at every tick, which is at least what (H4) and the
retention form of (V-ii-H) (OA3:474–475; P0:171–174) require.

### 1.3 Effects and C-PM accessibility

- C-PM (OA2:112–120): "A preparation procedure's own label cells are not effects on what it
  prepares. These are the setting and coin cells that select which preparation ran." "Effects are
  all post-processings of held records **other than those label cells**. No read of the prepared
  configuration is removed." "It reconciles with 'none removed by fiat' because the label is a
  property of the procedure, not of the system it prepared." Physical form C-PM′: "C-PM holds
  physically when the preparation gadget moves its label cells out of reach of every procedure
  within the horizon." OA3:101–102 adds herald records to the labels.
- Held = a function of the present `V` (OA1:111–114; OA2:107); a herald is "still held at use time"
  (OA1:131). The use time of a preparation herald is the handoff `t_p` or a later read (P0:125–126).
- Preparations: label values, coin mixtures, heralds on reads at ticks `≤ t_p` (P0:122–124).
  Measurements: post-processings of held reads at ticks in `(t_p, T]`, heralded composites included
  (P0:127–128). A common effect set excludes every cell holding a preparation-stage record
  (P0:252–255).
- **C-PM-accessible effect** (this record's formal statement of the above, given a label set
  `Lab(τ) ⊆ V` at each tick): a single-tick effect at `τ` is a function of `V∖Lab(τ)` at `τ`; a
  heralded composite (event at `τ₁`, read at `τ`) is available iff the `τ₁` event is a function of
  `V∖Lab(τ)` at `τ` on the support. "Reading no preparation label" (P0:62–64) means exactly this.

### 1.4 C1–C4 and (LF)

P0:136–146. With `Z₀` the measurement record (settings removed): C1 law form; C2 reachability;
**C3**: for every coset `t + S` meeting `U_Z`, `1[Z₀ ∈ t + S]` is an available C-PM effect; C4:
preparations equivalent iff coset-weight vectors agree, effects equivalent iff they agree on every
vertex. **(LF)** (P0:259–261): the measurement-stage reads are jointly held at `T` by cells of `V`
holding no preparation-stage record; `Z_e` is the label-free part of `V(T)`. Under (LF), C1–C4 hold
with `S*_e = H_e(K ∩ ker G_{J*})` (P0:262–293) [P0, R-off].

### 1.5 The two terms of the obligation

- **Label-cell-only retention**: some C-PM-accessible read at a tick `τ₁ ∈ (t_p, T)` is a function of
  `V(T)` but not of `Z_e = V∖Lab(T)` at `T`. This is the failure of (LF) for the accessible reads.
  P0's (LF), which covers every measurement-stage read, fails whenever this does.
- **Lost common effects**: for every subgroup `S` satisfying C1 and C2, some `S`-coset indicator of
  the joint measurement record is not a C-PM-accessible effect. This is the failure of C3.

(LF) implies C3 (P0 N5). A witness needs both terms; a proof that they cannot occur needs (LF).

### 1.6 The undefined item: label status after the use time

Under in-`V` retention a cell of `V` can hold herald content and also be read as part of the
prepared configuration. The frozen texts define label cells as the procedure's setting and coin
cells and its herald records (OA2:112–113; OA3:101–102) but do not say which cells of `V(τ)`, for
`τ > t_p`, are label cells. The synthesis lists this as an unfixed interface item (SY:201–202, MM-2
item 3), as do P0 N8.3 (P0:353–355) and P0N:36–38. P0 fixes it at evaluated points only:

| Precedent | Evaluation | Source |
|---|---|---|
| Instance II (R-lin) | `y₀(1) = x₀(0)` (copy of the herald cell) is a label; `x₁(1) = x₀(0) + x₂(0) − y₁(0) = w + c` is label-free | P0:402–411, :353–355 |
| N8.2(b) ring conveyor | cells reached from the herald cells by the shift `r_j(t+1) = r_{j−1}(t)` are labels; `r_0(t+1) = r_L(t) + s0(t)`, `s0(4) = x`, `s0(5) = y` are label-free | P0:318–349; P0R:135–144; P0N:22–24 |
| Instance I | `x₀(1) = u + c − p` label-free | P0:392–400 |

Two choices are left open by these precedents: whether a copy is judged on the rule's coefficients
(structural) or on the support of the admitted procedures, where designated constants drop out; and
whether constant cells of `V(t_p)` count as label cells or as fixed inputs. A **fixed constant** at a
tick is a cell whose content then is the same known value under every admitted procedure
(designated cells other than label and setting cells, P0:116–117, and their images). The readings
checked (definitions, not adopted):

- **R1s (structural exact move).** `Lab(t_p)` = the cells holding the herald record at use time, with
  the preparation's label, coin and setting cells and their copies. `Lab(τ+1)` = the cells whose
  update reads exactly one cell, with a unit coefficient, and that cell is in `Lab(τ)`.
- **R1v (exact move on the support).** As R1s after dropping, from each update, the inputs that are
  fixed constants at that tick: `Lab(τ+1)` = the cells whose remaining update has exactly one input,
  with a unit coefficient, and that input is in `Lab(τ)`. Settings and labels vary with the procedure
  and are never dropped.
- **R2 (structural domain of dependence).** `Lab(τ+1)` = the cells all of whose inputs (nonzero
  coefficients) are in `Lab(τ)`. Sub-readings: **R2(i)** `Lab(t_p) ⊇ V(t_p)` (the finest herald `J*`
  reads all of `V(t_p)`, P0:217–223); **R2(ii)** `Lab(t_p)` = the cells of `V(t_p)` whose content
  varies over the herald's outcomes; **R2(iii)** R2 after dropping fixed-constant inputs, with
  `Lab(τ+1)` = the cells with at least one remaining input and every remaining input in `Lab(τ)`.
- **R3 (functional, per cell).** A cell of `V` is a label at `τ` iff its content is non-constant and
  constant on every `L*`-coset, i.e. a function of the preparation's herald record (and its label,
  coin and setting values) alone. It is a per-cell counterpart of the functional variant noted at
  P0N:36–38, and the functional reading of C-PM's "property of the procedure" clause (OA2:117–118).
- **R0 (fixed locations).** A cell location that held the herald at `t_p` is a label at all later
  ticks.

Precedent controls, re-derived by hand (NOTES-r2 §2 gives the cell-by-cell checks):

| Reading | Instance I | Instance II | N8.2(b) | Precedent-consistent |
|---|---|---|---|---|
| R1s | ✓ | ✓ | ✓ | yes |
| R1v | ✓ (`c`, `u`, `p` all non-fixed) | ✓ (`y₁(0)` dropped; `x₀`, setting `c` remain) | ✓ (`r_0(4)`: `s0(3) = 0` dropped, `r_L(3) = u` not a label) | yes |
| R2(i) | ✓ | ✓ | ✓ | yes |
| R2(ii) | ✓ | ✓ | ✓ | yes |
| R2(iii) | ✓ | ✓ (`x₁(1)` has the non-label input `c`) | ✓ (as R1v) | yes |
| R3 | ✓ | ✓ if only the preparation's own settings count; ✗ if measurement settings count (`w + c` a label) | ✗ (`s0(4) = x`, `s0(5) = y` labels; every label-free statistic is then equal on the four `[ab]`, so the fragment is trivial) | no |
| R0 | — | — | ✗ (`r_0(5)`, `r_1(5)` labels, against P0R:141–144; for `J*` it removes all of `V`) | no |

C-PM's "property of the procedure" clause, read functionally, is R3, which fails N8.2(b); read by
cell provenance, it is the open choice above. So the clause does not fix the delimitation. R0 and
R3 are not aggregated; R3 is reported.

***

## 2. Decision rule (fixed after §1 and before §3; outcome clauses (A)–(C) as in r1; reading enumerations replaced by the criterion)

For each reading R:

- **(A) Witness under R.** An explicit instance with φ = R-lin on a stated carrier, every class
  hypothesis checked by hand (`D_0`, H-AR, (H3), full retention at every tick, herald held at use
  with records inside `S`, H-xiv, C-PM), in which label-cell-only retention occurs **and** C3 fails
  for every `S` satisfying C1–C2 (§1.5). Cell values are exact algebra over `ℤ/q`; a surrogate rule
  does not count. If the fragment is also contextual, that is recorded with the reading attached.
- **(B) Proof under R.** For every instance of the class (scope of §1.1), (LF) holds, hence C3 holds
  with `S*_e`.
- **(C) Unresolved under R.** Neither; the remaining gap is stated.

**Class-level verdict** (no reading adopted): (A) or (B) only if every precedent-consistent reading
gives that verdict; otherwise (C), with the gap named as the delimitation and the per-reading
verdicts stated. R3 is reported, not aggregated.

**Controls.** The precedent table of §1.6 for each reading. For a (B) branch, a multi-tick instance
in which (LF) is not satisfied by construction. For an (A) branch, the same instance under the other
readings. A favourable branch (in either direction) gets a pressure-test node. Verdict text is
generated from the node outcomes.

**Standing and limits of the rule.**
- The reading set is not exhaustive. r1 carried R1s (as R1), R2(i), R2(ii), R3 and R0; the review
  showed that R1v and R2(iii) were missing, and they are added here. A class-level (A) or (B) would
  need every admissible reading; (C) is unchanged by adding readings once two admissible readings
  disagree on one instance.
- "Fixed after §1 and before §3" is an ordering inside one file in one commit; it carries no
  separate preregistration weight.
- (B) requires (LF), which is sufficient for, not equivalent to, the obligation's "cannot happen". An
  instance where (LF) fails and C3 holds gives (C), not (B).

***

## 3. Depth-first nodes

### N1. Single-input updates of R-lin [A]

Structurally (on the rule's coefficients), the update reads, per site, `y_i ← x_i` (one input,
coefficient 1) and `x_i ← Σ_{j∈N(i)} x_j − y_i` (inputs `y_i` with coefficient −1 and at least one `x_j`
with a coefficient not divisible by `q`, by the scope of §1.1). So the only single-input update of
the rule's coefficient graph is `y_i ← x_i`. Under (H3) no supplied isolation (E-iso) removes the
neighbour terms (OA1:339–349; OA2:501). This is the content of OA1:335–349 and OA1:399 ("Under R-lin
no cell is inert") [R], restated.

On the support the statement does not hold: under `D_0`, designated zeros drop out of a
multi-input update, which is then an exact copy. With `y ≡ 0` and one free `X_j`,
`x_i(t) = X_j` for `|i−j| ≤ t` of the parity of `t` (NOTES-r2 §1), a multi-tick light-cone copy. In
W1, `y_3(2) = x_3(1) = x_2(0) = a`, two ticks after use.

Verdict: proved structurally [A]; on the support, exact copies can last several ticks [A].

### N2. R1s: label-cell-only retention cannot occur, at use time `t_p` [P]

*Claim.* Under R1s, for every instance of the class with φ = R-lin (scope §1.1), any law, any
H-AR observer at slot or site level, any `t_p ≤ T`, and **use time `t_p`**:
`Lab(t_p+1) ⊆ {y_i : x_i ∈ Lab(t_p)}` and `Lab(τ) = ∅` for `τ ≥ t_p + 2`. Hence (LF) holds.

*Proof.* By N1 (structural), `Lab(τ+1) = {y_i : x_i ∈ Lab(τ)}` for `τ ≥ t_p`. `Lab(t_p+1)` contains only
`y` cells, so `Lab(t_p+2) = ∅`, and every later set is empty. If `T = t_p + 1`, the only measurement
tick is `T` and `Z_e` is its label-free part, so (LF) holds. If `T ≥ t_p + 2`, `Z_e = V(T)`; by full
retention every `V(τ₁)`, `τ₁ ≤ T`, is a function of `V(T)`, so every accessible single-tick effect and
every heralded composite is a post-processing of `Z_e`. ∎

*Use at each effect's read time.* With use at a read `τ ≥ t_p + 2`, the herald must be held at `τ`,
and the cells holding it there are herald records (OA3:101–102). R1s does not say which cells of
`V(τ)` those are; its propagation from `t_p` gives `Lab(τ) = ∅` while the herald is held at `τ`. N2 is
open for that convention.

*Consequence.* With (LF), P0's N1, N4–N6 (P0:192–293) give C1–C4 with `S*_e` and the coset-space
simplex embedding of the C-PM fragment, under H-xiv, one direction only, transformation
noncontextuality not claimed [P on P0, R-off]. `D_0` is not used in N2 itself; (H3) is used (N1).

Verdict: (B) under R1s with use time `t_p` [P] (the §2 control cannot be met under R1s, N3.3; the
verdict rests on the proof N2 alone); (C) under R1s with use at each effect's read.

### N3. Pressure test of N2 (favourable to closure) [P]

1. **What R1s does to C-PM in R-lin.** At ticks `≥ t_p + 2` R1s leaves no label cell, while full
   retention makes the herald record a function of `V(T)`. So under R1s an effect may compute the
   preparation's herald record from mixed cells. Instance II already does this at one tick
   (`z₁ − c₀ = w`, P0:405–408). C3 holds under R1s because the label exclusion is empty after one
   tick, not because R-lin keeps measurement values in a separate register.
2. **Is N2 the reading P0 used?** It reproduces every evaluated precedent (§1.6), but so do R1v,
   R2(i), R2(ii) and R2(iii). N2 settles R1s only.
3. **The (B)-branch control is vacuous.** Under R1s, `Lab(T) = ∅` whenever `T ≥ t_p + 2`, so (LF) at
   `T` holds by definition and any such instance (W1 included) reproduces the claimed formula. With
   `T = t_p + 1` labels remain at `T` (Instance II), but there is a single measurement tick and (LF)
   is again immediate. No non-vacuous control of the several-tick kind P0 lacked (P0:387–388) exists
   for R1s; none is claimed.

Verdict: N2 stands for R1s at use time `t_p`; its scope is that reading, not the class.

### N4. Can label status outlive one tick in R-lin? Instance W1 [A, P]

Under R1v, R2(i) and R2(iii), a cell at `t_p + 2` can be a label: in R-lin `y_i(t_p+2) = x_i(t_p+1)`
qualifies when `x_i(t_p+1)`'s inputs other than fixed constants (R1v, R2(iii)), or all its inputs
(R2(i)), are in `Lab(t_p)`.

**W1.** R-lin on the ring `ℤ/16` (`d = 1`), any `q ≥ 2`, `t_p = 0`, `T = 2`, no settings.
Free (uniform, independent): `X_0 = n`, `X_2 = a`, `X_7 = b`, `X_9 = m`, `Y_5 = p` (`X_i = x_i(0)`,
`Y_i = y_i(0)`). Every other cell designated 0. `V = {y_0, x_1, x_2, y_3, x_4, x_7, y_7, y_8, y_10}`
(slot level, H-AR). Hand formulas: `x_i(1) = X_{i−1} + X_{i+1} − Y_i`, `y_i(1) = X_i`,
`x_i(2) = X_{i−2} + X_i + X_{i+2} − Y_{i−1} − Y_{i+1}`, `y_i(2) = x_i(1)`.

| cell | t = 0 | t = 1 | t = 2 |
|---|---|---|---|
| `y_0` | 0 | `n` | 0 |
| `x_1` | 0 | `n+a` | 0 |
| `x_2` | `a` | 0 | `n+a` |
| `y_3` | 0 | 0 | `a` |
| `x_4` | 0 | 0 | `a−p` |
| `x_7` | `b` | 0 | `b+m` |
| `y_7` | 0 | `b` | 0 |
| `y_8` | 0 | 0 | `b+m` |
| `y_10` | 0 | 0 | `m` |

Hypotheses, checked: `D_0` (designated zeros, five free cells); H-AR; (H3); H-xiv trivially (no
setting); `n`, `m`, `p` are outside `V(0)` (`x_0`, `x_9`, `y_5 ∉ V`); records inside `S`; the herald
`J*` on `V(0)` fixes `(a, b)` and is held at `t_p` and at every later read. **Full retention at
every tick:** `V(2)` gives `a = y_3`, `n = x_2 − y_3`, `p = y_3 − x_4`, `m = y_10`, `b = y_8 − y_10`,
hence `V(1)` and `V(0)`; `V(1)` gives `n`, `a = x_1 − y_0`, `b = y_7`, hence `V(0)`. Window: every
formula reads sites −2…12, distinct mod 16.

Label sets on `V` (NOTES-r2 §3 lists every cell):
- R1v: `Lab(0) = {x_2, x_7}`; `Lab(1) = {y_2, y_7, x_3, x_6}` (`x_3(1)`'s non-fixed inputs are `x_2(0)`
  alone, `x_6(1)`'s are `x_7(0)` alone); `Lab(1) ∩ V = {y_7}`; `Lab(2) ∩ V = {y_3}` (`y_3 ← x_3`).
  `x_2(2)`, `x_4(2)`, `x_7(2)` have several non-fixed inputs and are label-free.
- R2(iii): the same sets on `V` (each non-fixed input of `x_3(1)`, `x_6(1)` is a label; `x_2(2)` reads
  the non-label `x_1(1)`, `x_4(2)` reads `x_5(1) = −p`, `x_7(2)` reads `x_8(1) = b+m`).
- R2(i): `Lab(0) = V`; `Lab(1) = {y_1, y_2, y_4, y_7, x_3}`; `Lab(2) ∩ V = {y_3}`.
- R3: `{y_7}` at tick 1, `{y_3}` at tick 2.

Effects on the point preparations `[ab]`, `a, b ∈ {0, 1}`, under any of these four:
- tick 1, label-free `(n, n+a)`: `X = x_1(1) − y_0(1) = a` is sharp; `b` sits only in the label
  `y_7(1)`;
- tick 2, label-free `(n+a, a−p, b+m, b+m, m)`: `Y = y_8(2) − y_10(2) = b` is sharp; with `n`, `p`
  uniform and independent, `(n+a, a−p)` is uniform for each `a`;
- composites: a tick-1 event is held at tick 2 in label-free cells only if it is a function of
  `n+a` (`= x_2(2)`); every composite's law is that of a function of `(n+a, b, m)`.

Label-cell-only retention: the tick-1 read `y_0(1) = n` is a function of `V(2)` (`x_2 − y_3`) and not
of the label-free part of `V(2)`. Lost common effects: C1–C2 hold only for `S` with cosets indexed
by `(a, b)` (finer cosets are never prepared: no preparation-stage read sees `n`, `m`, `p`; coarser
cosets do not contain the point laws as mixtures). The `(a, b)` indicator is neither accessible nor
a sum of accessible effect statistics: every such statistic has the form `f(a) + g(b)`, and the
indicator of `(0, 0)` would need `f(0)+g(0) + f(1)+g(1) = 1` and `f(0)+g(1) + f(1)+g(0) = 0` at once.
So C3 fails for every admissible `S`.

Contextuality: every accessible effect depends on the `a`-marginal or the `b`-marginal only, so
`½([00]+[11]) ∼ ½([01]+[10])` (coin mixtures under C-PM). `X` and `Y` are sharp and label-free, so the
four supports are pairwise disjoint. The argument of OA-2 Claim 2, steps 1, 2 and 4 (OA2:446–448,
:457–458), as abstracted in P0 R7 (P0:182–183), with step 3 supplied by the equivalence above under
the reading named, then excludes a preparation-noncontextual model: a gbit, with raw (SP) failing.
Claim 2 itself is stated for `𝔊_K` with its labels out of reach (C-PM′, OA2:449–450); W1's
equivalence holds under the reading's label convention.

Verdict: (A) under R1v, R2(i), R2(iii) and R3 for `d = 1` [A for the table and label sets; P for the
contextuality step].

### N5. Pressure test of N4 (favourable to non-classicality) [A, P]

1. **The same W1 under the other readings.**
   - R1s: `Lab(1) ∩ V = {y_7}`, `Lab(2) = ∅`; the `(a, b)` indicator is a function of `V(2)`; C3
     holds; simplex-embeddable.
   - R2(ii): `Lab(0) = {x_2, x_7}`; `x_3` reads `x_4(0)`, `y_3(0)` (constant, not labels), so
     `x_3 ∉ Lab(1)`; `Lab(2) = ∅`; classical as under R1s.
   - R1v and R2(iii) reach the gbit by treating `x_4(0)`, `y_3(0)` as fixed inputs; R2(i) reaches it by
     treating them as label cells. The split is between structural and on-the-support provenance
     (R1s against R1v), and between constants as labels, as fixed inputs, or neither (R2(i), R2(iii),
     R2(ii)). Nothing in the rule decides it.
2. **`d = 3`.** Embed the chain in `(ℤ/16) × (ℤ/s)²`, `s ≥ 3`, transverse cells designated 0. Tick 1
   and every `y` cell are unchanged; an `x` cell at tick 2 gains `4X_i`: `x_2(2) = n + 5a`,
   `x_7(2) = 5b + m`, the others unchanged.
   - R1v and R2(iii): the transverse inputs of `x_3(1)` are fixed zeros, so `x_3 ∈ Lab(1)` and
     `y_3(2) ∈ Lab(2)`; `x_2(2)`, `x_4(2)`, `x_7(2)` stay label-free. Label-free at tick 2:
     `(n+5a, a−p, 5b+m, b+m, m)`; `b = y_8 − y_10`; `(n+5a, a−p)` uniform for each `a`; a tick-1 event is
     label-free-held at tick 2 only through `n + a`, and only when `4 ≡ 0 (mod q)`, with laws still
     independent of `a`; retention `a = y_3`, `n = x_2 − 5a`, `p = a − x_4`. A gbit for every `q ≥ 2` [A, P].
   - R3: the same labels and the same gbit, every `q` [A, P].
   - R2(i), this embedding: `x_3(1)` also reads its four transverse `x(0)` cells, which are not in
     `V`, so `x_3 ∉ Lab(1)`, `Lab(2) = ∅`, and the fragment is classical [A].
   - R2(i), enlarged observer: add the four transverse `x` cells of site 3 to `V` (0 at ticks 0 and 1).
     Then `x_3 ∈ Lab(1)` and `y_3(2) ∈ Lab(2)`; each added cell holds `2a` at tick 2 and is label-free
     (its input `x_{2+e⊥}(1) = a` is not a label). For odd `q` this exposes `a`; at `q = 2` it is 0, and
     the rest of N4 goes through (`n + 5a = n + a`, `5b + m = b + m`). A gbit at `q = 2` [A, P];
     other `q` open.
3. **Site-level observers (Main:292–294).** Site alignment copies every `x_i(τ)` into `y_i(τ+1) ∈ V`,
   so a label-only hold needs a gap of two ticks. **W2′** (`d = 1`, ring `ℤ/24`, `T = 3`, `t_p = 0`):
   free `X_0 = n`, `X_2 = a`, `X_10 = b`, `X_12 = r`, `X_14 = m`; all `Y` and every other `X` designated
   0; `V` = sites `{−1, 1, 2, 5, 8, 10, 11, 15}` (both slots). With `y = 0` initially,
   `x_i(t) = Σ_j X_j [|i−j| ≤ t, |i−j| ≡ t mod 2]` (checked by hand for `t ≤ 3`); the table is in
   NOTES-r2 §4.
   - Label-free cells: `(n, n+a, b+r, m)` at tick 1 and `(n, n+a, n+a, b+r, b+r, m)` at tick 2, which
     give `a`, not `b`; `(n+a, n+a, n+a, b+r, b+r+m, r+m)` at tick 3, which give `b`, not `a`.
   - Labels under R1v, R2(iii) and R3, in `V`: `y_2(1) = a`, `y_10(1) = b`, `x_8(2) = b`, `x_5(3) = a`,
     `y_8(3) = b`. `x_5(3)` is a label through the on-the-support chain
     `x_2(0) → x_3(1) → x_4(2) → x_5(3)`, each step with one non-fixed input.
   - Full retention at every tick: `V(3)` gives `a = x_5`, `b = y_8`, `r = y_10 − b`, `m = x_15 − r`,
     `n = x_{−1} − a`; `V(2)` gives `n = y_{−1}`, `a = y_1 − n`, `b = x_8`, `r = x_10 − b`, `m = y_15`; `V(1)`
     gives `n`, `a`, `b = y_10`, `r = x_11 − b`, `m`.
   - The same gbit argument as N4 applies under R1v, R2(iii) and R3 [A, P]. Under R1s, R2(i) and
     R2(ii), `Lab(2) ∩ V = ∅`, so `x_5(3) = a` and `b` are both label-free at tick 3 and the fragment is
     classical [A].
   - W2′ adds site 8 and the mask `r` to r1's W2. Under R1v, r1's W2 is classical, because
     `x_10(2) = b` has three non-fixed inputs and is label-free.
4. **Convention artefact test (OA3:445–455).** OA-3 discards a gbit present already for trivial
   dynamics. W1's gbit needs R-lin's additive masking. Under permutation dynamics, R2 coincides with
   R1s and R1v, and R3 leaves no herald content in label-free cells. So the test as stated does not
   discard W1. The decisive observation is item 1: the same instance is classical under R1s and
   R2(ii).

Verdict: W1 (`d = 1`, and `d = 3` except under R2(i) for general `q`) and W2′ (site level) stand as
in-class witnesses under the readings named; neither is a witness at the frozen scope.

### N6. R2(ii): not settled [P]

Under R2(ii) a label at `t_p + 2` needs a cell whose inputs at `t_p + 1` are labels whose inputs at
`t_p` all hold varying herald content. One attempt (`d = 1`, `t_p = 0`, `T = 2`, label
`y_3(2) = x_3(1) = a + a′ − a″` with `x_2 = a`, `x_4 = a′`, `y_3 = a″` herald cells): `y_3(0)` is read
only by `x_3`'s update, so `a″` reaches tick 2 only inside `a + a′ − a″` (in `x_2(2)`, `x_4(2)`,
`y_3(2)`). Recovering `a″` at tick 2 (full retention) then needs `a` from a label-free cell, whose
mask is fresh and so recoverable only label-free; `X = a` becomes label-free at `T`. The attempt
fails for this geometry. Other geometries, longer horizons and `d = 3` are not examined.

Gap: whether some R-lin instance has, under R2(ii), a tick-`T` label holding the herald part of a
measurement-stage read while full retention holds and the label-free part of `V(T)` leaves that part
undetermined on the point preparations.

### N7. Aggregation

| Reading | Precedent-consistent | Verdict | Node |
|---|---|---|---|
| R1s | yes | (B) at use time `t_p`, all of §1.1's scope (the §2 control cannot be met under R1s, N3.3; the verdict rests on the proof N2 alone); (C) with use at each effect's read | N2 |
| R1v | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level in `d = 1`) | N4, N5 |
| R2(i) | yes | (A): W1 `d = 1`; `d = 3`: W1's embedding classical, enlarged observer a gbit at `q = 2`, other `q` open | N4, N5 |
| R2(ii) | yes | (C), N6 gap | N6 |
| R2(iii) | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level in `d = 1`) | N4, N5 |
| R3 | no (fails N8.2(b)) | (A): W1 (`d = 1, 3`), W2′ | N4, N5 |

The precedent-consistent readings disagree on W1 itself. By §2 the class-level verdict is (C).

***

## 4. Verdict

**(C) at the frozen scope.**

- Under R1s (structural exact move) with use time `t_p`, label-cell-only retention cannot occur for
  R-lin with (xiii): label status survives at most one tick past the use time (N1, N2). (LF) and C3
  hold for the class (the §2 control cannot be met under R1s, N3.3; the verdict rests on the proof
  N2 alone).
- Under R1v (exact move on the support), R2(i) and R2(iii), W1 is an R-lin instance of the class with
  label-cell-only retention and lost common effects, and the fragment is a gbit (N4). Under R1v and
  R2(iii) this holds in `d = 1` and `d = 3` for every `q`, and at site level in `d = 1` (W2′).
- Under R2(ii), and under R1s with use at each effect's read, the question is open (N2, N6).
- The remaining gap is the delimitation itself: which cells of `V(τ)`, `τ > t_p`, C-PM counts as
  preparation labels when records are held in `V` (SY:201–202, MM-2 item 3). The precedents leave two
  choices open: structural or on-the-support provenance, and whether fixed constant cells count as
  labels, as fixed inputs or as neither. Two exact-copy readings that both agree with every precedent,
  R1s and R1v, give opposite verdicts on W1.
- Decisive node: N5 item 1 with N4 (W1 under every reading), resting on N1's two statements.

***

## 5. Consequences for C4 and P0

**C4, preparation side (§A.34, one direction at a time).**
- (⇐) Equal coset-weight vectors ⇒ operationally equivalent: holds for every instance and reading,
  since a preparation's law of the record is fixed by its coset weights (P0 N1, N4) [P, R-off].
- (⇒) Operationally equivalent ⇒ equal coset-weight vectors: needs C3. Established under R1s with use
  time `t_p` for the class (N2 with P0 N6). Fails in W1 under R1v, R2(i), R2(iii) and R3
  (`½([00]+[11]) ∼ ½([01]+[10])` with different weights). Open under R2(ii) and under R1s with use at
  each effect's read.

**C4, measurement side.** Both directions hold without (LF), from C1–C2 (P0:280–281) [P, R-off].

**Simplex embedding.** Under R1s with use time `t_p`: (LF) for the class ⇒ simplex-embeddable (one
direction; the converse is not claimed; transformation noncontextuality not claimed).

**P0.** P0 stays **O-U**. Its unresolved check (P0:424–427) is now located: C3 for R-lin turns on the
label delimitation (N4, N5) and, under R1s, on the use-time convention. Conditional bearings, neither
adopted:
- if the owner fixes R1s with use time `t_p` and confirms the R-lin reading of the class (owner
  question 4), and the result survives independent review, the C3 and C4 checks pass for the
  class, P0's pass condition (P0:67–71) is met with C1–C2 (P0 N1, N4), subject to P4, and the ordering
  rule (R9:317–320) hands Q4 to AW-OA2-1 (N2 holds for every carrier of §1.1, so owner question 5
  does not affect it);
- if the owner fixes R1v or R2(iii) (any carrier treated), or R2(i) with a ring carrier, W1 is an
  in-class contextual counterexample, which P0:74–76 permits in place of O-U; whether a
  reading-produced gbit counts (compare OA3:445–455) is a separate decision.

Nothing here changes a status, priority or premise.

***

## 6. Support for each claim

| Claim | Layer | Hypotheses |
|---|---|---|
| Structurally, R-lin's only single-input update is `y_i ← x_i` (N1) | [A] | (xiii), R-lin `F`, (H3), scope §1.1 |
| On the support, multi-tick exact copies exist (N1; W1, W2′) | [A] | `D_0` with designated zeros |
| Under R1s, `Lab(τ) = ∅` for `τ ≥ t_p+2`; (LF) and C3 for the class (N2) | [P] | R1s, use time `t_p`, L reading, H-AR, (H3), the class |
| Simplex embedding under R1s (N2 consequence) | [P] on P0 N1–N6 [R-off] | as above, H-xiv, `D_0`, one direction |
| W1 and W2′ cell tables, label sets and full retention | [A] | stated instances |
| W1 gbit under R1v, R2(i), R2(iii), R3 (`d = 1`); under R1v, R2(iii), R3 (`d = 3`); under R2(i) (`d = 3`, enlarged `V`, `q = 2`); W2′ gbit under R1v, R2(iii), R3 | [P] via the argument of OA-2 Claim 2 [R] and P0 R7 [R-off] | the reading named |
| W1 classical under R1s, R2(ii) and, in W1's `d = 3` embedding, R2(i); W2′ classical under R1s, R2(i), R2(ii) | [A] + P0 N6 [R-off] | the reading named |
| R2(ii) open; one geometry fails | [P] | as stated in N6 |
| Precedent table of §1.6 | [P], re-checked by hand on P0 [R-off] | — |
| [L] Schmid et al., PRX Quantum 2, 010331 (2021), via P0 | [L] | context only |

No [K] support is involved.

***

## 7. §A.31 classification and assumption-watch

- **NEW.** Inside R-lin, one in-class instance (W1) is classical under some precedent-consistent
  delimitations (R1s, R2(ii)) and a gbit under others (R1v, R2(i), R2(iii)). The unfixed delimitation
  itself is SY MM-2 item 3 (SY:201–202), P0 N8.3 (P0:353–355) and P0N:36–38.
- **ELABORATING** of OA1:335–349, :399. R-lin's coefficient graph has one single-input update,
  `y_i ← x_i` (N1, structural). On the support under `D_0`, exact copies last several ticks (N1).
- **ELABORATING AW-P0-2 (record-only).** Every in-`V` C-PM argument in the affine class depends on a
  label delimitation after the use time: P0 N5, N8.2(b) (a gbit under R1s, R1v, R2; trivial under R3),
  OA-2 E(b) step 4 (OA2:534) and OA-3 N4.3 step 4 (OA3:468–469) (AW-P0-2, P0:488–492; SY T5). For
  R-lin with full retention, `T ≥ t_p+2` and use time `t_p`, the singleton-indicator presumption holds
  under R1s and can fail under R1v, R2(i), R2(iii) or R3 (W1 has (SP) failing, so it does not bear on
  E(b)).

***

## 8. Owner questions

1. **Delimitation.** Which cells of `V(τ)`, `τ > t_p`, are preparation labels under C-PM when records
   are held in `V`: R1s, R1v, R2(i), R2(ii), R2(iii), the functional R3, or another rule? Two
   sub-choices decide it: structural or on-the-support provenance, and whether fixed constant cells
   count as labels, as fixed inputs or as neither. This is SY MM-2 item 3, and it decides C3 for
   R-lin (§4).
2. **Reading-produced contextuality.** If a reading other than R1s is chosen, does a gbit that appears
   under that reading and not under R1s (W1) count as an OBL-SP outcome, or as a convention artefact
   in the sense of OA3:445–455?
3. **Observer granularity.** Are H-AR cells slots (P0's instances) or sites (Main:292–294)? W2′ covers
   R1v, R2(iii) and R3 at site level; R2(i) at site level is classical for W2′ and otherwise not
   settled.
4. **Rule class.** This record follows P0 and review 5892912758 in reading OBL-SP's class as R-lin with
   (xiii). Under R1s the N8.2(b) conveyor is an affine gbit, so a reading of the class as all of
   ledger (vii) would change P0's outcome. Confirm the R-lin reading.
5. **Carrier.** Does the class admit rings and other `d`, as P0's instances use (P0:392, :402), or only
   the simple cubic lattice (P:85–86; Main:724 (x))? R1s's (B) holds for all of them. Under R1v and
   R2(iii) W1 is a gbit in `d = 1` and `d = 3`; under R2(i) only in `d = 1` and, with an enlarged
   observer, in `d = 3` at `q = 2`. W2′ (site level) is a `d = 1` instance; W2′ in `d = 3` is not
   examined.
6. **Use time under R1s.** With use at each effect's read, which cells of `V(τ)` hold the herald? N2
   holds for use time `t_p` only.

***

## 9. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| P0 (`REC-1-P0-r3.md`, blob `611a4d9a`) at `3a3aa146`, branch `research/rec-1-1169-20261113`, draft PR #1268: C1–C4, (LF), N1–N6, R7, Instances I and II, N8.2(b), the outcome rule | §1.4–1.6, N2–N5, §5 | Support off `main` (definitions, the scoped result under (LF), R7, the precedents): a gap until landed |
| P0R (`REC-1-P0-REVIEW-r1.md`, blob `ec5178ca`) at `3a3aa146`: the N8.2(b) label evaluation (P0R:135–144) | §1.6 | Support off `main` for one precedent row: a gap until landed; the row is re-checked by hand here |
| P0N (`REC-1-P0-NOTES-r2.md`, blob `1cd2e3fa`) at `3a3aa146`: the functional variant (P0N:36–38), tick-5 labels (P0N:22–24) | §1.6, §7 | Support off `main` for one precedent detail; provenance for R3's relation to the variant: a gap until landed |
| P0C (`REC-1-P0-CONFIRM-r3.md`, blob `8b440f2d`) at `3a3aa146` | read for context | Provenance |
| R9 (`REC-1-r9.md`, blob `945b7982`) at `3a3aa146`: OBL-SP's statement (R9:259–272), the L reading (R9:301–307), the ordering rule (R9:317–320) | §1.2, §5 | Support off `main` (class definition and reading): a gap until landed |
| SY (`SYNTHESIS-r3.md`, blob `e6829509`) at `9eeee392`, branch `research/synthesis-1169-20261113`, PR #1276: MM-2 item 3 (SY:201–202), T5 | §1.6, §7, §8 | Provenance (placement of the check; prior art for §7; no step rests on it) |
| RV (`REVIEW-r1.md`) at `a03af682`, branch `research/c3-rlin-xiii-1169-20261113` | revision line; R1v, R2(iii), §2 limits | Provenance: every reading and label set taken from it was re-derived by hand here (NOTES-r2 §2–3) |
| ChatGPT review 5892912758 on #1268 | header, §1.2 | Provenance (origin of the obligation; the rule-class reading it states is also P0's, P0:350–352) |
| #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z) | header | Governance provenance, fetched and quoted |
| #1268 c.6860582570 (`amaybaum`, 2026-11-13T17:47:34Z) | §1.2 | Governance provenance, fetched and quoted |
| Main, OA1, OA2, OA3, P at `c3b5f37a` | throughout | Support on `main` ([R]; Main as manuscript) |
| [L] Schmid et al. 2021 | §6 | External literature, context only |
