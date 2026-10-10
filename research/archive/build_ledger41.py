"""Builds ledger41.json (scratch builder; not part of the deliverable)."""
import json, subprocess, sys

REPO = '/home/user/incompleteness'
D41 = '78ea3c39004e97aad027ee6153051c6d372bdd55'
OUT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a41draft/ledger/ledger41.json'

H = 'verification/lean/dita_hierarchy_probe.py'
X = 'verification/lean/dita_arc_exclusivity_probe.py'
L = 'verification/lean/dita_local_escape_probe.py'
T = 'verification/lean/dita_torus_probe.py'
Y = 'verification/lean/dita_torus_locus_probe.py'
LH = 'verification/lean-mathlib/OIBridge/DitaHierarchy.lean'
LA = 'verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean'
LE = 'verification/lean-mathlib/OIBridge/DitaLocalEscape.lean'
LL = 'verification/lean-mathlib/OIBridge/DitaTorusLocus.lean'
J = 'verification/lean-manuscript-census.json'
R = 'verification/ROADMAP.md'

ENTRIES = []
def E(id_, path, old, new, kind, reason):
    ENTRIES.append({'id': id_, 'path': path, 'old': old, 'new': new, 'kind': kind, 'reason': reason})

# the structure-search docstring shared by the four heads (X2, L2, T2, Y2)
DOC_OLD = '"""the exhaustive Dita structure search (act 36\'s, section 2) on a matrix of monomials:'
DOC_NEW = ('"""the Dita structure search (act 36\'s, section 2), exhaustive over column blocks and row classes and testing the\n'
           '    rank-one condition at the sorted alignment, on a matrix of monomials:')
# the monomial-calculus comment shared by the four heads (X31 and its mirrors)
COM_OLD = '# structure (column blocks, row classes) is admitted at u iff'
COM_NEW = '# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at\n# u iff'

# ================= act 36: dita_hierarchy_probe.py =================
E('H12', H, "Its first part is act 35's probe head, verbatim, for the shared objects.\n",
  "Its first part is act 35's probe head, verbatim, for the shared objects.\n"
  "Its Diţă searches test each partition structure at the sorted alignment (the rows of each row class in sorted\n"
  "order); the censuses over every index map are act 41's probes dita_index_map_probe.py,\n"
  "dita_index_map_independent.py and dita_index_map_hulls.py.\n",
  'docstring', 'module docstring: scope of the searches and the pointer to act 41\'s probes (new row; the census counts the docstring as c)')
E('H1', H, "print('== 2. Diţă factorizations by exhaustive search over block structures ==')",
  "print('== 2. Diţă factorizations by exhaustive search over block structures, the rows of each row class in sorted order ==')",
  'string', 'census H1: section title re-scoped to the sorted alignment')
E('H2', H, "at %s: (candidates, exact factorizations)'",
  "at %s: (candidates, exact at the sorted alignment)'",
  'string', 'census H2: check label re-scoped')
E('H4', H, "at SIG = Pu(1): (candidates, exact factorizations) (control)'",
  "at SIG = Pu(1): (candidates, exact at the sorted alignment) (control)'",
  'string', 'census H4: check label re-scoped; SIG has five admitted 4x4 partition structures per orientation under every index map')
E('H5', H, "print('== 4. every 4x4 Diţă hull through SIG: orientations,",
  "print('== 4. the 4x4 Diţă hulls through SIG at the sorted alignment: orientations,",
  'string', 'census H5: section title re-scoped')
E('H6', H, "'4x4 Diţă hulls through SIG (orientations × circle choices)'",
  "'4x4 Diţă hull parametrizations through SIG at the sorted alignment (orientations × circle choices)'",
  'string', 'census H6: label re-scoped; the value counts parametrizations (Hazard 7)')
E('H7', H, "'every hull tangent in ker DF and D²F vanishing exactly on every hull (failures)'",
  "'every sorted-alignment hull tangent in ker DF and D²F vanishing exactly on every sorted-alignment hull (failures)'",
  'string', 'census H7: label re-scoped')
E('H8', H, "'every hull tangent has dimension 14 mod gauge'",
  "'every sorted-alignment hull tangent has dimension 14 mod gauge'",
  'string', 'census H8: label re-scoped')
E('H9', H, "'the span of all 4x4 hull tangents mod gauge equals the defect'",
  "'the span of the sorted-alignment 4x4 hull tangents mod gauge equals the defect'",
  'string', 'census H9: label re-scoped')
E('H10', H,
  "print('dita_hierarchy_probe: OK -- P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has its 4x4 factorizations; W is an exact straight line at SIG; the 492 4x4 hulls through SIG span",
  "print('dita_hierarchy_probe: OK -- with the rows of each row class in sorted order, P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has four exact 4x4 factorizations of five candidates per orientation; W is an exact straight line at SIG; the 492 sorted-alignment 4x4 hull parametrizations through SIG span",
  'string', 'census H10: success text re-scoped (tail unchanged)')

