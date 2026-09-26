"""The A32 P0 cell per case, built from D's ROADMAP."""
import json, sys
CLAUSE = (" Whether every surjective isometry of the normalized space at that configuration belongs to the "
          "family is recorded undecided, with the step named; no isometry outside the family is exhibited, "
          "and the absence of a proof is not a counterexample.")
STANDING = ("`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law "
            "is adopted as the physical one, and nothing here names, endorses or excludes a selection principle.")
ADMITS = ("At the product configuration, the ladder's conditions through factorization admit every pair of "
          "local class bijections: each such pair is the class action of the factor families of a single law "
          "carrying all of them, so those conditions do not select among local behaviours.")
STAND32 = ("`P0`'s threading part is untouched, no isometry of the normalized space is adopted as physical, "
           "and nothing here names, endorses or excludes a selection principle.")
CASE = {
    'A32-NOT-RIGID': ("At the single-carrier configuration, the positive classification proposition posed as act "
                      "25's `ISO3` is false: the map that conjugates the Fourier parameter on the Fourier circle "
                      "and fixes the class of every point of the other eight relabelled Fourier circles preserves "
                      "realizability, is surjective on classes and preserves the distance, and for no pair of "
                      "relabellings does it satisfy any of the four shapes of act 25's family."),
    'A32-RIGID': ("At the single-carrier configuration, every surjective isometry of the normalized space "
                  "belongs, on realizable classes, to act 25's finite family."),
}


def cell(road, label):
    if label == 'A32-UNDECIDED':
        return road
    assert road.count(CLAUSE) == 2, road.count(CLAUSE)
    r = road.replace(CLAUSE, '')
    old = ' ' + ADMITS + ' ' + STANDING + ' |'
    assert r.count(old) == 1
    return r.replace(old, ' ' + ADMITS + ' ' + STANDING + ' ' + CASE[label] + ' ' + STAND32 + ' |', 1)


if __name__ == '__main__':
    road = open(sys.argv[1], encoding='utf-8').read()
    for lab, fn in (('A32-NOT-RIGID', 'road-notrigid.md'), ('A32-RIGID', 'road-rigid.md')):
        open(fn, 'w', encoding='utf-8').write(cell(road, lab))
