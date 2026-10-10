"""Stage 3 surfaces for A37: the census family (appended last, kernel-only) and the P0 sentence for the case.
usage: python3 surfaces37.py <worktree> <label> <number of named results>"""
import json, os, sys, importlib.util
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c37', os.path.join(S, 'rec', 'controls.py')); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W, label, NTHM = sys.argv[1], sys.argv[2], sys.argv[3]
cen_path = os.path.join(W, 'verification/lean-manuscript-census.json')
c = json.load(open(cen_path, encoding='utf-8'))
assert not any('DitaArcExclusivity' in f.get('modules', []) for f in c['families'])
import hashlib
_b = open(os.path.join(S, 'rec', 'preregistration.md'), 'rb').read()
PREREG_BLOB = hashlib.sha1(b'blob %d\0' % len(_b) + _b).hexdigest()
PRE = "Track B act 37, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/track-b/act-37-arc-exclusivity/preregistration.md, blob " + PREREG_BLOB + ". "
NOTE = {
 'A37-EXCLUSIVITY-PROVED': PRE + "Outcome: A37-EXCLUSIVITY-PROVED. Along act 36's arc Pu u = SIG ∘ u^W through the certified rational stratum point SIG = F₄(z) ⊗ F₄(w), z = (3+4i)/5, w = (5+12i)/13: the arc is symmetric (a37_shared_symmetric); the frozen 2 × 8 factorization persists at every unit u in both orientations (a37_shared_persistence); and for each of the eight other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Pu u at that class's index maps, in either orientation, forces u = 1 (a37_shared_excl_k1, k2, k3, k4, e1, e2, t2, t3). The base point Pu 1 = SIG carries the Kronecker 4 × 4 factorization with flat unitary factors (a37_control_base). The verdict a37_exclusivity; the corollary a37_c_exclusive excludes the other verdict. " + NTHM + " named results, each within propext, Classical.choice and Quot.sound; zero definitions against a budget of zero. The round's exact-computation probe verification/lean/dita_arc_exclusivity_probe.py, run by the A36 hierarchy shard, replays by exact Gaussian-rational arithmetic and an exact monomial calculus: the census of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition; the generic arc point admitting exactly the frozen class; each other class obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of twenty exactly named points ζ z^s w^t; and the exhaustive search at each of them admitting only the frozen class away from u = 1, so that the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all. These are exact arithmetic replayed, not kernel-certified. The arc lies in the frozen 2 × 8 hull at every unit u and escapes no hull; whether every realizable class near the stratum lies in some Diţă hull of some factorization is open, recorded and not decided. Act 36's recorded verdict stands as recorded; the product normalized set and its isometries are not classified. P0 stays OPEN; no hull, family, factorization, class or isometry is adopted as a physical symmetry, principle or law. Non-sealing.",
 'A37-EXCLUSIVITY-FAILS': PRE + "Outcome: A37-EXCLUSIVITY-FAILS. The arc-exclusivity package fails at a named part, exhibited in the kernel; the base control holds. Non-sealing.",
}
c['families'].append({'name': "the exclusivity of the 2 × 8 arc through the product-embedded stratum point — the arc symmetric, its frozen 2 × 8 factorization persistent in both orientations, and each of the eight other factorization classes of the stratum point admitted only at the base point (act 37, Track B)",
                      'modules': ['DitaArcExclusivity'], 'status': 'kernel-only', 'manuscript': [], 'note': NOTE[label]})
open(cen_path, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
road_path = os.path.join(W, 'verification/ROADMAP.md')
road = open(road_path, encoding='utf-8').read()
new = C.expected_roadmap(road, label)
assert new is not None and new != road
open(road_path, 'w', encoding='utf-8').write(new)
print('surfaces written for', label)