# ================= act 37: dita_arc_exclusivity_probe.py =================
E('X1', X, "act 36's exhaustive structure search.\n",
  "act 36's structure search, exhaustive over column blocks and row classes and testing each partition structure at the\n"
  "sorted alignment (the rows of each row class in sorted order). The censuses over every index map are act 41's probes\n"
  "dita_index_map_probe.py and dita_index_map_independent.py.\n",
  'docstring', 'census X1: module docstring re-scoped, with the pointer to act 41\'s probes')
E('X31', X, COM_OLD, COM_NEW, 'string', 'census X31: comment; admission is decided for a given alignment (comment only, invisible to ast)')
E('X2', X, DOC_OLD, DOC_NEW, 'docstring', 'census X2: search docstring re-scoped')
E('X3', X, "print('== 1. the census: every Diţă structure of the stratum point, and its classes modulo the stabilizer ==')",
  "print('== 1. the census at the sorted alignment: the Diţă partition structures of the stratum point with the rows of each row class in sorted order, and their partition orbits under the stabilizer ==')",
  'string', 'census X3: section title re-scoped; act 37\'s classes are partition orbits (Hazard 10)')
E('X4', X, "'exact structures of SIG by shape and form: 4x4, 8x2, 2x8, each column and row'",
  "'exact partition structures of SIG at the sorted alignment by shape and form: 4x4, 8x2, 2x8, each column and row'",
  'string', 'census X4: label re-scoped')
E('X5', X, "'every structure reconstructs SIG exactly from its factors, with trivial twist'",
  "'every sorted-alignment partition structure reconstructs SIG exactly from its factors, with trivial twist'",
  'string', 'census X5: label re-scoped')
E('X6', X, "'the column-form and row-form structures coincide as index sets (SIG symmetric)'",
  "'the column-form and row-form sorted-alignment partition structures coincide as index sets (SIG symmetric)'",
  'string', 'census X6: label re-scoped')
E('X7', X, "'the stabilizer (order 1024, with transposition) permutes the 18 structures; orbit count and sizes'",
  "'the stabilizer (order 1024, with transposition) permutes the 18 partition structures admitted at the sorted alignment; partition-orbit count and sizes'",
  'string', 'census X7: label re-scoped')
E('X8', X, "'each orbit pairs a structure with its own transpose and identifies nothing else'",
  "'each partition orbit of the sorted-alignment restriction pairs a partition structure with its own transpose and identifies nothing else'",
  'string', 'census X8: label re-scoped')
E('X10', X, "'the other classes: four 4x4, two 8x2, two 2x8'",
  "'the other partition orbits of the sorted-alignment restriction: four 4x4, two 8x2, two 2x8'",
  'string', 'census X10: label re-scoped; the eight are partition orbits of the sorted-alignment restriction')
E('X11', X, "'P admits exactly the frozen class (column form; the row form is the same by symmetry)'",
  "'at the sorted alignment P admits exactly the frozen 2x8 partition structure (column form; the row form is the same by symmetry)'",
  'string', 'census X11: label re-scoped')
E('X12', X, "'Pu(u5) admits exactly the frozen class'",
  "'at the sorted alignment Pu(u5) admits exactly the frozen 2x8 partition structure'",
  'string', 'census X12: label re-scoped')
E('X13', X, "print('== 3. the generic arc point, and the obstruction monomial of each other class ==')",
  "print('== 3. the generic arc point, and the obstruction monomial of each other named index map of the sorted-alignment census ==')",
  'string', 'census X13: section title re-scoped')
E('X14', X, "'structures at a generic u (u a free symbol): (candidates, exact) by shape'",
  "'partition structures at a generic u (u a free symbol): (candidates, exact at the sorted alignment) by shape'",
  'string', 'census X14: label re-scoped')
E('X15', X, "'the one exact generic structure is the frozen 2x8 class'",
  "'the one exact generic partition structure at the sorted alignment is the frozen 2x8 partition structure'",
  'string', 'census X15: label re-scoped')
E('X16', X, "'each other class imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'",
  "'each of the eight other named index maps of the sorted-alignment census imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'",
  'string', 'census X16: label names the eight index maps tested')
E('X17', X, "'the kernel witness identity of each other class is forced by its Diţă form,",
  "'the kernel witness identity of each of the eight other named index maps is forced by its Diţă form,",
  'string', 'census X17: label names the eight index maps tested')
E('X18', X, "print('== 4. the candidate exceptional set: every point where an extra proportionality or the rank-one condition of a generic candidate appears ==')",
  "print('== 4. the candidate exceptional set: every point where an extra proportionality, or the sorted-alignment rank-one condition of a generic candidate, appears ==')",
  'string', 'census X18: section title re-scoped')
E('X19', X, "'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at u = 1 only'",
  "'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at the sorted alignment at u = 1 only'",
  'string', 'census X19: label re-scoped')
