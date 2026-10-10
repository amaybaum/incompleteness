"""Emit controls.py for A40 from props40.json (single source with the preregistration's Lean blocks).
usage: python3 gen_controls40.py <probe blob> <module blob>"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props40.json')))
P39 = json.load(open(os.path.join(S, '..', 'a39', 'props39.json')))
T39 = json.load(open(os.path.join(S, '..', 'a39', 'texts39.json')))
PROBE_BLOB, MODULE_BLOB = sys.argv[1], sys.argv[2]
def lit(d):
    return '{\n' + ',\n'.join(' %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)) for k, v in d.items()) + '\n}'
A39_HEAD = P39['COMPONENTS']['HEAD']
assert P['COMPONENTS']['HEAD39'] == A39_HEAD and P['COMPONENTS']['HEAD'] == A39_HEAD + P['COMPONENTS']['HEAD40']

SENT = {
 "A40-LOCUS-CLASSIFIED": "At the frozen product configuration, the Diţă locus of act 39's three-parameter family is classified, in two layers named separately: for `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, `H3 u₁ u₂ u₃` admits a Diţă structure — of some shape, index map and orientation, strictly or up to diagonal equivalence — exactly when `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1` or `u₃ = −1`. The if-direction is proved in the kernel, at evidence level 2: at every point of each of the five faces, `H3` or its transpose is an explicit strict Diţă product of a named shape and index map with flat unitary factors. The kernel also proves, for each of twenty named index maps — act 37's nine classes in both orientations and act 38's `M_COL` and `M_ROW` — that a strict Diţă form of `H3` at that map forces its named coordinate equations. The only-if direction, over every shape, index map and orientation, and the agreement of the strict locus with the locus up to diagonal equivalence, are certified by the round's exact-computation probe and not by the kernel: forty-six candidate structures contain every structure admitted anywhere, the strict and relaxed loci of each coincide, the thirty nonempty loci are cut out by coordinate characters alone, and their union is exactly the five faces. This is a statement about the frozen mathematical objects; it censuses no exponent matrices, decides no minimality, concerns no family other than `H3`, and adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A40-LOCUS-FAILS": "At the frozen product configuration, the kernel layer of the Diţă-locus classification fails, at evidence level 2: at some point of one of the five faces `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` admits no strict Diţă product of the frozen shape and index map, or at one of the twenty named index maps a strict Diţă form of `H3` holds off its named coordinate equations, and the witness is exhibited in the kernel. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A40-UNDECIDED": "Neither the kernel layer nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = ("Act 40 proves and computes statements about act 39's three-parameter family through act 34's certified rational\n"
          "stratum point, and adopts none of them as anything but mathematics. A `LOCUS-CLASSIFIED` verdict settles which\n"
          "points of the three-torus admit a Diţă structure of the family, in two layers named separately: the kernel proves\n"
          "the explicit factorizations on the five faces and the exclusions at twenty named index maps, and the round's\n"
          "exact-computation probe certifies that no other point admits one. A `LOCUS-FAILS` verdict exhibits a failure of\n"
          "the kernel layer in the kernel. Neither verdict censuses the exponent matrices with entries in `{0, 1}`, decides\n"
          "whether support 48 is minimal or says anything about a family other than act 39's; both leave the product\n"
          "normalized set unclassified. Neither verdict establishes that any admissible transition law is covariant under\n"
          "any isometry, selects a physical law or closes `P0`. No hull, family, factorization, isometry, carrier, group or\n"
          "principle gains physical status by appearing here, and nothing here derives, recognises or approaches quantum\n"
          "evolution.")
P0_END_D = T39['P0_CASE']['A39-REALIZABLE-PROVED'] + ' ' + T39['P0_STANDING_39']
P0_CASE = {
 "A40-LOCUS-CLASSIFIED": "For act 39's three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, the points of the three-torus at which it admits a Diţă structure, of any shape, index map and orientation and up to diagonal equivalence, are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.",
 "A40-LOCUS-FAILS": "For act 39's three-parameter family through the certified rational stratum point, the kernel layer of the frozen Diţă-locus classification fails, by a witness exhibited in the kernel."
}
P0_STANDING_40 = "The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, no family other than act 39's is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

HEADER = open(os.path.join(S, '_head_tpl40.txt'), encoding='utf-8').read()
HEADER = HEADER[HEADER.index("'''") + 3:HEADER.rindex("'''")]
BODY = open(os.path.join(S, '_body40.txt'), encoding='utf-8').read()
BODY = BODY[BODY.index("r'''") + 4:]
ST = open(os.path.join(S, '_selftest40.txt'), encoding='utf-8').read()
SELFTEST = ST[ST.index("r'''") + 4:ST.rindex("'''")]
text = HEADER % (json.dumps(PROBE_BLOB), json.dumps(MODULE_BLOB), json.dumps(P['OPEN'], ensure_ascii=False), json.dumps(A39_HEAD, ensure_ascii=False),
                 lit(P['PROPS']), lit(P['COMPONENTS']), json.dumps(P['THEOREMS'], ensure_ascii=False, indent=1),
                 json.dumps(P['PARTS']), lit(SENT), json.dumps(CLAUSE, ensure_ascii=False), json.dumps(P0_END_D, ensure_ascii=False),
                 lit(P0_CASE), json.dumps(P0_STANDING_40, ensure_ascii=False)) + BODY + SELFTEST
os.makedirs(os.path.join(S, 'rec'), exist_ok=True)
open(os.path.join(S, 'rec', 'controls.py'), 'w', encoding='utf-8').write(text)
json.dump({'SENTENCES': SENT, 'CLAUSE': CLAUSE, 'P0_END_D': P0_END_D, 'P0_CASE': P0_CASE, 'P0_STANDING_40': P0_STANDING_40},
          open(os.path.join(S, 'texts40.json'), 'w'), ensure_ascii=False, indent=1)
print('controls.py written', len(text))
