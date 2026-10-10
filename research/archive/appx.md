## Appendix — the claim-surface census at `D`, in full

All text below was read from git objects at D41 = `78ea3c39004e97aad027ee6153051c6d372bdd55`. Nothing in the
repository was modified.

## Scope and method

- **In scope:** every file not under `verification/programmes/`, `verification/receipts/`,
  `verification/seals/`, `verification/certificates/`, and not listed in
  `verification/infrastructure/legacy-records.json` (none of the files below is listed there).
- **Search:** `git grep` at D41 for `Diţă|Diță|Dita|dita_|SIG|index map|eighteen|support 48|three-parameter|census`
  and for `A3[6-9]-|A40-|a3[6-9]_|a40_|exceptional set|five faces|DitaHierarchy|DitaArc|DitaLocal|DitaTorus`.
  The only non-record files carrying act 36–40 content are the five probes, the five Lean modules (plus
  their `import` lines in `OIBridge.lean`), `verification/lean-manuscript-census.json`,
  `verification/ROADMAP.md` and `.github/workflows/verify.yml`. The remaining hits were checked and are
  unrelated. `verification/README.md` has four "eighteen" hits, all about seals and contracts.
  `papers/GR.md` has one "eighteen" hit, which is unrelated. `tools/`, `papers/` and `book/` contain no
  Diţă content.
- **Probes:** every docstring, comment, section title, check label and OK line was read. The Lean modules
  contain comments only in their module headers (checked with a block-comment scan; there are no `--` or
  `/--` comments).

### Kinds

| code | meaning |
| --- | --- |
| **a** | Absolute claim that is false under all alignments. |
| **a\*** | Absolute claim whose content holds under all alignments but which says it was certified by a probe that tested one alignment. The certification it cites does not exist at D41. |
| **b≠** | Sorted-only count or verdict presented without scope; the all-alignment value differs. |
| **b=** | Sorted-only computation presented as exhaustive; the value happens to equal the all-alignment value. |
| **b?** | Sorted-only computation presented without scope; the supplied all-alignment table does not give this value. |
| **c** | Survives unchanged; the reason is stated. |
| **d** | Text in the ROADMAP P0 cell that reproduces a round's frozen P0 sentence verbatim. Verified: each act-36…40 segment of the cell appears word for word in that act's `preregistration.md`. |

"Sorted alignment" means one index map per partition structure: the rows of each class in sorted order,
i.e. `row[(a,b)] = rows[b][a]` in `dita_orientations`, `structures`, `conditions`,
`conditions_E`, `relaxed_at_point` and act 40's `conditions`. Proportionality candidates (column
partition plus row classes) do not depend on the alignment. Rank-one, relaxed rank-one, factor
unitarity, loci and hulls do.

**Replacement convention.** The replacements use "at the sorted alignment" or "with the rows of each class in
sorted order", with no revision-history words and no capitals. Where a sentence's content survives and it
cites all-index-map certification (kind a\*), the replacement cites "exact computation over every index
map". That wording is supported only once the all-alignment search is itself part of the
exact-computation layer, for example as the act-41 probe; the replacement must cite that probe. Until then
the only supported text is the sorted-scoped fallback that is also given.

### Independent sanity check (in memory, no files written)

I executed the act-38 probe head from the D41 blob and ran an all-alignment rank-one + factor-unitarity
test with class 0's alignment fixed; a simultaneous relabelling of `a` across all classes permutes the rows
of `X` only. Results:

- At SIG, 4×4: all 5 candidates admit an exact alignment in each orientation, with 8, 64, 8, 8 and 8 of the
  13824 relative alignments exact. k5 is the fifth candidate, whose sorted alignment fails. 2×8: 3 of 3,
  with every one of the 128 alignments exact.
- At H(−1) = SIG∘(−1)^E, the single 4×4 candidate is exact in each orientation (8 alignments), and so is the
  single 2×8 candidate. This gives **one 2×8 and one 4×4 structure per orientation**, which matches the
  supplied "4 (two 2×8 plus two 4×4)".
- The 4×4 partition at H(−1) is **not** any of SIG's five 4×4 candidates, and in particular it is not k5. So
  on act 38's arc, k5 is not even a proportionality candidate at u = −1. Together with the surviving
  exceptional set {1, −1}, k5 is admitted along that arc only at u = 1. The replacements below still speak
  only of named classes and do not rely on this.
- For m = 2 (2×8) every alignment gives the same verdict, so all 2×8 statements are alignment-free.

***

## Summary count by kind

| file | a | a\* | b≠ | b= | b? | c | d | total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `verification/lean/dita_hierarchy_probe.py` | 0 | 0 | 4 | 2 | 3 | 2 | 0 | 11 |
| `verification/lean/dita_arc_exclusivity_probe.py` | 0 | 0 | 6 | 9 | 14 | 3 | 0 | 32 |
| `verification/lean/dita_local_escape_probe.py` | 0 | 0 | 12 | 5 | 9 | 5 | 0 | 31 |
| `verification/lean/dita_torus_probe.py` | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 3 |
| `verification/lean/dita_torus_locus_probe.py` | 0 | 0 | 7 | 2 | 6 | 4 | 0 | 19 |
| `verification/lean-mathlib/OIBridge/Dita*.lean` (5 modules) + `OIBridge.lean` | 3 | 4 | 0 | 0 | 0 | 4 | 0 | 11 |
| `verification/lean-manuscript-census.json` | 5 | 4 | 1 | 2 | 1 | 6 | 0 | 19 |
| `verification/ROADMAP.md` | 2 | 0 | 0 | 0 | 0 | 2 | 7 | 11 |
| `.github/workflows/verify.yml` | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| **total** | **10** | **8** | **30** | **20** | **35** | **28** | **7** | **138** |

Rolled up to the four requested kinds, there are **(a) 18** rows: 10 are false and 8 are true in content
but cite a certification that does not exist. There are **(b) 85** rows: 30 whose value differs, 20 whose
value coincides and 35 with no supplied all-alignment value. There are **(c) 28** and **(d) 7**. Five (d)
rows need a change: R2, R3, R4, R5 and R7, which is A40's attribution clause. Two need none: R1, A36's
kernel sentence, and R6, A39.

***

## Replay: would a label-only edit pass `tools/probe_replay_check.py` against the D41 blob?

**What the tool compares** (`tools/probe_replay_check.py` at D41, lines 20–39):

```python
CHECK = re.compile(r'^  (PASS|FAIL)  .*$')
SUMMARY = re.compile(r'^\w+: (OK|FAILED)')
...
out = [l for l in log.split('\n') if CHECK.match(l)]
out += [l for l in log.split('\n') if SUMMARY.match(l)]
...
if x != y: diffs.append((i, x, y))
```

