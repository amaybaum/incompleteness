# Track B act 37 — the exclusivity of the `2 × 8` arc through the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #@@PR@@. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A37.json`, and on the pull request.

- **`D`** — `d014bafef404b991b4544e6d2041edcfab1ac765`, the head of `main` after the landing of
  #763, the last of the continuous-integration pull requests that followed act 36's landing.
- **`F`** — `@@F@@`, the child of `D` that adds the
  preregistration alone, blob `@@PREREG_BLOB@@`. `F`'s `check-run`
  attestation is run @@F_RUN@@; the owner's designation is comment @@F_COMMENT@@ on #@@PR@@.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A37-EXCLUSIVITY-PROVED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A37` | `A37-EXCLUSIVITY-PROVED`, theorem `a37_exclusivity` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a37_c_exclusive` and the eleven statements required under this label:
- `A37-1`: `a37_shared_symmetric`;
- `A37-2`: `a37_shared_persistence`;
- `A37-3`: `a37_shared_excl_k1`, `a37_shared_excl_k2`, `a37_shared_excl_k3`, `a37_shared_excl_k4`,
  `a37_shared_excl_e1`, `a37_shared_excl_e2`, `a37_shared_excl_t2` and `a37_shared_excl_t3`;
- the control `a37_control_base`.

***

## The frozen post-round sentence

> @@SENTENCE@@

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `Pu u = SIG ∘ u^W` is act 36's arc,
`SIG = F₄(z) ⊗ F₄(w)` the certified rational stratum point, `dg X Y D` Diţă's column construction
`(a,b),(c,d) ↦ X[a,c]·D[c,b]·Y_c[b,d]`, `flg X` flatness of a unitary on a finite type, `dita28` act
36's `2 × 8` form at the frozen index maps, and `dita…` the form of each of the eight other classes
at its own index maps, given as lookup tables inside the statements.

**`A37-1`, `a37_shared_symmetric`.** An entry of the transpose is
`F₄(z)[j.1, i.1] · F₄(w)[j.2, i.2] · u^{W(j, i)}`; the Fourier matrix at any parameter is symmetric,
by a sixteen-case split on its two indices (`a37_shared_f4_symm`), and the exponent `W(i, j)` is
symmetric because its condition `a even ∧ c even` and its value `[b = 1] + [d = 1]` are
(`a37_shared_wt_symm`); three rewrites give the entry of `Pu u` (`a37_shared_sym_core`).

**`A37-2`, `a37_shared_persistence`.** The column form is the first component of act 36's
`a36_shared_line_core` at `z`, `w` and `u`, whose witnesses are the nested `2 × 8` factors; the row
form is the same witnesses under the symmetry, `Pu u = (Pu u)ᵀ = (dita28 X Y D)ᵀ`
(`a37_shared_persist_core`).

**`A37-3`, the eight exclusions.** For each class, from a Diţă form `Pu u = dita… X Y D`, the four
entries at the frozen witness positions factor as `X a c · D c b · Y c b d` with the class's tables
evaluated, and the product of the first two equals the product of the last two by `ring`, because
they pair the same factors: for a proportionality witness (`k1`, `k3`, `k4`, `e1`, `t2`) the two rows
lie in one class and the two columns in one block, and for a rank-one witness (`k2`, `e2`, `t3`) the
four rows `(a,b), (0,0), (a,0), (0,b)` sit in one column. The same four entries of `Pu u`, evaluated
by `simp` with `decide` on the concrete indices, are `±1/4` times `u^0` or `u^1` with exponent sums
`0` and `1`, so the identity reads `±u/16 = ±1/16`, and `linear_combination` with the frozen
coefficient `±16` closes `u = 1`. The transpose orientation is reduced to the column one by the
symmetry and `Matrix.transpose_transpose` (`a37_shared_excl_core_k1` to `a37_shared_excl_core_t3`).

**The control, `a37_control_base`.** `Pu 1 = SIG` is act 36's `a36_shared_one_core`; `F₄(z)` and
`F₄(w)` are flat unitaries by act 35's `a35_shared_f4_flat` and `a35_shared_half`; and `SIG` is the
Kronecker form at the class `k1` with the trivial twist because the two lookup tables of `k1`
return `i.1` and `i.2`, by sixteen-case splits, after which the entry is `F₄(z)[a,c] · 1 · F₄(w)[b,d]`
(`a37_shared_base_core`).

**`a37_exclusivity`** is the conjunction of the ten cores over the frozen head;
**`a37_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries @@NTHM@@ theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a37_shared_…`, `a37_c_…` other than `a37_c_exclusive`, or
`a37_control_…` consumes a verdict theorem or `a37_c_exclusive`, and `a37_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's to act 36's
modules among them — and it records a helper absent from that list as a deviation against the row
it departs from, not repaired. @@DEVIATIONS@@

***

## The exact-computation layer

The frozen probe `verification/lean/dita_arc_exclusivity_probe.py`, blob
`@@PROBE_BLOB@@`, is added at stage 1 and wired into the
`Numerical probes / A36 hierarchy` shard by the two frozen lines. Its run at the stage commits
reports @@NPASS@@ `PASS` and no `FAIL` and ends with the line

```text
@@PROBELINE@@
```

These are exact arithmetic replayed, not kernel-certified: the census of the stratum point's
Diţă structures — eighteen, four `4 × 4`, two `8 × 2` and three `2 × 8` in each form, every one
reconstructing `SIG` with the trivial twist, forming nine orbits under the stabilizer of order 1024
with transposition, each a structure and its transpose; the arc symmetric, with `P` and `Pu u₅`
admitting exactly the frozen class; the generic arc point admitting exactly the frozen class, and
each other class obstructed by between 4 and 40 monomial conditions all of the form `u^{±1} = 1`;
the candidate exceptional set of twenty exactly named points `ζ z^s w^t`, twelve of them Gaussian
rational; the exhaustive search at each of them — the eighteen structures at `u = 1`, the same
proportionality candidates but only the frozen class at `u = −1`, and only the frozen class at
every other candidate — so that **the exact exceptional set is `{1}`**; and the controls: the
numeric search with factor unitarity agreeing at all twelve Gaussian-rational candidates, a
genuine deformation inside each other class found in its class, transpose and stabilizer
invariance, and a perturbed index map admitted nowhere.

By the probe, and not by the kernel: **for every unit `u ≠ 1`, the arc point `Pu u` is a Diţă
matrix for the frozen `2 × 8` class and its transpose orientation and for no other index maps at
all.** With the kernel's eight exclusions and its persistence and symmetry theorems, the arc is
exclusive to its `2 × 8` class, with the exceptional set `{1}`.

**Open**, recorded and not decided: whether every realizable class of the product normalized set
sufficiently near the stratum lies in some Diţă hull of some factorization of the sixteen-point
carrier. The arc lies in the frozen `2 × 8` hull at every unit `u` and escapes no hull; nothing here
says the hierarchy exhausts anything or that it does not.

***

## The `P0` cell and the guard

On `A37-EXCLUSIVITY-PROVED` this round's sentence and its standing clause are appended once after
act 36's standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`@@ROAD_BLOB@@`, the blob rehearsed for this case in the
preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the two lines
inserted.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `@@PREREG_BLOB@@`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `@@CONTROLS_BLOB@@` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 8 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, @@NMUTS@@ mutation controls fail as required` and
    `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C3`:** the probe has blob `@@PROBE_BLOB@@` at stage 1; its run is
  green at the stage commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on twelve receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A37-EXCLUSIVITY-PROVED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

@@RUNS@@

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

@@DISCREPANCIES@@

@@CLAUSE@@
