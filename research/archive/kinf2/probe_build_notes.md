# kinf2_foundations_probe.py: build notes

## Replay

| item | value |
| --- | --- |
| probe file | `kinf2/kinf2_foundations_probe.py` (869 lines; sha256 `fe76a97b698beb497c9ca5db41a99b0e717c987065da365c888566028db872dc`) |
| interpreter | Python 3.11.15, sympy 1.14.0 |
| checks run (N) | **192**: identity 25, witness 55, enumerate 16, sample 96. The 15 `NOTE [written]` lines are not counted |
| last line | `kinf2_foundations_probe: OK -- 192 checks` |
| stdout | 224 lines, 23141 bytes |
| sha256 of stdout | `7eb66142dd766ea256c61b898e9687307c36e5e642f0da2f9c03bed34f061f0a` |
| runtime | 1.08 s and 1.11 s (wall clock, two consecutive runs) |
| determinism | both runs byte-identical (`cmp` on the two outputs); same sha256 under `PYTHONHASHSEED` = 0, 1, 12345 |
| failure path | in-memory mutations of `pent.aut_count`, `pent.capacity_le_2` and `c2.not_centrally_symmetric` each print `kinf2_foundations_probe: FAILED <name> -- ...` and exit 1 |

Imports: `sys`, `fractions`, `itertools`, `sympy`. No floating point, randomness, time, file or network I/O.

## Section map

`A` = `threads/A/a_controls.py`, `D` = `threads/D/d3_route3_frames.py`, `K1` = `wt-kinf1/verification/lean/kinf_foundations_probe.py`.
Check names are `s<N>.<source name>`. Each source check's kind is now the leading `[kind]` tag of its detail.

