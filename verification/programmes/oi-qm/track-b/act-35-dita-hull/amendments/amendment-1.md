# Track B act 35 — the Diţă hulls of the product-embedded stratum: preregistration amendment 1

This is an **append-only amendment** to
`verification/programmes/oi-qm/track-b/act-35-dita-hull/preregistration.md`, a control-plane file of
the round's record directory under `AGENTS.md` §A.39 and the specification's `G9`. It is drafted
from `D = 100bb1e86931fa769a200e9b117f4f9fb0a745b9` on pull request #755, after the owner's review
of the commit `62479b5780c1c3e3809e5d49cf7e1cf3684ced80`, which comment 5854712207 had designated as
`F` and which the review then held before any execution commit existed. Under `G9` the control plane
is a draft until execution begins; the owner's hold supersedes that designation, and the commit
carrying this amendment is the one presented for designation as `F`. The preregistration is
unchanged; where the two disagree, this amendment controls. Nothing in the fifteen frozen
propositions, the corollary, the theorem list, the route-authorization matrix, the outcome grammar
or the stage plan changes.

The four corrections are the owner's review findings: the probe's run sites (`A1`), a vacuous check
and a floating-point comparison in the frozen probe (`A2`), the wording of the open modulus and of
the `P0` sentence, stronger than what the probe measures (`A3`), and the record files and the blobs
that `A2` and `A3` move (`A4`).

## `A1` — where the probe runs

Hazard 3 says the probe is "run by the `Numerical probes` job at `F` and at `E`", and the
exact-computation layer says the workflow token is inserted "so that the job runs it at `F` and at
`E`". Both are superseded. `F` carries the preregistration and this amendment alone and no probe:
the probe and the workflow token are added at stage 1, and the job runs the probe at every
execution commit from stage 1 on, and so at `E`. The runs at `F` exercise the probes job at `D`'s
list. The probe's design runs before `F`, on disposable heads, are run 36309156707 for the probe of
the preregistration's blob and run 36313140818 for the probe of this amendment; both are the
executor's evidence, recorded here and in the result note, and neither is an attestation. `C3` is
unchanged: the probe's blob at stage 1 and its green run at the stage commits and at `E`.

## `A2` — the frozen probe, corrected

The probe of blob `0570327f3a89927e803f3d6b68fdb5142c766b08` carried two checks that did not
measure what their labels state.

1. **The tangent check was vacuous.** Its line

   ```text
   check('every hull tangent lies in the defect space at the Σ point', rank_int(defect_rows(SIG) + []) == rank_int(defect_rows(SIG)), True)
   ```

   compares the rank of the defect system with itself and reads no tangent vector. The comparison
   `26 < 49` that follows is meaningful only once the tangent span is known to lie in the solution
   space of the defect system. The corrected probe tests each of the 65 tangent and gauge vectors
   against each of the 240 defect equations at the rational stratum point, by integer dot products,
   and passes only when every product is zero; beside it a control asserts that a single-entry phase
   direction fails the same test. The vectors of the preregistration's probe pass the corrected test:
   the defect was in the verification, not in the mathematics.

2. **The stabilizers were floating-point, and wrong.** The enumeration dephased `numpy` complex
   matrices and compared `np.round(·, 6).tobytes()`; the values 512 and 16 were not exact
   arithmetic replayed in the sense the preregistration claims, and they are not the stabilizers.
   The byte comparison distinguishes `0.0` from `−0.0`, and the phase divisions leave the sign of a
   zero part undetermined: at `F₄ ⊗ F₄`, of the 8192 group elements whose image agrees with the
   reference to within `10⁻⁹` after rounding, 7680 differ from it only in the sign of a zero and
   were not counted. The corrected probe writes each of the two matrices, whose entries are fourth
   roots of unity, as its exponent matrix `E` with `H = i^E`, asserting that every entry is a fourth
   root; it applies the swap, the conjugation (`E ↦ −E mod 4`), the transpose and the product row and
   column relabellings on exponents; it dephases by subtracting the first column from every row and
   then the first row from every column, modulo 4; and it counts exact equalities of integer arrays.
   The stabilizers are **8192** at `F₄ ⊗ F₄` and **128** at the twisted point, in place of 512 and
   16 wherever the preregistration names them: in the measurement summary's list of stabilizers and
   in the frozen-probe section's line "Stabilizers in `G_ext`: 512 at `F₄ ⊗ F₄`, 16 at `Hw`". The
   probe asserts the corrected values. Its independent control
   is the orbit of each dephased class under `G_ext`, computed by breadth-first search over eleven
   generators (four product row transpositions and cycles, the same on columns, the swap, the
   conjugation and the transpose) on exponent matrices: 324 at `F₄ ⊗ F₄` and 20736 at the twisted
   point, and the probe asserts both and that orbit times stabilizer is 2 654 208 at each. The
   measurement's other stabilizer values, 64 and 2 at random points and 4608 at `H₄ ⊗ H₄`, came from
   the same comparison, were not frozen and are not asserted.

