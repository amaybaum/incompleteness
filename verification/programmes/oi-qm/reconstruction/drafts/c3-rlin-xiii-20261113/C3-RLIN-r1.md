# C3 for R-lin with (xiii): label-cell-only retention (paper-only check, r1)

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
| P0 | `…/drafts/rec-1-20261113/REC-1-P0-r3.md` | `research/rec-1-1169-20261113` `2a9f10ba` | `611a4d9a` |
| P0C | `…/drafts/rec-1-20261113/REC-1-P0-CONFIRM-r3.md` | `2a9f10ba` | `8b440f2d` |
| P0R | `…/drafts/rec-1-20261113/REC-1-P0-REVIEW-r1.md` | `2a9f10ba` | `ec5178ca` |
| P0N | `…/drafts/rec-1-20261113/REC-1-P0-NOTES-r2.md` | `2a9f10ba` | `1cd2e3fa` |
| R8 | `…/drafts/rec-1-20261113/REC-1-r8.md` | `2a9f10ba` | `615b7de8` |
| SY | `…/drafts/synthesis-1169-20261113/SYNTHESIS-r3.md` | `research/synthesis-1169-20261113` `9eeee392` | `e6829509` |

`…` abbreviates `verification/programmes/oi-qm/reconstruction`. P0, P0C, P0R, P0N, R8 and SY are off
`main` (§9).

**Support labels.** [K] kernel-checked; [A] exact algebra, checked by hand here; [P] paper
derivation (this record unless a source is named), unreviewed; [L] literature, context only;
[R] research record on `main`, not independently established; [R-off] research record off `main`.
A *reading* is an interpretation of an undefined interface item; no reading is adopted here.

***

## 1. C3 stated for R-lin with (xiii)

### 1.1 The rule

- Ledger (xiii) (Main:724): each site carries a previous and a current value in a finite abelian
  group, and one step is `(x(t−1), x(t)) ↦ (x(t), F(x(t)) − x(t−1))`; ledger (vii) linearity, (viii)
  site factorization, (x) nearest-neighbour range, (xi) no explicit copy of the site's own value
  (Main:724). Main:292–294 displays the instance at `q = 2`.
- R-lin: `F` is the nearest-neighbour sum on the simple cubic lattice, at general `q` (P:85–89).
  Per site, `(y_i, x_i) ↦ (x_i, Σ_{j∈N(i)} x_j − y_i)` (OA1:335–336).
- Cells are the slots `y_i`, `x_i`. P0's instances use slot-level observers on rings (P0:392–411);
  Main:292–294 uses site regions (both slots). Both granularities are treated below.
- Scope of "R-lin" here: a finite torus `(ℤ/L)^d` or a finite-horizon window of `ℤ^d` (OA2:92),
  any `q ≥ 2`, in which every site has a neighbour whose multiplicity in `N(i)` is not divisible by
  `q` (true on every window and on every torus with a side ≥ 3). This excludes only the decoupled
  case `F ≡ 0 (mod q)` (all sides 2 at `q = 2`).

### 1.2 The class (OBL-SP)

R8:255–268: φ in the gauge-derived affine class (ledger (vii); R-lin with (xiii)) on a finite
carrier; initial law in `D_0` (designated cells known, every other cell uniform and independent);
H-AR observers (OA2:182–193); (H3) no supplied control (OA2:501); records as in (H4) (OA2:502) or in
the (V-ii-H) effect class (OA3:120–123); heralds held at use with records formed inside `S`; the
closure-defined prepare–measure fragment under C-PM (OA2:88–125); H-xiv. The literal L reading,
adopted by the owner and stated at R8:297–303: every observer of the class retains every read of
the horizon in `V`. P0 and the review treat the rule class as R-lin with (xiii), not the whole
affine class (P0:350–352; review 5892912758: the ring conveyor "is outside R-lin with (xiii)"). This
record does the same.