- It keeps each **entire** check line and the **entire** summary line, and compares them in order with
  exact string equality.
- All five probes print checks as `'  %s  %-70s %s' % ('PASS'|'FAIL', name, got)`. The label is
  therefore part of every compared line. In `dita_hierarchy_probe.py` the first definition, with width 58,
  is shadowed at line 153 before any call.
- The OK lines (`dita_…_probe: OK -- …`) match `SUMMARY` and are compared in full.
- The tool does **not** compare section titles (`== … ==`), timing lines (`  (Ns)`), docstrings or
  comments, because none of them is printed as a PASS/FAIL or summary line.

| probe | check call sites | check labels / OK line needing change | label-only edit passes replay vs D41? |
| --- | --- | --- | --- |
| `dita_hierarchy_probe.py` | 36 (the loop renders 12 lines at l.314, 4 at l.317 and 6 at l.319) | yes: l.314, 319, 439, 469, 470, 472 and the OK line | **No.** Every relabelled line and the OK line produce `DIFF`; the tool prints FAILED. |
| `dita_arc_exclusivity_probe.py` | 33 | yes: many labels and the OK line | **No** |
| `dita_local_escape_probe.py` | 44 | yes: many labels and the OK line | **No** |
| `dita_torus_probe.py` | 15 | none; only docstrings need change | **Yes.** Docstring edits are not printed. |
| `dita_torus_locus_probe.py` | 22 | yes: many labels and the OK line | **No** |

The tool cannot tell a label change from a value change, and its self-test rejects both. A label-only
round therefore cannot use it unmodified as the equality control. One option is a label-insensitive
comparison, which checks for each `DIFF` pair that the verdict and the `got` field are identical. For
labels of at most 70 characters, `got` starts at column 79 (2 + 4 + 2 + 70 + 1). For longer labels,
`got` starts after the label, so the label map must be applied first. Another option is to replay the
D41 blob with its labels substituted by the new ones and then require zero diffs. Section-title,
docstring and comment edits are invisible to the tool as it stands.

**Check values that encode more than their label.** No check value hard-codes an all-index-map assertion.
Every value is either an output of the sorted search or a computation over a named list (`CLASSES`,
`M_COL`, `M_ROW`, `WIT`), so every value remains valid as a sorted-alignment regression value. Four points
nevertheless need flagging:

1. **Act 40, l.646 (value `True`: every nonempty locus is coordinate).** This is the one value that is
   *false* under all alignments (four non-coordinate points). It is correct only as a sorted regression
   value.
2. **Controls that share the defect.** Act 37 l.517, act 38 l.560 and act 40 l.731/748 compare the
   numeric sorted search with the symbolic sorted search. Act 40's section 7 is titled "an independent
   control". Both sides use the same `rows[b][a]` convention, so none of these controls can detect the
   alignment dependence. At (1,1,1) and (−1,−1,−1), act 40's control values (18, 2) are the defective
   counts.
3. **Equivariance controls too weak to catch it.** The sorted alignment is not equivariant under the
   stabilizer. Act 37 l.555 and act 38 l.618 transport only P, H(−1) and H(u5), where the transported
   sorted search happens to agree. Transporting SIG's k3/k5 pair would have exposed k5.
4. **Vacuous component in act 38, l.541.** The first element `any(x[2] == GEN_ONE for x in [])` iterates
   an empty list and is constantly `False`. The generic-u non-admission is carried by components 2–3.
   This defect is unrelated to alignment, but it is a vacuous control component under a label that claims
   it.

***

## `verification/lean/dita_hierarchy_probe.py` (act 36)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| H1 | 256 | `print('== 2. Diţă factorizations by exhaustive search over block structures ==')` | b≠ | The section contains SIG's 4×4 control (4 exact; 5 over all alignments). | `print('== 2. Diţă factorizations by exhaustive search over block structures, the rows of each class in sorted order ==')` |
| H2 | 314 | `'%s-Diţă %dx%d at %s: (candidates, exact factorizations)'` (12 rendered lines: column/row × 4x4, 8x2, 2x8 × P, Pu(u5); values (1, 0), (1, 0), (1, 1)) | b= | P survives (supplied). Pu(u5) survives by act 37's strict exceptional set {1}, since u5 ≠ 1. | `'%s-Diţă %dx%d at %s: (candidates, exact at the sorted alignment)'` |
| H3 | 317 | `'%s-Diţă 2x8 at %s: the frozen blocks and row classes'` | c | A partition-level statement. The 2×8 verdict is alignment-free (m = 2). | — |
| H4 | 319 | `'%s-Diţă %dx%d at SIG = Pu(1): (candidates, exact factorizations) (control)'` (values 4x4 (5, 4), 8x2 (3, 2), 2x8 (3, 3)) | b≠ | 4x4 is (5, 5) over all alignments; 8x2 and 2x8 are unchanged. | `'%s-Diţă %dx%d at SIG = Pu(1): (candidates, exact at the sorted alignment) (control)'` |
| H5 | 353 | `print('== 4. every 4x4 Diţă hull through SIG: orientations, factor circles, exact integrability, the span ==')` | b≠ | The k5 hulls are absent, and so are hulls at other exact alignments of k1–k4 (8, 64, 8, 8 alignments exact). | `print('== 4. the 4x4 Diţă hulls through SIG at the sorted alignment: orientations, factor circles, exact integrability, the span ==')` |
| H6 | 439 | `'4x4 Diţă hulls through SIG (orientations × circle choices)'` → 492 | b? | Being recounted. | `'4x4 Diţă hulls through SIG at the sorted alignment (orientations × circle choices)'` |
| H7 | 469 | `'every hull tangent in ker DF and D²F vanishing exactly on every hull (failures)'` → 0 | b? | The k5 hulls and the other alignments were not tested. | `'every sorted-alignment hull tangent in ker DF and D²F vanishing exactly on every sorted-alignment hull (failures)'` |
| H8 | 470 | `'every hull tangent has dimension 14 mod gauge'` → [14] | b? | Same as H7. | `'every sorted-alignment hull tangent has dimension 14 mod gauge'` |
| H9 | 472 | `'the span of all 4x4 hull tangents mod gauge equals the defect'` → 49 | b= | Survives. The sorted subset already spans 49 = dim ker DF − 31, which bounds any set of hull tangents. | `'the span of the sorted-alignment 4x4 hull tangents mod gauge equals the defect'` |
| H10 | 646 | `'dita_hierarchy_probe: OK -- P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has its 4x4 factorizations; W is an exact straight line at SIG; the 492 4x4 hulls through SIG span the 49-dimensional defect space; the stabilizer …'` | b≠ | "the 492 4x4 hulls" is presented as the complete set. The P / Pu(u5) clause coincides with the all-alignment result. | `'dita_hierarchy_probe: OK -- with the rows of each class in sorted order, P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has four exact 4x4 factorizations of five candidates per orientation; W is an exact straight line at SIG; the 492 sorted-alignment 4x4 hulls through SIG span the 49-dimensional defect space; the stabilizer …'` (tail unchanged) |
| H11 | 322, 581 and sections 1, 3, 5, 6 | `'== 3. the first-order census at SIG: …'`, `'== 6. the second-order form and the obstruction census =='`, and the defect, T_c/T_r, stabilizer and sector checks | c | "census" there means the first- and second-order defect census. It is alignment-free (fixed-pairing T_c/T_r, the stabilizer). | — |