E('X20', X, "'the candidate exceptional set, exactly (twenty points)'",
  "'the candidate exceptional set of the sorted-alignment calculus, exactly (twenty points)'",
  'string', 'census X20: label re-scoped')
E('X21', X, "print('== 5. the exhaustive search at every candidate point: the exact exceptional set ==')",
  "print('== 5. the search at the sorted alignment at every candidate point: the exceptional set at the sorted alignment ==')",
  'string', 'census X21: section title re-scoped')
E('X22', X, "'at u = 1 the search returns the eighteen structures: (candidates, exact) by shape'",
  "'at u = 1 the search at the sorted alignment returns eighteen partition structures: (candidates, exact) by shape'",
  'string', 'census X22: label re-scoped')
E('X23', X, "'at u = -1 the proportionality candidates are those of u = 1, but only the frozen class is exact'",
  "'at u = -1 the proportionality candidates are those of u = 1, but at the sorted alignment only the frozen 2x8 partition structure is exact'",
  'string', 'census X23: label re-scoped')
E('X24', X, "'at every candidate point other than u = 1, exactly the frozen class is admitted'",
  "'at every candidate point other than u = 1, exactly the frozen 2x8 partition structure is admitted at the sorted alignment'",
  'string', 'census X24: label re-scoped')
E('X25', X, "'THE EXACT EXCEPTIONAL SET IS {1}: outside the candidates the structure is the generic one, at the candidates the search decides'",
  "'the exceptional set at the sorted alignment is {1}: outside the candidates the partition structure is the generic one, at the candidates the search decides'",
  'string', 'census X25: label re-scoped, capitals removed')
E('X26', X, "'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates'",
  "'the numeric search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates, both at the sorted alignment'",
  'string', 'census X26: label re-scoped; both sides share the alignment rule')
E('X27c', X, "# genuine deformations: each other class, with one twist phase moved off 1, is a point of that class's hull off SIG",
  "# genuine deformations: each of the eight other named index maps, with one twist phase moved off 1, gives a point of its hull off SIG",
  'string', 'census X27 (comment): names the eight index maps')
E('X27', X, "'a genuine deformation inside each other class (one twist phase u5): unitary, off SIG, and found by the search in its own class'",
  "'a genuine deformation at each of the eight other named index maps (one twist phase u5): unitary, off SIG, and found by the search at the sorted alignment at its own partition structure'",
  'string', 'census X27: label names the eight index maps')
E('X28', X, "the transported frozen class is the one structure found'",
  "the transported frozen 2x8 partition structure is the one found at the sorted alignment'",
  'string', 'census X28: label re-scoped')
E('X32', X,
  "'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG the eighteen Diţă structures form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes is admitted only where u = 1, the candidate exceptional set of the monomial calculus has twenty points, and the exhaustive search at each of them finds only the frozen class away from u = 1: the exact exceptional set is {1}'",
  "'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG, with the rows of each row class in sorted order, the eighteen Diţă partition structures found form nine partition orbits under the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 partition structure persists identically, each of the eight other named index maps is admitted only where u = 1, the candidate exceptional set of the sorted-alignment monomial calculus has twenty points, and the search at the sorted alignment at each of them finds only the frozen 2x8 partition structure away from u = 1: the exceptional set at the sorted alignment is {1}'",
  'string', 'census X32: success text re-scoped')

# ================= act 38: dita_local_escape_probe.py =================
E('L1', L, "act 36's objects and exhaustive\nstructure search, act 36's stabilizer, and act 37's monomial calculus.\n",
  "act 36's objects and structure search\n(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment), act 36's\n"
  "stabilizer, and act 37's monomial calculus. The censuses over every index map are act 41's probes\n"
  "dita_index_map_probe.py and dita_index_map_independent.py.\n",
  'docstring', 'census L1: module docstring re-scoped, with the pointer to act 41\'s probes')
E('L32', L, COM_OLD, COM_NEW, 'string', 'mirror of census X31 in the verbatim head (comment only, invisible to ast)')
E('L2', L, DOC_OLD, DOC_NEW, 'docstring', 'census L2: search docstring re-scoped')
E('L3', L, "print('== 2. class exclusions: the eighteen census structures, each admitted only at u = 1 ==')",
  "print('== 2. named exclusions: the eighteen named index maps of the sorted-alignment census, each admitted only at u = 1 ==')",
  'string', 'census L3: section title re-scoped')
E('L4', L, "\"act 37's census replayed: the nine column-form structures of SIG are exactly the frozen classes' index sets\"",
  "\"act 37's census replayed at the sorted alignment: the nine column-form partition structures of SIG admitted there are exactly the index sets of act 37's nine named index maps\"",
  'string', 'census L4: label re-scoped')