Notation (P0 §2.1, P0:115–129): an instance is `(φ, V, D, r, T, t_p)`; `K` is the free subgroup;
records `Z_τ = V(τ)`. **Full retention** (L reading): `V(τ)` is a function of `V(τ′)` on the support
for `τ ≤ τ′ ≤ T`. The check below verifies it at every tick, which is at least what (H4) and the
retention form of (V-ii-H) (OA3:474–475; P0:171–174) require.

### 1.3 Effects and C-PM accessibility

- C-PM (OA2:110–118): "A preparation procedure's own label cells are not effects on what it
  prepares"; "Effects are all post-processings of held records **other than those label cells**. No
  read of the prepared configuration is removed." OA3:101–102 adds herald records to the labels.
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
  `V(T)` but not of `Z_e = V∖Lab(T)` at `T`. This is the failure of (LF).
- **Lost common effects**: for every subgroup `S` satisfying C1 and C2, some `S`-coset indicator of
  the joint measurement record is not a C-PM-accessible effect. This is the failure of C3.

(LF) implies C3 (P0 N5). A witness needs both terms; a proof that they cannot occur needs (LF).

### 1.6 The undefined item: label status after the use time

Under in-`V` retention a cell of `V` can hold herald content and also be read as part of the
prepared configuration. The frozen texts name label cells (OA2:110–118; OA3:101–102) but do not say
which cells of `V(τ)`, for `τ > t_p`, are label cells. The synthesis lists this as an unfixed
interface item (SY:201–202, MM-2 item 3). P0 fixes it at evaluated points only:

| Precedent | Evaluation | Source |
|---|---|---|
| Instance II (R-lin) | `y₀(1) = x₀(0)` (exact copy of the herald cell) is a label; `x₁(1) = x₀(0) + x₂(0) − y₁(0) = w + c` is label-free | P0:402–411, :353–355 |
| N8.2(b) ring conveyor | cells reached from the herald cells by the shift `r_j(t+1) = r_{j−1}(t)` are labels; `r_0(t+1) = r_L(t) + s0(t)`, `s0(4) = x`, `s0(5) = y` are label-free | P0:318–349; P0R:135–144; P0N:22–24 |
| Instance I | `x₀(1) = u + c − p` label-free | P0:392–400 |

The readings checked (definitions, not adopted):

- **R1 (exact-move provenance).** `Lab(t_p)` = the cells holding the herald record at use time, with
  the preparation's label, coin and setting cells and their copies. `Lab(τ+1)` = the cells whose
  update reads exactly one cell, with a unit coefficient, and that cell is in `Lab(τ)`.
- **R2 (structural domain of dependence).** `Lab(τ+1)` = the cells all of whose inputs (nonzero
  coefficients) are in `Lab(τ)`. Sub-readings: **R2(i)** `Lab(t_p) ⊇ V(t_p)` (the finest herald `J*`
  reads all of `V(t_p)`, P0:217–223); **R2(ii)** `Lab(t_p)` = the cells of `V(t_p)` whose content
  varies over the herald's outcomes.
- **R3 (functional, per cell).** A cell of `V` is a label at `τ` iff its content is non-constant and
  constant on every `L*`-coset, i.e. a function of the herald record (and label, coin, setting
  values) alone. This is the "functional variant" recorded as not pursued at P0N:36–38.
- **R0 (fixed locations).** A cell location that held the herald at `t_p` is a label at all later
  ticks.

Precedent controls, checked by hand: R1, R2(i) and R2(ii) reproduce all three rows. R3 fails two:
it makes `s0(4) = x`, `s0(5) = y` labels in N8.2(b) (then every label-free effect has the same
statistics on the four `[ab]` and the fragment is trivial, not a gbit), and it makes `x₁(1) = w + c`
a label in Instance II. R0 makes `r_0(5)`, `r_1(5)` labels in N8.2(b), against P0R:141–144, and for
`J*` it removes every cell of `V`, against "No read of the prepared configuration is removed". R0 is
not used further. R3 is reported separately as P0N's variant.

