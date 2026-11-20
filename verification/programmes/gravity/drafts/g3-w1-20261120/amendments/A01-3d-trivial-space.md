# G3-W1 amendment A01: the 3D trivial space (after run D, before run D2)

**Standing.** Append-only amendment to `PREREG.md`, committed before run D2, which it governs. It
changes nothing for parts A, B, C and does not alter run D's recorded outcome.

**What run D gave (preregistered, unchanged).** With the trivial space of PREREG §3 for the 3D
classes (the constant and `b(y at P + e_j) − b(y at P)` for monomials `b` on `P ⊆ {0, −e_j}`),
no 3D class is certified, with both primes: excess 24 for `3D-RZ:P3(2)`, 96 for `3D-RZ:P3(3)`, 24
for `3D-RZ:P3r(2)`, and 40 for the linear control `3D-LIN:P3(2)` (`results-D.json`). That is the
preregistered result for the 3D classes, and it stands.

**Diagnosis, stated before D2.** The preregistered generator set omits translation coboundaries
whose shift is not a single lattice step from `{0, −e_j}`. Example: `y_{e1} y_{e2}` and
`y_{−e2} y_{−e1}` are both star monomials and are translates of each other by `−e1 − e2`, so their
difference sums to zero on every periodic configuration and is conserved by every rule, but it is
not in the preregistered span. Such vectors lie in `ker E` and inflate the excess without being
conserved quantities.

**Change.** Run D2 repeats part D (the four 3D classes, same seeds, same equations, same stopping
rule, same controls P2 and C1, C3) with

  `T3' = span{ constant } + span{ m∘τ_a − m : m and m∘τ_a both monomials of the class, a ∈ ℤ³ }`,

applied uniformly across residue patterns for P3r. Every element of `T3'` is trivial and conserved
by every rule, so the certificate argument of PREREG §3 holds unchanged with `T3'` in place of `T`.
For the polynomial classes `T3'` is the whole trivial subspace: monomials in distinct translation
orbits give independent functionals, so a density is trivial exactly when its coefficients sum to
zero on each non-constant orbit. For P3r it is a subspace of the trivial space, which can only make
certification harder.

**Reporting.** RESULT reports D and D2 side by side. The decision for the 3D classes uses D2,
labelled as governed by this amendment. Output: `checks/results-D2.json`; `--render` reads it in
addition to the preregistered parts.