The module docstring (l.1–15) contains no census claim (c; not counted separately).

## `verification/lean/dita_arc_exclusivity_probe.py` (act 37)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| X1 | 7–8 | `Its first part is act 36's probe head, verbatim, for the shared objects and act 36's exhaustive structure search.` | b? | The search is exhaustive over partitions but tests one alignment. | `Its first part is act 36's probe head, verbatim, for the shared objects and act 36's structure search, exhaustive over column blocks and row classes and testing each at the sorted alignment (the rows of each class in sorted order).` |
| X2 | 294–297 | `"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials: …` | b? | Same as X1. | `"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the rank-one condition at the sorted alignment, on a matrix of monomials: …` |
| X3 | 343 | `print('== 1. the census: every Diţă structure of the stratum point, and its classes modulo the stabilizer ==')` | b≠ | 18/9 sorted versus 20/10. | `print('== 1. the census at the sorted alignment: the Diţă structures of the stratum point with the rows of each class in sorted order, and their classes modulo the stabilizer ==')` |
| X4 | 362 | `'exact structures of SIG by shape and form: 4x4, 8x2, 2x8, each column and row'` → (4, 4, 2, 2, 3, 3) | b≠ | (5, 5, 2, 2, 3, 3) | `'exact structures of SIG at the sorted alignment by shape and form: 4x4, 8x2, 2x8, each column and row'` |
| X5 | 363 | `'every structure reconstructs SIG exactly from its factors, with trivial twist'` | b? | k5 was not tested. | `'every sorted-alignment structure reconstructs SIG exactly from its factors, with trivial twist'` |
| X6 | 364 | `'the column-form and row-form structures coincide as index sets (SIG symmetric)'` | b? | Same as X5. | `'the column-form and row-form sorted-alignment structures coincide as index sets (SIG symmetric)'` |
| X7 | 390 | `'the stabilizer (order 1024, with transposition) permutes the 18 structures; orbit count and sizes'` → (9, [2]\*9) | b≠ | 10 classes of 2 | `'the stabilizer (order 1024, with transposition) permutes the 18 sorted-alignment structures; orbit count and sizes'` |
| X8 | 391 | `'each orbit pairs a structure with its own transpose and identifies nothing else'` | b? | This is over the 18 sorted structures only. | `'each orbit of the sorted-alignment structures pairs a structure with its own transpose and identifies nothing else'` |
| X9 | 393 | `'the frozen 2x8 class is one orbit: column and row forms of the frozen blocks and classes'` | c | A named class; 2×8 is alignment-free. | — |
| X10 | 395 | `'the other classes: four 4x4, two 8x2, two 2x8'` | b≠ | Over all alignments there are five 4×4 classes. | `'the other classes at the sorted alignment: four 4x4, two 8x2, two 2x8'` |
| X11 | 406 | `'P admits exactly the frozen class (column form; the row form is the same by symmetry)'` | b= | Survives (supplied). | `'at the sorted alignment P admits exactly the frozen class (column form; the row form is the same by symmetry)'` |
| X12 | 407 | `'Pu(u5) admits exactly the frozen class'` | b= | Survives by the strict exceptional set {1}. | `'at the sorted alignment Pu(u5) admits exactly the frozen class'` |
| X13 | 410 | `print('== 3. the generic arc point, and the obstruction monomial of each other class ==')` | b? | "each other class" means the eight sorted classes; k5 was not tested. | `print('== 3. the generic arc point, and the obstruction monomial of each other sorted-alignment class ==')` |
| X14 | 412 | `'structures at a generic u (u a free symbol): (candidates, exact) by shape'` → ((1, 0), (1, 0), (1, 1)) | b= | Survives: a generic exact 4×4 or 8×2 would contradict the strict exceptional set {1}. | `'structures at a generic u (u a free symbol): (candidates, exact at the sorted alignment) by shape'` |
| X15 | 413 | `'the one exact generic structure is the frozen 2x8 class'` | b= | Same as X14. | `'the one exact generic structure at the sorted alignment is the frozen 2x8 class'` |
| X16 | 435 | `'each other class imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'` | b? | The eight named classes only. | `'each of the eight other sorted-alignment classes imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'` |
| X17 | 455 | `'the kernel witness identity of each other class is forced by its Diţă form, has rational entries and exponent sums {0, 1}'` | b? | The eight named classes (`k1 … t3`). | `'the kernel witness identity of each of the eight named other classes is forced by its Diţă form, has rational entries and exponent sums {0, 1}'` |
| X18 | 458 | `print('== 4. the candidate exceptional set: every point where an extra proportionality or the rank-one condition of a generic candidate appears ==')` | b? | `E_rank` uses the sorted rank-one condition. The all-alignment candidate set is not supplied. | `print('== 4. the candidate exceptional set: every point where an extra proportionality, or the sorted-alignment rank-one condition of a generic candidate, appears ==')` |
| X19 | 491 | `'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at u = 1 only'` | b? | Same as X18. | `'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at the sorted alignment at u = 1 only'` |
| X20 | 493 | `'the candidate exceptional set, exactly (twenty points)'` | b? | Same as X18. | `'the candidate exceptional set of the sorted-alignment calculus, exactly (twenty points)'` |
| X21 | 497 | `print('== 5. the exhaustive search at every candidate point: the exact exceptional set ==')` | b= | {1} survives. | `print('== 5. the search at the sorted alignment at every candidate point: the exceptional set at the sorted alignment ==')` |
| X22 | 502 | `'at u = 1 the search returns the eighteen structures: (candidates, exact) by shape'` → ((5, 4), (3, 2), (3, 3)) | b≠ | 4x4 (5, 5); 20 structures | `'at u = 1 the search at the sorted alignment returns eighteen structures: (candidates, exact) by shape'` |
| X23 | 503 | `'at u = -1 the proportionality candidates are those of u = 1, but only the frozen class is exact'` | b= | Survives ({1} strict). | `'at u = -1 the proportionality candidates are those of u = 1, but at the sorted alignment only the frozen class is exact'` |
| X24 | 504 | `'at every candidate point other than u = 1, exactly the frozen class is admitted'` | b= | Same as X23. | `'at every candidate point other than u = 1, exactly the frozen class is admitted at the sorted alignment'` |
| X25 | 505 | `'THE EXACT EXCEPTIONAL SET IS {1}: outside the candidates the structure is the generic one, at the candidates the search decides'` | b= | {1} survives. The label also uses capitals for emphasis. | `'the exceptional set at the sorted alignment is {1}: outside the candidates the structure is the generic one, at the candidates the search decides'` |
| X26 | 517 | `'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates'` | b? | Both sides use the sorted alignment, so this is not a control on alignment. | `'the numeric search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates, both at the sorted alignment'` |
| X27 | 518 (comment), 538 | `# genuine deformations: each other class, …` / `'a genuine deformation inside each other class (one twist phase u5): unitary, off SIG, and found by the search in its own class'` → [(True, True, True)]\*8 | b? | The eight named classes. | `'a genuine deformation inside each of the eight other sorted-alignment classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` (comment: `# genuine deformations: each of the eight other sorted-alignment classes, …`) |
| X28 | 555 | `'the membership classifier commutes with three stabilizer elements (product, transposed, conjugating): the transported frozen class is the one structure found'` | b= | Survives (P). | `'… : the transported frozen class is the one structure found at the sorted alignment'` |
| X29 | 556–560 | the perturbed-index-map controls | c | Named maps only; a 2×8 statement. | — |
| X30 | 215 | `print("== 0. act 36's stabilizer of SIG in G_ext, replayed for the census ==")` | c | The stabilizer does not depend on the alignment. | — |
| X31 | 245–252 | the comment `# … A Dita structure (column blocks, row classes) is admitted at u iff finitely many monomial equations hold: the row proportionality on every block and the rank-one condition on the block ratios. …` | b? | "admitted iff" holds for a *given index map*. A structure given as (column blocks, row classes) needs the alignment too. | `# … A Dita structure (column blocks, row classes, and an alignment of the rows within classes) is admitted at u iff finitely many monomial equations hold: …` |
| X32 | 566 | `'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG the eighteen Diţă structures form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes is admitted only where u = 1, the candidate exceptional set of the monomial calculus has twenty points, and the exhaustive search at each of them finds only the frozen class away from u = 1: the exact exceptional set is {1}'` | b≠ | 18/9 and "eight other" are sorted counts; {1} coincides. | `'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG, with the rows of each class in sorted order, the eighteen Diţă structures found form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes found is admitted only where u = 1, the candidate exceptional set of the sorted-alignment monomial calculus has twenty points, and the search at the sorted alignment at each of them finds only the frozen class away from u = 1: the exceptional set at the sorted alignment is {1}'` |

