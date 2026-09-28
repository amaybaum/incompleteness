# Track B act 38 — a genuine non-Diţă local escape at the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #765. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A38.json`, and on the pull request.

- **`D`** — `5949740297034d0ddc522aff9577bd1fa36fe42f`, the head of `main` after the landing of
  act 37's #764.
- **`F`** — `47f1694fd8455ef58d735044d603360e3e02321d`, the child of `D` that adds the
  preregistration alone, blob `9c385e8363ee8d4ea4796fa71b15c66ef540ec15`. `F`'s `check-run`
  attestation is run 36399875682; the owner's designation is comment 5866714226 on #765.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A38-NON-DITA-WITNESS-PROVED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A38` | `A38-NON-DITA-WITNESS-PROVED`, theorem `a38_witness` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a38_c_exclusive` and the twelve statements required under this label:
- `A38-1`: `a38_shared_realizable`;
- `A38-2`: `a38_shared_excl_k1`, `a38_shared_excl_k2`, `a38_shared_excl_k3`, `a38_shared_excl_k4`,
  `a38_shared_excl_e1`, `a38_shared_excl_e2`, `a38_shared_excl_t1`, `a38_shared_excl_t2` and
  `a38_shared_excl_t3`;
- `A38-3`: `a38_c_local_escape`;
- the control `a38_control_base`.

***

## The frozen post-round sentence

> At the frozen product configuration, the local-escape package holds, at evidence level 2: for the explicit exponent matrix `E = A + B + C` on the sixteen-point carrier and the arc `Hu u = SIG ∘ u^E` through the certified rational stratum point, `Hu u` is a flat unitary — a complex Hadamard matrix, realizable — at every unit `u`; and for each of the nine Diţă factorization classes of the stratum point — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; so, as the corollary, every neighbourhood of `SIG` contains a realizable matrix admitting none of the eighteen forms. Beside the package, required under both decided labels: the base point `Hu 1 = SIG` carries the Kronecker `4 × 4` factorization with flat unitary factors. By the round's exact-computation probe, and not by the kernel: at a generic `u` no index maps whatever pass the proportionality test in either orientation; every unit at which any structure could be admitted lies in an explicitly named candidate set of forty points; the exhaustive search at each of them finds a Diţă structure at `u = 1` and at `u = −1` only, and the same up to diagonal equivalence; so the exceptional set is exactly `{1, −1}`, and for every unit `u ∉ {1, −1}` the arc point `Hu u` admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences. The local Diţă hulls of the stratum point's factorizations do not exhaust the realizable geometry near `SIG`: realizable points in no such hull lie arbitrarily close to it. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `Hu u = SIG ∘ u^E` is the witness arc with
`E = A + B + C` in closed form on the product index, `SIG = F₄(z) ⊗ F₄(w)` the certified rational
stratum point, `dg X Y D` Diţă's column construction `(a,b),(c,d) ↦ X[a,c]·D[c,b]·Y_c[b,d]`,
`flg X` flatness of a unitary on a finite type, `dita28` act 36's `2 × 8` form at the frozen index
maps, and `dita…` the form of each of the eight other classes at its own index maps, act 37's lookup
tables carried verbatim inside the statements.

**`A38-1`, `a38_shared_realizable`.** With `z`, `w` and `u` symbolic units, `star x = x⁻¹` for each
(`a38_shared_inv_of_unit`). For each of the sixteen rows `(a, b)`, the entry `((a,b), j)` of
`Hu · (Hu)^*` is a sum of sixteen monomials in `z`, `w`, `u` and their inverses with rational
coefficients and equals `[ (a,b) = j ]`: a sixteen-case split on `j`, `simp` with the product-sum
expansion, the star rewrites and the conjugates of `1/2` and `2`, then `field_simp` and `ring`
(`a38_shared_row_core_00` to `a38_shared_row_core_33`). The unitarity assembles the sixteen rows by
`ext` and a sixteen-case split on the row (`a38_shared_unitary_core`); flatness is act 35's
`a35_shared_half` twice and `‖u‖ = 1` (`a38_shared_flat_core`); the realizable Gram and the feature
vector are act 35's `a35_shared_gram_realizable` (`a38_shared_real_core`), instantiated at `z`, `w`
by act 36's unit lemmas. The identity holds with `z` and `w` symbolic because the witness's level-set
sums vanish monomial by monomial, as the probe checks.

