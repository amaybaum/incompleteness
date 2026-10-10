# Track B act 42 — the least class support of a non-Diţă straight line in D1: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> {{CLAUSE}}

## The declarations

```v3-round
round A42
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-42-support-minimality/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-42-support-minimality/
record AM verification/receipts/A42.json
execution A verification/lean/a42/
execution A verification/lean/dita_support_minimality_probe.py
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/A42.json`. Every other path the round changes is an execution
path listed above: the twenty-two frozen tool files under `verification/lean/a42/`, the frozen probe that runs them, the
frozen workflow edit, and the frozen `ROADMAP.md` propagation. No manuscript, Lean module, census entry or built artifact
changes. The round has no kernel layer.

## The objects

- **`D`** = `0e87c4a129d91276c10f0438d03c1bcca3a0a3b8`: the head of `main` after act 45's landing,
  `A45-BRIDGE-PROVED`, receipt `verification/receipts/A45.json`; its parents are act 45's base `fa6ddf77` and act 45's
  receipt commit `3900f486`. It is certified by push run 36629048484: thirteen jobs green, the release gate passing
  21 of 21 steps with eighteen receipts holding and the 303 legacy records intact, `lean-axioms` at 5278 named results
  and no sorry. Every measurement here was taken at `D` or, for the design evidence, at act 41's landing `fa6ddf77`,
  with the drift between the two measured below.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only `verification/receipts/A42.json`.

No other round runs beside A42 at this freeze; the stronger fixed-basis and full-equivalence round is not started.
Should one land first, its movement of `main` enters A42 only by reconciliation after `E`, with each row taken from the
round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — three layers, never merged.** The conclusion rests on three kinds of evidence, reported separately wherever
it is cited:
- **exact computation**, replayed in CI: Gaussian-rational arithmetic, exact integer tables, exact rank over the
  rationals, exhaustive enumeration;
- **SAT verdicts** from CaDiCaL 1.5.3 through python-sat 1.9.dev15, **carried without proof logs**: no DRAT or LRAT
  certificate is produced or checked, so an UNSAT verdict is the solver's answer on the frozen encoding and nothing more;
- **the lemmas of the case split**, stated and argued in prose in this file (the section *The argument*), with their
  finite ingredients computed exactly by the probe; the lemmas themselves are not kernel-checked.

There is no Lean layer. No sentence of the result note, the roadmap or any later text may present the SAT verdicts as
certified, or the prose lemmas as kernel-checked.

**Hazard 2 — the domain and the notion.** The conclusion is scoped to **D1**, the classes that have a least-support
representative with entries in `{−1, 0, 1}`, and to **act 41's semantics** of Diţă, relaxed (up to diagonal
equivalence), over every partition structure and every valid alignment. The exhaustive exclusions test membership in
the eighteen subspaces **N18** of the pre-freeze analysis; each is shown equal, by exact rank, to the relaxed identity
subspace of one of act 41's 976 realizing triples, so N18 membership implies Diţă under act 41's semantics. The
passage from a representative to its class uses the invariance of straightness and of Diţă under the class action
(Lemmas G and I below).

**Hazard 3 — scope, unchanged from the design evidence.**
- no claim for the class supports 41 to 43 or 45 to 47;
- no claim outside D1, in particular none that 40 is least over all integer exponent matrices;
- no promotion of the SAT verdicts beyond their evidence level;
- no assertion that the general-integer exclusions of the pre-freeze analysis (every straight line of class support at
  most 19 is Diţă, and at most 23 when a least-support representative has a zero line) were re-proved: their exact
  computational ingredients are recomputed by the probe (`lemmas42.py` L1–L2, `spanAll.py` at 77), and the lemmas that
  would turn them into exclusions are neither re-derived nor claimed.

**Hazard 4 — CI cost, and which runs count.** The exclusion shards take about six CPU-hours between them. They run only
on `workflow_dispatch`; on a push or a pull request the matrix job is skipped, and the aggregate `Numerical probes` job
requires it to be skipped there and green under dispatch. A green pull-request run therefore says nothing about the
exclusions. The dispatch runs at the stage commit and at `E` are the execution's evidence; the dispatch run at exactly
`E` is its `check-run` attestation (§A.39). The two every-run shards (`witness` with `wlog`, and `d01span`) run on every
event.

