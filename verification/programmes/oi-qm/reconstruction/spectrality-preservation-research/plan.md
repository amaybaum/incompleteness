# Spectrality-to-preservation: bounded research decision rule

Research/design only, based on bridge commit `1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37`.
This is an exploratory decision rule, not a native control plane or F.

The question is whether externally postulated SP, on an independently given
closed convex cone satisfying SEP ⊆ C ⊆ maxCone, implies preservation by every
guaranteed stopped map. A counterexample counts only with a universal proof of
every retained cone/SP premise and an exact depth-one separator. Excluding the
two historical cones does not count as proving this implication.

The first branch examines order-isomorphic quantum models, beginning with
partial-transpose PSD and its local-congruence and CNOT-conjugate variants.
We will distinguish failure of preservation from failure of product inclusion.
All positive comparisons must use the actual stopped map; no arbitrary
fullClass replacement operation earns an exclusion. Written arguments and
exact certificates have separate labels. Required certificates: transpose
involution/pairing, a genuine transformed spectral frame and effects, local
CP covariance on a spanning matrix basis, a quantum exclusion witness, and
the proposed tilted cone's product-inclusion test. Two independent arithmetic
implementations must agree; deliberately wrong transpose, phase, effect or
product membership must fail. No result verdict prints before these checks.

If this branch supplies no common-domain counterexample, record the reason
and leave the SP implication open. A literature classification may be used
only with all its additional assumptions named, especially strong symmetry.
Do not import those assumptions into the SP-only question. A useful milestone
is a universal preservation theorem for this model family and a precise
remaining fork, rather than a false general verdict. No manuscript status,
adopted Lean module, workflow, native record or historical digest changes.