E('L5', L, "'the row-form structures are the same index sets (SIG symmetric)'",
  "'the row-form partition structures at the sorted alignment are the same index sets (SIG symmetric)'",
  'string', 'census L5: label re-scoped')
E('L6', L, "'each of the eighteen structures imposes non-identity conditions,",
  "'each of the eighteen named index maps imposes non-identity conditions,",
  'string', 'census L6: label names the eighteen index maps')
E('L9', L, "print('== 4. the exceptional set: every point at which any structure could appear, decided by the exhaustive search ==')",
  "print('== 4. the exceptional set: every point at which any partition structure could appear, decided by the search at the sorted alignment ==')",
  'string', 'census L9: section title re-scoped')
E('L11', L, "'at u = 1 the search returns the eighteen structures: (candidates, exact) by form and shape'",
  "'at u = 1 the search at the sorted alignment returns eighteen partition structures: (candidates, exact) by form and shape'",
  'string', 'census L11: label re-scoped')
E('L12', L, "'at u = -1 exactly one 2x8 structure per form is admitted: (candidates, exact) by form and shape'",
  "'at u = -1 the search at the sorted alignment admits exactly one 2x8 partition structure per form: (candidates, exact) by form and shape'",
  'string', 'census L12: label re-scoped')
E('L13', L, "'the two structures at u = -1: index maps outside the census, blocks by column parity in the column form'",
  "'the two 2x8 partition structures found at u = -1 at the sorted alignment: index maps outside the sorted-alignment census of SIG, blocks by column parity in the column form'",
  'string', 'census L13: label re-scoped')
E('L14', L, "'THE EXACT EXCEPTIONAL SET IS {1, -1}: the units at which some index maps admit a Diţă form of H(u) in some orientation'",
  "'the exceptional set at the sorted alignment is {1, -1}: the units at which a sorted-alignment index map admits a Diţă form of H(u) in some orientation'",
  'string', 'census L14: label re-scoped, capitals removed')
E('L15', L, "satisfies the relaxed rank-one condition'",
  "satisfies the relaxed rank-one condition at the sorted alignment'",
  'string', 'census L15: label re-scoped')
E('L16', L, "'at u = 1 and u = -1 the relaxed structures are the strict ones'",
  "'at u = 1 and u = -1 the relaxed partition structures at the sorted alignment are the strict ones'",
  'string', 'census L16: label re-scoped')
E('L17', L, "print('== 5. sharpness: the structures at u = 1 and u = -1 are certified by exact reconstruction ==')",
  "print('== 5. sharpness: the nine named index maps of the sorted-alignment census at u = 1 and the two 2x8 index maps M_COL, M_ROW at u = -1 are certified by exact reconstruction ==')",
  'string', 'census L17: section title names what is reconstructed')
E('L19', L, "'at u = -1 the numeric exhaustive search with factor unitarity finds exactly these two structures and nothing of the other shapes'",
  "'at u = -1 the numeric search at the sorted alignment, with factor unitarity, finds exactly these two partition structures and nothing of the other shapes'",
  'string', 'census L19: label re-scoped')
E('L20', L, "'at u = 1: SIG is reconstructed exactly at every one of the nine census structures, and H(1) = SIG'",
  "'at u = 1: SIG is reconstructed exactly at every one of the nine named index maps of the sorted-alignment census, and H(1) = SIG'",
  'string', 'census L20: label re-scoped')
E('L21', L,
  "check('the structures at u = -1 are not admitted at generic u nor at u = 1 (the exceptional structures are isolated)', (any(x[2] == GEN_ONE for x in []) , all(x[2] == GEN_ONE for x in conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)), all(x[2] == GEN_ONE for x in conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)), admitted_points(conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)) == frozenset([PT_MINUS]), admitted_points(conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)) == frozenset([PT_MINUS])), (False, False, False, True, True))",
  "check('M_COL and M_ROW, the two 2x8 index maps at u = -1, are admitted neither at generic u nor at u = 1 (they are isolated)', (all(x[2] == GEN_ONE for x in conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)), all(x[2] == GEN_ONE for x in conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)), admitted_points(conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)) == frozenset([PT_MINUS]), admitted_points(conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)) == frozenset([PT_MINUS])), (False, False, True, True))",
  'bugfix', 'census L21: label re-scoped; the vacuous first component any(... for x in []) and its expected False removed (owner decision)')
E('L22', L, "'the set of units at which H(u) admits any Diţă structure, of any shape, index map or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}; every other unit is a realizable non-Diţă point'",
  "'at the sorted alignment, the set of units at which H(u) admits a Diţă structure, of any shape or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}'",
  'string', 'census L22: label re-scoped')
E('L23', L, "at all twenty Gaussian-rational candidates, both forms'",
  "at all twenty Gaussian-rational candidates, both forms, both at the sorted alignment'",
  'string', 'census L23: label re-scoped')