**`A38-2`, the nine exclusions.** For each class, from a Diţă form `Hu u = dita… X Y D`, or
`Hu u = (dita… X Y D)ᵀ`, the four entries at the frozen witness positions factor as
`X a c · D c b · Y c b d` with the class's tables evaluated, and the product of the first two equals
the product of the last two by `ring`, because they pair the same factors: for a proportionality
witness the two rows lie in one class and the two columns in one block; for the rectangle witness
of `e1` in the row form the rows `(a,b), (a',b')` against `(a,b'), (a',b)` sit in one column; in the
row form the roles of rows and columns are exchanged. The same four entries of `Hu u`, evaluated by
`simp` with `decide` on the concrete indices, are `±1/4` times `u^0` or `u^1` with exponent sums
differing by one, so the identity reads `±u/16 = ±1/16`, and `linear_combination` with the frozen
coefficient `±16` closes `u = 1`; for the column form of `t2`, whose four entries are `z/4, 1/4, z/4,
1/4`, the identity reads `(z/16) u = z/16`, `linear_combination (16 : ℂ) * key` gives
`z · (u − 1) = 0`, and `z ≠ 0` by `norm_num` on real and imaginary parts leaves `u = 1`
(`a38_shared_excl_core_k1` to `a38_shared_excl_core_t3`).

**`A38-3`, `a38_c_local_escape`.** For `t > 0` the Cayley point `u = (1 + t i)/(1 − t i)` is a unit,
by conjugating and cancelling; is not `1`, since `1 + t i = 1 − t i` forces `t = 0`; and satisfies
`‖u − 1‖ = 2t / ‖1 − t i‖ ≤ 2t`, since `‖1 − t i‖ ≥ |Re| = 1` (`a38_shared_cayley_core`). With
`t = ε/8`, `‖u − 1‖ ≤ ε/4 < ε`. Entrywise, `Hu u − SIG = SIG ∘ (u^E − 1)`, `‖SIG i j‖ = 1/4` by
`a35_shared_half` twice, `‖u^n − 1‖ ≤ n · ‖u − 1‖` for a unit `u` by induction
(`a38_shared_pow_sub_one`), and `E i j ≤ 3` by `split_ifs` (`a38_shared_ew_le`), so every entry
differs from `SIG`'s by at most `3ε/16 < ε`. Realizability is `A38-1` at `u`; each of the eighteen
negations is the corresponding exclusion at `u` against `u ≠ 1` (`a38_shared_escape_core`).

**The control, `a38_control_base`.** `Hu 1 = SIG` entrywise by `one_pow` and `mul_one`; `F₄(z)` and
`F₄(w)` are flat unitaries by act 35's `a35_shared_f4_flat` and `a35_shared_half`; and `SIG` is the
Kronecker form at the class `k1` with the trivial twist because the two lookup tables of `k1`
return `i.1` and `i.2`, by sixteen-case splits, after which the entry is `F₄(z)[a,c] · 1 · F₄(w)[b,d]`
(`a38_shared_base_core`).