***

## 2. Decision rule (fixed after §1 and before §3)

For each reading R ∈ {R1, R2(i), R2(ii), R3}:

- **(A) Witness under R.** An explicit instance with φ = R-lin on a stated carrier, every class
  hypothesis checked by hand (`D_0`, H-AR, (H3), full retention at every tick, herald held at use
  with records inside `S`, H-xiv, C-PM), in which label-cell-only retention occurs **and** C3 fails
  for every `S` satisfying C1–C2 (§1.5). Cell values are exact algebra over `ℤ/q`; a surrogate rule
  does not count. If the fragment is also contextual, that is recorded with the reading attached.
- **(B) Proof under R.** For every instance of the class (scope of §1.1), (LF) holds, hence C3 holds
  with `S*_e`.
- **(C) Unresolved under R.** Neither; the remaining gap is stated.

**Class-level verdict** (no reading adopted): (A) or (B) only if every precedent-consistent reading
(R1, R2(i), R2(ii)) gives that verdict; otherwise (C), with the gap named as the delimitation and
the per-reading verdicts stated. R3 is reported, not aggregated.

**Controls.** The precedent table of §1.6 for each reading. For a (B) branch, a multi-tick instance
in which (LF) holds non-trivially (P0's controls had none, P0:387–388). For an (A) branch, the same
instance under the other readings. A favourable branch (in either direction) gets a pressure-test
node. Verdict text is generated from the node outcomes.

***

## 3. Depth-first nodes

### N1. Exact moves of R-lin [A]

The update reads, per site, `y_i ← x_i` (one input, coefficient 1) and
`x_i ← Σ_{j∈N(i)} x_j − y_i` (inputs `y_i` with coefficient −1 and at least one `x_j` with a coefficient
not divisible by `q`, by the scope of §1.1). So the only exact move is `x_i(τ) → y_i(τ+1)`, and a
`y` cell is overwritten by a fresh mixture one tick later.

Check: on `y_i(τ+2) = x_i(τ+1) = Σ x_j(τ) − y_i(τ)`. Under (H3) no supplied isolation (E-iso)
removes the neighbour terms (OA1:339–349; OA2:501). Corroborated by OA1:399 ("Under R-lin no cell
is inert") [R].

Verdict: proved [A]. The conveyor of N8.2(b) (`r_j(t+1) = r_{j−1}(t)`, multi-tick exact moves) has no
counterpart in R-lin under (H3).

### N2. R1: label-cell-only retention cannot occur [P]

*Claim.* Under R1, for every instance of the class with φ = R-lin (scope §1.1), any law, any
H-AR observer at slot or site level, any `t_p ≤ T` and either use time:
`Lab(t_p+1) ⊆ {y_i : x_i ∈ Lab(t_p)}` and `Lab(τ) = ∅` for `τ ≥ t_p + 2`. Hence (LF) holds.

*Proof.* By N1, `Lab(τ+1) = {y_i : x_i ∈ Lab(τ)}` for `τ ≥ t_p`. `Lab(t_p+1)` contains only `y` cells,
so `Lab(t_p+2) = ∅`, and every later set is empty. If `T = t_p + 1`, the only measurement tick is
`T` and `Z_e` is its label-free part, so (LF) holds. If `T ≥ t_p + 2`, `Z_e = V(T)`; by full
retention every `V(τ₁)`, `τ₁ ≤ T`, is a function of `V(T)`, so every accessible single-tick effect
and every heralded composite is a post-processing of `Z_e`. ∎

*Consequence.* With (LF), P0's N1, N4–N6 (P0:192–293) give C1–C4 with `S*_e` and the coset-space
simplex embedding of the C-PM fragment, under H-xiv, one direction only, transformation
noncontextuality not claimed [P on P0, R-off]. D_0 is not used in N2 itself; (H3) is used (N1).

Verdict: (B) under R1 [P].

### N3. Pressure test of N2 (favourable to closure) [P]

1. **What R1 does to C-PM in R-lin.** At ticks `≥ t_p + 2` R1 leaves no label cell, while full
   retention makes the herald record a function of `V(T)`. So under R1 an effect may compute the
   preparation's herald record from mixed cells. Instance II already does this at one tick
   (`z₁ − c₀ = w`, P0:405–408). C3 holds under R1 because the label exclusion is empty after one
   tick, not because R-lin keeps measurement values in a separate register.
2. **Is N2 the reading P0 used?** It reproduces every evaluated precedent (§1.6), but so do R2(i)
   and R2(ii). No precedent covers a cell whose update reads only label cells, which is where R1 and
   R2 differ. N2 therefore settles R1 only.
3. **Multi-tick control.** W1 below (N4) has two measurement ticks. Under R1, `Lab(1) ∩ V = {y_7}`
   and `Lab(2) = ∅`; `V(2)` gives `(a, b)` jointly, `S*_e` = the span of the `n`, `m`, `p` directions,
   and its coset indicators are functions of `V(2)`. (LF) holds non-trivially, as N2 predicts.

Verdict: N2 stands for R1; its scope is R1, not the class.

### N4. Can label status outlive one tick in R-lin? R2(i): instance W1 [A, P]

Under R2, a cell at `t_p + 2` is a label when its whole one-tick input set is labelled; in R-lin
`y_i(t_p+2) = x_i(t_p+1)` qualifies when `y_i`, `x_{i±1}` (all `x`-neighbours) are in `Lab(t_p)`.

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

R2(i) labels: `Lab(0) = V`; `Lab(1) = {y_1, y_2, y_4, y_7, x_3}` (`x_3` reads `y_3`, `x_2`, `x_4`, all in
`V`); `Lab(2) ∩ V = {y_3}` (`y_3` reads `x_3`); no `x` cell of `V` qualifies at tick 2 (`x_1` reads
`x_0 ∉ Lab(1)`, `x_2` reads `x_1`, `x_4` reads `x_5`, `x_7` reads `x_6`).

Effects on the point preparations `[ab]`, `a, b ∈ {0, 1}`:
- tick 1, label-free `(n, n+a)`: `X = a` is sharp; `b` sits only in the label `y_7(1)`;
- tick 2, label-free `(n+a, a−p, b+m, b+m, m)`: `Y = b` is sharp; with `n`, `p` uniform and
  independent, `(n+a, a−p)` is uniform for each `a`;
- composites: a tick-1 event is held at tick 2 in label-free cells only if it is a function of
  `n+a` (`= x_2(2)`); every composite's law is that of a function of `(n+a, b, m)`.

Label-cell-only retention: the tick-1 read `y_0(1) = n` is a function of `V(2)` (`x_2 − y_3`) and not
of the label-free part of `V(2)`. Lost common effects: C1–C2 hold only for `S` with cosets indexed
by `(a, b)` (finer cosets are never prepared: no preparation-stage read sees `n`, `m`, `p`; coarser
cosets do not contain the point laws as mixtures). The `(a, b)` indicator is neither accessible nor
a sum of accessible effect statistics, since every such statistic depends on one marginal only
(next paragraph). So C3 fails for every admissible `S`.

Contextuality: every accessible effect depends on the `a`-marginal (tick 1) or the `b`-marginal
(tick 2, composites) only, so `½([00]+[11]) ∼ ½([01]+[10])` (coin mixtures under C-PM). `X` and `Y`
are sharp. OA-2 Claim 2 (OA2:443–458; P0 R7) then excludes a preparation-noncontextual model: a gbit,
with raw (SP) failing.

Verdict: (A) under R2(i) [A for the table; P for the contextuality step].

### N5. Pressure test of N4 (favourable to non-classicality) [A, P]

1. **The same W1 under the other readings.**
   - R1: `Lab(1) ∩ V = {y_7}`, `Lab(2) = ∅`; the `(a, b)` indicator is a function of `V(2)`; C3
     holds; simplex-embeddable (N3.3).
   - R2(ii): `Lab(0) = {x_2, x_7}`; `x_3` reads `x_4(0)`, `y_3(0)` (constant) so `x_3 ∉ Lab(1)`;
     `Lab(2) = ∅`; classical as under R1.
   - R3: labels `y_7(1) = b` and `y_3(2) = a`, the others carry `n`, `m` or `p`; identical to R2(i),
     so a gbit.
   The non-classicality of W1 is produced by the reading: under R2(i) it rests on the two constant
   cells `x_4(0)`, `y_3(0)` being herald-record cells. Nothing in the rule decides it. It is not a
   reading-independent property of R-lin.
2. **`d = 3`.** Embed the chain in `(ℤ/16) × (ℤ/s)²`, `s ≥ 3`, transverse cells designated 0. Tick 1
   and every `y` cell are unchanged; an `x` cell at tick 2 gains `4X_i`: `x_2(2) = n + 5a`,
   `x_7(2) = 5b + m`, the others unchanged. Under R3 the argument of N4 goes through for every `q`
   (`b = y_8 − y_10`; `(n+5a, a−p)` uniform; `n = x_2 − 5y_3` for retention) [A]. Under R2(i), `x_3`
   now also reads its four transverse `x` neighbours, which are not in `V`; the `d = 3` case is not
   settled here.
3. **Site-level observers (Main:292–294).** Site alignment copies every `x_i(τ)` into `y_i(τ+1) ∈ V`,
   so a label-only hold needs a gap of two ticks. **W2** (R3, `d = 1`, ring `ℤ/24`, `T = 3`,
   `t_p = 0`): free `X_0 = n`, `X_2 = a`, `X_10 = b`, `X_14 = m`, all `Y` and every other `X` designated
   0, `V` = sites `{−1, 1, 2, 5, 10, 11, 15}` (both slots). With `y = 0` initially,
   `x_i(t) = Σ_j X_j [|i−j| ≤ t, |i−j| ≡ t mod 2]` (checked by hand for `t ≤ 3`). Then:
   label-free `(n, n+a, m)` at ticks 1 and 2 give `a`, not `b`; at tick 3 label-free `(n+a, n+a,
   n+a, b+m, m)` give `b`, not `a`; `a` at tick 3 is only in the R3 label `x_5(3) = a`; full
   retention holds at every tick (`V(3)`: `a = x_5`, `n = x_{−1} − a`, `b = y_10`, `m = x_15`). Same gbit
   under R3 [A, P]. Under R1, `x_5(3)` is label-free and the fragment is classical; under R2(i) no
   cell of `V` is a label at tick 2 or 3 and the fragment is classical.
4. **Convention artefact test (OA3:445–455).** OA-3 discards a gbit present already for trivial
   dynamics. W1's gbit needs R-lin's additive masking: under permutation dynamics R2 coincides with
   R1, and R3 leaves no herald content in label-free cells. So the test as stated does not
   discard W1. The decisive observation is item 1: the same instance is classical under R1 and
   R2(ii).

Verdict: W1 stands as an in-class witness under R2(i) and R3, with the reading attached; it is not a
witness at the frozen scope.

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
| R1 | yes | (B), all of §1.1's scope | N2 |
| R2(i) | yes | (A), W1, `d = 1`; `d = 3` unsettled | N4 |
| R2(ii) | yes | (C), N6 gap | N6 |
| R3 (P0N variant) | no (fails two precedents) | (A), W1 (`d = 1, 3`), W2 (site level) | N5 |

The precedent-consistent readings disagree on W1 itself. By §2 the class-level verdict is (C).

***

## 4. Verdict

**(C) at the frozen scope, with no dynamical gap left under R1 or R2(i).**

- Under R1 (exact-move provenance), label-cell-only retention cannot occur for R-lin with (xiii):
  label status survives at most one tick past the use time (N1, N2). (LF) and C3 hold for the class.
- Under R2(i) (structural domain of dependence, all of `V(t_p)` labelled), W1 is an R-lin instance of
  the class with label-cell-only retention and lost common effects, and the fragment is a gbit (N4).
- Under R2(ii) the question is open (N6).
- The remaining gap is the delimitation itself: which cells of `V(τ)`, `τ > t_p`, C-PM counts as
  preparation labels when records are held in `V` (SY:201–202, MM-2 item 3). The frozen texts and
  P0's precedents do not fix it, and R1 and R2(i) both agree with every precedent while giving
  opposite verdicts on W1.
- Decisive node: N5 item 1 (W1 under R1, R2(i), R2(ii) and R3), resting on N1.

***

## 5. Consequences for C4 and P0

**C4, preparation side (§A.34, one direction at a time).**
- (⇐) Equal coset-weight vectors ⇒ operationally equivalent: holds for every instance and reading,
  since a preparation's law of the record is fixed by its coset weights (P0 N1, N4) [P, R-off].
- (⇒) Operationally equivalent ⇒ equal coset-weight vectors: needs C3. Established under R1 for the
  class (N2 with P0 N6). Fails in W1 under R2(i) and R3 (`½([00]+[11]) ∼ ½([01]+[10])` with different
  weights). Open under R2(ii).

**C4, measurement side.** Both directions hold without (LF), from C1–C2 (P0:280–281) [P, R-off].

**Simplex embedding.** Under R1: (LF) for the class ⇒ simplex-embeddable (one direction; the
converse is not claimed; transformation noncontextuality not claimed).

**P0.** P0 stays **O-U**. Its unresolved check (P0:424–427) is now located: C3 for R-lin turns on the
label delimitation and on nothing else in the rule except N1. Conditional bearings, neither adopted:
- if the owner fixes R1 and the result survives independent review, the C3 and C4 checks pass for
  the class, P0's pass condition (P0:67–71) is met with C1–C2 (P0 N1, N4), subject to P4, and the
  ordering rule (R8:313–316) hands Q4 to AW-OA2-1;
- if the owner fixes R2(i), W1 is an in-class contextual counterexample, which P0:74–76 permits in
  place of O-U; whether a reading-produced gbit counts (compare OA3:445–455) is a separate decision.

Nothing here changes a status, priority or premise.

***

## 6. Support for each claim

| Claim | Layer | Hypotheses |
|---|---|---|
| R-lin's only exact move is `x_i → y_i`, one tick (N1) | [A] | (xiii), R-lin `F`, (H3), scope §1.1 |
| Under R1, `Lab(τ) = ∅` for `τ ≥ t_p+2`; (LF) and C3 for the class (N2) | [P] | R1, L reading, H-AR, (H3), the class |
| Simplex embedding under R1 (N2 consequence) | [P] on P0 N1–N6 [R-off] | as above, H-xiv, `D_0`, one direction |
| W1 and W2 cell tables and full retention | [A] | stated instances |
| W1 gbit under R2(i), R3; W2 gbit under R3 | [P] via OA-2 Claim 2 [R] | the reading named |
| W1 classical under R1, R2(ii) | [A] + P0 N6 [R-off] | the reading named |
| R2(ii) open; one geometry fails | [P] | as stated in N6 |
| Precedent table of §1.6 | [P], re-checked by hand on P0 [R-off] | — |
| [L] Schmid et al., PRX Quantum 2, 010331 (2021), via P0 | [L] | context only |

No [K] support is involved.

***

## 7. §A.31 classification and assumption-watch

- **NEW.** C-PM is undefined after the use time when records are held in `V`, and for R-lin the C3
  verdict is fixed by that definition: the same in-class instance is classical under one
  precedent-consistent reading and a gbit under another (N5).
- **NEW (structural, R1).** Second-order rules under (H3) confine exact copies to one tick (N1);
  multi-tick label registers of the N8.2(b) kind do not exist in R-lin.
- **ELABORATING.** (LF) for the class under R1; W1 as the multi-tick control P0 lacked.
- **AW-C3-1 (record-only).** Every in-`V` C-PM argument in the affine class depends on a label
  delimitation after the use time: P0 N5, N8.2(b) (a gbit under R1, R2; trivial under R3), OA-2 E(b)
  step 4 (OA2:534) and OA-3 N4.3 step 4 (OA3:468–469) (AW-P0-2, SY T5). For R-lin with full
  retention and `T ≥ t_p+2`, the singleton-indicator presumption holds under R1 and can fail under
  R2(i) or R3 (W1 has (SP) failing, so it does not bear on E(b)).

***

## 8. Owner questions

1. **Delimitation.** Which cells of `V(τ)`, `τ > t_p`, are preparation labels under C-PM when records
   are held in `V`: R1, R2(i), R2(ii), the functional variant R3, or another rule? This is SY MM-2
   item 3 and decides C3 for R-lin (§4).
2. **Reading-produced contextuality.** If a reading other than R1 is chosen, does a gbit that appears
   under that reading and not under R1 (W1) count as an OBL-SP outcome, or as a convention artefact
   in the sense of OA3:445–455?
3. **Observer granularity.** Are H-AR cells slots (P0's instances) or sites (Main:292–294)? W2 covers
   R3 at site level; R2(i) at site level and in `d = 3` is not settled.
4. **Rule class.** This record follows P0 and review 5892912758 in reading OBL-SP's class as R-lin with
   (xiii). Under R1 the N8.2(b) conveyor is an affine gbit, so a reading of the class as all of ledger
   (vii) would change P0's outcome. Confirm the R-lin reading.

***

## 9. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| P0 (`REC-1-P0-r3.md`, blob `611a4d9a`) at `2a9f10ba`, branch `research/rec-1-1169-20261113`, draft PR #1268: C1–C4, (LF), N1–N6, Instances I and II, N8.2(b), the outcome rule | §1.4–1.6, N2–N5, §5 | Support off `main` (definitions, the scoped result under (LF), the precedents): a gap until landed |
| P0R (`REC-1-P0-REVIEW-r1.md`, blob `ec5178ca`) at `2a9f10ba`: the N8.2(b) label evaluation (P0R:135–144) | §1.6 | Support off `main` for one precedent row: a gap until landed; the row is re-checked by hand here |
| P0N (`REC-1-P0-NOTES-r2.md`, blob `1cd2e3fa`) at `2a9f10ba`: the functional variant (P0N:36–38), tick-5 labels (P0N:22–24) | §1.6, R3 | Support off `main` for the definition of R3's source and one precedent detail: a gap until landed |
| P0C (`REC-1-P0-CONFIRM-r3.md`, blob `8b440f2d`) at `2a9f10ba` | read for context | Provenance |
| R8 (`REC-1-r8.md`, blob `615b7de8`) at `2a9f10ba`: OBL-SP's statement (R8:255–268), the L reading (R8:297–303), the ordering rule (R8:313–316) | §1.2, §5 | Support off `main` (class definition and reading): a gap until landed; the L decision itself is #1268 c.6860582570 as relayed in R8 |
| SY (`SYNTHESIS-r3.md`, blob `e6829509`) at `9eeee392`, branch `research/synthesis-1169-20261113`, PR #1276: MM-2 item 3 (SY:201–202), T5 | §1.6, §7, §8 | Provenance (placement of the check; no step rests on it) |
| ChatGPT review 5892912758 on #1268 | header, §1.2 | Provenance (origin of the obligation; the rule-class reading it states is also P0's, P0:350–352) |
| #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z) | header | Governance provenance, fetched and quoted |
| #1268 c.6860582570 (owner, as relayed in R8:14–18) | §1.2 | Governance provenance, not fetched |
| Main, OA1, OA2, OA3, P at `c3b5f37a` | throughout | Support on `main` ([R]; Main as manuscript) |
| [L] Schmid et al. 2021 | §6 | External literature, context only |