E('L24', L, "'a genuine deformation inside each of the nine classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'",
  "'a genuine deformation at each of the nine named index maps of the sorted-alignment census (one twist phase u5): unitary, off SIG, and found by the search at the sorted alignment at its own partition structure'",
  'string', 'census L24: label names the nine index maps')
E('L25', L, "# searched directly, as act 37's control does: two structures at u = -1 (one per orientation), none at u5",
  "# searched directly at the sorted alignment, as act 37's control does: two 2x8 partition structures at u = -1 (one per\n# orientation), none at u5",
  'string', 'census L25: comment re-scoped (comment only, invisible to ast)')
E('L26', L, "the transported matrices admit exactly two structures at u = -1 and none at u5'",
  "at the sorted alignment the transported matrices admit exactly two partition structures at u = -1 and none at u5'",
  'string', 'census L26: label re-scoped')
E('L27', L, "each admitting some census structure identically;",
  "each admitting some named index map of the sorted-alignment census identically;",
  'string', 'census L27: label re-scoped')
E('L28', L, "\"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure (control of the classifier)\"",
  "\"act 37's arc W is straight and identically admitted at the frozen 2x8 index map t1 in both orientations and at no other named index map of the sorted-alignment census (control of the classifier)\"",
  'string', 'census L28: label re-scoped')
E('L29', L, "lies in none of the eighteen subspaces, while the tangent space is the sum of all eighteen:",
  "lies in none of the eighteen subspaces of the named index maps, while the tangent space is the sum of those eighteen:",
  'string', 'census L29: label names the eighteen index maps')
E('L31', L,
  "each of the eighteen census structures is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation'",
  "each of the eighteen named index maps of the sorted-alignment census is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the search at the sorted alignment at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: at the sorted alignment, for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape or orientation'",
  'string', 'census L31: success text re-scoped')

# ================= act 39: dita_torus_probe.py =================
E('T1', T, "act 36's\nobjects and exhaustive structure search, act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.\n",
  "act 36's\nobjects and structure search (exhaustive over column blocks and row classes, each partition structure tested at the\n"
  "sorted alignment), act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.\n",
  'docstring', 'census T1: module docstring re-scoped')
E('T4', T, COM_OLD, COM_NEW, 'string', 'mirror of census X31 in the verbatim head (comment only, invisible to ast)')
E('T2', T, DOC_OLD, DOC_NEW, 'docstring', 'census T2: search docstring re-scoped')

# ================= act 40: dita_torus_locus_probe.py =================
E('Y1', Y, "act 36's objects, exhaustive structure search and stabilizer, act 37's monomial calculus and act 38's\n"
           "pieces. It asserts the preregistered values and exits 1 on any mismatch; it certifies nothing beyond the arithmetic it replays.\n",
  "act 36's objects, structure search\n"
  "(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment) and\n"
  "stabilizer, act 37's monomial calculus and act 38's pieces. It asserts the preregistered values and exits 1 on any\n"
  "mismatch; it certifies nothing beyond the arithmetic it replays. The loci over every index map are act 41's probes\n"
  "dita_index_map_probe.py and dita_index_map_independent.py.\n",
  'docstring', 'census Y1: module docstring re-scoped, with the pointer to act 41\'s probes')
E('Y20', Y, COM_OLD, COM_NEW, 'string', 'mirror of census X31 in the verbatim head (comment only, invisible to ast)')
E('Y2', Y, DOC_OLD, DOC_NEW, 'docstring', 'census Y2: search docstring re-scoped')
E('Y3', Y, "# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe",
  "# ---- act 37's sorted-alignment census of SIG's Dita partition structures and act 38's two 2x8 exceptional index maps,\n# verbatim from act 38's probe",
  'string', 'census Y3: comment re-scoped (comment only, invisible to ast)')
E('Y5', Y, "print('== 3. locus exactness: each candidate strictly and up to diagonal equivalence ==')",
  "print('== 3. locus exactness: each candidate at the sorted alignment, strictly and up to diagonal equivalence ==')",
  'string', 'census Y5: section title re-scoped')
E('Y6', Y, "'the relaxed locus equals the strict locus for every candidate'",
  "'the relaxed locus equals the strict locus for every candidate at the sorted alignment'",
  'string', 'census Y6: label re-scoped')
E('Y7', Y, "'empty and nonempty strict loci'",
  "'empty and nonempty strict loci at the sorted alignment'",
  'string', 'census Y7: label re-scoped')
E('Y8', Y, "'every nonempty locus is cut out by coordinate characters u_k = +-1 alone'",
  "'every nonempty sorted-alignment locus is cut out by coordinate characters u_k = +-1 alone'",
  'string', 'census Y8: label re-scoped; the value holds only at the sorted alignment')
E('Y9', Y, "print('== 4. union reduction: the union of the loci is five coordinate 2-subtori ==')",
  "print('== 4. union reduction: the union of the sorted-alignment loci is five coordinate 2-subtori ==')",
  'string', 'census Y9: section title re-scoped')
