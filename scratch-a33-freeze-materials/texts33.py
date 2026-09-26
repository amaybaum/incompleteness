"""A33: the frozen prose texts -- outcome sentences, THE CLAUSE, the P0 cell texts."""
SENTENCES = {
 'A33-CLASSIFIED':
  "At the frozen single-carrier configuration, the surjective isometries of the normalized space are classified, at evidence level 2: every such map carries each of act 26's nine relabelled Fourier circles onto one of them, acts on each circle by `w ↦ λ w` or `w ↦ λ w̄` with `λ ∈ {1, −1}` fixed by its action on the two shared points of that circle, and is determined by the automorphism it induces on the incidence graph `K₃,₃` of the six shared points together with nine independent conjugation bits; every such pair is realized, the composition law is `ε''ᵣ = ε'ᵣ · ε_{σ'(r)}`, and there are exactly `72 · 2⁹ = 36864` surjective isometries. Act 25's four-shape family is a subgroup of index 16, meeting the kernel of the incidence action exactly in the conjugation patterns whose degree parities at the six shared points are uniform. This is a classification of the isometries of the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law.",
 'A33-NOT-CLASSIFIED':
  "At the frozen single-carrier configuration, the classification proposition for the surjective isometries of the normalized space is false, at evidence level 2: either some surjective isometry admits no normal form over the incidence graph `K₃,₃` and nine conjugation bits or admits two, or some automorphism of the incidence graph together with some choice of conjugation bits is the normal form of no surjective isometry. The witness is exhibited in the kernel. This is a statement about the frozen space; it adopts no isometry as a symmetry, a principle or a law.",
 'A33-UNDECIDED':
  "Neither the classification nor its negation was obtained. The step at which the proof stopped is named, with what would settle it.",
}

CLAUSE = """Act 33 classifies the surjective isometries of the frozen normalized single-carrier space, and adopts
none. The group obtained is the isometry group of a mathematical object, a finite union of circles
in a Euclidean space; its elements are not thereby physical symmetries, transformation laws,
dynamics, time reversals, antiunitary operations or principles of nature, and its order and
structure are facts about that object and about nothing else. A `CLASSIFIED` verdict settles that
frozen isometry problem, and a `NOT-CLASSIFIED` verdict exhibits its failure. Neither verdict
selects a physical law or closes `P0`. No isometry, carrier, family, group or principle gains
physical status by appearing in this classification, and nothing here derives, recognises or
approaches quantum evolution."""

# the end of the P0 cell at D: act 32's sentence and its standing clause
P0_A32 = "At the single-carrier configuration, the positive classification proposition posed as act 25's `ISO3` is false: the map that conjugates the Fourier parameter on the Fourier circle and fixes the class of every point of the other eight relabelled Fourier circles preserves realizability, is surjective on classes and preserves the distance, and for no pair of relabellings does it satisfy any of the four shapes of act 25's family."
P0_STANDING_32 = "`P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."
P0_END_D = P0_A32 + ' ' + P0_STANDING_32
P0_CASE = {
 'A33-CLASSIFIED':
  "At the single-carrier configuration, the surjective isometries of the normalized space are classified: each permutes the nine relabelled Fourier circles by an automorphism of their incidence graph `K₃,₃` and conjugates the parameter on an arbitrary subset of the circles, 36864 in all, and act 25's four-shape family is a subgroup of index 16.",
 'A33-NOT-CLASSIFIED':
  "At the single-carrier configuration, the classification of the surjective isometries of the normalized space by the automorphisms of the circles' incidence graph `K₃,₃` and nine conjugation bits fails, by a witness exhibited in the kernel.",
}
P0_STANDING_33 = "`P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."
