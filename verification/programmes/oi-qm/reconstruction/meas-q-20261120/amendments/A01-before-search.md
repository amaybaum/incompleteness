# MEAS-Q amendment A01 (before any run on Q)

Committed after `PREREG.md` (`b8bffca2`) and before any enumeration, search or simulation on Q.
The only computation run before it is control PC1 on U₂ (the S-A enumerator on the `q = 2` member),
which reproduced NP1's counts 0, 184, 1904, 736. Nothing here changes a requirement, a bound or the
decision rule.

1. **DT_A log block.** DT_A's persistence clause (§2, A2) asks for one fixed block `L` throughout
   `[τ₂, τ₂ + 60]`. A single-site log is sufficient for DT_s (§4 S-A), not for persistence: a block
   can differ between the carrier branches at every tick while no one of its sites does. DT_A is
   therefore evaluated with the largest admissible block: all sites of `A ∖ {H}` (S-A: of the box
   minus the carrier site and `H`) that meet (R). Any admissible `L` is a subset of it, so this
   decides whether some admissible `L` exists. DT_s keeps single-site logs.
2. **Signal launch per phase and direction (S-C, S-D).** For each of the four line phases and each
   direction, the W2 signal is launched by flipping the background pair `(x₀, x₀+1)` with `x₀`
   chosen from `{−12, −11}` (direction `+e₁`) or `{10, 11}` (direction `−e₁`). The choice is made by
   control K0 on the plain line: the first `x₀` whose defect differs from `N` on at most 3 sites at
   every tick of 30 and whose centre moves toward the origin. The choice is recorded. If neither
   works for a phase and direction, that cell of the family is reported as not launched.
3. **Phase symmetry check (S-D).** RZ is odd (`G(−s) = −G(s)`), and shifting the line phase by 2
   negates the W2 background. The outcomes at phase `φ + 2` must equal those at phase `φ` with every
   gadget value negated. This is checked as an exactness control (K5).
4. **Dilution on Q (Node 3).** In addition to the enumeration named in §4, the step on which NP1
   Lemma N2.3 rests is checked directly in Q: every single-site perturbation with both slices in
   `[c−1, c+1]` stays on its site for 64 ticks, at `c ∈ {1, 2^15, q−2}` (check D1).