The corrected probe is `verification/lean/dita_defect_probe.py`, blob
**`99f98ca79b0089d15cf9babb9ca965e88598cfa6`**, which replaces the preregistration's blob wherever it
is named: in the exact-computation layer, in `C3`, and in the constants `controls.py` agrees with.
Its docstring's account of `numpy` supersedes the preregistration's: `numpy` is used in the grid
enumeration, where classes are identified by a distance that is zero or at least `1/5` on the finite
set concerned, and in the stabilizer enumeration, in integer exponent arithmetic, exact. Every other
value the probe asserts is Python integer and fraction arithmetic as before. The probe reports
43 `PASS` and no `FAIL` and ends with the line `dita_defect_probe: OK`; the preregistration's runs
table says the probe of its blob "reports 57 `PASS`", which is superseded: that probe prints 39
`PASS` lines, and the corrected probe prints 43, the 39 with the tangent control of item 1 and the
three orbit controls of item 2.

## `A3` — the open modulus, stated to the measurement

The probe computes the exact rank, 26, of the tangent vectors of the two hulls `Δc` and `Δr` at the
fixed pairing `(a, b) ↦ 4a + b`, and the exact defect, 49, at the certified rational stratum point.
The defect is the dimension of the solution space of the linearized unitarity constraints modulo
the phase directions, an upper bound on the dimension of any family of realizable classes through
the point (Hazard 4); it is not "the linearized dimension of the product normalized set", and the
comparison says nothing about the hulls at other pairings or relabellings. Three passages of the
preregistration say more than this and are superseded.

- The overview's "the linearized dimension of the product normalized set at a stratum point exceeds
  even those" reads: *the defect at the certified rational stratum point, 49, exceeds the tangent
  rank, 26, of the two fixed-pairing hulls there.*
- The countercontrol paragraph's "the hulls do not exhaust the defect space, so the linear level
  already carries 23 directions no hull accounts for" reads: *at the certified rational stratum
  point the tangent spaces of the two fixed-pairing hulls do not exhaust the defect space, which
  carries 23 directions beyond them; whether those directions integrate to realizable classes, and
  whether the hulls at other pairings or relabellings reach the classes near the stratum, is not
  measured.* The open modulus itself, whether every realizable class of the product normalized set
  sufficiently near the stratum lies in some relabelled Diţă hull, is unchanged; the countercontrol
  is exactly the rank 26 of the two fixed-pairing hulls against the defect 49, and no relabelled
  orientation is analysed.
- The `P0` sentence for `A35-DITA-STRATIFIED` reads, in place of the preregistration's, with the
  standing clause that follows it unchanged:

  > At the product configuration, two explicit families of realizable classes, the column and row Diţă hulls, contain the product-embedded stratum, are realizable for every choice of flat unitary factors and unit twist phases, and carry infinitely many classes through every stratum point that no finite set of maps identifies; act 34's properness witness is a column relabelling of a stratum point, so stratum membership is not an invariant of the isometry classes of the product normalized set; and, by the round's exact-computation probe, at the certified rational stratum point the defect, the dimension of the solution space of the linearized unitarity constraints modulo phases and an upper bound on the dimension of any family of realizable classes through the point, is 49, while the tangent span of the two fixed-pairing hulls has rank 26, so those two tangent spaces do not exhaust the defect space; whether the relabelled hulls exhaust the realizable classes near the stratum is an open modulus, recorded and not decided.

The rehearsed `ROADMAP.md` blob for `A35-DITA-STRATIFIED` is therefore
**`243e9b973e5afe115014ffa0a807fe185727be6e`** in place of `15a6cd4e243b61817a3a7c253324d412b1082cd0`;
the blob for `A35-NOT-DITA-STRATIFIED`, `61875bd48472bf03abf75ae1df3e1609c443e2db`, is unchanged.
The census family's note names the countercontrol in the same terms, as the two fixed-pairing
hulls' tangent rank 26 against the defect 49 at the certified rational stratum point, and the
result note's account of the open modulus does the same. The post-round sentences of the three
labels and the standing clause are unchanged.

## `A4` — the record files and `controls.py`

The record directory holds four files: the preregistration, this amendment under `amendments/`,
the round's frozen controls `controls.py`, and the result note; "three files" and "the three record
files" in the preregistration read "four". The paths changed from `D` at `E` are the
preregistration's list with this amendment added among the added record files.

`controls.py`, blob **`4834dd888cc87ae914c5d2a517d61d083f4daf23`** in place of
`52009e086a3079b8c3bf50621d6f68d8f35c7530`, is written before `F` and added by the execution with
exactly this blob. It differs from the preregistration's in these four places and nowhere else: the
probe blob of `A2`; the `P0` sentence of `A3`; this amendment among the expected added paths; and
its self-test, which reads the preregistration and this amendment beside it as the sources of the
shared texts and requires the amended sentence in this amendment. Its self-test prints

```text
controls: the two verdict propositions are duals and every shared text has one source; 8 duality mutations fail as required
controls: 3 rows hold as frozen, 74 mutation controls fail as required
controls: self-test OK
```

and `C2`'s expected output reads accordingly.

Nothing else in the preregistration is amended. The witness story, the theorem package, the census,
the group computations and the stage plan stand as frozen.
