# ---- follow-up overrides (coordinator items 1-6); executed inside build_ledger41.py before verification
def _idx(id_):
    return next(i for i, e in enumerate(ENTRIES) if e['id'] == id_)
def REPLACE(id_, path, old, new, kind, reason):
    ENTRIES[_idx(id_)] = {'id': id_, 'path': path, 'old': old, 'new': new, 'kind': kind, 'reason': reason}
def INSERT_AFTER(after, id_, path, old, new, kind, reason):
    ENTRIES.insert(_idx(after) + 1, {'id': id_, 'path': path, 'old': old, 'new': new, 'kind': kind, 'reason': reason})

PR, IN, HU = ('verification/lean/dita_index_map_probe.py', 'verification/lean/dita_index_map_independent.py',
              'verification/lean/dita_index_map_hulls.py')

# item 5: act 41's probes cited by their repository paths
REPLACE('H12', H, "Its first part is act 35's probe head, verbatim, for the shared objects.\n",
  "Its first part is act 35's probe head, verbatim, for the shared objects.\n"
  "Its Diţă searches test each partition structure at the sorted alignment (the rows of each row class in sorted\n"
  "order); the censuses over every index map are act 41's probes %s,\n%s and\n%s.\n" % (PR, IN, HU),
  'docstring', "module docstring: scope of the searches and the pointer to act 41's probes (new row; the census counts the docstring as c)")
REPLACE('X1', X, "act 36's exhaustive structure search.\n",
  "act 36's structure search, exhaustive over column blocks and row classes and testing each partition structure at the\n"
  "sorted alignment (the rows of each row class in sorted order). The censuses over every index map are act 41's probes\n"
  "%s and %s.\n" % (PR, IN),
  'docstring', "census X1: module docstring re-scoped, with the pointer to act 41's probes")
REPLACE('L1', L, "act 36's objects and exhaustive\nstructure search, act 36's stabilizer, and act 37's monomial calculus.\n",
  "act 36's objects and structure search\n(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment), act 36's\n"
  "stabilizer, and act 37's monomial calculus. The censuses over every index map are act 41's probes\n"
  "%s and %s.\n" % (PR, IN),
  'docstring', "census L1: module docstring re-scoped, with the pointer to act 41's probes")
REPLACE('Y1', Y, "act 36's objects, exhaustive structure search and stabilizer, act 37's monomial calculus and act 38's\n"
                 "pieces. It asserts the preregistered values and exits 1 on any mismatch; it certifies nothing beyond the arithmetic it replays.\n",
  "act 36's objects, structure search\n"
  "(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment) and\n"
  "stabilizer, act 37's monomial calculus and act 38's pieces. It asserts the preregistered values and exits 1 on any\n"
  "mismatch; it certifies nothing beyond the arithmetic it replays. The loci over every index map are act 41's probes\n"
  "%s and %s.\n" % (PR, IN),
  'docstring', "census Y1: module docstring re-scoped, with the pointer to act 41's probes")

# item 1: measured verdicts under flags
REPLACE('LH2', LH,
  "The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either\n"
  "orientation under any relabelling: the `4 × 4` hierarchy is locally insufficient at the stratum,\n"
  "and the first escaping family belongs to the `2 × 8` construction.",
  "[[Exact computation over every index map (act 41) shows that `P` admits no `4 × 4` Diţă\n"
  "factorization of either orientation: the `4 × 4` hierarchy is locally insufficient at the stratum,\n"
  "and the first escaping family belongs to the `2 × 8` construction. | Exact computation over every index map\n"
  "(act 41) finds a `4 × 4` or `8 × 2` Diţă factorization at `P` or at the family's point `u = (3+4i)/5`,\n"
  "strictly or up to diagonal equivalence, with {p.p44} `4 × 4` and {p.p82} `8 × 2` partition structures per\n"
  "orientation at `P`, strictly. : p.no_44_82]]",
  'docstring', 'census LH2: the verdict under the flag p.no_44_82, attributed to exact computation over every index map (act 41)')
