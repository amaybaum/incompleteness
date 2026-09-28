# Track B act 40 — the Diţă locus of the three-parameter family through the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #768. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A40.json`, and on the pull request.

- **`D`** — `b271b1dfe5a145d360c7c9433c81bfdf24ba0743`, the head of `main` after act 39's landing.
- **`F`** — `db91869ee4e606c123013ab105e765d0719f46e1`, the child of `D` that adds the
  preregistration alone, blob `0c8a95112ca45958bf697d90b2011b878a033d8c`, designated by the owner.
  `F`'s `check-run` attestation is run 36472063346, recorded on #768 in comment 5877013377.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A40-LOCUS-CLASSIFIED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A40` | `A40-LOCUS-CLASSIFIED`, theorem `a40_locus_kernel` with the probe green | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a40_c_exclusive` and the twenty-five statements required under this label:
`A40-1`, `a40_shared_face_1p`, `a40_shared_face_1m`, `a40_shared_face_2p`, `a40_shared_face_3p`, `a40_shared_face_3m`; and `A40-2`, `a40_shared_excl_k1_c`, `a40_shared_excl_k1_r`, `a40_shared_excl_k2_c`, `a40_shared_excl_k2_r`, `a40_shared_excl_k3_c`, `a40_shared_excl_k3_r`, `a40_shared_excl_k4_c`, `a40_shared_excl_k4_r`, `a40_shared_excl_e1_c`, `a40_shared_excl_e1_r`, `a40_shared_excl_e2_c`, `a40_shared_excl_e2_r`, `a40_shared_excl_t1_c`, `a40_shared_excl_t1_r`, `a40_shared_excl_t2_c`, `a40_shared_excl_t2_r`, `a40_shared_excl_t3_c`, `a40_shared_excl_t3_r`, `a40_shared_excl_mc_c`, `a40_shared_excl_mr_r`.

***

## The frozen post-round sentence

> At the frozen product configuration, the Diţă locus of act 39's three-parameter family is classified, in two layers named separately: for `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, `H3 u₁ u₂ u₃` admits a Diţă structure — of some shape, index map and orientation, strictly or up to diagonal equivalence — exactly when `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1` or `u₃ = −1`. The if-direction is proved in the kernel, at evidence level 2: at every point of each of the five faces, `H3` or its transpose is an explicit strict Diţă product of a named shape and index map with flat unitary factors. The kernel also proves, for each of twenty named index maps — act 37's nine classes in both orientations and act 38's `M_COL` and `M_ROW` — that a strict Diţă form of `H3` at that map forces its named coordinate equations. The only-if direction, over every shape, index map and orientation, and the agreement of the strict locus with the locus up to diagonal equivalence, are certified by the round's exact-computation probe and not by the kernel: forty-six candidate structures contain every structure admitted anywhere, the strict and relaxed loci of each coincide, the thirty nonempty loci are cut out by coordinate characters alone, and their union is exactly the five faces. This is a statement about the frozen mathematical objects; it censuses no exponent matrices, decides no minimality, concerns no family other than `H3`, and adopts no family, factorization or isometry as a symmetry, a principle or a law.

***

## The two layers, as certified

| direction | witness | layer |
| --- | --- | --- |
| if: on each of the five faces, at every point, `H3` or its transpose is a strict Diţă product | the five theorems of `A40-1` | kernel, evidence level 2 |
| only if: off the five faces no structure of any shape, index map or orientation, strictly or up to diagonal equivalence | the probe's sections 2, 3 and 4 | exact computation, replayed in CI |
| beside the only-if: at twenty named index maps, a strict form forces the named coordinate equations | the twenty theorems of `A40-2` | kernel, evidence level 2 |

The kernel does not prove the only-if direction: `A40-2` concerns twenty named maps in strict form,
and the exhaustion over every map and the relaxed forms are the probe's.

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `H3 u₁ u₂ u₃ = SIG ∘ u₁^{Ea} u₂^{Eb} u₃^{Ec}` is
act 39's family, act 39's head carried verbatim inside every statement, followed by this round's
`let`-bound maps `rmc`, `cmc`, `ditamc`, `rmr`, `cmr`, `ditamr` for act 38's `M_COL` and `M_ROW`.

