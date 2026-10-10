"""Emit controls.py for A39 from props39.json (single source with the preregistration's Lean blocks).
usage: python3 gen_controls39.py <probe blob>"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props39.json')))
P38 = json.load(open(os.path.join(S, '..', 'a38', 'props38.json')))
T38 = json.load(open(os.path.join(S, '..', 'a38', 'texts38.json')))
PROBE_BLOB = sys.argv[1] if len(sys.argv) > 1 else '0' * 40
def lit(d):
    return '{\n' + ',\n'.join(' %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)) for k, v in d.items()) + '\n}'
A38_HEAD = P38['COMPONENTS']['HEAD']
assert P['COMPONENTS']['HEAD38'] == A38_HEAD and P['COMPONENTS']['HEAD'] == A38_HEAD + P['COMPONENTS']['HEAD39']

SENT = {
 "A39-REALIZABLE-PROVED": "At the frozen product configuration, the three-parameter realizability package holds, at evidence level 2: for act 38's three disjoint exponent pieces `A`, `B`, `C`, with entries in `{0, 1}` on the sixteen-point carrier and sum act 38's exponent matrix `E`, and the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, `H3 u₁ u₂ u₃` is a flat unitary — a complex Hadamard matrix — whose Gram family is realizable and whose feature vector lies in the product normalized set, at every point `(u₁, u₂, u₃)` of the three-torus. Beside the package, required under both decided labels: the family passes through the stratum point, `H3 1 1 1 = SIG`, and its diagonal is act 38's arc, `H3 u u u = Hu u` for every `u`. The round's exact-computation probe certifies the identity the kernel proves: for every ordered pair of rows, the columns grouped by their joint exponent-difference triple cancel exactly, 552 joint level sets and none failing, monomial by monomial in the stratum point's two units. This is a statement about the frozen mathematical objects; it does not decide which points of the three-torus admit a Diţă structure, and it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A39-REALIZABLE-FAILS": "At the frozen product configuration, the three-parameter realizability package fails, at evidence level 2: at some point of the three-torus the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` is not a flat unitary with realizable Gram family and feature vector in the product normalized set, and the witness is exhibited in the kernel; the base and diagonal controls hold. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A39-UNDECIDED": "Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = "Act 39 proves statements about one exact three-parameter family of realizable classes through act 34's certified\nrational stratum point, given by act 38's three exponent pieces, and adopts none of them as anything but\nmathematics. A `REALIZABLE-PROVED` verdict settles the frozen package, and a `REALIZABLE-FAILS` verdict exhibits\nthe failure at a named point. Neither verdict classifies which points of the three-torus admit a Diţă structure,\ncensuses the exponent matrices with entries in `{0, 1}` or decides whether support 48 is minimal, and neither\ncarries act 38's exclusion of Diţă structures along the diagonal to the generic point of the family; both leave\nthe product normalized set unclassified. Neither verdict establishes that any admissible transition law is\ncovariant under any isometry, selects a physical law or closes `P0`. No hull, family, factorization, isometry,\ncarrier, group or principle gains physical status by appearing here, and nothing here derives, recognises or\napproaches quantum evolution."
P0_END_D = T38['P0_CASE']['A38-NON-DITA-WITNESS-PROVED'] + ' ' + T38['P0_STANDING_38']
P0_CASE = {
 "A39-REALIZABLE-PROVED": "For act 38's three exponent pieces `A`, `B`, `C`, the three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point is realizable at every point of the three-torus, by the kernel, with the joint level-set cancellation certified exactly by the round's probe; the family passes through the stratum point and its diagonal is act 38's arc.",
 "A39-REALIZABLE-FAILS": "The three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point fails to be realizable at a named point of the three-torus, by a witness exhibited in the kernel, while the base and diagonal controls hold."
}
P0_STANDING_39 = "Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, act 38's diagonal exclusion is not carried to the generic point of the family, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

HEADER = open(os.path.join(S, '_head_tpl39.txt'), encoding='utf-8').read()
HEADER = HEADER[HEADER.index("'''") + 3:HEADER.rindex("'''")]
BODY = open(os.path.join(S, '_body39.txt'), encoding='utf-8').read()
BODY = BODY[BODY.index("r'''") + 4:]
ST = open(os.path.join(S, '_selftest39.txt'), encoding='utf-8').read()
SELFTEST = ST[ST.index("r'''") + 4:ST.rindex("'''")]
text = HEADER % (json.dumps(PROBE_BLOB), json.dumps(P['OPEN'], ensure_ascii=False), json.dumps(A38_HEAD, ensure_ascii=False),
                 lit(P['PROPS']), lit(P['COMPONENTS']), json.dumps(P['THEOREMS'], ensure_ascii=False, indent=1),
                 lit(SENT), json.dumps(CLAUSE, ensure_ascii=False), json.dumps(P0_END_D, ensure_ascii=False),
                 lit(P0_CASE), json.dumps(P0_STANDING_39, ensure_ascii=False)) + BODY + SELFTEST
os.makedirs(os.path.join(S, 'rec'), exist_ok=True)
open(os.path.join(S, 'rec', 'controls.py'), 'w', encoding='utf-8').write(text)
json.dump({'SENTENCES': SENT, 'CLAUSE': CLAUSE, 'P0_END_D': P0_END_D, 'P0_CASE': P0_CASE, 'P0_STANDING_39': P0_STANDING_39},
          open(os.path.join(S, 'texts39.json'), 'w'), ensure_ascii=False, indent=1)
print('controls.py written', len(text))