## `verification/lean/dita_local_escape_probe.py` (act 38)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| L1 | 7–8 | `Its first part is act 37's probe head, verbatim: act 36's objects and exhaustive structure search, act 36's stabilizer, and act 37's monomial calculus.` | b? | Same as X1. | `… act 36's objects and structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment), act 36's stabilizer, and act 37's monomial calculus.` |
| L2 | 294 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| L3 | 407 | `print('== 2. class exclusions: the eighteen census structures, each admitted only at u = 1 ==')` | b≠ | The census has 20 structures. The checks cover the 18 named ones. | `print('== 2. class exclusions: the eighteen structures of the sorted-alignment census, each admitted only at u = 1 ==')` |
| L4 | 414 | `"act 37's census replayed: the nine column-form structures of SIG are exactly the frozen classes' index sets"` | b≠ | 10 column-form structures | `"act 37's sorted-alignment census replayed: the nine column-form structures of SIG at the sorted alignment are exactly the frozen classes' index sets"` |
| L5 | 415 | `'the row-form structures are the same index sets (SIG symmetric)'` | b? | This is the sorted row-form set. | `'the row-form structures at the sorted alignment are the same index sets (SIG symmetric)'` |
| L6 | 446 | `'each of the eighteen structures imposes non-identity conditions, all of the form u^k = 1 with trivial constant part'` | b? | The eighteen named structures. | `'each of the eighteen named structures imposes non-identity conditions, all of the form u^k = 1 with trivial constant part'` |
| L7 | 447, 448, 469, 470 | the per-structure counts, "admitted at u = 1 alone", "rational constants for seventeen of the eighteen", "the one non-rational witness" | c | These are computations over the named list `CLASSES` and carry no census claim once L3/L6 are scoped. | — |
| L8 | 473, 475, 547 | `'== 3. all-index exhaustion: at a generic u no index maps whatever pass the proportionality test =='`; `(0, 0)` at generic u; `'at generic u: no candidates at all (section 3), …'` | c | Proportionality does not depend on the alignment, so zero candidates means no structure at any index map. | — |
| L9 | 478 | `print('== 4. the exceptional set: every point at which any structure could appear, decided by the exhaustive search ==')` | b= | The first half survives: the candidate set comes from proportionality alone and is complete. The "exhaustive search" part is sorted. | `print('== 4. the exceptional set: every point at which any structure could appear, decided by the search at the sorted alignment ==')` |
| L10 | 499, 500 | `'the candidate exceptional set, exactly (forty points), both forms together'`; `'twenty of the candidates are Gaussian rational, …'` | c | `E_all` here is `E_cand` only (proportionality), which does not depend on the alignment. | — |
| L11 | 513 | `'at u = 1 the search returns the eighteen structures: (candidates, exact) by form and shape'` → (5, 4), (3, 2), (3, 3) | b≠ | 4x4 is (5, 5) per form. | `'at u = 1 the search at the sorted alignment returns eighteen structures: (candidates, exact) by form and shape'` |
| L12 | 514 | `'at u = -1 exactly one 2x8 structure per form is admitted: (candidates, exact) by form and shape'` → 4x4 (1, 0) | b≠ | Over all alignments, 4x4 is (1, 1) per form and there are four structures (verified above). | `'at u = -1 the search at the sorted alignment admits exactly one 2x8 structure per form: (candidates, exact) by form and shape'` |
| L13 | 517 | `'the two structures at u = -1: index maps outside the census, blocks by column parity in the column form'` | b≠ | There are four structures at −1. "Outside the census" survives, because every 2×8 structure of SIG is exact at every alignment. | `'the two 2x8 structures at u = -1: index maps outside the census, blocks by column parity in the column form'` |
| L14 | 518 | `'THE EXACT EXCEPTIONAL SET IS {1, -1}: the units at which some index maps admit a Diţă form of H(u) in some orientation'` | b= | {1, −1} survives. The label also uses capitals for emphasis. | `'the exceptional set at the sorted alignment is {1, -1}: the units at which a sorted-alignment index map admits a Diţă form of H(u) in some orientation'` |
| L15 | 519 | `'and the same up to diagonal equivalence: the units at which a proportionality candidate satisfies the relaxed rank-one condition'` | b= | Same as L14. | `'and the same up to diagonal equivalence: the units at which a proportionality candidate satisfies the relaxed rank-one condition at the sorted alignment'` |
| L16 | 520 | `'at u = 1 and u = -1 the relaxed structures are the strict ones'` | b? | The supplied table establishes strict = relaxed for act 40 only. | `'at u = 1 and u = -1 the relaxed structures at the sorted alignment are the strict ones'` |
| L17 | 523 | `print('== 5. sharpness: the structures at u = 1 and u = -1 are certified by exact reconstruction ==')` | b≠ | The two 4×4 structures at −1 and k5 at 1 are not reconstructed. | `print('== 5. sharpness: the nine census classes at u = 1 and the two 2x8 structures at u = -1 are certified by exact reconstruction ==')` |
| L18 | 538 | `'at u = -1: H(-1) is reconstructed exactly … at the column-form maps, and H(-1)^T at the row-form maps'` | c | Named maps (M_COL, M_ROW). | — |
| L19 | 539 | `'at u = -1 the numeric exhaustive search with factor unitarity finds exactly these two structures and nothing of the other shapes'` | b≠ | Over all alignments it also finds one 4×4 per form. | `'at u = -1 the numeric search at the sorted alignment, with factor unitarity, finds exactly these two structures and nothing of the other shapes'` |
| L20 | 540 | `'at u = 1: SIG is reconstructed exactly at every one of the nine census structures, and H(1) = SIG'` | b≠ | The census has ten classes. | `'at u = 1: SIG is reconstructed exactly at every one of the nine sorted-alignment census classes, and H(1) = SIG'` |
| L21 | 541 | `'the structures at u = -1 are not admitted at generic u nor at u = 1 (the exceptional structures are isolated)'` | b≠ | Only M_COL/M_ROW are checked. Component 1 (`any(… for x in [])`) is vacuous. | `'the two 2x8 structures at u = -1 are not admitted at generic u nor at u = 1 (they are isolated)'` |
| L22 | 546 | `'the set of units at which H(u) admits any Diţă structure, of any shape, index map or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}; every other unit is a realizable non-Diţă point'` | b= | {1, −1} survives, but this computation tested one index map per structure. | `'at the sorted alignment, the set of units at which H(u) admits a Diţă structure, of any shape or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}'` |
| L23 | 560 | `'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twenty Gaussian-rational candidates, both forms'` | b? | Both sides are sorted. | `'the numeric search (with factor unitarity) agrees with the symbolic one at all twenty Gaussian-rational candidates, both forms, both at the sorted alignment'` |
| L24 | 577 | `'a genuine deformation inside each of the nine classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` | b? | The nine named classes. | `'a genuine deformation inside each of the nine sorted-alignment census classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` |
| L25 | 578–581 | `# … the transported matrices at u = -1 and u5 are searched directly, as act 37's control does: two structures at u = -1 (one per orientation), none at u5` | b≠ | Four at −1 | `# … searched directly at the sorted alignment, as act 37's control does: two structures at u = -1 (one per orientation), none at u5` |
| L26 | 618 | `'… the transported matrices admit exactly two structures at u = -1 and none at u5'` | b≠ | Four at −1 | `'the exponent matrix transported by three stabilizer elements (product, transposed, conjugating) is straight and admits no candidate at generic u; at the sorted alignment the transported matrices admit exactly two structures at u = -1 and none at u5'` |
| L27 | 628 | `'the three pieces and their pairwise sums are straight lines, each admitting some census structure identically; the triple admits none (interpretation: three Diţă directions whose sum is not Diţă)'` | b? | The lists cover the 18 named structures; k5 was not tested. "The triple admits none" survives absolutely because of L8. | `'the three pieces and their pairwise sums are straight lines, each admitting some structure of the sorted-alignment census identically; the triple admits none (interpretation: three Diţă directions whose sum is not Diţă)'` |
| L28 | 630 | `"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure (control of the classifier)"` | b= | Survives: an identically admitted structure would contradict {1} strict. | `"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure of the sorted-alignment census (control of the classifier)"` |
| L29 | 693 | `'the witness exponent matrix is tangent (it is straight) and lies in none of the eighteen subspaces, while the tangent space is the sum of all eighteen: the obstruction is nonlinear compatibility, not a missing tangent direction'` | b? | The value 80 survives. Whether E lies in k5's subspace is not computed. | `'the witness exponent matrix is tangent (it is straight) and lies in none of the eighteen named structures\' subspaces, while the tangent space is the sum of those eighteen: the obstruction is nonlinear compatibility, not a missing tangent direction'` |
| L30 | 692, 687, section 8 title | per-class tangent dimensions; the tangent-space rank | c | Named classes; alignment-free. | — |
| L31 | 699 | `'dita_local_escape_probe: OK -- … each of the eighteen census structures is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation'` | b≠ | "eighteen census structures" is a sorted count. {1, −1} coincides. | `'dita_local_escape_probe: OK -- along the arc H(u) = SIG o u^E through the certified stratum point, E = A + B + C the frozen exponent matrix: H(u) is a complex Hadamard matrix at every unit u; each of the eighteen structures of the sorted-alignment census is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the search at the sorted alignment at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: at the sorted alignment, for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape or orientation'` |

## `verification/lean/dita_torus_probe.py` (act 39)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| T1 | 5–6 | `Its first part is act 38's probe head, verbatim: act 36's objects and exhaustive structure search, act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.` | b? | Same as X1. The search is carried but not used by any act-39 check. | `… act 36's objects and structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment), act 36's stabilizer, …` |
| T2 | 291 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| T3 | all checks, l.212 section 0, OK line l.462–465 | realizability, joint level sets, subfamilies, countercontrol | c | No Diţă-structure claim. Act 39 states that it says nothing about Diţă loci. | — |

The act-39 edits are docstring-only, so this probe passes `probe_replay_check` against D41.

## `verification/lean/dita_torus_locus_probe.py` (act 40)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| Y1 | 5–7 | `Its first part is act 38's probe head, verbatim: act 36's objects, exhaustive structure search and stabilizer, …` | b? | Same as X1. | `… act 36's objects, structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment) and stabilizer, …` |
| Y2 | 287 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| Y3 | 523 | `# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe` | b≠ | 18 versus 20 at SIG; four structures at −1 | `# ---- act 37's sorted-alignment census of SIG's Dita structures and act 38's two 2x8 exceptional index maps, verbatim from act 38's probe` |
| Y4 | 544–545, 636, 638, 639 | `"""every (orientation, shape, column blocks, row classes) whose within-class pairs have, on every block, a common point of their proportionality loci; a structure admitted anywhere on T^3 is among them …"""`; `'== 2. completeness: every Dita structure admitted anywhere is among the enumerated candidates =='`; 13/5/5 per orientation; 46 | c | The candidates come from proportionality only, which is alignment-free, and the set is complete. | — |
| Y5 | 642 | `print('== 3. locus exactness: each candidate strictly and up to diagonal equivalence ==')` | b? | Each candidate's locus is computed at one alignment. | `print('== 3. locus exactness: each candidate at the sorted alignment, strictly and up to diagonal equivalence ==')` |
| Y6 | 644 | `'the relaxed locus equals the strict locus for every candidate'` | b= | Survives (supplied). | `'the relaxed locus equals the strict locus for every candidate at the sorted alignment'` |
| Y7 | 645 | `'empty and nonempty strict loci'` → (16, 30) | b≠ | (3, 43) | `'empty and nonempty strict loci at the sorted alignment'` |
| Y8 | 646 | `'every nonempty locus is cut out by coordinate characters u_k = +-1 alone'` → True | b≠ | **False** over all alignments: four loci are non-coordinate points inside faces. This is the one value that inverts. | `'every nonempty sorted-alignment locus is cut out by coordinate characters u_k = +-1 alone'` |
| Y9 | 649 | `print('== 4. union reduction: the union of the loci is five coordinate 2-subtori ==')` | b= | The five-face union survives. | `print('== 4. union reduction: the union of the sorted-alignment loci is five coordinate 2-subtori ==')` |
| Y10 | 651, 652, 658 | `'the maximal loci'`; `'every nonempty locus lies in one of them, and each of them is itself a locus'`; the diagonal restriction | c | The maximal loci and the containments are unchanged: the four extra loci are points inside faces, and each face is still a locus. | — |
| Y11 | 663 | `'at (1, 1, 1): eighteen structures, exactly act 37 census in both orientations'` → (18, True) | b≠ | 20 | `'at (1, 1, 1) at the sorted alignment: eighteen structures, exactly act 37 census in both orientations'` |
| Y12 | 664 | `'at (-1, -1, -1): one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'` | b≠ | 4 | `'at (-1, -1, -1) at the sorted alignment: one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'` |
| Y13 | 666, 679, 682, 727, 728 | the absent face u2 = −1, the +1 faces as act 39 subfamilies, the kernel-layer title, the whole-face factorizations | c | The union is unchanged; these are named structures. | — |
| Y14 | 704 | `'for each of the twenty named structures (the census in both orientations, M_COL, M_ROW), single four-position witnesses …'` | b? | The named list is correct, but "the census" means the sorted census, and "twenty" collides with the all-alignment census count of 20. | `'for each of the twenty named structures (the sorted-alignment census in both orientations, M_COL, M_ROW), single four-position witnesses …'` |
| Y15 | 731 | `print('== 7. an independent control: act 36\'s exhaustive structure search, with factor unitarity, at exact points ==')` | b? | This control is not independent of the loci with respect to alignment, since both use `rows[b][a]`. | `print('== 7. a control: act 36\'s structure search at the sorted alignment, with factor unitarity, at exact points ==')` |
| Y16 | 748 | `'at seventeen exact points (two generic, the five faces, two absent directions, three lines, five special points) the search finds exactly the predicted structures'` → counts [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4] | b≠ | At least (1,1,1) → 20 and (−1,−1,−1) → 4. The other counts are not supplied. | `'at seventeen exact points (…) the search at the sorted alignment finds exactly the predicted sorted-alignment structures'` |
| Y17 | 755 | `'the classifier applied to the perturbed pieces: candidates, nonempty loci and the union, which collapses to the one face where C drops out'` → (30, 23, ['u3 = 1'], True) | b? | 23 is a sorted count. The all-alignment count is not supplied. | `'the classifier at the sorted alignment applied to the perturbed pieces: candidates, nonempty loci and the union, which collapses to the one face where C drops out'` |
| Y18 | 761–765 | `'dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the 30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1'` | b≠ | 30 → 43. The five-face conclusion coincides. | `'dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted anywhere is among 46 enumerated candidates; their strict and relaxed loci at the sorted alignment are computed exactly and agree; the union of the 30 nonempty sorted-alignment loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so at the sorted alignment H3 admits a Dita structure of some shape and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1'` |
| Y19 | 208 | `print("== 0. act 36's stabilizer of SIG in G_ext, replayed for the census ==")` | c | The stabilizer does not depend on the alignment. | — |