REPLACE('LA2', LA,
  "The\nexact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps\n"
  "whatever admit a Diţă form of `Pu u` but the frozen class's.",
  "[[Exact\ncomputation over every index map (act 41) carries the exhaustive complement: at every unit `u ≠ 1`, no\n"
  "index maps whatever admit a Diţă form of `Pu u` but those of the frozen `2 × 8` partition structure. | Exact\n"
  "computation over every index map (act 41) finds the arc not exclusive to the frozen `2 × 8` partition\n"
  "structure away from `u = 1`, strictly; its strict exceptional set is `{w.exc_strict}`. : w.exclusive]]",
  'docstring', 'census LA2: the complement under the flag w.exclusive, attributed to act 41')
REPLACE('LL2', LL,
  "The module does not state that the five faces exhaust the\npoints admitting a Diţă structure: that converse, over every shape, index map and orientation and up to\n"
  "diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.",
  "[[The module does not state that the five faces exhaust the\npoints admitting a Diţă structure: that converse, over every shape, index map and orientation and up to\n"
  "diagonal equivalence, is certified by exact computation over every index map (acts 40 and 41), not by the\n"
  "kernel. | The module does not state which points outside the five faces admit a Diţă structure: exact\n"
  "computation over every index map (act 41), not the kernel, finds the union of the loci, over every shape,\n"
  "index map and orientation and up to diagonal equivalence, to be the flats {h3.maximal}. : h3.five_faces]]",
  'docstring', 'census LL2: the converse under the flag h3.five_faces, attributed to acts 40 and 41')
REPLACE('R2', R,
  "and, by the round's exact-computation probe, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;",
  "and, [[by exact computation over every index map (act 41), that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy | by exact computation over every index map (act 41), that point, of defect 37, or the family's point at `u₅ = (3+4i)/5` admits a `4 × 4` or `8 × 2` Diţă factorization, strictly or up to diagonal equivalence, with {p.p44} `4 × 4` and {p.p82} `8 × 2` partition structures per orientation at the named point, strictly : p.no_44_82]];",
  'roadmap', 'census R2: the P0 verdict under the flag p.no_44_82, attributed to act 41')
REPLACE('R4', R,
  "each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:",
  "each of nine named Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by exact computation over every other index map (act 41), the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter [[outside `{1, −1}`, strictly or up to diagonal equivalence | outside `{e.exc_strict}` strictly, or outside `{e.exc_relaxed}` up to diagonal equivalence : e.exc_is_pm1]]:",
  'roadmap', "census R4: completeness reading removed; the exceptional set under the flag e.exc_is_pm1, from act 41's measurement")
REPLACE('R7', R,
  "are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.",
  "[[are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse by exact computation over every index map (acts 40 and 41). | include the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`, with the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and, by exact computation over every index map (act 41), form the union of the flats {h3.maximal}. : h3.five_faces]]",
  'roadmap', 'census R7: the P0 verdict under the flag h3.five_faces; the converse attributed to acts 40 and 41')
REPLACE('J4', J,
  "These are exact arithmetic replayed, not kernel-certified; by them the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.",
  "These are exact arithmetic replayed, not kernel-certified. [[By exact computation over every index map (act 41), both points admit no 4 × 4 and no 8 × 2 Diţă factorization of either orientation, strictly or up to diagonal equivalence, and, strictly, {p.partitions} partition structures each, all of shape 2 × 8, so the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction. | Exact computation over every index map (act 41) finds a 4 × 4 or 8 × 2 Diţă factorization at one of the two points, strictly or up to diagonal equivalence, with {p.p44} 4 × 4 and {p.p82} 8 × 2 partition structures per orientation at the named point, strictly. : p.no_44_82]]",
  'registry', 'census J4: the conclusion under the flag p.no_44_82, attributed to act 41')
