"""Stage 3 surfaces for A38: the census family (appended last, kernel-only) and the P0 sentence for the case.
usage: python3 surfaces38.py <worktree> <label> <number of named results>"""
import json, os, sys, importlib.util, hashlib
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c38', os.path.join(S, 'rec', 'controls.py')); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W, label, NTHM = sys.argv[1], sys.argv[2], sys.argv[3]
cen_path = os.path.join(W, 'verification/lean-manuscript-census.json')
c = json.load(open(cen_path, encoding='utf-8'))
assert not any('DitaLocalEscape' in f.get('modules', []) for f in c['families'])
_b = open(os.path.join(S, 'rec', 'preregistration.md'), 'rb').read()
PREREG_BLOB = hashlib.sha1(b'blob %d\0' % len(_b) + _b).hexdigest()
PRE = "Track B act 38, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/track-b/act-38-local-escape/preregistration.md, blob " + PREREG_BLOB + ". "
NOTE = {
 'A38-NON-DITA-WITNESS-PROVED': PRE + "Outcome: A38-NON-DITA-WITNESS-PROVED. For the explicit exponent matrix E = A + B + C on the product index — A = [a odd][b = 3][c odd], B = [a = 2][d = 1], C = [a+b odd][(c,d) ∈ {(0,2),(2,0)}] — and the arc Hu u = SIG ∘ u^E through the certified rational stratum point SIG = F₄(z) ⊗ F₄(w), z = (3+4i)/5, w = (5+12i)/13: Hu u is a flat unitary, a realizable complex Hadamard matrix, at every unit u (a38_shared_realizable); for each of the nine Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Hu u at that class's index maps, in either orientation, forces u = 1 (a38_shared_excl_k1, k2, k3, k4, e1, e2, t1, t2, t3); and every neighbourhood of SIG contains a realizable matrix admitting none of the eighteen forms (a38_c_local_escape). The base point Hu 1 = SIG carries the Kronecker 4 × 4 factorization with flat unitary factors (a38_control_base). The verdict a38_witness; the corollary a38_c_exclusive excludes the other verdict. " + NTHM + " named results, each within propext, Classical.choice and Quot.sound; zero definitions against a budget of zero. The round's exact-computation probe verification/lean/dita_local_escape_probe.py, run by its own shard, replays by exact Gaussian-rational arithmetic, an exact monomial calculus and exact integer ranks: the Laurent identity of the arc, level set by level set; the eighteen exclusions and their forced witness identities; that at a generic u no index maps whatever pass the proportionality test in either orientation; the candidate exceptional set of forty exactly named points ζ z^s w^t and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences; and the tangent space at SIG, of dimension 80, spanned by the eighteen first-order Diţă subspaces, so that the escape is a nonlinear compatibility obstruction. These are exact arithmetic replayed, not kernel-certified. The local Diţă hulls of the stratum point's factorizations do not exhaust the realizable geometry near SIG. Nothing is claimed about the number of straight lines through SIG, the minimality of the witness's support, the orbits of witnesses, the three-parameter family, or the decomposition E = A + B + C beyond its use as a control. Act 37's recorded verdict stands as recorded; the product normalized set and its isometries are not classified. P0 stays OPEN; no hull, family, factorization, class or isometry is adopted as a physical symmetry, principle or law. Non-sealing.",
 'A38-WITNESS-FAILS': PRE + "Outcome: A38-WITNESS-FAILS. The local-escape package fails at a named part, exhibited in the kernel; the base control holds. Non-sealing.",
}
c['families'].append({'name': "a genuine non-Diţă local escape at the product-embedded stratum point — the explicit arc SIG ∘ u^E realizable at every unit u, each of the nine factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of the eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)",
                      'modules': ['DitaLocalEscape'], 'status': 'kernel-only', 'manuscript': [], 'note': NOTE[label]})
open(cen_path, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
road_path = os.path.join(W, 'verification/ROADMAP.md')
road = open(road_path, encoding='utf-8').read()
new = C.expected_roadmap(road, label)
assert new is not None and new != road
open(road_path, 'w', encoding='utf-8').write(new)
print('surfaces written for', label)