***

## Lean modules — `verification/lean-mathlib/OIBridge/` (module-header comments only)

| id | file:line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| LH1 | `DitaHierarchy.lean:6–13` | `…an outer factor on α, inner factors on β, a twist, and any bijections of α × β with the product carrier for rows and for columns — realizable for flat unitary factors and unit twists; …` | c | A kernel statement over any bijections. | — |
| LH2 | `DitaHierarchy.lean:14–16` | ``The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either orientation under any relabelling: the `4 × 4` hierarchy is locally insufficient at the stratum, and the first escaping family belongs to the `2 × 8` construction.`` | a\* | The content survives (supplied), but act 36's layer tested one alignment. | Unchanged once the all-alignment search is a probe of the layer. Otherwise: ``Exact computation over every index map shows that `P` admits no `4 × 4` Diţă factorization of either orientation: …`` (the rest unchanged, citing that computation) |
| LA1 | `DitaArcExclusivity.lean:11–13` | ``and, for each of the eight other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two `2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — that a Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.`` | a | "Complete census" is false: there are nine other classes (five 4×4). | ``and, for each of eight named other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two `2 × 8` — that a Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.`` |
| LA2 | `DitaArcExclusivity.lean:13–15` | ``The exact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps whatever admit a Diţă form of `Pu u` but the frozen class's.`` | a\* | The content survives ({1} strict). Act 37's probe tested one alignment. | ``Exact computation over every index map carries the exhaustive complement: at every unit `u ≠ 1`, no index maps whatever admit a Diţă form of `Pu u` but the frozen class's.`` |
| LE1 | `DitaLocalEscape.lean:10–14` | ``that for each of the nine Diţă factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a realizable matrix admitting none of the eighteen forms.`` | a | "Complete census" is false: there are ten classes. "The eighteen forms" then reads as all forms; the kernel corollary is about the named ones. | ``that for each of nine named Diţă factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8` — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a realizable matrix admitting none of their eighteen forms.`` |
| LE2 | `DitaLocalEscape.lean:14–15` | ``The exact-computation layer carries the exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,`` | a\* | The content survives ({1, −1}). | ``Exact computation over every index map carries the exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,`` |
| LE3 | `DitaLocalEscape.lean:16` | ``and at `u = −1` exactly one `2 × 8` structure per orientation does.`` | a | False: at u = −1 there is one 2×8 and one 4×4 structure per orientation (four in all; verified above). | ``and at `u = −1` exactly one `2 × 8` and one `4 × 4` structure per orientation do.`` |
| LT1 | `DitaTorus.lean:12–13` | ``It says nothing about which points of the torus admit a Diţă structure.`` | c | No dependency. | — |
| LL1 | `DitaTorusLocus.lean:11–13` | ``For each of twenty named index maps — act 37's nine classes in both orientations and act 38's two maps `M_COL` and `M_ROW` — a strict Diţă form of `H3` at that map forces the named coordinate equations.`` | c | A kernel statement over named maps. "Act 37's nine classes" is a reference to named classes. | — (optional: "act 37's nine named classes") |
| LL2 | `DitaTorusLocus.lean:13–15` | ``The module does not state that the five faces exhaust the points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.`` | a\* | The content survives (five faces). The round's probe tested one alignment. | ``… that converse, over every shape, index map and orientation and up to diagonal equivalence, is certified by exact computation over every index map, not by the kernel.`` |
| LK | `OIBridge.lean:220–225` | `import OIBridge.Dita…` | c | Import lines only. | — |