**Hazard 5 — pinned toolchain.** The A42 shards install `numpy==2.4.6` and `python-sat==1.9.dev15`, whose `Cadical153`
is CaDiCaL 1.5.3. The tables `msize.npy` are rebuilt in each shard and replay-matched against a frozen SHA-256.

**Hazard 6 — history and provenance.** Acts 36 to 41 and 45 stand as recorded. Two disposable research threads are
design evidence only, never evidence of the verdict: the pre-L41 thread (`claude/a42-support-research`, head
`b9ef8b8e`, base act 40's landing) supplied candidates and algorithms; the revalidation thread
(`claude/a42-revalidation`, head `{{RESEARCH_HEAD}}`, base act 41's landing) recomputed every value from act 41's
landing. The tools below are that thread's files, copied byte for byte except for one relocation line in four of them;
their docstrings refer to research notes that are not in the repository, and this file, not those notes, states what
each tool computes and what the round concludes.

***

## Provenance

Consumed, never modified and never re-proved:

- `verification/lean/dita_arc_exclusivity_probe.py` (act 37) — `SIG`, the 1 024-element stabilizer `elems`, and the
  census data of its head, loaded by `lib42.py` up to the line that opens its first section, with no section run;
- `verification/lean/dita_index_map_probe.py` and `verification/lean/dita_index_map_independent.py` (act 41) — each
  executed whole, so that it replays act 41's `measurements.json`, before any of its functions is used (path A and
  path B(ii));
- `verification/programmes/oi-qm/track-b/act-41-index-map-semantics/measurements.json` — act 41's census, compared
  structure by structure (control C1c).

The frozen tools, each added under `verification/lean/a42/` with exactly the blob in the fourth column. The source is
the revalidation thread's head `{{RESEARCH_HEAD}}`; the pre-L41 tools are the ones it carried unchanged in
`research/a42-rerun/`.

| file | source at the research head | source blob | frozen blob | edit | what it computes |
| --- | --- | --- | --- | --- | --- |
{{TOOL_TABLE}}

The relocation edit is the whole of each difference: the research tree placed these files two directories below the
repository root and the frozen tree places them three below, so the one line computing the root gains one `dirname`.

## Locating controls — at `D`

| file at `D` | blob |
| --- | --- |
| `verification/lean/dita_arc_exclusivity_probe.py` | `c64bd86b5f5f856d57a22e4f55e070954b11b51a` |
| `verification/lean/dita_index_map_probe.py` | `d539fe5f660b198aa944e17984718c0d9106f3b5` |
| `verification/lean/dita_index_map_independent.py` | `e7645da5ffec1c21cbdde90763dd1e9e01a14d48` |
| `verification/programmes/oi-qm/track-b/act-41-index-map-semantics/measurements.json` | `f716ce5ff49cd698aff716d39c2cfd213f5c66b1` |
| `verification/ROADMAP.md` | `4e53a3b266d2b63ab1f1aa7728de329298e9fcf9` |
| `.github/workflows/verify.yml` | `876f2e6d15ea30a435c868cc29ed4d0dacf98ae3` |

The names this round introduces return nothing from `git grep -l` at `D`: `act-42`, `A42-`, `dita_support_minimality`,
`probes_a42`, `lean/a42` and `support-minimality`.

**Drift from act 41's landing to `D`.** The design evidence was measured at act 41's landing `fa6ddf77`. The difference
from there to `D` is exactly act 45's governed paths; the four consumed files above, every `verification/lean/dita_*`
file, the records of acts 36 to 41, the Diţă Lean modules, their receipts and the Diţă families of the census are
byte-identical at both commits, and `ROADMAP.md`'s minimal-support section is unchanged (only the `P0` cell gained act
45's sentence). The revalidation therefore stands as design evidence at `D` without a wholesale rerun; the probe
recomputes every value at the stage commit and at `E`.

***

## Why this round exists

Act 38 exhibited a non-Diţă straight line through the certified rational stratum point, `E = A + B + C`, with 48 nonzero
entries in its `{0, 1}` form, and the roadmap has since carried *the minimality of support 48* as open. The pre-L41
thread found a line of support 40, `E40`, and an exhaustive exclusion below 40 in the domain D1; its minimality values
rested on a floating-point integer programme and its Diţă notion predated act 41's correction. The revalidation from act
41's landing recomputed everything exactly under act 41's semantics: `E40` non-Diţă by two independent paths; the class
supports 40 (`E40`), 44 (act 38's witness) and 16 (`A`) by an exact method with a completeness argument; every exclusion
run reproduced; each N18 subspace equal to a realizing triple's relaxed identity subspace. This round freezes that
conclusion in its narrow form, with its computation replayed in CI.

***

## The definitions, FROZEN

- **`SIG`** = `F4(z) ⊗ F4(w)`, `z = (3 + 4i)/5`, `w = (5 + 12i)/13`, index `(a, b) ↦ 4a + b`, as act 37's probe defines it.
- **Straight line.** An integer matrix `E ∈ ℤ^{16×16}` such that `SIG ∘ u^E` is complex Hadamard for every unit `u`.
  Equivalently, for every row pair `(i, i′)` and every integer `d`, `Σ_{k : E_ik − E_i′k = d} SIG_ik · conj(SIG_i′k) = 0`:
  every level set of every row difference vanishes.
- **The class action `G`**, generated by the gauge `E ↦ E + α1ᵀ + 1βᵀ` (`α, β ∈ ℤ¹⁶`); the 1 024 elements of act 36's
  stabilizer of `SIG`, acting as signed position permutations `(σE)[p(t)] = s·E[t]`; and the sign `E ↦ −E`.
- **Class support** `s(E)`: the least number of nonzero entries over the `G`-orbit of `E`. A representative attaining it
  is a **least-support representative**.
- **D1**: the classes having a least-support representative with entries in `{−1, 0, 1}`.
- **Diţă, act 41's semantics.** A partition structure of `SIG` (orientation, shape, column blocks, row classes) with a
  valid alignment is a *realizing triple*; there are 976, over 20 partition structures. A straight line is **Diţă** when
  for some realizing triple the relaxed identity equations — the triple's Diţă form up to diagonal equivalence — hold
  for every unit `u`, and **non-Diţă** otherwise.
- **N18**: the eighteen relaxed census subspaces of the pre-freeze analysis (nine structures in column and row form),
  as `lib42.py` builds them.
- **`E40`** `[(a,b),(c,d)] = −[b = 0][c = 0] + [a = 2][b odd][d even] − [a even][c odd][d = 0]` `= −P + Q − T`, with `P`
  (`4 × 4`), `Q` (`2 × 8`) and `T` (`8 × 2`) straight rectangles of support 16 that cancel on four cells; act 38's `A`,
  `B`, `C` as `lib42.py` defines them.

## The argument, FROZEN — what the conclusion rests on

**Upper bound.** `E40` is straight (exact, two methods), has entries `{−1, 0, 1}` and 40 nonzero entries, has class
support exactly 40 (exact enumeration with its completeness argument), and is non-Diţă under act 41's semantics (path A,
the landed production machinery; path B, an independent enumeration of every realizing triple and the landed
independent census at exact points of its arc). It is its own least-support representative, so its class lies in D1.

**Lower bound: no class of D1 with `s ≤ 39` is non-Diţă.** Let `E` be straight with its class in D1 and `s(E) ≤ 39`,
and `M` a least-support representative with entries in `{−1, 0, 1}`. The following lemmas are stated and argued here;
each names the exact computation that checks its finite ingredient.

- **Lemma G (straightness is a class property).** The gauge multiplies `SIG ∘ u^E` by diagonal unitaries on both sides;
  each stabilizer element fixes `SIG` up to dephasing (and conjugation when `s = −1`); the sign replaces `u` by `ū`.
  *Ingredient:* `lemmas42.py` L3 on all 1 024 elements.
- **Lemma I (Diţă is a class property).** Diagonal equivalence is absorbed by the relaxed notion; the sign maps an
  identity in `u` to one in `ū`; a stabilizer element permutes rows and columns (W3), possibly transposing, and fixes
  `SIG` up to dephasing, so it carries a realizing triple holding identically to a partition structure with a valid
  alignment at `SIG` holding identically — which is again one of the 976, since act 41's census enumerates every
  partition structure in both orientations. *Ingredients:* W3, `lemmas42.py` L3, control C3 (the relaxed equations
  annihilate the gauge generators).
- **Lemma Z (mode 0).** In `M`, 0 is a most frequent value of every row and column; otherwise subtracting that line's
  most frequent value, a gauge move, lowers the support.
- **Lemma M.** Let `m` be the least support of a row or column of `M`. If `m ≥ 3` every row has at least three nonzero
  entries and `s ≥ 48`; so `m ∈ {0, 1, 2}`.
- **Lemma T (transposition).** `SIG` is symmetric (W5), so `Mᵀ` is straight, of the same support, in `{−1, 0, 1}`; act
  41's census contains both orientations, so `M` is Diţă exactly when `Mᵀ` is.
- **Lemma CV (common vanishing) and LB.** If `z` is a zero row of `M`, every level set of row `i` is a level set of
  `M_i − M_z` and so vanishes for the pair `(i, z)`. Hence each nonzero row `i` has at least `msize(i, Z)` nonzero entries,
  where `Z` is the zero-row set, and `|supp M| ≥ LB(R) = Σ_{i ∈ R} msize(i, Z)` over the nonzero-row set `R`.
  *Ingredient:* `cvsize.py`, replay-matched by SHA-256.
- **Lemma R1.** `M` does not have exactly one nonzero row: against fifteen zero rows the only vanishing column set of
  that row is the whole row (W2), so the row is constant, a gauge move removes it, and `s(E) = 0`, contradicting that the
  row is nonzero in a least-support representative.
- **Lemma NS (subtree pruning).** At a node of the DFS, if for some N18 subspace every free row's candidates contribute
  the same vector to the subspace's equations and the fixed part plus these contributions is zero, every leaf below lies
  in that subspace; skipping the subtree loses no leaf outside N18. Sound by linearity.
- **Lemma W (the reductions of the SAT cases).** Every stabilizer element maps lines to lines (W3), preserves entries in
  `{−1, 0, 1}`, support, line supports and mode 0; the row-preserving elements act transitively on the rows (W4). So a
  zero row, or a line of least support `m`, may be taken to be row 0, and row 0 may be taken to be a representative of
  its orbit under the 32-element row-0 stabilizer and sign. Only existence is asked in the SAT cases, so only Lemma G is
  needed there, not Lemma I.
- **Lemma VS (the encoding).** Each level-set vanishing condition is encoded through the exact pair structure of the
  row pair: antipodally balanced sets, and for the exceptional pairs one of the exceptional vanishing sets. *Ingredients:*
  `lemmas42.py` L1 (minimal vanishing sets of sizes 2 and 6 only); W6, agreement of the encoding with the exact test on
  92 matrices, 23 straight and 69 not.

**The case split.**
1. `m = 0`, and by Lemma T a zero row. By Lemma R1, `|R| ≥ 2`; by LB, `LB(R) ≤ 39`.
   - `|R| ≤ 13`: the DFS (`dfsR2.py`, no symmetry reduction) over every one of the 5 494 row sets with
     `2 ≤ |R| ≤ 13` and `LB(R) ≤ 39` (W1: the list is exactly that set), enumerating every `{−1, 0, 1}` matrix with that
     zero-row set, mode 0, straight, support at most 39, less the subtrees Lemma NS prunes. Every leaf lies in N18.
   - `|R| ≥ 14`: if the number of nonzero columns is at most 13, `Mᵀ` has a zero row and at most 13 nonzero rows and is
     covered above; otherwise `sat_hr.py` (row 0 zero, at least 14 nonzero rows and 14 nonzero columns, mode 0, support
     at most 39) is **UNSAT**. W1 counts 104 row sets in this case with `LB ≤ 39`.
2. `m ∈ {1, 2}`, no zero line: 26 SAT cubes (row 0 a line of support `m`, fixed to each orbit representative; every line
   of support at least `m`; mode 0; support at most 39): 2 cubes for `m = 1`, 24 for `m = 2`, each **UNSAT**.
3. `m ≥ 3`: excluded by Lemma M.

By the n18 shards, each N18 subspace equals the relaxed identity subspace of exactly one realizing triple, at its
partition structure's sorted alignment; so every DFS leaf is Diţă under act 41's semantics, and by Lemma I so is its
class. Every case is therefore excluded, and with the upper bound the least class support of a non-Diţă straight line in
D1 is 40.

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_support_minimality_probe.py`, blob **`{{PROBE_BLOB}}`**, is written before `F` and added by the
execution with exactly this blob. It runs the frozen tools with `verification/lean/a42/` as working directory, parses
their output and asserts every value frozen below; it exits 1 on any mismatch. One part per CI shard, each ending with
its summary line:

| part | shard | what it runs and asserts | checks |
| --- | --- | --- | --- |
| `witness` | `A42 witness`, every event | `r3_run.py`: exact class supports `E40` 40, act 38's witness 44, `A` 16, with representatives (`E40` itself, entries `{−1, 0, 1}`; act 38's witness at support 44, entries `{−2, …, 1}`). `r2b_independent.py`: 20 partition structures and 976 triples equal to act 41's census in both notions (C1c), 18 at the sorted alignment (C5), gauge annihilated (C3), `E40`, gauged `E40` and act 38's witness in 0 triples, `A` 596, `B` 272, `C` 576, `P` 272, `Q` 596, `T` 596, `−P+Q` 128, `−P−T` 128, `Q−T` 256 (C2). `c6_control.py`: 150 instances, 146 equal at box 4, the 4 gaps closed at box 8, the exact method never above brute force (C6). `msize.npy` replay. `lemmas42.py` L1–L4 on `A`, `B`, `C` and act 38's witness. `ctrl16.py`: 896 leaves at budget 16, all in N18, with `A`, `B`, `C`, `−A` among them | {{N:witness}} |
| `wlog` | `A42 witness`, every event | W1–W7 of the controls table below | {{N:wlog}} |
| `d01span` | `A42 census01`, every event | `dfs01.py`: `{0, 1}` with a zero row, budget 47: 12 520 leaves, supports 16 (176) and 32 (12 344), all in N18; every row of support at least 2, budget 32: 288 leaves, support 32, all in N18; Lemma P on all 12 808 leaves (`lemmas42.py`); `spanAll.py` at 77: 65 390 row sets, 13 922 dead, least live `LB` 24, every row set with `LB < 24` dead | {{N:d01span}} |
| `paths` | exclusion, dispatch only | `r2a_landed.py` after the landed production probe replays (C0): `E40 = −P+Q−T`, entries `{−1, 0, 1}`, support 40, straight by levels and at exact points (R1); one entry changed fails both (C5); 28 candidates, no structure identically, exceptional sets `{1}` strict and `{1, −1}` relaxed, 20 structures and 976 alignments at `u = 1`, 4 structures and 272 alignments at `u = −1` relaxed only; act 38's arc reproduces act 41 (C1b); gauged `E40` the same (C3). `r2b2_census.py` after the landed independent probe replays (C0): the census empty at `(3+4i)/5`, `(5+12i)/13`, `(8+15i)/17` and `i`, 20/976 at `u = 1` in both notions, 4/272 at `u = −1` relaxed only | {{N:paths}} |
| `r5` | exclusion, dispatch only | `r5_family.py`: 128 members, all straight, exact, in 0 triples; class supports 40 for 16 and 44 for 48 members of each family | {{N:r5}} |
| `n18:K`, `K ∈ {0, 1, 2}` | exclusion, dispatch only | the N18 subspaces `STRUCTS[K::3]`: each, by exact rational rank, equal to the relaxed identity subspace of exactly one realizing triple of `triples.py`, at its sorted alignment | {{N:n18:0}} each |
| `dfs:K`, `K ∈ {0, …, 5}` | exclusion, dispatch only | `dfsR2.py` on the row sets `Rle13_39[K::6]` (916, 916, 916, 916, 915, 915) at budget 39: 0 leaves outside N18; (nodes, pruned) = (151 625, 18 685), (471 631, 46 227), (281 624, 24 040), (428 775, 44 974), (722 178, 72 305), (277 373, 22 143), totals 2 333 206 and 228 374 | {{N:dfs:0}} each |
| `sathr` | exclusion, dispatch only | `sat_hr.py 39`: 270 792 clauses, UNSAT | {{N:sathr}} |
| `cubes:K`, `K ∈ {0, 1, 2}` | exclusion, dispatch only | the 26 cubes (row-0 stabilizer 32; 2 for `m = 1`, 24 for `m = 2`), those of index `≡ K (mod 3)`, each UNSAT | {{N:cubes:0}}, {{N:cubes:1}}, {{N:cubes:2}} |

The loops of the `n18`, `dfs` and `cubes` parts are the probe's own sharded restatements of the revalidation thread's
`n18_in_a41.py`, of `dfsR2.py`'s command-line loop and of `sat_cubes.py`, calling the same frozen functions on the same
inputs; the frozen node counts and verdicts are the ones those scripts gave, which the shards must reproduce.

The `d01span` part is recorded context and not a premise of the conclusion. It shows why act 38's `{0, 1}` domain saw
nothing below 48 (by Lemma P a `{0, 1}` straight line has support `16 · rank(SIG ∘ E)`, and every `{0, 1}` line of
support 16 or 32 the two searches reach lies in N18), and it recomputes the exact ingredients of the general-integer
bounds of the pre-freeze analysis (`spanAll.py` at 77), which Hazard 3 keeps unclaimed.

The summary lines on success, which the result note carries verbatim from the run at `E`:

```text
{{PART_LINES}}
```

A failing part prints `dita_support_minimality_probe <part>: FAILED …` instead.

***

## The question, FROZEN — one target

### `A42` — the least class support of a non-Diţă straight line in D1

**Within D1, is the least class support of a non-Diţă straight line exactly 40? The frozen answer is yes, by the
argument above, with every part of the probe green at `E`.**

## The controls

| id | control | pass condition | where |
| --- | --- | --- | --- |
| C0 | the two landed act 41 probes, executed whole | each ends `OK -- REPLAYED` | `paths` |
| C1 | path A at `u = 1` on `E40`'s arc | 20 structures, 976 alignments, strict and relaxed | `paths` |
| C1b | path A on act 38's arc | act 41's exceptional sets and `u = −1` values | `paths` |
| C1c | path B(i)'s enumeration | 20 structures, 976 triples, per-structure counts equal to act 41's, both notions | `witness` |
| C2 | known Diţă lines accepted | `A`, `B`, `C`, `P`, `Q`, `T` and the pairwise sums in some triples, with frozen counts | `witness` |
| C3 | gauge | the relaxed equations annihilate the gauge generators; gauged `E40` gives the same results | `witness`, `paths` |
| C5 | exactness countercontrols | `E40` with one entry changed fails both straightness methods; the sorted-alignment restriction gives 18 | `paths`, `witness` |
| C6 | the class-support method | agreement with brute force on 150 instances as frozen; never above it | `witness` |
| ctrl16 | the D1 search sees known lines | budget 16, every row set: 896 leaves, all in N18, `A`, `B`, `C`, `−A` present | `witness` |
| W1 | the DFS row sets | the frozen list is exactly the row sets of 2 to 13 rows with `LB(R) ≤ 39` (5 494); 104 row sets of 14 or 15 rows with `LB(R) ≤ 39` | `wlog` |
| W2 | Lemma R1's ingredient | against fifteen zero rows the least vanishing column set of every row is 16 | `wlog` |
| W3 | Lemmas I and W | every stabilizer element maps lines to lines; 512 of 1 024 transpose | `wlog` |
| W4 | Lemma W | the row-preserving elements are transitive on rows; the row-0 stabilizer has 32 elements | `wlog` |
| W5 | Lemma T | `SIG` symmetric, exactly | `wlog` |
| W6 | Lemma VS | the SAT straightness encoding agrees with `straight_direct` on 92 matrices, 23 straight and 69 not | `wlog` |
| W7 | Lemma Z on the witness | `E40` has entries `{−1, 0, 1}`, support 40, and 0 a most frequent value of every line | `wlog` |
| msize | replay | `msize.npy` rebuilt with SHA-256 `5ac7c84aa7506a2741fe8a81cba28a607472cc9357344216c2f6eaa56ce0787d` | every part that uses it |

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A42` | `A42-D1-MINIMUM-40` | **very high** | every value frozen here was reproduced by the revalidation from act 41's landing and by the probe's parts run locally at the predicted tree; the drift to `D` touches none of the inputs |

A prediction that misses is recorded as missed.

***

## The outcome, with its FROZEN post-round sentence

### `A42-D1-MINIMUM-40`

> {{SENTENCE}}

**The rule.** The label is `A42-D1-MINIMUM-40` exactly when the dispatch run at `E` has every A42 shard green — the two
every-run shards and all fifteen exclusion shards — each with its frozen summary line, and the aggregate `Numerical
probes` job green. There is no second decided label: a red part at `E` means a frozen value was not reproduced, which is
a failure of the freeze, not a different mathematical answer; the round then halts under the specification's `S12`, its
result note naming the part, the check and what would settle it, and no minimality statement is made. A job that dies
before the probe starts (checkout, installation, runner loss) may be re-run once; a failing check is never re-run.

The result note carries exactly one line `**Outcome:** \`A42-D1-MINIMUM-40\``, the sentence above, the clause at its
mention `**THE CLAUSE, carried at this mention — the result.**`, the eighteen summary lines, and the probe's blob.

***

## The roadmap propagation, FROZEN — on `A42-D1-MINIMUM-40` only

`verification/ROADMAP.md` changes by exactly four replacements of `D`'s text; `controls.py` embeds each and checks the
file at `E` against them. The first two correct in place the three clauses of the `P0` cell that carry *the minimality
of support 48* as open; the third appends the round's sentence to the cell; the fourth rewrites the body of the
minimal-support section to the current state.

{{ROAD_BLOCKS}}

**The propagation audit (§A.25).** At `D`, *support 48* and its paraphrases occur in the `P0` cell (three clauses), in
the minimal-support section, and in the census notes of the act 39 and act 40 families, which say that those modules
claim nothing about the minimality of support 48. The census notes describe what those modules claim, which remains
true, and are not changed. No paper, chapter or `FULL` file carries a support-minimality statement at `D`, so no
manuscript or built artifact changes.

***

## What no outcome licenses

- **No claim outside D1**, and none that 40 is least over all integer exponent matrices.
- **No claim about the class supports 41 to 43 or 45 to 47.**
- **No presentation of a SAT verdict as certified**, and none of the case split's lemmas as kernel-checked.
- **No assertion that the general-integer exclusions of the pre-freeze analysis were re-proved.**
- **No revision of any earlier verdict**; act 38's witness keeps its recorded support 48 in its `{0, 1}` form, and its
  class support 44 is a separate statement.
- **No adoption** of any line, family or support value as a physical symmetry, principle or law; `P0` stays `OPEN`.

## Non-doings

This round does not do any of the following:
- add or change a Lean module, a census entry, a manuscript or a built artifact;
- change any tool beyond the four frozen relocation lines, or add any tool not listed;
- change the workflow beyond the frozen edit;
- edit any closed round's record;
- start the fixed-basis or full-equivalence round.

## Evidence level

**Exact computation, replayed in CI**, for every value the probe asserts; **SAT verdicts without proof logs** for the
two SAT cases; **stated prose lemmas** for the case split. No kernel layer.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-42-support-minimality/controls.py`, blob **`{{CTRL_BLOB}}`**, is written
before `F` and added by the execution with exactly this blob. It imports nothing from the repository and changes
nothing; it reads `D` and the commit under check through `git`; it embeds every frozen text it compares against.

`controls.py check <commit> [--freeze F]` fails unless all of the following hold:
- **the tools**: the files under `verification/lean/a42/` are exactly the twenty-two frozen ones, each with its frozen
  blob; **the probe** has its frozen blob;
- **the workflow** is `D`'s with the frozen edit; **`ROADMAP.md`** is `D`'s with the four frozen replacements, each
  anchor found exactly as often as frozen;
- **the result note**: the outcome line once; the sentence once; the clause after its mention; each of the eighteen
  summary lines exactly once; no `FAILED` summary line; the probe's blob in backticks;
- **the paths** changed from `D` are exactly the governed ones; with `--freeze F`, `F` is `D` plus this file alone and
  this file is unchanged at the commit.

`controls.py --self-test` checks its constants against this file (the sentence, the clause, the four roadmap
replacements, every tool blob, the probe blob and every summary line); builds a synthetic execution and requires it to
hold; and applies twenty-two mutation controls, each of which must fail with its named code. Run at `D` beside this
file, it prints:

```text
controls: the frozen constants match the preregistration beside this file
controls: the synthetic execution holds as frozen
controls: 22 mutation controls fail as required
controls: self-test OK
```

***

## Pre-freeze evidence — design evidence, not attestation

| evidence | what | result |
| --- | --- | --- |
| the revalidation thread, head `{{RESEARCH_HEAD}}` | R1–R5 and controls C0–C6 from act 41's landing, every pre-L41 exclusion rerun | every value frozen here |
| local runs of the probe at the predicted tree | every part except the six `dfs` parts, whose per-row-set node and pruning counts were spot-checked on 12 row sets against the rerun logs | every part run `OK` with its frozen check count; the 12 row sets equal |
| run 36635398265 at `51bec3d5` on `claude/a42-predicted`, cancelled | the first predicted tree | `dfs:4` red at import: `dfsR.py` reads its command-line argument at import time; the probe now sets it to the rerun's `39` before importing, and the run was cancelled |

{{PRED}}

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear commits from `F`, each
with one parent:

1. **Stage 1 — the computation.** `controls.py` with its frozen blob; the twenty-two tools with their frozen blobs; the
   probe with its frozen blob; the frozen workflow edit. The workflow is dispatched on the stage commit, and every A42
   shard must be green.
2. **The result note and the roadmap** — `result.md` and the four frozen `ROADMAP.md` replacements; this commit is `E`.
   The note carries the eighteen summary lines from the dispatch run at stage 1; the dispatch run at `E` confirms them.

A stage whose run is red is not repaired by changing a frozen file: see the status rule.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the tools and the probe are the frozen ones | `C3`: `controls.py check E` (tool set and blobs, probe blob) |
| every frozen value is reproduced, exclusions included | `C4`: the dispatch run at `E`, every A42 shard green with its summary line, the aggregate green |
| the exclusion shards are skipped off dispatch and required on it | `C5`: the aggregate job's event test, visible in any push or pull-request run as `a42_exclusion=skipped` |
| the native receipts and the legacy records hold | `C6`: the release gate's `v3-receipts` and `legacy-records` steps at every stage commit and at `Q` |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the frozen surfaces, the note and the paths | `C9`: `controls.py check E --freeze F` prints `controls: check OK` |
| the round is protocol-valid | `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |

### The status rule for the round

The label is the measurement, read off the dispatch run at `E`. If `C1` fails the round does not begin. A red A42 part
at stage 1 or at `E`, other than a job that died before the probe started, is a freeze failure: it is not repaired by
changing a tool, the probe, a frozen value or the target, and the round halts under the specification's `S12` with the
result note naming the part and the check. A round that cannot otherwise reach a green `E` also halts under `S12`.
