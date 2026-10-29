# Fixed-interface regress and ancillary revision

Guiding draft: #998; review requirements: PR comment 6498003796. Parent source: `5bdb72d6bdf801b410ea108110f406e1847b99aa`; pinned main: `ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`.

## Scope and preserved results

Theorem 24(iii) now states the finite coherent-channel identity cited by the regress discussion: an independently prepared normalized ancillary density matrix, fixed visible/hidden interface, and exactly decoupled product dynamics. Its partial-trace proof is written explicitly; this is not a new Lean certificate. Hidden-uniform relabelling in (i), the alphabet hypothesis in (ii), the structural status of (iv), nearest-neighbour premise and recovered local results are unchanged.

The direct regress argument and its immediate summaries distinguish fixed-interface redundancy from unresolved hidden-state facts or a complete classification of implementations. The deep-sector comparison does not establish infinite normalized preparations or total-carrier finiteness from an accessible-sector bound. The effective-finiteness corollary retains grade GAP and mapping `not formalized`; only its statement fingerprint is reaffirmed, `2a8021590988a99b` to `4f8577fff9f60573`.

## Review dispositions

- Blocker 1: Chapter 3:34 relates some equivalent substrata; generator completeness stays open. FULL is mirrored.
- Blocker 2: Substratum:235/424 and SM:1368 no longer assert an all-measurements undecidability theorem about metaphysical interpretation. Substratum:432/438/533 receive the same scope.
- Blocker 3: direct deep-sector cardinality, all-partitions and all-measurements claims in ch02:44/134/172, ch04:172, Explainer:946 and Substratum:60/92/249 are replaced by fixed-interface comparisons and their hypotheses. Structure:86/154/692 are scoped likewise.
- Citation item 4: the finite coherent ancillary result and proof are explicit in Theorem 24(iii), not merely asserted by its callers.
- Items 5–6: alphabet wording and the gauge/incompleteness comparison at ch03:80/132/234 are narrowed; ch03:152 is stated without revision-history narration.
- Items 8–9: Explainer:902 does not treat regress as an unproved theorem; the exact finite decoupled factor adds no distinction to the fixed channel.

## Complete-argument review follow-up

The independent source review of checkpoint `550d826f44ad73e0ed38e6555606d060e04b3a87` confirmed the finite coherent ancillary identity and requested three additional direct-chain repairs. The current source uses Proposition 24.5's nonempty record-fibre criterion in ch03:138/144/148, ch02:42 and Explainer:944/948, explicitly separating informational non-identifiability from computational resource bounds. Proper embedding alone is not a blanket prediction impossibility. Substratum:52/54, Explainer:892/906/908/910 and ch02:32 now distinguish finite OI results, the observed-sector bound, and separately specified infinite extensions. Both theorem proof openings refer to the specified data under stated hypotheses. The unchanged ancillary equation is split across aligned rows for publication margins.

## Explicit residual assignments under #981 / #946

These are not closed or accepted by this correction. Locations below refer to the parent source unless noted. They require separate clause-by-clause mathematical/physical assessment and propagation; historical PR incorporation is insufficient.

| Residual source | Assigned obligation |
|---|---|
| Methodology:43, 323, 357, 371, 427, 433, 453, 473, 477, 479, 489, 499–501 | Replace or justify the broader gauge-classification, empty-question and substrate-computability claims. The fixed-interface ancillary identity does not establish exhaustive classification or a no-go on arbitrary calculations of a chosen representative. This includes the proof/statement distinction at §21 and downstream computation consumers. |
| Structure:346, 374 and the all-class transport/universality arguments | Assess claims that the displayed families classify every within-class equivalence and transport all observable structure. Fixed-interface examples alone do not establish such a classification. |
| Complexity:198 and its structural-chain transport consumers | Assess whether each listed generator preserves the specific physical input, including the conditional alphabet branch. No full chemistry/complexity transport theorem is supplied here. |
| Substratum §4's full variable-carrier gauge-group formalization and alphabet branch | Specify admissible interfaces, their correspondences, and the algebraic organization of enlargement/removal on different carriers. The finite coherent identity does not prove generator exhaustiveness or all-partitions equivalence. |
| Infinite ancillary extensions | Supply a normalized measure or trace-class state, well-defined evolution and observation map before asserting an infinite-extension equality. Finite uniform counting supplies none of these by itself. |

No residual in this table is counted as fixed on main. #998 is not closure of #981, #992 or #946, and #918 remains unchanged and held.

## Checkpoint status

WIP / UNVERIFIED source revision. Generated TeX/PDF publications are STALE until canonical rebuilds and selected-page inspection complete. Independent review must read the complete revised regress argument, not only changed paragraphs. Fresh ordinary PR CI and separate owner approval remain required; no merge, closure, special dispatch or designation is authorized.
