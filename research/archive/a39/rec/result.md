# Track B act 39 — the three-parameter realizable family through the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #767. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A39.json`, and on the pull request.

- **`D`** — `08a7707dfe282f85c14e598f93cc27113ad00157`, the head of `main` after the landing of #766.
- **`F`** — `7deb404e9c772ce3f7ae65c89509d9dd3965f16e`, the child of `D` that adds the
  preregistration alone, blob `e09afe2f95df04e62c1aa76085cfc294f9bb182b`. `F`'s `check-run`
  attestation is run 36415055421; the owner's designation is comment 5869013084 on #767.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A39-REALIZABLE-PROVED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A39` | `A39-REALIZABLE-PROVED`, theorem `a39_realizable` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a39_c_exclusive` and the three statements required under this label:
`A39-1`, `a39_shared_realizable`; and the controls `a39_control_base` and `a39_control_diagonal`.

***

## The frozen post-round sentence

> At the frozen product configuration, the three-parameter realizability package holds, at evidence level 2: for act 38's three disjoint exponent pieces `A`, `B`, `C`, with entries in `{0, 1}` on the sixteen-point carrier and sum act 38's exponent matrix `E`, and the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, `H3 u₁ u₂ u₃` is a flat unitary — a complex Hadamard matrix — whose Gram family is realizable and whose feature vector lies in the product normalized set, at every point `(u₁, u₂, u₃)` of the three-torus. Beside the package, required under both decided labels: the family passes through the stratum point, `H3 1 1 1 = SIG`, and its diagonal is act 38's arc, `H3 u u u = Hu u` for every `u`. The round's exact-computation probe certifies the identity the kernel proves: for every ordered pair of rows, the columns grouped by their joint exponent-difference triple cancel exactly, 552 joint level sets and none failing, monomial by monomial in the stratum point's two units. This is a statement about the frozen mathematical objects; it does not decide which points of the three-torus admit a Diţă structure, and it adopts no family, factorization or isometry as a symmetry, a principle or a law.

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `H3 u₁ u₂ u₃ = SIG ∘ u₁^{Ea} u₂^{Eb} u₃^{Ec}` is
the family, `Ea`, `Eb`, `Ec` act 38's pieces `A`, `B`, `C` in closed form on the product index, and
`SIG = F₄(z) ⊗ F₄(w)` the certified rational stratum point, act 38's head carried verbatim inside
every statement.

**`A39-1`, `a39_shared_realizable`.** With `z`, `w`, `u₁`, `u₂` and `u₃` symbolic units,
`star x = x⁻¹` for each (`a39_shared_inv_of_unit`) and `x ≠ 0` (`a39_shared_ne_zero_of_unit`). For
each row `(a, b)` and each column block `c`, the four entries `((a,b), (c,d))` of `H3 · H3^*` are
sums of sixteen monomials in the five units and their inverses with rational coefficients, and equal
`[ (a,b) = (c,d) ]`: a four-case split on `d`, `simp` with the product-sum expansion, the star
rewrites and the conjugates of `1/2` and `2`, then `field_simp` and `ring`
(`a39_shared_row_core_00_0` to `a39_shared_row_core_33_3`, sixty-four lemmas). They assemble into the
sixteen rows (`a39_shared_row_core_00` to `a39_shared_row_core_33`), the four row blocks
(`a39_shared_rowblock_core_0` to `a39_shared_rowblock_core_3`) and all rows
(`a39_shared_rows_core`), and the unitarity follows by `ext` (`a39_shared_unitary_core`). Flatness is
act 35's `a35_shared_half` twice with `‖uₖ‖ = 1` for each `k` (`a39_shared_flat_core`); the
realizable Gram and the feature vector are act 35's `a35_shared_gram_realizable`
(`a39_shared_real_core`), instantiated at `z`, `w` by act 36's unit lemmas. The identity holds with
`z` and `w` symbolic because every joint level set cancels monomial by monomial, as the probe checks.

**The controls.** `a39_control_base`: `H3 1 1 1 = SIG` entrywise by `one_pow` and `mul_one`
(`a39_shared_base_core`). `a39_control_diagonal`: `H3 u u u = Hu u` entrywise, `u^(Ea + Eb + Ec)`
split by `pow_add` twice and closed by `ring` (`a39_shared_diag_core`).

**`a39_realizable`** is `a39_shared_real_core` over the frozen head; **`a39_c_exclusive`**: `P_N` is
the negation of `P_R`.