**`a38_witness`** is the conjunction of the ten cores over the frozen head;
**`a38_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries one hundred and twenty-two theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a38_shared_…`, `a38_c_…` other than `a38_c_exclusive`, or
`a38_control_…` consumes a verdict theorem or `a38_c_exclusive`, and `a38_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's to act 37's
modules among them — and it records a helper absent from that list as a deviation against the row
it departs from, not repaired. None. The audit of every identifier consumed by the proofs against the Provenance list finds no landed
declaration outside it: the one hundred and twenty-two theorems consume Mathlib, this round's own shared
lemmas, and listed declarations of acts 35 and 36 only — `a35_shared_f4_flat`, `a35_shared_half`,
`a35_shared_norm_of_unit` and `a35_shared_gram_realizable` from act 35's module, and `a36_shared_z_unit`,
`a36_shared_w_unit`, `a36_shared_div` and `a36_shared_mod` from act 36's, both modules authorized whole.
No theorem of act 37's module is consumed by a proof; its head and lookup tables are carried verbatim in
the statements.

***

## The exact-computation layer

The frozen probe `verification/lean/dita_local_escape_probe.py`, blob
`00be96c384f63efaaa52995d38704428404b0497`, is added at stage 1 and run by its own shard
`Numerical probes / A38 escape`, required by the aggregate `Numerical probes` job. Its run at the
stage commits reports 44 `PASS` and no `FAIL` and ends with the line

```text
dita_local_escape_probe: OK -- along the arc H(u) = SIG o u^E through the certified stratum point, E = A + B + C the frozen exponent matrix: H(u) is a complex Hadamard matrix at every unit u; each of the eighteen census structures is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation
```

These are exact arithmetic replayed, not kernel-certified: the Laurent identity of the arc, all 248
level sets of the 120 row pairs vanishing exactly and monomial by monomial; act 37's census
replayed, the eighteen structures each imposing non-identity conditions all of the form `u^k = 1`,
`k ∈ {−2, −1, 1, 2}`, and each admitted at `u = 1` alone, with its kernel witness identity forced by
its Diţă form; at a generic `u` no block structure passing the proportionality test in either
orientation; the candidate exceptional set of forty exactly named points `ζ z^s w^t`, twenty of
them Gaussian rational; the exhaustive search at each of them — the eighteen structures at `u = 1`,
one `2 × 8` structure per orientation at `u = −1` at index maps outside the census, and nothing
elsewhere, strictly and up to diagonal equivalence — so that **the exact exceptional set is
`{1, −1}`**; the two structures at `u = −1` certified by exact reconstruction from flat unitary
factors and unit twists and found by the numeric search with factor unitarity; and the controls:
the numeric search agreeing at all twenty Gaussian-rational candidates in both orientations, a
genuine deformation inside each of the nine classes found in its class, three stabilizer transports
of `E` straight and admitting nothing generically, a perturbed exponent matrix not straight, the
pieces `A`, `B`, `C` and their pairwise sums straight lines in named census classes while the
triple lies in none, and act 37's `W` in `t1` alone; and the tangent space at `SIG`, of dimension
80 with defect 49, spanned by the eighteen first-order Diţă subspaces of dimensions 36, 46, 36, 36,
44, 44, 57, 57 and 49, the witness tangent and in none of them.

By the probe, and not by the kernel: **for every unit `u ∉ {1, −1}`, the arc point `Hu u` admits no
Diţă structure of any admissible shape, index map or orientation, including up to the allowed
diagonal equivalences; at `u = −1` it admits exactly one `2 × 8` structure per orientation.** With
the kernel's realizability, its eighteen exclusions and its local-escape corollary, the frozen main
statement is earned: `Hu u` is a complex Hadamard matrix for every unit `u`, and for every unit
`u ∉ {1, −1}` it lies in no Diţă hull of any admissible factorization of the sixteen-point carrier.
The local Diţă hulls of the stratum point's factorizations do not exhaust the realizable geometry
near `SIG`: since `u` may approach `1` through units other than `1`, realizable non-Diţă points lie
arbitrarily close to it, which the kernel corollary states for the eighteen census forms and the
probe extends to every index map. That the eighteen first-order subspaces span the whole tangent
space, while the exact union of the Diţă families is locally incomplete, says the obstruction is a
nonlinear compatibility and not a missing tangent direction; this is interpretation, probe-checked
and kernel-free.

**Not claimed**, recorded as such: the number of straight lines through `SIG`, the minimality of
the witness's support, the orbits of witnesses, the three-parameter family `SIG ∘ u₁^A u₂^B u₃^C`,
and the decomposition `E = A + B + C` beyond its use as a control; each is a possible round of its
own.

***

## The `P0` cell and the guard

On `A38-NON-DITA-WITNESS-PROVED` this round's sentence and its standing clause are appended once
after act 37's standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E`
is `480651814998ca4def7978ff81fe3b0cb382b3f1`, the blob rehearsed for this case in the
preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the shard
`probes_a38` inserted and required by the aggregate job, the five frozen edits.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `9c385e8363ee8d4ea4796fa71b15c66ef540ec15`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `1c46a7bcdf2a5fdeb2847712397593c4bc67bde6` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 9 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 64 mutation controls fail as required` and
    `controls: self-test OK`.
  - At stage 1 `controls.py`'s module checks report the corollary that stage 2 adds and the two primed
    helper names recorded under Discrepancies; at the repair commit only the corollary; from stage 2 on,
    none.
- **`C3`:** the probe has blob `00be96c384f63efaaa52995d38704428404b0497` at stage 1; its run is
  green at the stage commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on thirteen receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A38-NON-DITA-WITNESS-PROVED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports `ALL CHECKS PASS` in `D`'s order. That run is evidence
for the executor and not an attestation.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36399875682 | `47f1694fd8455ef58d735044d603360e3e02321d` | `F`: the preregistration alone | all seven jobs green; the release gate passes with thirteen receipts holding; the probe shards run `D`'s lists; `F`'s `check-run` attestation |
| 36400614526 | `64418a8a2392389c043437d02cad969cbce6598d` | stage 1: the controls, the probe in its own shard, the module with its shared and control theorems, the import line | red at exactly one step of the release gate, `lean-manuscript`, one problem: the module has no census family until stage 3, as the frozen plan orders. The `Mathlib bridge` build itself reports no error, `lean-axioms` 4949 named results and no sorry; the kernel check and all five probe shards are green, the A38 shard with the probe's `OK` line. `controls.py check` at this head reports, beside the findings stage 1 expects, the two primed helper names recorded under Discrepancies |
| 36400756752 | `cde1c98d37c2a6c18635e5336d23a727549100a3` | the stage-1 repair: the two primed helpers renamed | red at the same one gate step for the same reason; no Lean error, `lean-axioms` 4949 named results and no sorry; every other job green. `controls.py check` at this head reports only the findings stage 1 expects |
| 36401680413 | `f09d1f0f512a34ee052fdc2f1c163fc23d65c532` | stage 2: the verdict `a38_witness` and the corollary | red at the same one gate step for the same reason; no Lean error, `lean-axioms` 4951 named results and no sorry; every other job green, the probe's `OK` line again. The label read off the module is `A38-NON-DITA-WITNESS-PROVED`, and the module passes every one of `controls.py`'s module checks |
| 36402777894 | `f5640a453b16bfcb9d3eff3722702aa5f6b791a4` | stage 3: the census family and the `P0` sentence | all eight jobs green: the release gate passes all 21 steps with thirteen receipts holding, `lean-axioms` 4951 named results and no sorry, every one of the module's one hundred and twenty-two theorems within `propext`, `Classical.choice` and `Quot.sound`; the census reports every carried family anchored; the probe reports 44 `PASS` and no `FAIL` in 349 seconds and ends with the line carried above — the run at `E`'s predecessor |

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

- **Two helper names at stage 1.** Stage 1 (`64418a8a…`) carried two shared helpers whose names end in a
  prime, `a38_shared_conj_half'` and `a38_shared_conj_two'`; `controls.py`'s module check admits only
  names matching `a38_shared_[A-Za-z0-9_]+` beside the frozen ones and reported both. The design runs
  before `F` compiled the module but did not run `controls.py check` against a design head, so the name
  pattern was first applied at stage 1. The repair commit `cde1c98d…` renames them to
  `a38_shared_conj_half_ring` and `a38_shared_conj_two_ring` at their definitions, their `#print axioms`
  lines and their uses, 196 occurrences, and changes nothing else; it is a proof-implementation repair
  by a later linear commit, as the frozen status rule provides. No frozen statement is touched, and the
  compiled module is the design pass's green module with exactly that rename.
