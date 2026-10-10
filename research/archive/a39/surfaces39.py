"""Stage 3 surfaces for A39: the census family (appended last, kernel-only) and the P0 sentence for the case.
usage: python3 surfaces39.py <worktree> <label> <number of named results, in words>"""
import json, os, sys, importlib.util, hashlib
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c39', os.path.join(S, 'rec', 'controls.py')); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W, label, NTHM = sys.argv[1], sys.argv[2], sys.argv[3]
cen_path = os.path.join(W, 'verification/lean-manuscript-census.json')
c = json.load(open(cen_path, encoding='utf-8'))
assert not any('DitaTorus' in f.get('modules', []) for f in c['families'])
_b = open(os.path.join(S, 'rec', 'preregistration.md'), 'rb').read()
PREREG_BLOB = hashlib.sha1(b'blob %d\0' % len(_b) + _b).hexdigest()
PRE = "Track B act 39, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/track-b/act-39-realizable-torus/preregistration.md, blob " + PREREG_BLOB + ". "
NOTE = {
 'A39-REALIZABLE-PROVED': PRE + "Outcome: A39-REALIZABLE-PROVED. For act 38's three disjoint exponent pieces on the product index — A = [a odd][b = 3][c odd], B = [a = 2][d = 1], C = [a+b odd][(c,d) ∈ {(0,2),(2,0)}], with A + B + C act 38's E — and the family H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C through the certified rational stratum point SIG = F₄(z) ⊗ F₄(w), z = (3+4i)/5, w = (5+12i)/13: H3 u₁ u₂ u₃ is a flat unitary, a realizable complex Hadamard matrix whose feature vector lies in the product normalized set, at every point of the three-torus (a39_shared_realizable). The family passes through the stratum point, H3 1 1 1 = SIG (a39_control_base), and its diagonal is act 38's arc, H3 u u u = Hu u (a39_control_diagonal). The verdict a39_realizable; the corollary a39_c_exclusive excludes the other verdict. " + NTHM + " named results, each within propext, Classical.choice and Quot.sound; zero definitions against a budget of zero. The round's exact-computation probe verification/lean/dita_torus_probe.py, run in act 38's shard, certifies by exact Gaussian-rational arithmetic and monomial by monomial in z and w the identity the kernel proves: for every ordered pair of rows, the columns grouped by their joint exponent-difference triple cancel, 552 joint level sets and none failing; with the base point, the diagonal, exact unitarity at four points off the diagonal, the eight single- and two-variable subfamilies, the merged diagonal triples and a countercontrol as controls. These are exact arithmetic replayed, not kernel-certified. Nothing is claimed about which points of the three-torus admit a Diţă structure, about the exponent matrices with entries in {0, 1}, about the minimality of support 48, or about act 38's diagonal exclusion at the generic point of the family. Act 38's recorded verdict stands as recorded; the product normalized set and its isometries are not classified. P0 stays OPEN; no family, factorization, class or isometry is adopted as a physical symmetry, principle or law. Non-sealing.",
 'A39-REALIZABLE-FAILS': PRE + "Outcome: A39-REALIZABLE-FAILS. The three-parameter family fails to be realizable at a named point of the three-torus, exhibited in the kernel; the base and diagonal controls hold. Non-sealing.",
}
c['families'].append({'name': "the three-parameter realizable family through the product-embedded stratum point — SIG ∘ u₁^A u₂^B u₃^C, act 38's pieces, a realizable complex Hadamard matrix at every point of the three-torus, through SIG at (1, 1, 1) and with act 38's arc as its diagonal (act 39, Track B)",
                      'modules': ['DitaTorus'], 'status': 'kernel-only', 'manuscript': [], 'note': NOTE[label]})
open(cen_path, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
road_path = os.path.join(W, 'verification/ROADMAP.md')
road = open(road_path, encoding='utf-8').read()
new = C.expected_roadmap(road, label)
assert new is not None and new != road
open(road_path, 'w', encoding='utf-8').write(new)
print('surfaces written for', label)