## `verification/lean-manuscript-census.json` (the five families; "name" and "note")

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| J1 | 1212 (A36 name) | `the Diţă factorization hierarchy at the product-embedded stratum — Diţă's construction over any factorization of the sixteen-point carrier realizable in both forms, its 2 × 8 and 8 × 2 instances, an exact 2 × 8 family through the certified rational stratum point, and a named point of it off the stratum (act 36, Track B)` | c | Kernel content only. | — |
| J2 | 1218 (A36 note) | `the exhaustive block-structure searches, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding the known factorizations of the stratum point;` | a\* | The point values survive. The searches are not exhaustive over index maps, and "the known factorizations" are 4 of 5 4×4 per orientation. | `the block-structure searches with the rows of each class in sorted order, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding four of the five 4 × 4 factorizations of the stratum point in each orientation;` |
| J3 | 1218 | `the 492 4 × 4 Diţă hulls through the stratum point spanning its 49-dimensional defect at first order;` | b? | Being recounted; the span survives. | `the 492 4 × 4 Diţă hulls through the stratum point at the sorted alignment, spanning its 49-dimensional defect at first order;` |
| J4 | 1218 | `These are exact arithmetic replayed, not kernel-certified; by them the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.` | a\* | The conclusion survives (P admits no 4×4 at any index map), but a one-alignment search does not reach it. | `These are exact arithmetic replayed, not kernel-certified; by them, and by exact computation over every index map at the named point, the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.` |
| J5 | 1221 (A37 name) | `… and each of the eight other factorization classes of the stratum point admitted only at the base point (act 37, Track B)` | a | "The eight other" implies completeness; there are nine. | `… and each of eight named other factorization classes of the stratum point admitted only at the base point (act 37, Track B)` |
| J6 | 1227 (A37 note) | `and for each of the eight other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Pu u …` | a | "Complete census" is false. | `and for each of eight named other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8 — a Diţă form of Pu u …` |
| J7 | 1227 | `the census of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;` | b≠ | 20 in 10 | `the census, at the sorted alignment, of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;` |
| J8 | 1227 | `the generic arc point admitting exactly the frozen class; each other class obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of twenty exactly named points ζ z^s w^t;` | b= | The generic statement survives. "Each other class" means the eight named. The candidate set is sorted-derived. | `the generic arc point admitting exactly the frozen class; each of the eight named other classes obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of the sorted-alignment calculus, twenty exactly named points ζ z^s w^t;` |
| J9 | 1227 | `and the exhaustive search at each of them admitting only the frozen class away from u = 1, so that the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.` | a\* | The content survives ({1} strict). The cited probe tested one alignment. | `and the search at the sorted alignment at each of them admitting only the frozen class away from u = 1; by exact computation over every index map the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.` |
| J10 | 1230 (A38 name) | `… each of the nine factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of the eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)` | a | "The nine" implies completeness; there are ten. | `… each of nine named factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of their eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)` |
| J11 | 1236 (A38 note) | `for each of the nine Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Hu u …` | a | "Complete census" is false. | `for each of nine named Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8 — a Diţă form of Hu u …` |
| J12 | 1236 | `the eighteen exclusions and their forced witness identities; that at a generic u no index maps whatever pass the proportionality test in either orientation; the candidate exceptional set of forty exactly named points ζ z^s w^t` | c | Named exclusions. Proportionality and the candidate set do not depend on the alignment. | — |
| J13 | 1236 | `and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;` | a | "The two structures at u = −1" is false: there are four. The {1, −1} content survives but is cited to a one-alignment search (a\*). | `and the search at the sorted alignment at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two 2 × 8 structures at u = −1 certified by exact reconstruction; by exact computation over every index map the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;` |
| J14 | 1236 | `and the tangent space at SIG, of dimension 80, spanned by the eighteen first-order Diţă subspaces, so that the escape is a nonlinear compatibility obstruction.` | b= | The span (80) survives. "The eighteen" reads as all structures. | `and the tangent space at SIG, of dimension 80, spanned by the first-order subspaces of the eighteen named structures, so that the escape is a nonlinear compatibility obstruction.` |
| J15 | 1236 | `and every neighbourhood of SIG contains a realizable matrix admitting none of the eighteen forms (a38_c_local_escape)` | c | A kernel corollary over the named forms. It reads correctly once J11 names the classes. | — |
| J16 | 1239, 1245 (A39) | name; `Nothing is claimed about which points of the three-torus admit a Diţă structure, about the exponent matrices with entries in {0, 1}, about the minimality of support 48, …` | c | No dependency. | — |
| J17 | 1248 (A40 name) | `… are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation (act 40, Track B)` | c | The five faces survive. The name says "exact computation" without naming the round's probe. It is supported once the all-alignment computation exists. | — |
| J18 | 1254 (A40 note) | `The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by the round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard: 46 candidate structures contain every structure admitted anywhere, their strict and relaxed loci coincide, and the union of the 30 nonempty loci is exactly the five faces.` | a\* | The content survives. The round's probe is one-alignment, and "30 nonempty loci" is sorted (43 over all alignments). | `The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by exact computation over every index map; the round's probe verification/lean/dita_torus_locus_probe.py, run in its own shard, shows that 46 candidate structures contain every structure admitted anywhere and computes each candidate's strict and relaxed loci at the sorted alignment, which coincide and whose 30 nonempty members have the five faces as union.` |
| J19 | 1254 | `and at twenty named index maps — act 37's nine classes in both orientations and act 38's M_COL and M_ROW — a strict Diţă form of H3 forces the named coordinate equations` | c | Named maps. | — |