**The scalars.** `star x = x⁻¹` and `x ≠ 0` for units; `1 + i ≠ 0`; `2/(1+i)² = −i` by
`linear_combination` with `i² = −1`, so `‖D‖ = 1`; the scalar identity
`(1+i)/2 · s · 2/(1+i)² · ((1+i) · m) = s · m` (`a40_shared_scal`); and `X = ((1+i)/2) · [[1, 1], [1, −1]]`
flat unitary.

**`A40-1`.** For each of the four structures — act 37's class `t2`, act 38's `M_COL`, act 36's frozen
`2 × 8` class, act 38's `M_ROW` — one generic lemma (`a40_shared_gen_t2`, `a40_shared_gen_mc`,
`a40_shared_gen_t1`, `a40_shared_gen_mr`): a flat unitary `M` whose partner rows equal the block sign
pattern times their class representatives is the Diţă product of `X`, `D ≡ 2/(1+i)²` and
`Y_c = (1+i) · M(representative rows on block c)`. Its sixteen row identities are each a definitional
`show` to the class representative followed by the scalar identity; the unitarity of `Y_c` follows
from the rows of `M` split by block. Each face applies its generic lemma to `H3` at the face value, or
to its transpose through `transpose_unitary`, with act 39's `a39_shared_unitary_core` and
`a39_shared_flat_core` at the face and eight partner relations evaluated entry by entry
(`a40_shared_face_…_rel0` to `…_rel7`, and `a40_shared_face_…_core`).

**`A40-2`.** For each named map: from a strict Diţă form of `H3`, a four-position witness
`H i j · H i' j' = H i j' · H i' j`, each entry evaluated to a monomial, reduces to `C · (u − v) = 0` with
`C ≠ 0` a product of units, so `u = v` (`a40_shared_excl_…_core`).

**`a40_locus_kernel`** assembles the twenty-five; **`a40_c_exclusive`**: `P_N` is the negation of
`P_R`.

**Zero definitions.** The module carries one hundred and ninety-nine theorems, each followed by its
`#print axioms` line; the release gate's `lean-axioms` step reports 5251 named results with no sorry,
and every axiom line of the module read in the logs is `[propext, Classical.choice, Quot.sound]`.

**The reference implementation is `829146f6eff2b99aab54d7e5e9292b0ecfb33d8d`; the module at E is `829146f6eff2b99aab54d7e5e9292b0ecfb33d8d`.** They are the same blob, so
there is no departure from the reference implementation: the module was added at stage 1 as the
reference implementation less the verdict and the corollary, and stage 2 added those two theorems
back, byte for byte.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a40_shared_…` consumes a verdict theorem or `a40_c_exclusive`,
`a40_not_locus_kernel` does not occur, and `a40_c_exclusive` consumes neither verdict theorem. Beside
Mathlib and this round's own shared lemmas, the module consumes only `a39_shared_unitary_core`,
`a39_shared_flat_core`, `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_div`, `a36_shared_mod`
and `transpose_unitary`, all listed under Provenance. No deviation.

***

## The exact-computation layer

The frozen probe `verification/lean/dita_torus_locus_probe.py`, blob `4b718e79f3800369855b6a9f0fc734ed2d59df4b`, is added at
stage 1 and run in its own shard, `Numerical probes / A40 locus`, which the aggregate `Numerical
probes` job requires. Its run at each stage commit reports 22 `PASS` and no `FAIL` and ends with the
line, here from the run at stage 3, 36478152302:

```text
dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the 30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1
```

These are exact arithmetic replayed, not kernel-certified: act 36's stabilizer replayed, order 1024;
the flat calculus self-tested on random and hand systems with explicit reconstruction; **46 candidate
structures** containing every structure admitted anywhere; for every candidate the relaxed locus equal
to the strict locus, **16 empty and 30 nonempty**, every nonempty locus cut out by coordinate
characters alone; **the union exactly the five faces** `u₁ = −1`, `u₁ = 1`, `u₂ = 1`, `u₃ = −1`,
`u₃ = 1`; and the controls — the diagonal giving act 38's exceptional set `{1, −1}`, act 37's census of
the eighteen structures of the stratum point at `(1, 1, 1)`, act 38's `M_COL` and `M_ROW` at
`(−1, −1, −1)`, the absent face `u₂ = −1` in no locus, act 39's pair faces with 480, 440 and 424 joint
level sets and none failing, the kernel's objects replayed at fifteen face points, act 36's structure
search agreeing at seventeen exact points, and the countercontrol with one entry of `C` cleared
giving 30 candidates, 23 loci and the one face `u₃ = 1`.

**Not claimed**, recorded as such: that the kernel proves the only-if direction; the census of exponent
matrices with entries in `{0, 1}`, which is neither used nor computed — act 37's census of the stratum
point appears only as a control; the minimality of support 48; and any family other than act 39's `H3`,
the countercontrol's perturbed pieces included.

***

## The `P0` cell and the guard

On `A40-LOCUS-CLASSIFIED` this round's sentence and its standing clause are appended once after act 39's standing
clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`145251197bede7d2bbd0c5a2605c7827e1b042fa`, the blob rehearsed for this case in the preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the frozen edit that
runs the probe in its own shard, blob `08586b8ecf334ba68e217e0e21af953e30466914`.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `0c8a95112ca45958bf697d90b2011b878a033d8c`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `d3821d5d1c88dc057e64be3635cbc3bcc749188c` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 14 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 75 mutation controls fail as required` and
    `controls: self-test OK`.
  - At stage 1 `controls.py`'s module checks report only the corollary that stage 2 adds, the label
    read off the module being `A40-UNDECIDED`; from stage 2 on they report none, the label being
    `A40-LOCUS-CLASSIFIED`.