E('Y11', Y, "'at (1, 1, 1): eighteen structures, exactly act 37 census in both orientations'",
  "'at (1, 1, 1) at the sorted alignment: eighteen partition structures, exactly act 37 census in both orientations'",
  'string', 'census Y11: label re-scoped')
E('Y12', Y, "'at (-1, -1, -1): one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'",
  "'at (-1, -1, -1) at the sorted alignment: one 2 x 8 partition structure per orientation, act 38 M_COL and M_ROW'",
  'string', 'census Y12: label re-scoped')
E('Y14', Y, "'for each of the twenty named structures (the census in both orientations, M_COL, M_ROW),",
  "'for each of the twenty named index maps (the sorted-alignment census of act 37 in both orientations, M_COL, M_ROW),",
  'string', 'census Y14: label names the twenty index maps')
E('Y15', Y, "print('== 7. an independent control: act 36\\'s exhaustive structure search, with factor unitarity, at exact points ==')",
  "print('== 7. a control: act 36\\'s structure search at the sorted alignment, with factor unitarity, at exact points ==')",
  'string', 'census Y15: section title re-scoped; not independent of the loci in alignment')
E('Y16', Y, "the search finds exactly the predicted structures'",
  "the search at the sorted alignment finds exactly the predicted sorted-alignment partition structures'",
  'string', 'census Y16: label re-scoped')
E('Y17', Y, "'the classifier applied to the perturbed pieces:",
  "'the classifier at the sorted alignment applied to the perturbed pieces:",
  'string', 'census Y17: label re-scoped')
E('Y18', Y,
  "print('dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted '\n"
  "      'anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the '\n"
  "      '30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita '\n"
  "      'structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 '\n"
  "      'or u3 = +-1')",
  "print('dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted '\n"
  "      'anywhere is among 46 enumerated candidates; their strict and relaxed loci at the sorted alignment are computed exactly and '\n"
  "      'agree; the union of the 30 nonempty sorted-alignment loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, '\n"
  "      'u3 = 1, u3 = -1; so at the sorted alignment H3 admits a Dita structure of some shape and orientation, including up to '\n"
  "      'diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1')",
  'string', 'census Y18: success text re-scoped')

# ================= Lean module docstrings =================
E('LH2', LH, "The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either\n"
             "orientation under any relabelling:",
  "Exact computation over every index map (act 41) shows that `P` admits no `4 × 4` Diţă\n"
  "factorization of either orientation:",
  'docstring', 'census LH2: the conclusion re-attributed to exact computation over every index map (act 41)')
E('LA1', LA, "and, for each of the eight other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two\n"
             "`2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — that a\n"
             "Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.",
  "and, for each of eight other named factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two\n"
  "`2 × 8` — that a Diţă form of `Pu u` at its named index maps, in either orientation, forces `u = 1`.",
  'docstring', 'census LA1: removes the completeness claim; the classes are named')
E('LA2', LA, "The\nexact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps\n"
             "whatever admit a Diţă form of `Pu u` but the frozen class's.",
  "Exact\ncomputation over every index map (act 41) carries the exhaustive complement: at every unit `u ≠ 1`, no\n"
  "index maps whatever admit a Diţă form of `Pu u` but those of the frozen `2 × 8` partition structure.",
  'docstring', 'census LA2: the complement re-attributed to exact computation over every index map (act 41)')
E('LE1', LE, "that for each of the nine Diţă factorization\n"
             "classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's\n"
             "Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either\n"
             "orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a\n"
             "realizable matrix admitting none of the eighteen forms.",
  "that for each of nine named Diţă factorization\n"
  "classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8` — a Diţă form of `Hu u` at its named index\n"
  "maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG`\n"
  "contains a realizable matrix admitting none of their eighteen forms.",
  'docstring', 'census LE1: removes the completeness claim; the classes and forms are named')
E('LE2', LE, " The exact-computation layer carries the\nexhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,",
  "\nExact computation over every index map (act 41) carries the exhaustive complement: at every unit\n`u ∉ {e.exc_strict}`, no index maps whatever admit a Diţă form of `Hu u`,",
  'docstring', 'census LE2: the complement re-attributed to exact computation over every index map (act 41); the exceptional set from the measurement')
E('LE3', LE, "\nand at `u = −1` exactly one `2 × 8` structure per orientation does.",
  "\nand at `u = −1` exactly {e.m1} partition structures do, the two orientations together[[, among them in each\n"
  "orientation a `4 × 4` partition structure, the image of the partition structure of act 37's `k4` under the row\n"
  "exchange `7 ↔ 15` and the column exchange `2 ↔ 8` | : e.m1_k4_exchanged]].",
  'docstring', 'census LE3: the count at u = −1 from the measurement (one 2 × 8 per orientation is false under every index map)')