| new section | probe lines | source lines | checks | notes |
| --- | --- | --- | --- | --- |
| shared helpers | 63-290 | A 42-140 (Q3, linear algebra, `circle`, `CIRCLE_U`, `SPHERE`, polytope boundary); K1 44-114 (Q3 `is_zero`, merged into A's class); D 91-127 (Q5, `det3`, `solve3`); D 161-171 generalized as `poly_affine_auts`; `distinguishable_vertex_triples` new | - | - |
| 1. identities | 294-309 | A 143-158 (A §0) | 3 | 0 |
| 2. unit and non-proper effects | 311-338 | A 160-183 (A §1) | 5 | 0 |
| 3. square gbit, with 3b frozen vs corrected drivability | 340-419 | A 185-264 (A §2, §2b) | 27 | 1 |
| 4. torus | 421-455 | A 266-296 (A §3) | 9 | 1 |
| 5. Stiefel | 457-480 | A 298-321 (A §4) | 6 | 0 |
| 6. 3-ball, with 6b the disk | 482-550 | A 323-384 (A §5, §5b) | 22 | 3 |
| 7. SIC ball | 552-584 | A 386-418 (A §6) | 7 | 3 |
| 8. Caratheodory C₂ | 586-674 | K1 117-127 (COS, SIN, 12-point `CIRCLE_U`, local to the section), K1 181-228 (K1 §2) | 87 | 1 |
| 9. regular pentagon | 676-768 | D 115-152 (P, convex position, frames), D 161-176 (automorphisms, frame orbit, pure transitivity), D 182-196 (edge effect, Gram self-duality) | 13 | 2 |
| 10. degenerate bodies | 770-790 | A 420-441 (A §7) | 2 | 3 |
| 11. route neutrality, with 11b Lean convention | 792-809 | A 444-461 (A §9, §9b) | 3 | 1 |
| 12. countercontrols | 811-865 | A 463-505 (A §8, (a)-(f)); (g), (h) new | 8 | 0 |

`D/exact_la.py` supplies only `rank` and `nullspace` to D's Lemma I computations for the square, torus,
Stiefel body and ball. The pentagon block does not use them, so nothing from that file was merged.

Totals reconcile. A's 90 checks (identity 20, witness 40, enumerate 6, sample 24) are all present
with unchanged verdicts, and its 12 written notes are kept as `NOTE` lines. K1 §2's 83 checks are
present with unchanged names and verdicts. The 19 new checks are listed below. 90 + 83 + 19 = 192.

## Changes to checks (and why)

**Renamed**
- The 12 checks `ball.face.<point>` (A 339) are now named with `pt()` (`ball.face.(3/5,4/5,0)`)
  instead of the tuple of `Fraction` reprs. The old names contained spaces, so the output could
  not be split into fields. Points and verdicts are unchanged.

**Strengthened**
- `c2.capacity3` was `check(..., True, ...)` in K1 228, which is vacuous. It is now the conjunction
  of three things:
  - the three points are pairwise distinct;
  - `c2.unit` holds, and all nine `c2.delta` checks hold;
  - the three new symbolic identities hold.

  The verdict is the same, but it now rests on computation.

**Text changed, verdicts unchanged**
- A's internal section references in detail text were renumbered to the new sections: A §0 → 1,
  2b → 3b, A §5 → 6, A §6 → 7, A §7 → 10.
- Two references to private design documents were dropped from note text:
  - "as K-INF-DESIGN section 3 intends" (`sq.corrected.not_drivable`);
  - "(section 11)" (`torus.verdict`).
- "candidate L5, L7" now reads "L5, L7", to match the labels in `kinf2/KInfFoundations.lean`.

**Written notes now go through `note()`.** A's `check(..., True, 'written', ...)` calls are now `note()`.
They print `NOTE [written] ...`, as before, and are still not counted.

**New checks (19)**

| check | kind | reason |
| --- | --- | --- |
| `s8.c2.product_identity.symbolic.{0,1,2}` | identity | Without these, C₂'s capacity three rests on 12 sample points. Each checks the product identity for e_i over the whole circle: sympy, rational parametrization in Q(√3), plus the point t = π. That makes e_i ≥ 0 on C₂, and so the capacity-three witness, decisive. |
| `s8.c2.not_centrally_symmetric` | witness | K1 asserts this only in its docstring. The check is e_0(−x(0)) = −1/3 < 0. Note `c2.centre_is_0` gives the written step from the centre 0 to every centre. |
| `s9.pent.affine_regular` | identity | D's coordinates are an affine image of the regular pentagon. This certifies that image: centroid 0, the recurrence P_{k+1}+P_{k-1} = 2cos72·P_k, and P_0, P_1 independent. Without it, D's regular-coordinate Gram matrix would not be tied to D's P. |
| `s9.pent.convex_position`, `pent.frames`, `pent.aut_count`, `pent.frame_transitive`, `pent.pure_transitive`, `pent.strongly_self_dual`, `pent.edge_effect.valid` | as tagged | D 130, 152, 172-176, 187 and 196 were `assert` statements or printed booleans. They are now checks, with the same logic. |
| `s9.pent.capacity_ge_2`, `pent.edge_effect.proper`, `pent.SF_fails` | witness | These were implicit in D. Each is now explicit, with the effect values evaluated. |
| `s9.pent.capacity_le_2` | enumerate | D argued this only in writing (RESULT 3e). It is now an exhaustive barycentric test over all 10 vertex triples. Note `pent.capacity_reduction` gives the reduction from arbitrary states to vertices. |
| `s9.pent.not_centrally_symmetric` | enumerate | This was absent from D. None of the 10 enumerated automorphisms has linear part −I. |
| `s12.cc.pent_enumeration_finds_point_reflection` | enumerate | A countercontrol for the new enumeration: on the square it finds 8 automorphisms, including x ↦ −x. |
| `s12.cc.capacity_test_detects_simplex` | enumerate | A countercontrol for the new capacity test: on a triangle listed with two edge midpoints it finds the corner triple. |

**Omitted from the D pentagon block**
- D 153-160: every frame has an ideal measure-and-prepare test.
- D 177-181: spectrality fails at the centroid.
- D 197-208: the ideal compression of the edge effect is not positive.
- D 209: the output-file write, which would also break the no-I/O rule.

These are D's route-3 facts. None of them is among the requested pentagon facts.

## Scope stated in the docstring

The claim "corrected drivability excludes the square gbit and the disk" is checked only through
`s3.sq.aut_count`, the eight affine automorphisms of the square. For the disk the probe has only
the reflection conjugation identity, `s6.disk.corrected.J_normalizes`. The exclusion itself is a
written argument, recorded as `NOTE s3.sq.corrected.not_drivable`. The docstring says this,
naming the disk's identity check explicitly, because the disk has no automorphism enumeration.