Families for acts 36–40 carry `"manuscript": []`, so no manuscript anchor depends on these notes.

## `verification/ROADMAP.md`

### P0 cell (line 63; each segment verified verbatim against its act's `preregistration.md`)

| id | round | exact text | kind | status | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| R1 | A36 | ``At the product configuration, Diţă's construction over every factorization of the sixteen-point carrier, in the column and the row form, is realizable for every choice of flat unitary factors, unit twist phases and row and column bijections; an exact one-parameter family of `2 × 8` column Diţă matrices runs through the certified rational stratum point, every member realizable, and its named point at `u₆₀ = (60+i)/(60−i)` is a realizable class off the stratum;`` | d | Kernel content survives. | No change. |
| R2 | A36 | ``and, by the round's exact-computation probe, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;`` | d | The content survives (supplied). The attribution is to a one-alignment probe. | ``and, by exact computation over every index map, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;`` |
| R3 | A37 | ``and, by the kernel for the eight other factorization classes of the stratum point and by the round's exact-computation probe for every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;`` | d | "The eight other" implies completeness (there are nine). The attribution is to a one-alignment probe. The conclusion survives. | ``and, by the kernel for eight named other factorization classes of the stratum point and by exact computation over every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;`` |
| R4 | A38 | ``each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:`` | d | "The nine" implies completeness (there are ten). The attribution is to a one-alignment probe. {1, −1} survives. | ``each of nine named Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by exact computation over every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:`` |
| R5 | A38 | `The tangent space at the stratum point is spanned by the eighteen Diţă tangent subspaces, so the escape is a nonlinear compatibility obstruction and not a missing tangent direction.` | d | The span survives. "The eighteen" reads as all structures. | `The tangent space at the stratum point is spanned by the Diţă tangent subspaces of the eighteen named structures, so the escape is a nonlinear compatibility obstruction and not a missing tangent direction.` |
| R6 | A39 | ``For act 38's three exponent pieces `A`, `B`, `C`, the three-parameter family … is realizable at every point of the three-torus, by the kernel, …; Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, …`` | d | No dependency. | No change. |
| R7 | A40 | ``For act 39's three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, the points of the three-torus at which it admits a Diţă structure, of any shape, index map and orientation and up to diagonal equivalence, are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.`` | d | The five faces survive. The attribution is to a one-alignment probe. | ``… and the exclusions at twenty named index maps by the kernel, and the converse over every index map by exact computation.`` |