E('LL2', LL, "is certified by the round's exact-computation probe, not by the kernel.",
  "is certified by exact computation over every index map (act 41), not by the kernel.",
  'docstring', 'census LL2: the converse re-attributed to exact computation over every index map (act 41)')

# ================= the census registry =================
E('J2', J, "the exhaustive block-structure searches, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding the known factorizations of the stratum point;",
  "the block-structure searches with the rows of each row class in sorted order, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding four 4 × 4 partition structures of the stratum point in each orientation, of the {sig.p44} that exact computation over every index map (act 41) admits;",
  'registry', 'census J2: act 36\'s searches scoped to the sorted alignment; the stratum point\'s 4 × 4 count from act 41')
E('J3', J, "the 492 4 × 4 Diţă hulls through the stratum point spanning its 49-dimensional defect at first order;",
  "the 492 4 × 4 Diţă hulls through the stratum point at the sorted alignment, spanning its 49-dimensional defect at first order, while over every valid alignment exact computation over every index map (act 41) finds {hull.distinct_mat} distinct 4 × 4 hulls as matrix families and {hull.distinct_gauge} modulo the gauge, from {hull.params} parametrizations, with tangent dimensions modulo the gauge in {hull.dims}, [[each inside the linearized and second-order unitarity conditions | not all inside the linearized and second-order unitarity conditions : hull.dF_ok]], their tangents spanning {hull.span} dimensions;",
  'registry', 'census J3: act 36\'s hull count scoped to the sorted alignment; act 41\'s hull census from the measurement')
E('J4', J, "These are exact arithmetic replayed, not kernel-certified; by them the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.",
  "These are exact arithmetic replayed, not kernel-certified. By exact computation over every index map (act 41), both points admit no 4 × 4 and no 8 × 2 Diţă factorization of either orientation and exactly one 2 × 8 partition structure per orientation, so the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.",
  'registry', 'census J4: the conclusion re-attributed to exact computation over every index map (act 41)')
E('J5', J, "and each of the eight other factorization classes of the stratum point admitted only at the base point (act 37, Track B)",
  "and each of eight other named factorization classes of the stratum point admitted only at the base point (act 37, Track B)",
  'registry', 'census J5: removes the completeness reading')
E('J6', J, "and for each of the eight other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Pu u at that class's index maps",
  "and for each of eight other named factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8 — a Diţă form of Pu u at its named index maps",
  'registry', 'census J6: removes the completeness claim')
E('J7', J, "the census of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;",
  "the census, at the sorted alignment, of eighteen Diţă partition structures of the stratum point in nine partition orbits under the stabilizer of order 1024 with transposition, where exact computation over every index map (act 41) finds {sig.partitions} partition structures, forming {sig.porbits_full} partition orbits and {sig.classes_full} factorization classes under that stabilizer;",
  'registry', 'census J7: act 37\'s census scoped; act 41\'s counts from the measurement')
E('J8', J, "the generic arc point admitting exactly the frozen class; each other class obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of twenty exactly named points ζ z^s w^t;",
  "the generic arc point admitting exactly the frozen 2 × 8 partition structure; each of the eight other named index maps obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of the sorted-alignment calculus, twenty exactly named points ζ z^s w^t;",
  'registry', 'census J8: scoped; the eight are named')
E('J9', J, "and the exhaustive search at each of them admitting only the frozen class away from u = 1, so that the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.",
  "and the search at the sorted alignment at each of them admitting only the frozen 2 × 8 partition structure away from u = 1. By exact computation over every index map (act 41) the strict exceptional set is exactly {w.exc_strict} and [[for every unit u ≠ 1 the arc point is a Diţă matrix for the frozen 2 × 8 partition structure in its two orientations and for no other index maps at all | the arc is not exclusive to the frozen 2 × 8 partition structure : w.exclusive]]; up to diagonal equivalence, as a separate statement, the exceptional set is {w.exc_relaxed}.",
  'registry', 'census J9: act 37\'s search scoped; the exceptional sets from act 41\'s measurement')
E('J10', J, "each of the nine factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of the eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)",
  "each of nine named factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of their eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)",
  'registry', 'census J10: removes the completeness reading')
E('J11', J, "for each of the nine Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Hu u at that class's index maps",
  "for each of nine named Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8 — a Diţă form of Hu u at its named index maps",
  'registry', 'census J11: removes the completeness claim')
E('J13', J, "and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;",
  "and the search at the sorted alignment at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two 2 × 8 partition structures it finds at u = −1 certified by exact reconstruction; by exact computation over every index map (act 41) the arc point admits no Diţă structure of any admissible shape, index map or orientation at any unit outside {e.exc_strict}, and none up to the allowed diagonal equivalences at any unit outside {e.exc_relaxed}, with {e.m1} partition structures at u = −1;",
  'registry', 'census J13: act 38\'s search scoped; the exceptional sets and the count at u = −1 from act 41\'s measurement')