**Zero definitions.** The module carries one hundred and one theorems, each followed by its
`#print axioms` line, each within `propext`, `Classical.choice` and `Quot.sound`.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a39_shared_…` or `a39_control_…` consumes a verdict theorem or
`a39_c_exclusive`, and `a39_c_exclusive` consumes neither verdict theorem. Beside Mathlib and this
round's own shared lemmas, the module consumes only `a35_shared_half`, `a35_shared_norm_of_unit`,
`a35_shared_gram_realizable`, `a36_shared_z_unit` and `a36_shared_w_unit`, all listed under
Provenance. No deviation.

***

## The exact-computation layer

The frozen probe `verification/lean/dita_torus_probe.py`, blob `4405655907e1e508e0ce72b3335c905b0abcaf8d`, is added at
stage 1 and run in act 38's shard `Numerical probes / A38 escape`, directly after act 38's probe.
Its run at the stage commits reports 15 `PASS` and no `FAIL` and ends with the line

```text
dita_torus_probe: OK -- the three-parameter family SIG o u1^A u2^B u3^C through the certified stratum point, A, B, C act 38's three pieces: every joint level set of every ordered row pair cancels exactly, 552 of them, and monomial by monomial in z and w, so the family is a complex Hadamard matrix on the whole three-torus; it passes through SIG at (1, 1, 1) and its diagonal is act 38's arc
```

These are exact arithmetic replayed, not kernel-certified: act 36's stabilizer replayed, order 1024;
the pieces `A`, `B`, `C` disjoint with sum `E`, their rows, columns and supports, and the nine joint
difference triples; **the 552 joint level sets of the 256 ordered row pairs, none failing**, in
exact Gaussian rationals and monomial by monomial in `z` and `w`; and the controls — `H3(1, 1, 1) =
SIG`, the diagonal equal to act 38's arc at `u₅`, `u₆₀`, `−1` and `i`, exact unitarity at four
Gaussian-rational points off the diagonal, non-unitarity at `u₁ = 2`, the eight single- and
two-variable subfamilies with 512, 312, 352, 384, 424, 440, 480 and 536 level sets and none failing,
the countercontrol with one entry of `C` cleared failing on 60 level sets and not unitary at
`(u₅, w, u₁₇)`, and the 16 merged diagonal level sets, of two columns each, each cancelling on its
own. The probe's count is the certificate of the identity the kernel proves.

**Not claimed**, recorded as such: which points of the three-torus admit a Diţă structure; any
transfer of act 38's exclusion off `{1, −1}` from the diagonal to the generic point of the family,
to any other point off the diagonal, or to any subfamily; the exponent matrices with entries in
`{0, 1}`; and the minimality of support 48.

***

## The `P0` cell and the guard

On `A39-REALIZABLE-PROVED` this round's sentence and its standing clause are appended once after act
38's standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`f282da132c49711b2ac48127b74be66994f5382c`, the blob rehearsed for this case in the preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the two frozen lines
that run the probe in act 38's shard.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `e09afe2f95df04e62c1aa76085cfc294f9bb182b`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `7c0b2b3b0063c105d6e32743b87a41deec02d570` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 12 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 52 mutation controls fail as required` and
    `controls: self-test OK`.
  - At stage 1 `controls.py`'s module checks report only the corollary that stage 2 adds; from
    stage 2 on, none.
- **`C3`:** the probe has blob `4405655907e1e508e0ce72b3335c905b0abcaf8d` at stage 1; its run is green at the stage
  commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on fourteen receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A39-REALIZABLE-PROVED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports `ALL CHECKS PASS` in `D`'s order. That run is evidence
for the executor and not an attestation.

The exact-head `workflow_dispatch` runs at the stage commits, each on exactly the commit named:

| stage | commit | run | outcome |
| --- | --- | --- | --- |
| 1 — the module, the controls and the probe | `3a16021639a49a5eb32bd8c5466cdf458f4e3ee6` | 36416531599 | seven of eight jobs green; the `Mathlib bridge` build compiles the module's ninety-nine theorems and the release gate's `lean-axioms` step reports 5050 named results with no sorry; the gate is red only at `lean-manuscript`, the new module having no census family until stage 3, as the freeze orders; the probe reports its `OK` line |
| 2 — the verdict and the corollary | `e37cad3bf990b23f1e1615e2862a2ca57503b567` | 36417464997 | as at stage 1, with the one hundred and one theorems compiled and `lean-axioms` at 5052 named results with no sorry; red only at `lean-manuscript`, for the same reason |
| 3 — the surfaces | `a68dd1e1b658be5b66bfc2eb4662316f1d71a781` | 36418280236 | all eight jobs green; the release gate passes, `lean-manuscript` included, with fourteen receipts holding and `legacy-records` at 303; the probe reports its `OK` line |

Design evidence before the freeze is recorded in the preregistration; no disposable branch is part of
the execution.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 39 proves statements about one exact three-parameter family of realizable classes through act 34's certified
> rational stratum point, given by act 38's three exponent pieces, and adopts none of them as anything but
> mathematics. A `REALIZABLE-PROVED` verdict settles the frozen package, and a `REALIZABLE-FAILS` verdict exhibits
> the failure at a named point. Neither verdict classifies which points of the three-torus admit a Diţă structure,
> censuses the exponent matrices with entries in `{0, 1}` or decides whether support 48 is minimal, and neither
> carries act 38's exclusion of Diţă structures along the diagonal to the generic point of the family; both leave
> the product normalized set unclassified. Neither verdict establishes that any admissible transition law is
> covariant under any isometry, selects a physical law or closes `P0`. No hull, family, factorization, isometry,
> carrier, group or principle gains physical status by appearing here, and nothing here derives, recognises or
> approaches quantum evolution.