REPLACE('J13', J,
  "and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;",
  "and the search at the sorted alignment at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two 2 × 8 partition structures it finds at u = −1 certified by exact reconstruction; by exact computation over every index map (act 41) the arc point admits no Diţă structure of any admissible shape, index map or orientation at any unit [[outside {1, −1}, strictly or up to the allowed diagonal equivalences | outside {e.exc_strict} strictly, and none up to the allowed diagonal equivalences at any unit outside {e.exc_relaxed} : e.exc_is_pm1]], with {e.m1} partition structures at u = −1;",
  'registry', "census J13: act 38's search scoped; the exceptional set under the flag e.exc_is_pm1 and the count at u = −1 from act 41's measurement")
# item 6: hull counts stated separately
REPLACE('J3', J, "the 492 4 × 4 Diţă hulls through the stratum point spanning its 49-dimensional defect at first order;",
  "the 492 4 × 4 Diţă hull parametrizations through the stratum point at the sorted alignment, whose tangents span its 49-dimensional defect at first order, while over every valid alignment exact computation over every index map (act 41) finds {hull.params} parametrizations, {hull.distinct_mat} distinct 4 × 4 hulls as matrix families and, counted separately, {hull.distinct_gauge} distinct 4 × 4 hulls modulo the gauge, with tangent dimensions modulo the gauge in {hull.dims}, [[every distinct hull inside the linearized and second-order unitarity conditions | not every distinct hull inside the linearized and second-order unitarity conditions : hull.dF_ok]], and their tangents spanning {hull.span} dimensions;",
  'registry', "census J3: act 36's count scoped as parametrizations at the sorted alignment; act 41's hull counts, matrix-family and modulo-gauge, stated separately")
# item 3: the converse attributed to acts 40 and 41, consistently
REPLACE('J18', J, ENTRIES[_idx('J18')]['old'],
  "The round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard, shows that 46 partition candidates contain every Diţă structure admitted anywhere and computes each candidate's strict and relaxed loci at the sorted alignment, which coincide and whose 30 nonempty members have the five faces as union. The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — [[is certified by exact computation over every index map (acts 40 and 41), act 40's enumeration supplying the candidates and act 41 their loci under every alignment | fails under exact computation over every index map (act 41), which finds the flats {h3.maximal} as the union of the loci : h3.five_faces]]: {h3.candidates} partition candidates, {h3.nonempty} of them with nonempty loci, [[strict and relaxed loci equal for every candidate | strict and relaxed loci differing : h3.strict_eq_relaxed]], and {h3.noncoord} of the loci's {h3.flats} distinct flats off the coordinate characters.",
  'registry', "census J18: act 40's probe scoped to the sorted alignment; the converse under the flag h3.five_faces, attributed to acts 40 and 41")
INSERT_AFTER('J14', 'J17', J,
  "are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation (act 40, Track B)",
  "[[are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation over every index map (acts 40 and 41) | include the five faces u₁ = ±1, u₂ = 1, u₃ = ±1, with explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, and by exact computation over every index map (act 41) form the union of the flats {h3.maximal} : h3.five_faces]] (act 40, Track B)",
  'registry', 'census J17 (c, edited by owner direction): the converse attributed to acts 40 and 41, the verdict under the flag h3.five_faces')
# item 2: act 37's nine classes named as the kernel's named index maps
INSERT_AFTER('J18', 'J19', J,
  "act 37's nine classes in both orientations and act 38's M_COL and M_ROW",
  "the nine named index maps of act 37's sorted-alignment census, in both orientations, and act 38's M_COL and M_ROW",
  'registry', "census J19 (c, edited by owner direction): act 37's nine classes named as the kernel's named index maps")
INSERT_AFTER('LE3', 'LL1', LL,
  "act\n37's nine classes in both orientations and act 38's two maps `M_COL`",
  "the nine\nnamed index maps of act 37's sorted-alignment census, in both orientations, and act 38's two\nmaps `M_COL`",
  'docstring', "census LL1 (c, edited by owner direction): act 37's nine classes named as the kernel's named index maps")