E('J14', J, "spanned by the eighteen first-order Diţă subspaces,",
  "spanned by the first-order Diţă subspaces of the eighteen named index maps,",
  'registry', 'census J14: the eighteen are named')
E('J18', J, "The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by the round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard: 46 candidate structures contain every structure admitted anywhere, their strict and relaxed loci coincide, and the union of the 30 nonempty loci is exactly the five faces.",
  "The round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard, shows that 46 partition candidates contain every Diţă structure admitted anywhere and computes each candidate's strict and relaxed loci at the sorted alignment, which coincide and whose 30 nonempty members have the five faces as union. The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — [[is certified by exact computation over every index map (act 41) | fails under exact computation over every index map (act 41) : h3.five_faces]]: {h3.candidates} partition candidates, {h3.nonempty} of them with nonempty loci, [[strict and relaxed loci equal for every candidate | strict and relaxed loci differing : h3.strict_eq_relaxed]], and {h3.noncoord} of the loci's {h3.flats} distinct flats off the coordinate characters.",
  'registry', 'census J18: act 40\'s probe scoped to the sorted alignment; the converse and the locus counts from act 41\'s measurement')

# ================= ROADMAP.md =================
E('R2', R, "and, by the round's exact-computation probe, that point, of defect 37,",
  "and, by exact computation over every index map (act 41), that point, of defect 37,",
  'roadmap', 'census R2: the P0 statement re-attributed to act 41')
E('R3', R, "by the kernel for the eight other factorization classes of the stratum point and by the round's exact-computation probe for every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;",
  "by the kernel for eight other named factorization classes of the stratum point and by exact computation over every other index map (act 41), [[no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{w.exc_strict}`, and the arc is exclusive to its `2 × 8` partition structure | the exceptional set of the arc is `{w.exc_strict}`, and the arc is not exclusive to its `2 × 8` partition structure : w.exclusive]];",
  'roadmap', 'census R3: completeness reading removed; the exceptional set from act 41\'s measurement')
E('R4', R, "each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:",
  "each of nine named Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by exact computation over every other index map (act 41), the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{e.exc_strict}` strictly, or outside `{e.exc_relaxed}` up to diagonal equivalence:",
  'roadmap', 'census R4: completeness reading removed; the exceptional sets from act 41\'s measurement')
E('R5', R, "spanned by the eighteen Diţă tangent subspaces,",
  "spanned by the Diţă tangent subspaces of the eighteen named index maps,",
  'roadmap', 'census R5: the eighteen are named')
E('R7', R, "and the converse over every index map by the round's exact-computation probe.",
  "and the converse by exact computation over every index map (act 41).",
  'roadmap', 'census R7: the converse re-attributed to act 41')
E('R9', R, "for the classification of each against the\neighteen Diţă structures of the point:",
  "for the classification of each against the\nDiţă structures of the point:",
  'roadmap', 'census R9: removes the completeness reading')
E('R10', R, "none of the eighteen Diţă structures can have smaller",
  "none of the Diţă structures of the point can have smaller",
  'roadmap', 'census R10: removes the completeness reading')

P0_SENTENCE = ("Under the reading of an index map that acts 36 to 40 froze, a pair of bijections that fixes the alignment of the rows across row classes, act 41's exact computation in two independent paths gives: {sig.partitions} Diţă partition structures at the certified rational stratum point, forming {sig.porbits_full} partition orbits and {sig.classes_full} factorization classes under its stabilizer; act 37's arc [[exclusive to its `2 × 8` partition structure away from `u = 1`, strictly | not exclusive to its `2 × 8` partition structure : w.exclusive]]; act 38's exceptional set {e.exc_strict}, with {e.m1} partition structures at `u = −1`; and act 39's family admitting a Diţă structure [[exactly on act 40's five faces | on the flats {h3.maximal} : h3.five_faces]], through {h3.nonempty} nonempty candidate loci. The verdicts and kernels of acts 36 to 40 stand.")
STANDING = ("The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, no family other than those of acts 36 to 40 is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any realizable class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.")
TAIL = ("no family other than act 39's is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle. |")
E('R-A41', R, TAIL, TAIL[:-2] + ' ' + P0_SENTENCE + ' ' + STANDING + ' |',
  'append', 'this round\'s P0 sentence template and standing clause, appended once after act 40\'s standing clause')

exec(open('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/overrides41.py', encoding='utf-8').read())

def blob(path):
    return subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (D41, path)], capture_output=True, check=True).stdout.decode('utf-8')

bad = []
cache = {}
for e in ENTRIES:
    t = cache.setdefault(e['path'], blob(e['path']))
    c = t.count(e['old'])
    if c != 1: bad.append((e['id'], c))
if bad:
    print('NOT UNIQUE / MISSING:', bad); sys.exit(1)
ids = [e['id'] for e in ENTRIES]
assert len(ids) == len(set(ids))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(ENTRIES, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('wrote', len(ENTRIES), 'entries')