The standing clauses after each sentence ("Nothing here classifies …", "The census of exponent matrices …
support 48 stay open …") do not depend on the census.

### Future-direction sections

| id | line | exact text | kind | status | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| R9 | 1195–1196 | `and for the classification of each against the eighteen Diţă structures of the point: which lie identically in some structure and which in none.` | a | The point has twenty structures in ten classes. | `and for the classification of each against the Diţă structures of the point: which lie identically in some structure and which in none.` |
| R10 | 1210–1211 | `Whether a straight line through the certified stratum point that lies identically in none of the eighteen Diţă structures can have smaller support, …` | a | Same as R9. | `Whether a straight line through the certified stratum point that lies identically in none of the Diţă structures of the point can have smaller support, …` |
| R11 | 1224–1226 | `` Act 38's probe records, as a control of its classifier and not as a theorem, that `A`, `B`, `C` and their pairwise sums are straight lines each lying identically in some Diţă structure of the point while `A + B + C` lies in none.`` | c | "Lies in some" holds via named structures. "A + B + C lies in none" holds at every index map, because at generic u there are no proportionality candidates (L8). | — |
| R12 | 1215 | `which does not presuppose the full census` | c | This refers to the straight-line census. | — |

## Other in-scope files

| file | occurrence | kind | reason |
| --- | --- | --- | --- |
| `.github/workflows/verify.yml:213–269` | job names `Numerical probes / A36 hierarchy`, `… / A38 escape`, `… / A40 locus`; step `A40 Dita-locus probe`; no comments | c | Neutral names with no census claim. |
| `verification/README.md`, `tools/`, `papers/`, `book/` | no Diţă content ("eighteen" hits concern seals, contracts and primes) | — | Not counted. |

***

## Notes for the correction round

- Each **b≠ / b= / b?** probe row is a change to a label, title, docstring or OK line. No check *value*
  changes, so each computation remains a sorted-alignment regression control. The exception is Y8, whose
  value is correct only as a sorted value. None of these label changes is replay-neutral under
  `tools/probe_replay_check.py` as written (see the replay section).
- The **a\*** rows all cite "the round's exact-computation probe" or "the exhaustive search" for a
  conclusion that holds over every index map. Each needs the all-alignment search to exist as a cited
  artifact. The replacements name it generically ("exact computation over every index map") and must be
  tied to that probe when it lands. Without it, the only supported wording is the sorted scope, and
  LH2, R2 and J4 would then lose the "locally insufficient" conclusion.
- **LE3 and J13** carry the only outright false statement of a count outside the probes (two structures
  at u = −1, versus four). **LA1, LE1, J5, J6, J10, J11, R3, R4, R9 and R10** carry "complete census",
  "the eight / nine classes" or "the eighteen structures" as a completeness claim.
- The two 4×4 structures at u = −1 on act 38's arc have a partition that is none of SIG's five 4×4
  candidates. They are new classes, not k5. k5 is not a proportionality candidate at u = −1.