- **The realizability route's granularity.** The route names sixteen row lemmas, one per `(a, b)`,
  assembled into the unitarity by a sixteen-case split on the row. On the second design pass recorded in
  the preregistration's runs table, fifteen of those sixteen row lemmas compiled but the lemma for row
  `(1, 3)` and the sixteen-way assembly timed out at `whnf`; the proof as executed splits each row identity into four lemmas by column block
  (`a38_shared_row_core_ab_c`), assembles the rows from them, the row blocks from the rows
  (`a38_shared_rowblock_core_a`) and all entries from the row blocks (`a38_shared_rows_core`). The
  frozen statement `REAL` is unchanged.
- **The frozen class's index maps.** The exclusion core of `t1` evaluates act 36's `Fin.divNat`,
  `Fin.modNat` and `finProdFinEquiv` on the concrete witness indices with act 36's `a36_shared_div` and
  `a36_shared_mod`, which the route does not name; both lie in act 36's module, authorized whole.
- **The probe's time.** The preregistration gives about 6 to 8 minutes; in CI the probe runs in 349
  seconds of probe time at `E`'s predecessor, and in 485 seconds on the executor's container.

None otherwise against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 38 proves statements about one exact one-parameter arc of realizable classes through act 34's certified
> rational stratum point, given by an explicit exponent matrix, and about the Diţă factorization classes of that
> point, and adopts none of them as anything but mathematics. The classes are mathematical objects, index maps on
> the sixteen-point carrier; the realizability of the arc, the exclusion of the nine classes away from the base
> point and the local escape are facts about those objects and about nothing else. A `NON-DITA-WITNESS-PROVED`
> verdict settles the frozen package, and a `WITNESS-FAILS` verdict exhibits the failure of a named part; the
> exact-computation layer, and not the kernel, carries the exhaustive complement, that no index maps whatever
> admit a Diţă form of an arc point off the two exceptional units, strictly or up to diagonal equivalence; and
> both verdicts leave the product normalized set unclassified. Neither verdict establishes that any admissible
> transition law is covariant under any isometry, selects a physical law or closes `P0`. No hull, family,
> factorization, isometry, carrier, group or principle gains physical status by appearing here, and nothing here
> derives, recognises or approaches quantum evolution.