- **`C3`:** the probe has blob `4b718e79f3800369855b6a9f0fc734ed2d59df4b` at stage 1; its shard is green at every stage commit
  with the line above, and the aggregate `Numerical probes` job is green with it.
- **`C6`:** at each stage commit the release gate's `v3-receipts` step holds on fifteen receipts and
  its `legacy-records` step reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A40-LOCUS-CLASSIFIED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports `ALL CHECKS PASS`, its output byte-identical to its output
at `D`. That run is evidence for the executor and not an attestation.

The exact-head `workflow_dispatch` runs at the stage commits, each on exactly the commit named:

| stage | commit | run | outcome |
| --- | --- | --- | --- |
| 1 — the controls, the probe and its shard, the shared lemmas, the import | `c3096556865edc526dc3f315993c6de9b064f945` | 36474528405 | eight of nine jobs green; the `Mathlib bridge` build compiles the module's one hundred and ninety-seven theorems and the release gate's `lean-axioms` step reports 5249 named results with no sorry; the gate is red only at `lean-manuscript`, the new module having no census family until stage 3, as the freeze orders; the probe's shard reports its `OK` line |
| 2 — the verdict and the corollary | `d9d5227d436a14f8f3d97f4f50672dd90cce3ac0` | 36476760295 | as at stage 1, with the one hundred and ninety-nine theorems compiled, the module the reference implementation, and `lean-axioms` at 5251 named results with no sorry; red only at `lean-manuscript`, for the same reason |
| 3 — the surfaces | `c49cfbadef402f5250d1e6e269fae297b2cb0896` | 36478152302 | all nine jobs green; the release gate passes all 21 steps, `lean-manuscript` included, with fifteen receipts holding and `legacy-records` at 303; the guard `ALL CHECKS PASS`; the probe's shard reports its `OK` line |

Design evidence before the freeze is recorded in the preregistration; no disposable branch is part of
the execution.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 40 proves and computes statements about act 39's three-parameter family through act 34's certified rational
> stratum point, and adopts none of them as anything but mathematics. A `LOCUS-CLASSIFIED` verdict settles which
> points of the three-torus admit a Diţă structure of the family, in two layers named separately: the kernel proves
> the explicit factorizations on the five faces and the exclusions at twenty named index maps, and the round's
> exact-computation probe certifies that no other point admits one. A `LOCUS-FAILS` verdict exhibits a failure of
> the kernel layer in the kernel. Neither verdict censuses the exponent matrices with entries in `{0, 1}`, decides
> whether support 48 is minimal or says anything about a family other than act 39's; both leave the product
> normalized set unclassified. Neither verdict establishes that any admissible transition law is covariant under
> any isometry, selects a physical law or closes `P0`. No hull, family, factorization, isometry, carrier, group or
> principle gains physical status by appearing here, and nothing here derives, recognises or approaches quantum
> evolution.
