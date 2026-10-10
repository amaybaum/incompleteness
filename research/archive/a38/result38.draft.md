# Track B act 38 — a genuine non-Diţă local escape at the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #@@PR@@. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A38.json`, and on the pull request.

- **`D`** — `5949740297034d0ddc522aff9577bd1fa36fe42f`, the head of `main` after the landing of
  act 37's #764.
- **`F`** — `@@F@@`, the child of `D` that adds the
  preregistration alone, blob `@@PREREG_BLOB@@`. `F`'s `check-run`
  attestation is run @@F_RUN@@; the owner's designation is comment @@F_COMMENT@@ on #@@PR@@.
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

> @@SENTENCE@@

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

**Zero definitions.** The module carries @@NTHM@@ theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a38_shared_…`, `a38_c_…` other than `a38_c_exclusive`, or
`a38_control_…` consumes a verdict theorem or `a38_c_exclusive`, and `a38_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's to act 37's
modules among them — and it records a helper absent from that list as a deviation against the row
it departs from, not repaired. @@DEVIATIONS@@

***

## The exact-computation layer

The frozen probe `verification/lean/dita_local_escape_probe.py`, blob
`@@PROBE_BLOB@@`, is added at stage 1 and run by its own shard
`Numerical probes / A38 escape`, required by the aggregate `Numerical probes` job. Its run at the
stage commits reports @@NPASS@@ `PASS` and no `FAIL` and ends with the line

```text
@@PROBELINE@@
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
is `@@ROAD_BLOB@@`, the blob rehearsed for this case in the
preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the shard
`probes_a38` inserted and required by the aggregate job, the five frozen edits.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `@@PREREG_BLOB@@`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `@@CONTROLS_BLOB@@` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 9 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, @@NMUTS@@ mutation controls fail as required` and
    `controls: self-test OK`.
  - At stage 1 `controls.py`'s module checks report the corollary that stage 2 adds and the two primed
    helper names recorded under Discrepancies; at the repair commit only the corollary; from stage 2 on,
    none.
- **`C3`:** the probe has blob `@@PROBE_BLOB@@` at stage 1; its run is
  green at the stage commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on thirteen receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A38-NON-DITA-WITNESS-PROVED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports `ALL CHECKS PASS` in `D`'s order. That run is evidence
for the executor and not an attestation.

@@RUNS@@

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

@@DISCREPANCIES@@

@@CLAUSE@@
